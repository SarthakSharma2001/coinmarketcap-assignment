from django.http import JsonResponse
from .models import CryptoData
from .serializers import CryptoDataSerializer
from rest_framework.decorators import api_view
from .services.scrapper_wrapper import fetch_data
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def crypto_prices(request):
    if request.method == 'GET':
        top_10 = CryptoData.objects.filter(current_top_10=True)
        serializer = CryptoDataSerializer(top_10, many=True)
        res = {"crypto_prices": serializer.data}
        return JsonResponse(res)

    if request.method == 'POST':
        new_top_10 = fetch_data()

        for i in new_top_10:
            if CryptoData.objects.filter(name=i['name']).exists():
                # Update the Results
                # obj = CryptoData.objects.filter(name=i['name'])
                # obj.price = i['price']
                # obj.one_hour = i['one_hour']
                # obj.twentyfour_hour = i['twentyfour_hour']
                # obj.seven_day = i['seven_day']
                # obj.market_cap = i['market_cap']
                # obj.volume = i['volume']
                # obj.suppy = i['suppy']
                # obj.current_top_10 = True
                #
                # obj.save()

                obj = CryptoData.objects.filter(name=i['name'])

                obj.delete()

                serializer = CryptoDataSerializer(data=i)
                if serializer.is_valid():
                    serializer.save()

            else:
                # Create New Record
                serializer = CryptoDataSerializer(data=i)
                if serializer.is_valid():
                    serializer.save()

        return Response(status=status.HTTP_201_CREATED)