import csv
import re
import string

    # Get input and output vectors from file, build dataset
__all__ = ['extractData', 'formatData']
def extractData(file_name):
    """ Takes csv file path.
        Returns list of list of strings. """
    data = []
    with open(file_name, 'rb') as csv_file:
        reader = csv.reader(csv_file, dialect='excel')
        for row in reader:# row is now a list of entries in that row
            data += [row]
    return data



def formatData(extracted_data):
    """ Takes list of list of strings,
        Returns list of list of formated values. """
    formated_data = []
    for row in extracted_data:
        formated_row = []
        for entry in row:
            
            # Handling alternative Names
            entry = re.sub(r'Korea, North', 'North Korea', entry)
            entry = re.sub(r"Democratic People's Republic of Korea", 'North Korea', entry)
            entry = re.sub(r"Republic of Korea", 'South Korea', entry)
            
            entry = re.sub(r"People's Republic of China", "China", entry)
            entry = re.sub(r'Republic of China \(Taiwan\)', 'Taiwan', entry)

            entry = re.sub(r'DR Congo', 'Congo', entry)            
            entry = re.sub(r'Russian Federation', 'Russia', entry)
            entry = re.sub(r'United States of America', 'United States', entry)
            entry = re.sub(r'United Republic of Tanzania', 'Tanzania', entry)
            entry = re.sub(r'Slovakia', 'Slovak Republic', entry)
            entry = re.sub(r'United States Virgin Islands', 'U.S. Virgin Islands', entry)
            
            # Handling weird characters
            entry = re.sub(r"C.*?Ivoire", "Cote d'Ivoire", entry)
            entry = re.sub(r'R.union', "Reunion", entry)
            entry = re.sub(r'S.*?ncipe', "Sao Tome and Principe", entry)
            entry = re.sub(r"Cura.ao", "Curacao", entry)
            
            # remove formating vestages
            entry = entry.replace("#!", "")# get rid of #VALUE! error
            entry = entry.replace("*", "")    # get rid of *  astriks
            entry = entry.replace("\n", "")   # get rid of \n new lines
            entry = entry.replace("?", "")    # get rid of ?  question marks
            entry = re.sub(r'.*VALUE.*', "", entry) # Get rid of anything following an exclaimation point
            
            entry = re.sub(r'[!].*', "", entry) # Get rid of anything following an exclaimation point
            entry = re.sub(r'[,].*', "", entry) # Get rid of anything following a camma
            
            entry = re.sub(r'\[.*?\]', "", entry) # Get rid of brakets and anything in them
            entry = re.sub(r'A$', "", entry) # Get rid of any 'A's that are at the end for whyever
            entry = re.sub(r'[a-z].*[0-9]$', "", entry) # Get rid of any numbers that are after letters
            
            
            entry = re.sub(r'the ', "", entry) # Get rid of any 'the's
            entry = re.sub(r'The ', "", entry) # Get rid of any 'The's
            entry = re.sub(r'Democratic ', '', entry)  # Get rid of any 'Democratic' decoration
            entry = re.sub(r'Republic of ', '', entry) # Get rid of any 'Republic of' decoration
            
            entry = re.sub(r' *$', "", entry) # Get rid of trailing spaces
            entry = re.sub(r'^ *', "", entry) # Get rid of leading spaces

            formated_row += [entry]
        formated_data += [formated_row]
    return formated_data




