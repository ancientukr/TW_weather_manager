from rest_pandas import PandasSimpleView
from django.shortcuts import render
from DataMining.DataMiningManager import DataMiningManager

def index(request):
    return render(request, 'main/main.html')

class WeatherYear(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
        dm_manager = DataMiningManager()
        data = dm_manager.get_data_year(year=kwargs['year'])
        return data

class WeatherMonth(PandasSimpleView):
    def get_data(self, request, *args, **kwargs):
        dm_manager = DataMiningManager()
        data = dm_manager.get_data_month(year=kwargs['year'], month=kwargs['month'])
        return data


