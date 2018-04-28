from Ingestion import *
from numpy import nan as NA
from datetime import datetime
import re
# creating the database object to work with:

ingest = Ingestion('DC_Crime_Official.csv')
data = ingest.file_csv()


#Explore row content in columns of use:

class Wrangling(object):

# drop empty rows
    def dropNA(self, data= data):
        self.df = data.dropna(how='all')
        return self.df

    def offense_column(self, text1 ='theft/other', text2 ='theft f/auto', text3 = 'assault w/dangerous weapon',
                       repl1 = 'theft', repl2 = 'auto theft', repl3 = 'assault with weapon' ):

        """There are 9 categories of offenses here:
        This function will transform the caterogies into more readable text
        for example : assault w/dangerous weapon = assault with dangerous weapon"""

        self.df['offense_text'] = self.df['offense_text'].replace([text1, text2, # add the column name to the arguments.
        text3], [repl1, repl2, repl3])
        return self.df

    def date_time_parser(self, time = 'start_date'):
        ''' transform into datetime 64 object'''
        self.df[time] = pd.to_datetime(self.df['start_date'])
        return self.df


    def latlong_cutter(self):
        """ Reduce the presition of the lat long data by cutting them."""
        self.newlat = []
        self.newlon = []
        for item in self.df['latitude']:
            item = str(item)
            item = float(item[0:6])
            self.newlat.append(item)

        self.df['latitude'] = self.newlat

        for item in self.df['longitude']:
            item = str(item)
            item = float(item[0:7])
            self.newlon.append(item)
        self.df['longitude'] = self.newlon

        return self.df

    def lat_long_rounder(self, decimals = 3):
        """ Reduce the presition of the lat long data by rounging decimals"""
        self.df['latitude'] = self.df['latitude'].round(decimals = decimals)
        self.df['longitude'] = self.df['longitude'].round(decimals = decimals)
        return self.df

    def adress_format_modifier(self):
        """This columns replace some of the content from the block columns to it is easy to parse it"""

        self.splitted = []
        # creating the splited column
        for row in self.df['block']:
            row = row.replace("block of ", "")
            row = row.replace("street", "St")
            row = row.replace("-", "")
            row = row.split(' ', 1)
            self.splitted.append(row)
        self.df['splitted'] = self.splitted

    def block_parser(self):
""" This is the block parser that separate block in start and en blocks"""

        self.startblock = []
        self.endblock_1 = []
        self.endblock = []
        #  create column 'startblock'
        for row in self.df['splitted']:
            row = row[0]
            self.startblock.append(row)
        self.df['startblock'] = self.startblock
        # create column  'endblock_1'
        for row in self.df['splitted']:
            row = row[-1].lstrip() # enblock_1
            row = row.split(' ',1)
            self.endblock_1.append(row)
        self.df['endblock_1'] = self.endblock_1
        # create column  'endblock'
        for row in self.df['endblock_1']:
            row = row[0]
            self.endblock.append(row)
        self.df['endblock'] = self.endblock

    def street_parser(self):
        self.street = []
        #creating column 'street'
        for row in self.df['endblock_1']:
            row = row[1]
            self.street.append(row)
        self.df['street'] = self.street



###############################3 adding new crime score columns functions #################################################################3


Obj = Wrangling()
data =  Obj.dropNA()
new_offense_colum = Obj.offense_column()
#print (new_offense_colum)


new_time_column = Obj.date_time_parser()
latlong_rounded = Obj.lat_long_rounder()
#latlong_cutted = Obj.latlong_cutter()
adress = Obj.adress_format_modifier()
block =Obj.block_parser()
street = Obj.street_parser()




#print (latlong_rounded['latitude'])
#print (latlong_rounded['longitude'])
#print (latlong_cutted['latitude'])
#print (data['splitted'].head(100))
#print (data['startblock'].head(100))
#print (data['endblock_1'].head(100))
#print (data['endblock'].head(100))
#print (data['street'].head(100))



#data.to_csv('test2.csv', float_format='%.3f')



print (data.info())
#print (new_time_column['start_date'])
#print (data['start_date'])
