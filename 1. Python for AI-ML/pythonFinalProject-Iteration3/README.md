Setup :
1. Create your Command Line Script.
2. Set-up files and folder structure for Packaging.
3. Write Code for reading the RSS : rss_reader.py
4. Modify your setup.py file to incorporate your CLI scripts. 
5. Add and Update the requirement.txt to installed required plugins 
6. Test your package before publishing and then Build. : $ python setup.py install
7. Upload on pypi and publish your package : python setup.py sdist bdist_wheel
8. Install your newly-published package. : pip install pythonFinalProject_Iteration3


Package Installation : 
1. virtualenv - pip install virtualenv virtualenv is basically an isolated python env where we can test our tools/scripts etc while not installing them on our system globally.
2. wheel - pip install wheel wheel is a packaging mechanism for python tools/packages.
3. setuptools - pip install setuptools setuptools is a library that we will use to package our tool.
4. twine - pip install twine twine is used for distributing the packages to pypi/test.pypi.

Example commands to Test : 
NOTE: if using --json we need the --url as well to get data in JSON formate
>> rss_reader --date 202208211 
>> rss_reader --date 202208211 --json --url "https://news.yahoo.com/rss/"
>> rss_reader --date 202208211 --verbose