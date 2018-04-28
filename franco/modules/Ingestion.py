from sqlalchemy import create_engine
import psycopg2
import psycopg2.extras
import pandas as pd
import csv

class Ingestion(object):
    """This is the ingestion class to deal with csv directly from the same directory where this module is"""

    def __init__(self, file, sep = ",", header =0):
        self.file = file
        self.delimiter = sep
        self.df = pd.read_csv(file, sep= sep, header=header, engine='python')

    def file_csv(self):
        return self.df

class IngestionDatabase(object):

    """ This is the ingestion class to deal with postgress database """
    def __init__(self, database, query):
        self.engine = create_engine(database)
        self.table_names = self.engine.table_names()
        self.con = self.engine.connect()
        self.rs = self.con.execute(query)
        self.df = pd.DataFrame(self.rs.fetchmany(size=15))

    def cols(self):
        self.df.columns = self.rs.keys()
        return self.df









# test objects Ingestion class:
# ingest = Ingestion('DC_Crime_Official.csv')
# data = ingest.file_csv()
# print (a.info())


#test objects DatabaseClass:
#ingest2 = IngestionDatabase('postgresql://postgres:postgres@localhost:5432/DC_crime','SELECT * FROM dc_crime_data3')
#data2 = ingest2.cols()
#print (data2.info())
