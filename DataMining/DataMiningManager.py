import pandas as pd

class DataMiningManager:
    def __init__(self):
        #url data
        self.url_template = 'http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=1706&Year={year}&Month={month}&Day=14&timeframe=1&submit=Download+Data'
    def get_data_month(self, year, month):
        #select month and year
        url = self.url_template.format(year=year, month=month)
        #load data
        try:
            weather_data = pd.read_csv(url, skiprows=15, index_col='Date/Time',
                                    parse_dates=True, encoding='latin1')
        except Exception:
            return None
        #formating data
        weather_data = weather_data.dropna(axis=1)
        weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]
        weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time', 'Data Quality'], axis=1)
        return weather_data

    def get_data_year(self, year):
        temp_data = [self.get_data_month(year, i) for i in range(1, 13)]
        weather_data = pd.concat(temp_data)
        return weather_data
