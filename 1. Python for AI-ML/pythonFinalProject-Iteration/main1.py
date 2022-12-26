# based on https://codeburst.io/building-an-rss-feed-scraper-with-python-73715ca06e1f
import pip
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from PyPDF2 import PdfFileReader, PdfFileWriter


# scraping function
def get_rss(rss, DateOfLastPull):
    # Set up list of articles.
    article_list = []

    try:
        # Set up list of pdf files.
        input_streams = []
        input_files = []

        # Read rss feed.
        r = requests.get(rss)
        print('The scraping job succeeded: ', r.status_code)

        # Extract items (set of articles) from rss feed.
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')

        # Add each article to article_list iff it was published after the last pull.
        print('checking dates')
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text

            # In link, replace 'http://link.aps.org/doi' with 'https://journals.aps.org/prper/pdf' to get pdf.
            try:
                pdflink = link.replace('http://link.aps.org/doi', 'https://journals.aps.org/prper/pdf')
            except:
                try:
                    pdflink = link.replace('full', 'pdf')
                except:
                    print('Could not get pdf for', title)

            # Record published date.
            published = a.find('dc:date').text
            published = datetime.strptime(published[0:10], '%Y-%m-%d')

            # Record list of authors.
            authors = a.find('dc:creator').text

            # Was this article published since the last pull?
            PublishedSinceLastPull = (datetime.strptime(DateOfLastPull, '%Y-%m-%d') - published).days <= 0
            if PublishedSinceLastPull:  # Record article and pdf file in their respective lists.
                article = {
                    'title': title,
                    'link': link,
                    'pdflink': pdflink,
                    'published': published,
                    'authors': authors
                }
                datacaching_path = "./pdf_files/"
                # Download the pdf and clean up the file name.
                rpdf = requests.get(pdflink, stream=True)
                DownloadName = title.replace(':', '').replace('/', '').replace('\\', '').replace('?', '').replace('*','') + '.pdf'
                print('Downloading', title)
                with open(datacaching_path + DownloadName, 'wb') as f:
                    f.write(rpdf.content)
                article_list.append(article)
                input_files.append(DownloadName)
        print('found', len(articles), 'articles;', len(article_list), 'are new')

        # Compile the pdfs you just downloaded.
        for input_file in input_files:
            input_streams.append(open(input_file, 'rb'))
        writer = PdfFileWriter()
        for reader in map(PdfFileReader, input_streams):
            for n in range(reader.getNumPages()):
                writer.addPage(reader.getPage(n))
        output_name = str(datetime.now())[0:10] + '.pdf'
        output_stream = open(output_name, 'wb')
        writer.write(output_stream)
        for f in input_streams:
            f.close()

        # Lastly, create an index of articles for easier text searching later.
        ArticleIndex = 'articles.txt'
        with open(ArticleIndex, 'w') as f:
            for article in article_list:
                f.write(article['title'] + ' - ' + article['link'] + ' - ' + article['authors'] + ' - ' + str(
                    article['published']) + '\n')
        return  # Yay! We finished.

    except Exception as e:  # Something went wrong!
        print('The scraping job failed. See exception: ')
        print(e)


print('Starting scraping')

get_rss('http://feeds.aps.org/rss/recent/prstper.xml', '2021-02-15')

print('Finished scraping. Please update DateOfLastPull to', str(datetime.now())[0:10])

# Now download the compiled pdf to your computer and import into the reader of your choice.