from django.shortcuts import render
from rest_framework import generics
from serializers import EegSerializer
from models import Eeg
# Create your views here.

class EegList(generics.ListCreateAPIView):
	queryset = Eeg.objects.all()
	serializer_class = EegSerializer
	

class EegDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Eeg.objects.all()
	serializer_class = EegSerializer
