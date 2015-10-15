from django.http import JsonResponse
from django.shortcuts import render
from flask import Flask, session
# from flask.ext.sqlalchemy import SQLAlchemy
from core.models import Building, Crimes
from django.core import serializers
import sqlalchemy
import aldjemy

def building_view(request):
    # building = Building.objects.all()
    # data = building.crimes_set.all()
    data = Building.objects.all()
    return JsonResponse(serializers.serialize('json', data), safe=False)


def crimes_view(request):
    data = Crimes.odjects.all()
    # data = Crimes.objects.all().values('building__street', 'building__number')
    # data = crimes.biulding_set.all()
    # data = Crimes.objects.prefetch_related('building_set')
    return JsonResponse(serializers.serialize('json', data), safe=False)
