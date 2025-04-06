import os
import django
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(PROJECT_ROOT)

# Force Django settings module
os.environ["DJANGO_SETTINGS_MODULE"] = "MyProject.settings"

django.setup()  # Now initialize Django

from web.models import Agent, AgentAbility, AgentRole
from scripts.API import UN_OFFICIAL 

def main():

    agents = UN_OFFICIAL.get_agents()

    myAgents = Agent.objects.all()
    myAbilities = AgentAbility.objects.all()
    myRoles = AgentRole.objects.all()

    for agent in agents:
        if not myAgents.filter(id=agent["uuid"]).exists() and agent["isPlayableCharacter"]:

            try:
                role=AgentRole.objects.get(id=agent["role"]["uuid"])
            except:
                AgentRole.objects.create(
                    id=agent["role"]["uuid"],
                    name=agent["role"]["displayName"],
                    icon=agent["role"]["displayIcon"],
                    description=agent["role"]["description"]
                )
                role=AgentRole.objects.get(id=agent["role"]["uuid"])
            
            for ability in agent["abilities"]:
                if not myAbilities.filter(name=ability["displayName"]).exists():
                    AgentAbility.objects.create(
                        name=ability["displayName"],
                        description=ability["description"],
                        icon=ability["displayIcon"]
                    )
            
            
            def abilities():
                try:
                    ability_1=AgentAbility.objects.get(name=agent["abilities"][0]["displayName"])
                except:
                    ability_1=None
                
                try:
                    ability_2=AgentAbility.objects.get(name=agent["abilities"][1]["displayName"])
                except:
                    ability_2=None

                try:
                    grenade=AgentAbility.objects.get(name=agent["abilities"][2]["displayName"])
                except:
                    grenade=None

                try:
                    ultimate=AgentAbility.objects.get(name=agent["abilities"][3]["displayName"])
                except:
                    ultimate=None

                try:
                    passive=AgentAbility.objects.get(name=agent["abilities"][4]["displayName"])
                except:
                    passive=None
                
                return ability_1, ability_2, grenade, ultimate, passive
            ability1, ability2, grenade, ultimate, passive = abilities()


            Agent.objects.create(
                id=agent["uuid"],
                name=agent["displayName"],
                description=agent["description"],
                developerName=agent["developerName"],

                icon=agent["displayIcon"],
                icon_small=agent["displayIconSmall"],
                bust_image=agent["bustPortrait"],
                full_image=agent["fullPortrait"],
                full_image_v2=agent["fullPortraitV2"],
                background_image=agent["background"],
                
                role=role,
                
                ability1=ability1,
                ability2=ability2,
                grenade=grenade,
                ultimate=ultimate,
                passive=passive
            )

if __name__ == "__main__":
    main()
                
