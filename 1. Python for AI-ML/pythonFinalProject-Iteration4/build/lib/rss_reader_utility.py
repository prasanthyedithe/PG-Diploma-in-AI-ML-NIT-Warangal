import argparse
import logging as log
import sys

import LoggingUtil
import RSSFeedSupport
import Utils


# Main method call by default
def main():
    parser = argparse.ArgumentParser()

    # Adding all the required argument
    parser.add_argument('--url', type=str, help='First argument is for RSS-Feed URL')
    parser.add_argument('--limit', type=int, nargs='?', const=0, help='Limit news topics if this parameter provided')
    parser.add_argument('--version', type=str, nargs='?', const='version', help='Print version info')
    parser.add_argument('--json', type=str, nargs='?', const='json', help='Print result as JSON in stdout')
    parser.add_argument('--verbose', type=str, nargs='?', const='verbose', help='Outputs verbose status messages')
    parser.add_argument('--date', type=str, help='Provide Date formate in YYYYMMDD to fetch new')
    parser.add_argument('--to-pdf', nargs='?', const='json', type=str, help='Provide RSS Feed URL and Date (optional '
                                                                            'in YYYYMMDD) to convert to PDF')
    parser.add_argument('--to-html', nargs='?', const='html', type=str, help='Provide RSS Feed URL to convert to HTML')

    # Creating the Supporting Folders to save the generated data
    Utils.create_supporting_folder()

    # Parse the argument
    args = parser.parse_args()

    if args.verbose:
        log.info("We are in args.verbose")
        LoggingUtil.enable_logging_stdout()

    if args.version:
        log.info("We are in args.version")
        print("Current Version:", sys.version)

    if args.url:
        if args.to_pdf:
            log.info("We are in args.url & args.to_pdf , args.limit : Optional")
            RSSFeedSupport.save_news_feed_to_pdf(args.url, args.limit)
            log.info("Process Completed Successfully !! ")
        elif args.to_html:
            log.info("We are in args.url & args.html, args.limit : Optional")
            RSSFeedSupport.save_news_feed_to_html(args.url, args.limit)
            log.info("Process Completed Successfully !! ")
        elif args.json:
            log.info("We are in args.url & args.json, args.limit : Optional")
            RSSFeedSupport.save_news_feed_json(args.url, args.limit)
            log.info("Process Completed Successfully !! ")
        elif args.limit:
            log.info("We are in args.url & args.limit")
            RSSFeedSupport.news_feed_limit(args.url, args.limit)
            log.info("Process Completed Successfully !! ")
        else:
            log.info("We are in args.url")
            RSSFeedSupport.news_feed(args.url)
            log.info("Process Completed Successfully !! ")
    elif args.json:
        log.info("We are in args.json & args.limit")
        if args.limit is None:
            args.limit = 0
        RSSFeedSupport.fetch_news_feed_json_limit_date(args.limit, args.date)
        log.info("Process Completed Successfully !! ")
    elif args.date:
        log.info("We are in args.date & args.limit")
        RSSFeedSupport.fetch_news_feed_date_limit(args.date, args.limit)
        log.info("Process Completed Successfully !! ")
