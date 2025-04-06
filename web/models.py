import json
from os import path
from django.db import models

# ======================= USERS ==========================

class PlayerCard(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    name = models.CharField(max_length=120)
    
    icon = models.URLField(max_length=200, blank=True, null=True)
    small_art = models.URLField(max_length=200, blank=True, null=True)
    wide_art = models.URLField(max_length=200, blank=True, null=True)
    large_art = models.URLField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class PlayerTitle(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

class User(models.Model):
    puuid = models.CharField(max_length=120, primary_key=True)
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=5)
    card = models.ForeignKey(PlayerCard, on_delete=models.CASCADE, null=True)
    title = models.ForeignKey(PlayerTitle, on_delete=models.CASCADE, null=True)
    recent_matches = models.JSONField()

    def __str__(self):
        return f"{self.name}#{self.tag}"

# ======================= AGENTS ==========================

class AgentRole(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    icon = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class AgentAbility(models.Model):
    name = models.CharField(max_length=120, primary_key=True)
    description = models.TextField(null=True, blank=True)
    icon = models.TextField(null=True, blank=True)
        
    def __str__(self):
        return self.name

class Agent(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    developerName = models.CharField(max_length=120, null=True, blank=True)
    
    icon = models.URLField(max_length=200, blank=True, null=True)
    icon_small = models.URLField(max_length=200, blank=True, null=True)
    bust_image = models.URLField(max_length=200, blank=True, null=True)
    full_image = models.URLField(max_length=200, blank=True, null=True)
    full_image_v2 = models.URLField(max_length=200, blank=True, null=True)
    background_image = models.URLField(max_length=200, blank=True, null=True)
    
    role = models.ForeignKey(AgentRole, on_delete=models.CASCADE, blank=True, null=True)
    
    ability1 = models.ForeignKey(AgentAbility, on_delete=models.CASCADE, related_name='ability1', null=True)
    ability2 = models.ForeignKey(AgentAbility, on_delete=models.CASCADE, related_name='ability2', null=True)
    grenade = models.ForeignKey(AgentAbility, on_delete=models.CASCADE, related_name='grenade', null=True)
    ultimate = models.ForeignKey(AgentAbility, on_delete=models.CASCADE, related_name='ultimate', null=True)
    passive = models.ForeignKey(AgentAbility, on_delete=models.CASCADE, related_name='passive', null=True)

    def __str__(self):
        return self.name

# ======================= MAPS ==========================

class Map(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    name = models.CharField(max_length=120)
    displayIcon = models.URLField(max_length=200, blank=True, null=True)
    listViewIcon = models.URLField(max_length=200, blank=True, null=True)
    listViewIconTall = models.URLField(max_length=200, blank=True, null=True)
    splash = models.URLField(max_length=200, blank=True, null=True)
    stylizedBackgroundImage = models.URLField(max_length=200, blank=True, null=True)
    premierBackgroundImage = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    path = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name


# ======================= MATCHES ==========================

class Match(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    json_data = models.JSONField()
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='matches')
    red_result = models.IntegerField()
    blue_result = models.IntegerField()
    start_time = models.DateTimeField()
    game_duration = models.TimeField()

    def __str__(self):
        return f"Match {self.id} on {self.map.name}"

class MatchPlayer(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='player_matches')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='player_matches')
    team = models.CharField(max_length=120)
    hasWon = models.BooleanField(default=False)
    score = models.IntegerField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()

    def __str__(self):
        return f"{self.player.name} in match {self.match.id}"

class MatchRound(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='rounds')
    index = models.IntegerField()
    
    roundResult = models.CharField(max_length=120, null=True, blank=True)
    roundCeremony = models.CharField(max_length=120, null=True, blank=True)
    roundResultCode = models.CharField(max_length=120, null=True, blank=True)
    
    winner_team = models.CharField(max_length=120)
    winnerSide = models.CharField(max_length=120)
    loser = models.CharField(max_length=120)
    loserSide = models.CharField(max_length=120)
    
    bombPlanter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rounds_planted', null=True, blank=True)
    bombDefuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rounds_defused', null=True, blank=True)
    
    plantRoundTime = models.CharField(max_length=120, null=True, blank=True)
    defuseRoundTime = models.CharField(max_length=120, null=True, blank=True)
    plantSite = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return f"Round {self.round_number} of match {self.match.id}"



# For more info on how to use Django model fields: 
# https://docs.djangoproject.com/en/stable/ref/models/fields/
