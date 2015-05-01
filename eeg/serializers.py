from rest_framework import serializers
from models import Eeg
# Create your views here.

class EegSerializer(serializers.ModelSerializer):
	class Meta:
		model = Eeg
		field = ('id', 'name')
