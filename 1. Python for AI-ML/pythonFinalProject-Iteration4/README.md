# Final Python project task

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

Task Description is with in Project [Final_Task.md](Final_Task.md)

The Project consist of all the Tasks from `Iteration 1` to `Iteration 5` 

----
Setup : 
1. Create a Project with Name as pythonFinalProject2022
2. Created a below files
   1. `requirements.txt` : Used to store the libraries and plugins with their respective version that need to be installed to run the application
   2. `setup.py` : Used to configure the application to run using setuptools and python executable in CLI
   3. `README.md` : Help us the process of building the application
   4. `MANIFEST.in` : Consist of version of the application
3. Below folder will be created under parent folder `./data` 
   1. JSON_FILES : To store the generated .json files
   2. PDF_FILES : To store the generated .pdf files
   3. HTML_FILES : To store the generated .html files
   4. EPUB_FILES : To store the generated .epub files
4. Add and Update the requirement.txt to installed required plugins. Run the file using pip install ./requirement.txt
5. Test your package before publishing and then Build. : $ python setup.py install
7. Upload on pypi and publish your package : python setup.py sdist bdist_wheel
8. Install your newly-published package. : pip install pythonFinalProject_Iteration4

----
Application is divided into 2 python programs for easy maintenance 
1. Can be run based on the Python executable : `rss_reader.py`
   <br /> For Example : python.exe .\rss_reader.py --url "https://news.yahoo.com/rss/"
2. Can be run using setuptools : `rss_reader_utility.py`
   <br /> For Example : rss_reader_utility.py --url "https://news.yahoo.com/rss/"
----
Package Installation:
Below are the things that are considered while building the application
1. click : Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. It's the “Command Line Interface Creation Kit”. It's highly configurable but comes with sensible defaults out of the box.
2. setuptools : Setuptools is a collection of enhancements to the Python distutils that allow developers to more easily build and distribute Python packages, especially ones that have dependencies on other packages. Packages built and distributed using setuptools look to the user like ordinary Python packages based on the distutils .
3. feedparser : Universal Feed Parser is a Python module for downloading and parsing syndicated feeds. It can handle RSS 0.90, Netscape RSS 0.91, Userland RSS 0.91, RSS 0.92, RSS 0.93, RSS 0.94, RSS 1.0, RSS 2.0, Atom 0.3, Atom 1.0, and CDF feeds
4. xmltodict : xmltodict. xmltodict is a Python module that makes working with XML feel like you are working with JSON, as in this "spec"
5. goose3 : This is a complete rewrite in Python. The aim of the software is to take any news article or article-type web page and not only extract what is the main body of the article but also all metadata and most probable image candidate. Goose will try to extract the following information: Main text of an article.
6. django-wkhtmltopdf : django-wkhtmltopdf allows a Django site to output dynamic PDFs. It utilises the wkhtmltopdf library, allowing you to write using the technologies you know - HTML and CSS - and output a PDF file
7. pip : Package Installer for Python is the de facto and recommended package-management system written in Python and is used to install and manage software packages. It connects to an online repository of public packages, called the Python Package Index.
8. requests : Python requests module has several built-in methods to make Http requests to specified URI using GET, POST, PUT, PATCH or HEAD requests. A Http request is meant to either retrieve data from a specified URI or to push data to a server. It works as a request-response protocol between a client and a server.
9. beautifulsoup4 : Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work. The latest Version of Beautifulsoup is v4
10. PyPDF2 : PyPDF2 is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. PyPDF2 can retrieve text and metadata from PDFs as well.
11. pdfkit : Python 2 and 3 wrapper for wkhtmltopdf utility to convert HTML to PDF using Webkit. This is adapted version of ruby PDFKit library
12. Install wkhtmltopdf: https://wkhtmltopdf.org/downloads.html.Set class path in Environment Variables.As of now I have hardcoded the path in code for wkhtmltopdf

----
<h2>Commands</h2>

