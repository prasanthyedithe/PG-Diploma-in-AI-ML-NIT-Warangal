import argparse, feedparser, sys, json, xmltodict, urllib.request, logging as log
from datetime import date
from os.path import exists

datacaching_path = "./datacaching/"

def news_feed(args_value):
    newsfeed = feedparser.parse(args_value.url)
    entry = newsfeed.entries[1]
    print("Keys : ", entry.keys())
    print("Title : ", entry.title)
    print("Link : ", entry.link)
    print("Links : ", entry.links)
    print("Media Content : ", entry.media_content)


def news_feed_json(url_value):
    with urllib.request.urlopen(url_value) as response:
        data_dict = xmltodict.parse(response.read())
        json_data = json.dumps(data_dict)
        print(json_data)
        today = date.today()
        current_date = today.strftime("%Y%m%d")
        # if required we can add to the File
        with open(datacaching_path + current_date + ".json", "w") as json_file:
            json_file.write(json_data)
            json_file.close()
            response.close()

def news_feed_date(date_value):
    if exists(datacaching_path + date_value + ".json"):
        with open(datacaching_path + date_value + ".json") as f:
            data = json.load(f)
            print(data)
    else:
        print("No Latest New Available !!")

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--url', type=str, help='First argument is for RSS-Feed URL')
parser.add_argument('--limit', type=int, help='Limit news topics if this parameter provided')
parser.add_argument('--version', type=str, nargs='?', const='version', help='Print version info')
parser.add_argument('--json', type=str, nargs='?', const='json', help='Print result as JSON in stdout')
parser.add_argument('--verbose', type=str, nargs='?', const='verbose', help='Outputs verbose status messages')
parser.add_argument('--date', type=str, help='Provide Date formate in YYYYMMDD to fetch new')

# Parse the argument
args = parser.parse_args()

if args.version:
    log.info("We are in args.version")
    print("Current Version:", sys.version)

if args.url:
        log.info("We are in args.url")
        print('URL :,', args.url)
        news_feed(args)

if args.url and args.limit:
    log.info("We are in args.url & args.limit")
    print('URL :,', args.url)
    print('limit :,', args.limit)
    news_feed(args)

if args.url and args.json:
    log.info("We are in args.url & args.json")
    news_feed_json(args.url)

if args.date:
    log.info("We are in args.date")
    news_feed_date(args.date)

if args.verbose:
    log.info("INFO We are in args.verbose")
    log.warning("WARNING We are in args.verbos")
    log.error("ERROR We are in args.verbos")
    log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
    log.info("Verbose output.")
else:
    log.info("We are in else statement args.verbose")
    log.basicConfig(format="%(levelname)s: %(message)s")
