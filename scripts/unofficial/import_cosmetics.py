import os
import django
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(PROJECT_ROOT)

# Force Django settings module
os.environ["DJANGO_SETTINGS_MODULE"] = "MyProject.settings" 

django.setup()  # Now initialize Django

from web.models import Agent, AgentAbility, AgentRole, PlayerCard, PlayerTitle
from scripts.API import UN_OFFICIAL 

def import_cards(cards, myCards):
    for card in cards:
        if not myCards.filter(name=card["displayName"]).exists():
            PlayerCard.objects.create(
                id=card["uuid"],
                name=card["displayName"],
                
                icon=card["displayIcon"],
                small_art=card["smallArt"],
                wide_art=card["wideArt"],
                large_art=card["largeArt"],
            )

def import_titles(titles, myTitles):
    for title in titles:
        if not myTitles.filter(name=title["displayName"]).exists() and title["titleText"]:
            PlayerTitle.objects.create(
                id=title["uuid"],
                name=title["displayName"],
                title=title["titleText"],
            )

def main():
    cards = UN_OFFICIAL.get_cards()
    titles = UN_OFFICIAL.get_titles()
    
    myCards = PlayerCard.objects.all()
    myTitles = PlayerTitle.objects.all()
    
    import_cards(cards, myCards)
    import_titles(titles, myTitles)
    



if __name__ == "__main__":
    main()
                