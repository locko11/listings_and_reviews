import pandas as pd
import re
from tabulate import tabulate

from db import DBCOntroller


pd.options.display.width = None
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pdtabulate = lambda df: tabulate(df, headers='keys', tablefmt='psql')


class NbrhdNotValid(Exception):
    def __init__(self, mess):
        self.message = mess
        super().__init__(self.message)


def nbrhd_validator(neighbourhood):
    words = re.split(r"\W+", neighbourhood)
    for w in words:
        if not w.isalpha():
            mess = f"Your neighbourhood name ({neighbourhood}) is not valid, " \
                   "try W and use only letters from unicode and punctuation marks"
            raise NbrhdNotValid(mess)


def select_sugg(db: DBCOntroller, listings_name):
    try:
        print("Print neighbourhood name that you want to select:")
        neighbourhood = input()
        nbrhd_validator(neighbourhood)
    except NbrhdNotValid as e:
        print(e)
        return None
    sess = db.create_sess()
    listings = db.get_table_object(listings_name)
    selected_list = sess.query(listings).filter(listings.columns.neighbourhood == neighbourhood)

    df = pd.DataFrame(selected_list, columns=listings.columns.keys())
    print(f'Selected info for neighbourhood = {neighbourhood}:\n{pdtabulate(df)}')
    sess.close()


def select_reviews(db: DBCOntroller, listings_name, reviews_name):
    try:
        print("Print neighbourhood name that comments you want to select:")
        neighbourhood = input()
        nbrhd_validator(neighbourhood)
    except NbrhdNotValid as e:
        print(e)
        return None
    sess = db.create_sess()
    reviews = db.get_table_object(reviews_name)
    listings = db.get_table_object(listings_name)

    columns = [listings.columns.name, listings.columns.host_name, listings.columns.calculated_host_listings_count, \
               reviews.columns.reviewer_name, reviews.columns.comments]
    selected_list = sess.query(*columns).join(listings).filter(listings.columns.neighbourhood == neighbourhood)
    df = pd.DataFrame(selected_list, columns=columns)
    print(f'Selected info for neighbourhood = {neighbourhood}:\n{pdtabulate(df)}')
    sess.close()
