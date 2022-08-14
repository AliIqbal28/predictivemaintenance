"""erohalPredictiveModel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from predictiveModel.api import PredictionsList, PredictionDetails, InfluenceDetails, UserAuthentication

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/predictions_list/$', PredictionsList.as_view(), name='predictions_list'),
    url(r'^api/prediction_details/$', PredictionDetails.as_view(), name='prediction_Details'),
    url(r'^api/prediction_details/(?P<uuid>\d+)/$', PredictionDetails.as_view(), name='prediction_Details'),
    url(r'^api/influence_details/(?P<uuid>\d+)/$', InfluenceDetails.as_view(), name='influence_Details'),
    url(r'^api/auth/$', UserAuthentication.as_view(), name='User Authentication API'),
]
