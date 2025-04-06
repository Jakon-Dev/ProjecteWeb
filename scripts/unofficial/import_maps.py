import os
import django
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(PROJECT_ROOT)

# Force Django settings module
os.environ["DJANGO_SETTINGS_MODULE"] = "MyProject.settings" 

django.setup()  # Now initialize Django

from web.models import Map
from scripts.API import UN_OFFICIAL 

def main():
    maps = UN_OFFICIAL.get_maps()

    myMaps = Map.objects.all()


    for map in maps:
        if not myMaps.filter(id=map["uuid"]).exists() and map["tacticalDescription"] != None:
            Map.objects.create(
                id=map["uuid"],
                name=map["displayName"],
                description=map["tacticalDescription"],
                
                displayIcon=map["displayIcon"],
                listViewIcon=map["listViewIcon"],
                listViewIconTall=map["listViewIconTall"],
                splash=map["splash"],
                stylizedBackgroundImage=map["stylizedBackgroundImage"],
                premierBackgroundImage=map["premierBackgroundImage"],
                
                path=map["mapUrl"],
            )

if __name__ == "__main__":
    main()