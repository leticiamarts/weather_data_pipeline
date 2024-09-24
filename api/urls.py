from django.urls import path
from api.views import WeatherDataView, WeatherDataColumnView, test_view

urlpatterns = [
    path('weather/', WeatherDataView.as_view(), name='weather-list'),
    path('weather/<str:city>/', WeatherDataView.as_view(), name='weather-detail'),
    path('weather/column/<str:column>/', WeatherDataColumnView.as_view(), name='weather-column'),
    path('test/', test_view, name='test-view'),
]
