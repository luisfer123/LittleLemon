from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers

# Create your views here.
def sayHello(request):
    return HttpResponse('Hello world!')

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
