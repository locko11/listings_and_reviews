import csv

import pandas as pd
from sqlalchemy.engine import create_engine
from sqlalchemy.exc import InternalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Table, MetaData

engine = create_engine('postgresql://postgres:lockopgrev66@localhost:5432/test3')
Base = declarative_base()
meta_data = MetaData(bind=engine)


class DBCOntroller:

    def __init__(self, db):
        self.engine = create_engine(db)
        self.meta_data = MetaData(bind=engine)

    def create_sess(self):
        return sessionmaker(bind=engine)()

    def create_table_from_csv(self, csv_path, table_name):
        try:
            with open(csv_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                df = pd.DataFrame(data=reader, columns=reader.fieldnames)
        except Exception as e:
            print(f"Wrong csv path. Error: {e}")
            return False
        with engine.begin() as connection:
            try:
                df.to_sql(table_name, con=connection, index=False)
                return True
            except Exception as e:
                print(f"Table {table_name} havn't created. Error: {e}")
                return False

    def add_foringin_kay(self, table, column, ref_table, ref_column, session):
        statement = f"ALTER TABLE {table} ADD " \
                    f"FOREIGN KEY({column}) REFERENCES {ref_table}({ref_column});"
        session.execute(statement)

    def add_primary(self, table, column, session):
        statement = f"ALTER TABLE {table} ADD PRIMARY KEY ({column});"
        q = session.execute(statement)

    def get_table_object(self, table):
        return Table(table, self.meta_data, autoload=True, autoload_with=engine)

    def drop_table(self, table: Table) -> None:
        try:
            table.drop(engine)
        except InternalError as e:
            print(e)
            return None
        print(f"Table {table} droped.")

    def tables_name(self):
        return engine.table_names()