Iteration 1 to Iteration 5:

1. <b>`--url`</b> : 

| Command </br>(Python executable file)                                           | Command</br>(Setuptools Utility)                                        | Method Call                         | Description                                                                                                |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| python.exe .\rss_reader.py --url "https://news.yahoo.com/rss/"                  | rss_reader_utility --url "https://news.yahoo.com/rss/"                  | news_feed()                         | Reading the RSS feed and displaying in the console                                                         |
| python.exe .\rss_reader.py --url "https://news.yahoo.com/rss/" --limit 1        | rss_reader_utility --url "https://news.yahoo.com/rss/" --limit 1        | news_feed_limit()                   | Reading the first news from RSS feed and displaying in the console                                         |
| python.exe .\rss_reader.py --url "https://news.yahoo.com/rss/" --version        | rss_reader_utility --url "https://news.yahoo.com/rss/" --version        | news_feed(), version                | Reading the RSS feed and displaying in the console with Version                                            |
| python.exe .\rss_reader.py --url "https://news.yahoo.com/rss/" --json           | rss_reader_utility --url "https://news.yahoo.com/rss/" --json           | save_news_feed_json()               | Reading the RSS feed and adding the same to json file with current date in YYYYMMDD formate                |
| python.exe .\rss_reader.py --url "https://news.yahoo.com/rss/" --verbose        | rss_reader_utility --url "https://news.yahoo.com/rss/" --verbose        | news_feed(),enable_logging_stdout() | Reading the RSS feed and displaying in the console with log files                                          | 
| python.exe .\rss_reader.py --url "https://news.yahoo.com/rss/" --limit 1 --json | rss_reader_utility --url "https://news.yahoo.com/rss/" --limit 1 --json | save_news_feed_json()               | Reading the fist news from RSS feed and adding the same to json file with current date in YYYYMMDD formate |

2. <b>`--json`</b> :

| Command </br>(Python executable file)                         | Command</br>(Setuptools Utility)                      | Method Call                                                | Description                                                               |
|---------------------------------------------------------------|-------------------------------------------------------|------------------------------------------------------------|---------------------------------------------------------------------------|
| python.exe .\rss_reader.py --json                             | rss_reader_utility --json                             | fetch_news_feed_json_limit_date()                          | Reading the JSON news offline using current date                          |
| python.exe .\rss_reader.py --json --limit 1                   | rss_reader_utility --json --limit 1                   | fetch_news_feed_json_limit_date()                          | Reading the JSON news offline using current date based on the limit       |
| python.exe .\rss_reader.py --json --date "20220825"           | rss_reader_utility --json --date "20220825"           | fetch_news_feed_json_limit_date()                          | Reading the JSON news offline based on the passed date                    |
| python.exe .\rss_reader.py --json --verbose                   | rss_reader_utility --json --verbose                   | fetch_news_feed_json_limit_date(), enable_logging_stdout() | Reading the JSON news offline based on the passed date based on the limit |
| python.exe .\rss_reader.py --json --limit 1 --date "20220825" | rss_reader_utility --json --limit 1 --date "20220825" | fetch_news_feed_json_limit_date()                          | Reading the JSON news offline based on the passed date based on the limit |

3. <b>`--verbose`, `--version`, `--h`</b> :

| Command </br>(Python executable file) | Command</br>(Setuptools Utility) | Method Call             | Description                     |
|---------------------------------------|----------------------------------|-------------------------|---------------------------------|
| python.exe .\rss_reader.py --verbose  | rss_reader_utility --verbose     | enable_logging_stdout() | Outputs verbose status messages |
| python.exe .\rss_reader.py --h        | rss_reader_utility --h           | NA                      | show this help message and exit |
| python.exe .\rss_reader.py --version  | rss_reader_utility --version     | NA                      | Showing sys.version             |

4. <b>`--date`</b> :

