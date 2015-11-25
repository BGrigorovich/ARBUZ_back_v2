import json
from django.http import JsonResponse
from django.core import serializers
from core.models import Building, Crimes
from core.tileSystem import TileSystem

def building_view(request):
    # bbox = request.GET['bbox']
    # # print ('BBOX: ', bbox)
    # z = request.GET['z']
    # # print ('Z: ', z)
    # print(TileSystem.lalka(z))

    data = Building.objects.all()
    return JsonResponse(serializers.serialize('json', data), safe=False)


# todo: refactor this
# todo: add filtering
def crimes_view(request):
    data = Crimes.objects.filter(pk=1).select_related('building_id')
    crimes_dict = []
    for crime in data:
        crimes_dict.append(crime.__dict__)
        crimes_dict[-1]['building'] = crime.building_id.__dict__
        crimes_dict[-1]['year_month'] = str(crimes_dict[-1]['year_month'])
        del crimes_dict[-1]['_state']
        del crimes_dict[-1]['building']['_state']
        del crimes_dict[-1]['_building_id_cache']
    return JsonResponse(json.dumps(crimes_dict), safe=False)
