from django.shortcuts import render
from .models import Shop
import math

def haversine(lat1, lon1, lat2, lon2):
    # Haversine formula to calculate distance between two points
    R = 6371  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def search_shops(request):
    user_lat = float(request.GET.get('latitude', 0))
    user_lon = float(request.GET.get('longitude', 0))

    shops = Shop.objects.all()
    shop_distances = []

    for shop in shops:
        distance = haversine(user_lat, user_lon, shop.latitude, shop.longitude)
        shop_distances.append({'shop': shop, 'distance': distance})

    sorted_shops = sorted(shop_distances, key=lambda x: x['distance'])

    return render(request, 'shops/search_results.html', {'shops': sorted_shops})
from django.shortcuts import render
from .models import Shop
import math

def haversine(lat1, lon1, lat2, lon2):
    # Haversine formula to calculate distance between two points
    R = 6371  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def search_shops(request):
    user_lat = float(request.GET.get('latitude', 0))
    user_lon = float(request.GET.get('longitude', 0))

    shops = Shop.objects.all()
    shop_distances = []

    for shop in shops:
        distance = haversine(user_lat, user_lon, shop.latitude, shop.longitude)
        shop_distances.append({'shop': shop, 'distance': distance})

    sorted_shops = sorted(shop_distances, key=lambda x: x['distance'])

    return render(request, 'shops/search_results.html', {'shops': sorted_shops})
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ShopSerializer

@api_view(['GET'])
def shop_list_api(request):
    shops = Shop.objects.all()
    serializer = ShopSerializer(shops, many=True)
    return Response(serializer.data)

