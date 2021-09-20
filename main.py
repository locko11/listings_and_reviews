from config import *
from create_db import db_builder
from db import DBCOntroller
from nebrhd_sugg import select_sugg, select_reviews


def print_names():
    print('Name of listing table. For example - "listings"')
    print('listings_name:')
    listings_name = input()
    print('Name of reviews table. For example - "reviews"')
    print('reviews_name:')
    reviews_name = input()
    return listings_name, reviews_name


def tables_constructor(db):
    while True:
        print('To create new tables fill... :')
        listings_name, reviews_name = print_names()
        print(
            'Path for csv file with information for reviews. For example - "C:/Users/User/Desktop/csvs/reviews_detailed.csv".' \
            'Use only "/" for path separating')
        print('Provide path to reviews_detailed.csv:')
        print('reviews_path:')
        reviews_path = input()
        print(
            'Path for csv file with information for listings. For example - "C:/Users/User/Desktop/csvs/listings.csv".' \
            'Use only "/" for path separating')
        print('Provide path to listings.csv:')
        print('listing_path:')
        listing_path = input()
        continue_point = db_builder(db, listings_name=listings_name, reviews_name=reviews_name, \
                                    reviews_path=reviews_path, listing_path=listing_path)
        if continue_point:
            return listings_name, reviews_name


def start():
    db = DBCOntroller(DB_CREDENTIALS)
    listings_name, reviews_name = '', ''
    while True:
        print('You should choose tables for start!')
        print(f'You choose tables listings_name={listings_name} and reviews_name={reviews_name}')
        print('Choose your way: \n'
              'press 1 to select suggestions for the neighbourhood.\n'
              'press 2 to listings from the neighbourhood with reviews for the listings.\n'
              'press 3 to create new tables.\n'
              'press 4 to choose if it\'s already created tables.\n'
              '"q" - for quite.')
        choose = input()
        if choose == '1':
            print(f'You choose tables {listings_name} and {reviews_name}')
            select_sugg(db, listings_name)
        elif choose == '2':
            print(f'You choose tables {listings_name} and {reviews_name}')
            select_reviews(db, listings_name, reviews_name)
        elif choose == '3':
            listings_name, reviews_name = tables_constructor(db)
        elif choose == '4':
            listings_name, reviews_name = print_names()
        elif choose == 'q':
            return None


if __name__ == '__main__':
    start()
