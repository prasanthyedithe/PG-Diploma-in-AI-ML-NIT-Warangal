Setup :
1. Create a project.
2. Set-up files and folder structure for Packaging.
3. Write Code for reading the RSS : rss_reader.py
4. Add and Update the requirement.txt to installed required plugins  

Package Installation : 
1. feedparser - pip install feedparser
2. python-dateutil - pip install python-dateutil
3. xmltodict - pip install xmltodict
4. virtualenv - pip install virtualenv virtualenv is basically an isolated python env where we can test our tools/scripts etc while not installing them on our system globally.
5. wheel - pip install wheel wheel is a packaging mechanism for python tools/packages.
6. setuptools - pip install setuptools setuptools is a library that we will use to package our tool.
7. twine - pip install twine twine is used for distributing the packages to pypi/test.pypi.
Install wkhtmltopdf : https://wkhtmltopdf.org/downloads.html
Set class path in Environment Variables
As oof now I have hardcoded the path in code for wkhtmltopdf : 


Example commands to Test : 
>> rss_reader.py --url "https://news.yahoo.com/rss/"
>> rss_reader.py -h
>> rss_reader.py --version
>> rss_reader.py --json --url "https://news.yahoo.com/rss/"
>> rss_reader.py --verbose
>> rss_reader.py --url "https://news.yahoo.com/rss/" --limit 1







>> python.exe .\rss_reader_plane.py --url "https://news.yahoo.com/rss/"
>> python.exe .\rss_reader.py --url "https://news.yahoo.com/rss/" --limit 1
>> python.exe .\rss_reader_plane.py --url "https://news.yahoo.com/rss/" --version
>> python.exe .\rss_reader.py --url "https://news.yahoo.com/rss/" --json
>> python.exe .\rss_reader_plane.py --url "https://news.yahoo.com/rss/" --verbose
>> python.exe .\rss_reader_plane.py --url "https://news.yahoo.com/rss/" --limit 1 --json

>> python.exe .\rss_reader_plane.py --json
>> python.exe .\rss_reader_plane.py --json --limit 1 
>> python.exe .\rss_reader_plane.py --json --date "20220825"
>> python.exe .\rss_reader_plane.py --json --limit 1 --date "20220825"

>> python.exe .\rss_reader_plane.py --verbose
>> python.exe .\rss_reader_plane.py --h
>> python.exe .\rss_reader_plane.py --version

>> python.exe .\rss_reader_plane.py --date "20220825"
>> python.exe .\rss_reader_plane.py --date "20220825" --limit 1
>> python.exe .\rss_reader_plane.py --date "20220825" --verbose

>> python.exe .\rss_reader_plane.py --to-pdf --url "http://feeds.aps.org/rss/recent/prstper.xml"
>> python.exe .\rss_reader_plane.py --to-pdf --url "http://feeds.aps.org/rss/recent/prstper.xml" --limit 1
>> // TODO : python.exe .\rss_reader_plane.py --to-pdf --url "http://feeds.aps.org/rss/recent/prstper.xml" --json
>> python.exe .\rss_reader_plane.py --to-pdf --url "http://feeds.aps.org/rss/recent/prstper.xml" --verbose
--date fetch values from the folder

>> python.exe .\rss_reader_plane.py --to-html --url "https://news.yahoo.com/rss/"
>> python.exe .\rss_reader_plane.py --to-html --url "https://news.yahoo.com/rss/" --limit 1
>> // TODO : python.exe .\rss_reader_plane.py --to-html --url "https://news.yahoo.com/rss/" --json
>> python.exe .\rss_reader_plane.py --to-html --url "https://news.yahoo.com/rss/"  --verbose
--date fetch values from the folder

TESTING
ADD/UPDATE LOGS
EXCEPTION

