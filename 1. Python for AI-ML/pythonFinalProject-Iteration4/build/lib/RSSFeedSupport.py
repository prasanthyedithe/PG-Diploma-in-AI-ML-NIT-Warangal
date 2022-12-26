import os
import subprocess
import feedparser
import pdfkit
import json
import Constants
import DateUtil
import RSSFeedUtil
import Utils
import logging as log
from os.path import exists
from datetime import datetime
from goose3 import Goose


def fetch_rss_feed(url_value):
    log.info("In fetch_rss_feed(url_value) with Input values :" + url_value)
    return feedparser.parse(url_value)


def news_feed(url_value):
    log.info("In news_feed(url_value) with Input values :" + url_value)
    entry = fetch_rss_feed(url_value).entries
    RSSFeedUtil.print_all_feeds(entry)


def news_feed_limit(url_value, limit_value):
    log.info("In news_feed_limit(url_value, limit_value) with Input values :" + url_value, limit_value)
    if limit_value == 0:
        RSSFeedUtil.print_all_feeds(url_value)
    else:
        entry = fetch_rss_feed(url_value).entries
        RSSFeedUtil.print_range_feeds(entry, limit_value)


def save_news_feed_json(url_value, limit_value):
    log.info("In save_news_feed_json(url_value, limit_value) with Input values :" + url_value, limit_value)
    my_json_list = []

    if limit_value is None:
        entry = fetch_rss_feed(url_value).entries
        RSSFeedUtil.construct_json_all_feeds(entry, my_json_list)
    else:
        entry = fetch_rss_feed(url_value).entries
        RSSFeedUtil.construct_json_range_feeds(entry, limit_value, my_json_list)

    json_string = json.dumps(my_json_list, indent=4)
    # if required we can add to the File
    with open(Constants.JSON_FILES_DIR + DateUtil.get_date_YYYYMMDD(None) + Constants.FILE_EXTENSION_JSON,
              "w") as json_file:
        json_file.write(json_string)
        json_file.close()


def fetch_news_feed_date_limit(date_value, limit_value):
    log.info("In fetch_news_feed_date_limit(date_value, limit_value) with Input values :" + date_value, limit_value)
    if exists(Constants.JSON_FILES_DIR + date_value + Constants.FILE_EXTENSION_JSON):
        with open(Constants.JSON_FILES_DIR + date_value + Constants.FILE_EXTENSION_JSON, 'r') as f:
            json_obj = json.load(f)
        if limit_value is None or limit_value == 0:
            json_data_obj = json.dumps(json_obj, indent=1)
            print(json_data_obj)
        else:
            for item in range(0, limit_value):
                json_data_obj = json.dumps(json_obj[item], indent=1)
                print(json_data_obj)

    else:
        print("No Latest New Available !!")


def fetch_news_feed_json_limit_date(limit_value, date_value):
    log.info("In fetch_news_feed_json_limit_date(date_value, limit_value) with Input values :" + date_value,
             limit_value)
    if date_value is None:
        file_name_date_value = datetime.today().strftime('%Y%m%d')
    else:
        file_name_date_value = date_value

    if exists(Constants.JSON_FILES_DIR + file_name_date_value + Constants.FILE_EXTENSION_JSON):
        with open(Constants.JSON_FILES_DIR + file_name_date_value + Constants.FILE_EXTENSION_JSON, 'r') as f:
            json_obj = json.load(f)
        if limit_value == 0:
            json_data_obj = json.dumps(json_obj, indent=1)
            print(json_data_obj)
        else:
            for item in range(0, limit_value):
                json_data_obj = json.dumps(json_obj[item], indent=1)
                print(json_data_obj)

    else:
        print("No Latest New Available !!")


def save_news_feed_to_pdf(url_value, limit_value):
    log.info("In save_news_feed_to_pdf(url_value, limit_value) with Input values :" + url_value,
             limit_value)
    # Creating Directory based on the current date
    full_dir_path = Constants.PDF_FILES_DIR + DateUtil.get_date_YYYYMMDD(None) + '/'

    # Check if the directory exist? If not create it
    Utils.create_directory(full_dir_path)

    # Check if the limit is passed if not convert all the RSS to Pdfs
    if limit_value is None:
        entry = fetch_rss_feed(url_value).entries
        for item in entry:
            last_item_list = item.link.rsplit('/', 1)[-1]
            file_name_pdf = last_item_list.replace(".html", "") + '.pdf'
            full_der_file_path = full_dir_path + file_name_pdf
            log.info("Generating the RSS Feeds to PDF:" + last_item_list)
            pdfkit.from_url(item.link, full_der_file_path.strip(), configuration=Constants.PDFKIT_CONFIG)
    else:
        entry = fetch_rss_feed(url_value).entries
        for item in range(0, limit_value):
            last_item_list = entry[item].link.rsplit('/', 1)[-1]
            file_name_pdf = last_item_list.replace(".html", "") + '.pdf'
            full_der_file_path = full_dir_path + file_name_pdf
            log.info("Generating the RSS Feeds to PDF:" + last_item_list)
            pdfkit.from_url(entry[item].link, full_der_file_path.strip(), configuration=Constants.PDFKIT_CONFIG)