| Command </br>(Python executable file)                  | Command</br>(Setuptools Utility)               | Method Call                                           | Description                                                                             |
|--------------------------------------------------------|------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------------------------------|
| python.exe .\rss_reader.py --date "20220825"           | rss_reader_utility --date "20220825"           | fetch_news_feed_date_limit()                          | Reading the Offline JSON data using the data that is passed                             |
| python.exe .\rss_reader.py --date "20220825" --limit 1 | rss_reader_utility --date "20220825" --limit 1 | fetch_news_feed_date_limit()                          | Reading the Offline JSON data using the data that is passed with Limit                  |
| python.exe .\rss_reader.py --date "20220825" --verbose | rss_reader_utility --date "20220825" --verbose | fetch_news_feed_date_limit(), enable_logging_stdout() | Reading the Offline JSON data using the data that is passed and showing logs in console |

5. <b>`--to-pdf`</b> :

| Command </br>(Python executable file)                                                             | Command</br>(Setuptools Utility)                                                          | Method Call                                      | Description                                                                                                              |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| python.exe .\rss_reader.py --to-pdf --url "http://feeds.aps.org/rss/recent/prstper.xml"           | rss_reader_utility --to-pdf --url "http://feeds.aps.org/rss/recent/prstper.xml"           | save_news_feed_to_pdf()                          | Read the RSS feed's Item links and generate the PDF and save in the current date folder                                  |
| python.exe .\rss_reader.py --to-pdf --url "http://feeds.aps.org/rss/recent/prstper.xml" --limit 1 | rss_reader_utility --to-pdf --url "http://feeds.aps.org/rss/recent/prstper.xml" --limit 1 | save_news_feed_to_pdf()                          | Read the RSS feed's Item links and generate the PDF and save in the current date folder with limit                       |
| python.exe .\rss_reader.py --to-pdf --url "http://feeds.aps.org/rss/recent/prstper.xml" --json    | rss_reader_utility --to-pdf --url "http://feeds.aps.org/rss/recent/prstper.xml" --json    | save_news_feed_to_pdf()                          | <B>TODO :</B> Need to get clarity on requirement                                                                         |
| python.exe .\rss_reader.py --to-pdf --url "http://feeds.aps.org/rss/recent/prstper.xml" --verbose | rss_reader_utility --to-pdf --url "http://feeds.aps.org/rss/recent/prstper.xml" --verbose | save_news_feed_to_pdf(), enable_logging_stdout() | Read the RSS feed's Item links and generate the PDF and save in the current date folder and showcase the logs in console |

6. <b>`--to-html`</b> :
 
| Command </br>(Python executable file)                                              | Command</br>(Setuptools Utility)                                            | Method Call                                       | Description                                                                                                               |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| python.exe .\rss_reader.py --to-html --url "https://news.yahoo.com/rss/"           | rss_reader_utility --to-html --url "https://news.yahoo.com/rss/"            | save_news_feed_to_html()                          | Read the RSS feed's Item links and generate the HTML and save in the current date folder                                  | 
| python.exe .\rss_reader.py --to-html --url "https://news.yahoo.com/rss/" --limit 1 | rss_reader_utility --to-html --url "https://news.yahoo.com/rss/" --limit 1  | save_news_feed_to_html()                          | Read the RSS feed's Item links and generate the HTML and save in the current date folder with limit                       |
| python.exe .\rss_reader.py --to-html --url "https://news.yahoo.com/rss/" --json    | rss_reader_utility --to-html --url "https://news.yahoo.com/rss/" --json     | save_news_feed_to_html()                          | <B>TODO :</B> Need to get clarity on requirement                                                                          |
| python.exe .\rss_reader.py --to-html --url "https://news.yahoo.com/rss/" --verbose | rss_reader_utility --to-html --url "https://news.yahoo.com/rss/"  --verbose | save_news_feed_to_html(), enable_logging_stdout() | Read the RSS feed's Item links and generate the HTML and save in the current date folder and showcase the logs in console |

