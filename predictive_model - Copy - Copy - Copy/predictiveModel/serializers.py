from rest_framework import serializers
from predictiveModel.models import Predictions


class AllPredictionsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predictions
        fields = '__all__'


class PagePredictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predictions
        fields = ('UUID', 'truckLicenseNumber', 'truckModelNumber', 'dateTime', 'nextMaintenance')
