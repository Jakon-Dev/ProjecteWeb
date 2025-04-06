from django.contrib import admin

from .models import User, Map, Agent, Match, MatchPlayer, PlayerCard, PlayerTitle, AgentRole, AgentAbility
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
admin.site.register(User)
admin.site.register(Map)
admin.site.register(Agent)
admin.site.register(Match)
admin.site.register(MatchPlayer)
admin.site.register(PlayerCard)
admin.site.register(PlayerTitle)
admin.site.register(AgentRole)
admin.site.register(AgentAbility)



