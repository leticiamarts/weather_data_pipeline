from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from api.models import WeatherData
from api.controllers.serializers import WeatherDataSerializer

from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Django está funcionando!")

class WeatherDataView(generics.ListCreateAPIView, generics.RetrieveAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

    def get(self, request, city=None):
        if city:
            try:
                weather_data = WeatherData.objects.get(city=city)
                serializer = self.get_serializer(weather_data)
                return Response(serializer.data)
            except WeatherData.DoesNotExist:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return self.list(request)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WeatherDataColumnView(generics.ListAPIView):
    serializer_class = WeatherDataSerializer

    def get_queryset(self):
        column = self.kwargs['column']
        return WeatherData.objects.values_list(column, flat=True)

