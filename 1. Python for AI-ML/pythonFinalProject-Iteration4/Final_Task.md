# Introduction to Python. Final task.
You are proposed to implement Python RSS-reader using  **python 3.9**.

The task consists of few iterations. Do not start new iteration if the previous one is not implemented yet.

## Common requirements.
* It is mandatory to use `argparse` module.
* Codebase must be covered with unit tests with at least 50% coverage. It's a mandatory requirement.
* Yor script should **not** require installation of other services such as mysql server,
postgresql and etc. (except Iteration 6). If it does require such programs,
they should be installed automatically by your script, without user doing anything.
* In case of any mistakes utility should print human-readable.
error explanation. Exception tracebacks in stdout are prohibited in final version of application.
* Docstrings are mandatory for all methods, classes, functions and modules.
* Code must correspond to `pep8` (use `pycodestyle` utility for self-check).
  * You can set line length up to 120 symbols.
* Commit messages should provide correct and helpful information about changes in commit. Messages like `Fix bug`, 
`Tried to make workable`, `Temp commit` and `Finally works` are prohibited.
* All used third-party packages should be written in the `requirements.txt` file and in installation files (`setup.py`, `setup.cfg`, etc.).
* You have to write a file with documentation. Everything must be documented: how to run scripts, how to run tests, how to install the library and etc.

## [Iteration 1] One-shot command-line RSS reader.
RSS reader should be a command-line utility which receives [RSS](wikipedia.org/wiki/RSS) URL and prints results in human-readable format.

You are free to choose format of the news console output. The textbox below provides an example of how it can be implemented:

```shell
$ rss_reader.py "https://news.yahoo.com/rss/" --limit 1

Feed: Yahoo News - Latest News & Headlines

Title: Nestor heads into Georgia after tornados damage Florida
Date: Sun, 20 Oct 2019 04:21:44 +0300
Link: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html

[image 2: Nestor heads into Georgia after tornados damage Florida][2]Nestor raced across Georgia as a post-tropical cyclone late Saturday, hours after the former tropical storm spawned a tornado that damaged
homes and a school in central Florida while sparing areas of the Florida Panhandle devastated one year earlier by Hurricane Michael. The storm made landfall Saturday on St. Vincent Island, a nature preserve
off Florida's northern Gulf Coast in a lightly populated area of the state, the National Hurricane Center said. Nestor was expected to bring 1 to 3 inches of rain to drought-stricken inland areas on its
march across a swath of the U.S. Southeast.


Links:
[1]: https://news.yahoo.com/wet-weekend-tropical-storm-warnings-131131925.html (link)
[2]: http://l2.yimg.com/uu/api/res/1.2/Liyq2kH4HqlYHaS5BmZWpw--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media.zenfs.com/en/ap.org/5ecc06358726cabef94585f99050f4f0 (image)

```

Utility should provide the following interface:
```shell
usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]
                     source

Pure Python command-line RSS reader.

positional arguments:
  source         RSS URL

optional arguments:
  -h, --help     show this help message and exit
  --version      Print version info
  --json         Print result as JSON in stdout
  --verbose      Outputs verbose status messages
  --limit LIMIT  Limit news topics if this parameter provided

```

In case of using `--json` argument your utility should convert the news into [JSON](https://en.wikipedia.org/wiki/JSON) format.
You should come up with the JSON structure on you own and describe it in the README.md file for your repository or in a separate documentation file.



With the argument `--verbose` your program should print all logs in stdout.

### Task clarification (I)

1) If `--version` option is specified app should _just print its version_ and stop.
2) User should be able to use `--version` option without specifying RSS URL. For example:
```
> python rss_reader.py --version
"Version 1.4"
```
3) The version is supposed to change with every iteration.
4) If `--limit` is not specified, then user should get _all_ available feed.
5) If `--limit` is larger than feed size then user should get _all_ available news.
6) `--verbose` should print logs _in the process_ of application running, _not after everything is done_.
7) Make sure that your app **has no encoding issues** (meaning symbols like `&#39` and etc) when printing news to _stdout_.
8) Make sure that your app **has no encoding issues** (meaning symbols like `&#39` and etc) when printing news to _stdout in JSON format_.
9) It is preferrable to have different custom exceptions for different situations(If needed).
10) The `--limit` argument should also affect JSON generation.