def save_news_feed_to_html(url_value, limit_value):
    log.info("In save_news_feed_to_html(url_value, limit_value) with Input values :" + url_value,
             limit_value)
    # Creating Directory based on the current date
    full_dir_path = Constants.HTML_FILES_DIR + DateUtil.get_date_YYYYMMDD(None) + '/'
    ebook_name = DateUtil.get_date_YYYYMMDD(None) + ".epub"
    # Check if the directory exist? If not create it
    Utils.create_directory(full_dir_path)

    # Check if the limit is passed if not convert all the RSS to Pdfs
    if limit_value is None:
        d = fetch_rss_feed(url_value)
        # Enumerate through our feed, store the 'clean' article text in our temporary file, before exporting it to HTML
        for c, e in enumerate(d.entries):
            url = e.link
            log.info('Processing - {}'.format(url))
            g = Goose()
            retries = Constants.MAX_RETRIES
            while retries > 0:
                try:
                    article = g.extract(url=url)
                    g.close()
                    break
                except Exception as e:
                    print('Error establishing connection. Retrying...')
                    retries -= 1
            if retries <= 0:
                print('Failed to retreive article ({}). Moving on to next feed item.'.format(url))
                retries = Constants.MAX_RETRIES
            with open('temp.txt', 'w', encoding='utf-8') as file:
                file.write(article.cleaned_text)
            of = full_dir_path + '/s{}-{}.html'.format('{0:05d}'.format(c + 1), url.split("/")[-1].split(".")[0])
            subprocess.Popen('pandoc -i temp.txt -t html5 -o {}'.format(of), cwd=Constants.CURRENT_WORKING_DIR,
                             shell=True).wait()

            with open(of, 'r+', encoding='utf8') as f:
                content = f.read()
                f.seek(0, 0)
                f.write('<h1>{}</h1>'.format(article.title).rstrip('\r\n') + '\n' + content)

        # Feed title and Link are required as per the RSS2 spec ... we don't check if there's actually a value
        with open(full_dir_path + '/s00000.html', 'w') as file:
            file.write('<!DOCTYPE html><html><head><meta name="author" content="{}" />'
                       '<title>{}</title></head></html>'.format(d.feed.link, d.feed.title))
        # Convert the directory of (Ordered HTML file's into a single EPub)
        res = []
        file_names = ''
        for path in os.listdir(full_dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(full_dir_path, path)):
                if path != 's00000.html':
                    res.append(path)
        file_names = ' ' + full_dir_path + ' ' + full_dir_path.join(res)
        subprocess.Popen('pandoc -s -i {} -t epub -o {} --toc --metadata title=Test'.format(file_names,
                                                                                            full_dir_path + ebook_name),
                         cwd=Constants.CURRENT_WORKING_DIR, shell=True).wait()
        # Cleanup
        os.remove('temp.txt')
    else:
        d = fetch_rss_feed(url_value)
        entry = d.entries
        for c, e in enumerate(entry[0:1], 0):
            url = entry[c].link
            print('Processing - {}'.format(url))
            g = Goose()
            retries = Constants.MAX_RETRIES
            while retries > 0:
                try:
                    article = g.extract(url=url)
                    g.close()
                    break
                except Exception as e:
                    print('Error establishing connection. Retrying...')
                    retries -= 1
            if retries <= 0:
                print('Failed to retreive article ({}). Moving on to next feed item.'.format(url))
                retries = Constants.MAX_RETRIES
            with open('temp.txt', 'w', encoding='utf-8') as file:
                file.write(article.cleaned_text)
            of = full_dir_path + '/s{}-{}.html'.format('{0:05d}'.format(c + 1), url.split("/")[-1].split(".")[0])
            subprocess.Popen('pandoc -i temp.txt -t html5 -o {}'.format(of), cwd=Constants.CURRENT_WORKING_DIR,
                             shell=True).wait()

            with open(of, 'r+', encoding='utf8') as f:
                content = f.read()
                f.seek(0, 0)
                f.write('<h1>{}</h1>'.format(article.title).rstrip('\r\n') + '\n' + content)

            # Feed title and Link are required as per the RSS2 spec ... we don't check if there's actually a value
        with open(full_dir_path + '/s00000.html', 'w') as file:
            file.write('<!DOCTYPE html><html><head><meta name="author" content="{}" />'
                       '<title>{}</title></head></html>'.format(d.feed.link, d.feed.title))
            # Convert the directory of (Ordered HTML file's into a single EPub)
        res = []
        file_names = ''
        for path in os.listdir(full_dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(full_dir_path, path)):
                if path != 's00000.html':
                    res.append(path)

        file_names = ' ' + full_dir_path + '' + full_dir_path.join(res)
        print(file_names.strip())
        subprocess.Popen('pandoc -s -i {} -t epub -o {} --toc --metadata title=Test'.format(file_names,
                                                                                            Constants.EPUB_FILES_DIR + ebook_name),
                         cwd=Constants.CURRENT_WORKING_DIR, shell=True).wait()
        # Cleanup
        os.remove('temp.txt')
