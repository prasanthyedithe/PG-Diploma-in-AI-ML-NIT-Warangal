from datetime import date
import logging as log


def get_date_YYYYMMDD(date_value):
    log.info("In get_date_YYYYMMDD(date_value)")
    # Checking if Date is passed, if not we will get current date to create folder
    if date_value is None:
        today = date.today()
        current_date = today.strftime("%Y%m%d")
        return current_date
    return date_value