## [Iteration 2] Distribution.

* Utility should be wrapped into distribution package with `setuptools`.
* This package should export CLI utility named `rss-reader`.


### Task clarification (II)
 
1) User should be able to run your application _both_ with and without installation of CLI utility,
meaning that this should work:

```
> python rss_reader.py ...
```

as well as this:  

```
> rss_reader ...
```
2) Make sure your second iteration works on a clean machie with python 3.9. (!)
3) Keep in mind that installed CLI utility should have the same functionality, so do not forget to update dependencies and packages.


## [Iteration 3] News caching.
The RSS news should be stored in a local storage while reading. The way and format of this storage you can choose yourself.
Please describe it in a separate section of README.md or in the documentation.

New optional argument `--date` must be added to your utility. It should take a date in `%Y%m%d` format.
For example: `--date 20191020`
Here date means actual *publishing date* not the date when you fetched the news.

The cashed news can be read with it. The new from the specified day will be printed out.
If the news are not found return an error.

If the `--date` argument is not provided, the utility should work like in the previous iterations.

### Task clarification (III)
1) Try to make your application crossplatform, meaning that it should work on both Linux and Windows.
For example when working with filesystem, try to use `os.path` lib instead of manually concatenating file paths.
2) `--date` should **not** require internet connection to fetch news from local cache.
3) User should be able to use `--date` without specifying RSS source. For example:
```
> python rss_reader.py --date 20191206
......
```
Or for second iteration (when installed using setuptools):
```
> rss_reader --date 20191206
......
```
4) If `--date` specified _together with RSS source_, then app should get news _for this date_ from local cache that _were fetched from specified source_.
5) `--date` should work correctly with both `--json`, `--limit`, `--verbose` and their different combinations.

## [Iteration 4] Format converter.

You should implement the conversion of news in at least two of the suggested format: `.mobi`, `.epub`, `.fb2`, `.html`, `.pdf`

New optional argument must be added to your utility. This argument receives the path where new file will be saved. The arguments should represents which format will be generated.

For example:  `--to-mobi` or `--to-fb2` or `--to-epub`

You can choose yourself the way in which the news will be displayed, but the final text result should contain pictures and links, if they exist in the original article and if the  format permits to store this type of data.

### Task clarification (IV)

Convertation options should work correctly together with all arguments that were implemented in Iterations 1-3. For example: 
* Format convertation process should be influenced by `--limit`.
* If `--json` is specified together with convertation options, then JSON news should 
be printed to stdout, and converted file should contain news in normal format.
* Logs from `--verbose` should be printed in stdout and not added to the resulting file.
* `--date` should also work correctly with format converter and to not require internet access.

## * [Iteration 5] Output colorization.
> Note: An optional iteration, it is not necessary to implement it. You can move on with it only if all the previous iterations (from 1 to 4) are completely implemented.

You should add new optional argument `--colorize`, that will print the result of the utility in colorized mode.

*If the argument is not provided, the utility should work like in the previous iterations.*

> Note: Take a look at the [colorize](https://pypi.org/project/colorize/) library

## * [Iteration 6] Web-server.
> Note: An optional iteration, it is not necessary to implement it. You can move on with it only if all the previous iterations (from 1 to 4) are completely implemented. Introduction to Python course does not cover the topics that are needed for the implementation of this part.

There are several mandatory requirements in this iteration:
* `Docker` + `docker-compose` usage (at least 2 containers: one for web-application, one for DB)
* Web application should provide all the implemented in the previous parts of the task functionality, using the REST API:
    * One-shot conversion from RSS to Human readable format
    * Server-side news caching
    * Conversion in epub, mobi, fb2 or other formats
    
Feel free to choose the way of implementation, libraries and frameworks. (We suggest you `Django Rest Framework` + `PostgreSQL` combination)

You can implement any functionality that you want. The only requirement is to add the description into README file or update project documentation, for example:
* authorization/authentication
* automatic scheduled news update
* adding new RSS sources using API

---
Implementations will be checked with the latest cPython interpreter of 3.9 branch.
---

> Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. Code for readability. **John F. Woods**