----
<h2>Classes and respective Methods description</h2>
<b> Class :</b> <i>rss_reader.py and rss_reader_utility.py</i>
</BR></BR>
<b> Class :</b> <i>RSSFeedSupport.py</i>

| Methods                                                    | Description                                                                                                                     |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| fetch_rss_feed(url_value)                                  | Fetch the Entire RSS Feed Object                                                                                                |
| news_feed(url_value)                                       | Print all the RSS Feeds based on the URL provided : Required fields                                                             |
| news_feed_limit(url_value, limit_value)                    | Print limited RSS Feeds based on the URL provided : Required fields                                                             |
| save_news_feed_json(url_value, limit_value)                | Save all or limited RSS Feeds based on the URL provided in JSON formate with Current Date in YYYYMMDD formate: Required fields  |
| fetch_news_feed_date_limit(date_value, limit_value)        | Fetch all or limited RSS Feeds based on the URL provided in JSON formate with Current Date in YYYYMMDD formate: Required fields |
| fetch_news_feed_json_limit_date(limit_value, date_value)   | Fetch all or limited RSS Feeds based on the Date Provided offline in JSON formate: Required fields                              |
| save_news_feed_to_pdf(url_value, date_value, limit_value)  | Save all or limited RSS feeds in PDF formate , in the Folder with name as "YYYYMMDD" for Ex: 20220830                           |
| save_news_feed_to_html(url_value, date_value, limit_value) | Save all or limited RSS feeds in HTML formate , in the Folder with name as "YYYYMMDD" for Ex: 20220830                          |

<b> Class :</b> <i> DateUtil.py</i> 

| Methods                       | Description                                                             |
|-------------------------------|-------------------------------------------------------------------------|
| get_date_YYYYMMDD(date_value) | Checking if Date is passed, if not we will get current date in YYYYDDMM |

<b> Class :</b> <i>RSSFeedUtil.py</i>

| Methods                                                      | Description                                    |
|--------------------------------------------------------------|------------------------------------------------|
| print_all_feeds(entry)                                       | Print all available RSS feeds                  |
| print_range_feeds(entry, limit_value)                        | Print RSS feeds object with in a limit         |
| construct_json_all_feeds(entry, my_json_list)                | Constructs full List of JSON object            |
| construct_json_range_feeds(entry, limit_value, my_json_list) | Constructs List of JSON object with in a limit |

<b> Class :</b> <i>Utils.py</i>

| Methods                         | Description                                                  |
|---------------------------------|--------------------------------------------------------------|
| create_directory(full_dir_path) | Creates Directory if its no exist using os.path              |
| create_supporting_folder()      | Creates all the required folders to dump the generated files |

<b> Class :</b> <i>LoggingUtil.py</i>

| Methods                 | Description                                                  |
|-------------------------|--------------------------------------------------------------|
| enable_logging_stdout() | Print the logs in console or stdout if --verbose is provided |


<b> Class :</b> <i>Constants.py</i>
<br><br>Constant file is used to hold all the static values 


<b>Note :</b> Inorder to see the Process start and Completion please append ` --verbose `  in the command line

<BR><BR><BR>
JUNIT Test case:
<BR>I have installed coverage.py 

<BR>pip install coverage 
<BR>coverage run -m pytest .\tests\TestLoggingUtil.py
<BR>coverage report -m



| Class Name        | Stmts  | Miss   | Cover     |
|-------------------|--------|--------|-----------|
| Constants.py      | 12     | 0      | 100%      |
| DateUtil.py       | 9      | 0      | 100%      |
| LoggingUtil.py    | 11     | 0      | 100%      |
| RSSFeedSupport.py | 164    | 141    | 14%       | 
| RSSFeedUtil.py    | 43     | 0      | 100%      |
| Utils.py          | 21     | 6      | 71%       |
| <B>TOTAL          | <B>312 | <B>147 | <B>80.01% |
