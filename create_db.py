from os import path
from pathlib import Path

from db import DBCOntroller


def check_naming(db, csv_path, table_name):
    if table_name in db.tables_name():
        print(f"Table with name {table_name} already exists.")
        print(f"Rename table(press 'r') or continue with existing(press any key except 'r').")
        choice = input()
        if choice == "r":
            return False
        else:
            return True

    return db.create_table_from_csv(csv_path, table_name)


def db_builder(db, listing_path, reviews_path, listings_name, reviews_name):
    print('Creating tables...')
    if check_naming(db, listing_path, listings_name) and \
            check_naming(db, reviews_path, reviews_name):
        try:
            sess = db.create_sess()
            db.add_primary(listings_name, 'id', session=sess)
            db.add_primary(reviews_name, 'id', session=sess)
            db.add_foringin_kay(reviews_name, 'listing_id', listings_name, 'id', session=sess)
            sess.commit()
        except Exception as e:
            sess.rollback()
            db.drop_table(db.get_table_object(listings_name))
            db.drop_table(db.get_table_object(reviews_name))
            print(e)
            sess.close()
            return False
        sess.close()
        print('Tables created!')
        return True
    else:
        return False
