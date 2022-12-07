from requests import get
import sys
import os
import pandas as pd

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
    ZipCode = sys.argv[1]
    Parameters= "?unitGroup=us&include=days&key="
    Key = os.environ['API_KEY']
    Type = '&contentType=csv'
    Days= sys.argv[2]
    URL = BaseURL + ZipCode + Parameters + Key + Type
    data = pd.read_csv(URL)
    data = data[["datetime","tempmax","tempmin","temp","feelslike","description"]]
    data.columns = ['Date','Max Temp','Min Temp', 'Temp','Feels Like','Description']
    print(data.head(int(Days)))
