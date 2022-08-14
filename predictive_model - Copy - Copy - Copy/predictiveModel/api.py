from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .serializers import *
from .influence import *
from .misc import *
import json
from django.http import HttpResponse


class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print('UserAuthentication called')
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(token.key)
        return Response(token.key)


class PredictionsList(APIView):

    def get(self, request):
        model = Predictions.objects.all()
        for each in model:
            each.currentSpeed, each.totalFuelUsed, each.rpm, each.totalDistance, each.wheelSpeed, each.engineTemp, each.engineLoad, each.engineHours, each.nextMaintenance = misc().data(
                each.currentSpeed, each.totalFuelUsed, each.rpm, each.totalDistance, each.wheelSpeed, each.engineTemp,
                each.engineLoad, each.engineHours)
            obj, created = Predictions.objects.update_or_create(
                UUID=each.UUID,
                defaults={'dateTime': datetime.now(), 'currentSpeed': each.currentSpeed,
                          'totalFuelUsed': each.totalFuelUsed, 'rpm': each.rpm, 'totalDistance': each.totalDistance,
                          'wheelSpeed': each.wheelSpeed, 'engineTemp': each.engineTemp, 'engineLoad': each.engineLoad,
                          'engineHours': each.engineHours, 'nextMaintenance': each.nextMaintenance},
            )
            list_Predictions.append(obj)
        serializer = PagePredictionsSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):  # single object
        UUID = request.data.get("UUID")
        truckLicenseNumber = request.data.get("truckLicenseNumber")
        truckModelNumber = request.data.get("truckModelNumber")
        currentDateTime = datetime.now()
        currentSpeed = request.data.get("currentSpeed")
        totalFuelUsed = request.data.get("totalFuelUsed")
        rpm = request.data.get("rpm")
        totalDistance = request.data.get("totalDistance")
        wheelSpeed = request.data.get("wheelSpeed")
        engineTemp = request.data.get("engineTemp")
        engineLoad = request.data.get("engineLoad")
        engineHours = request.data.get("engineHours")
        nextMaintenance = linearRegressionModel(currentSpeed, totalFuelUsed, rpm, totalDistance, wheelSpeed, engineTemp,
                                                engineLoad, engineHours)

        model = Predictions.objects.create(UUID=UUID, truckLicenseNumber=truckLicenseNumber,
                                           truckModelNumber=truckModelNumber, dateTime=currentDateTime,
                                           currentSpeed=currentSpeed, totalFuelUsed=totalFuelUsed, rpm=rpm,
                                           totalDistance=totalDistance, wheelSpeed=wheelSpeed, engineTemp=engineTemp,
                                           engineLoad=engineLoad, engineHours=engineHours,
                                           nextMaintenance=nextMaintenance)

        serializer = AllPredictionsDetailsSerializer(data=model.__dict__)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PredictionDetails(APIView):
    def get(self, request, uuid):
        try:
            model = Predictions.objects.get(UUID=uuid)
        except Predictions.DoesNotExist:
            return Response(f'truck with uuid {uuid} doest not exists', status=status.HTTP_404_NOT_FOUND)
        serializer = AllPredictionsDetailsSerializer(model)
        return Response(serializer.data)


class InfluenceDetails(APIView):
    def get(self, request, uuid):
        influence_list = calculateInfluence(uuid)
        influence_list_as_json = json.dumps({"influence_list": influence_list})
        return HttpResponse(influence_list_as_json)
