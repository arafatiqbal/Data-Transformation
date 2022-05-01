from calendar import day_abbr
import pandas as pd
from regex import E
import re

#Using usecols
data = pd.read_csv('books.csv', usecols=['Identifier','Place of Publication','Date of Publication','Publisher','Title','Author','Contributors','Flickr URL'])

# Using Drop
DataDrop = pd.read_csv('books.csv')
DataDrop.drop('Edition Statement', inplace=True, axis=1)
DataDrop.drop('Corporate Author', inplace=True, axis=1)
DataDrop.drop('Issuance type', inplace=True, axis=1)
DataDrop.drop('Corporate Contributors', inplace=True, axis=1)
DataDrop.drop('Former owner', inplace=True, axis=1)
DataDrop.drop('Engraver', inplace=True, axis=1)
DataDrop.drop('Shelfmarks', inplace=True, axis=1)

data["Date of Publication"] = data["Date of Publication"].str.replace(r'[][]', '', regex=True)


print(data['Date of Publication'])
