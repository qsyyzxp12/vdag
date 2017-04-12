import datetime
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

OFFENSE_WAY_CHOICES = (	
	('F', 'Fast'), ('I', 'Isolation'), ('OS', 'Off-ball Screen'), ('DK', 'Driving Kick'),
	('C', 'Cut'), ('O', 'Other'), ('PNR', 'Pick and Roll'), ('S', 'Second'), ('PU', 'Post Up'), 
	('HU', 'High Post'),
)

class Game(models.Model):
	team = models.CharField(max_length=200)
	against = models.CharField(max_length=200, default='')
	date = models.DateTimeField('date published')
	def __str__(self):
		return self.team + " vs " + self.against + " " + self.date.strftime("%Y-%m-%d")

class PPP(models.Model):
	class Meta:
		unique_together = (('game', 'offense_way', 'shot_way', 'result'), )
	game = models.ForeignKey(Game)	
	offense_way = models.CharField(max_length=3, choices=OFFENSE_WAY_CHOICES, default='')
	SHOT_WAY_CHOICES = (
		('D', 'Drive'), ('PU', 'Pull Up'), ('SU', 'Spot Up'), ('TO', 'Turnover'), ('PO', 'Possession'),
	)
	shot_way = models.CharField(max_length=2, choices=SHOT_WAY_CHOICES, default='')
	RESULT_CHOICES = (
		('M', 'Made'), ('A', 'Attempt'), ('F', 'Foul'), ('Pts', 'Points'),
	)
	result = models.CharField(max_length=3, choices=RESULT_CHOICES, blank=True, null=True)
	value = models.PositiveSmallIntegerField(default=0)
	def __str__(self):
		val = self.value
		if(self.result):
			return str(self.game) + ' ' + self.offense_way + '/' + self.shot_way + '/' + self.result + '/' + str(self.value)
		else:
			return str(self.game) + ' ' + self.offense_way + '/' + self.shot_way + '/' + str(self.value)
	def clean(self):
		if((self.shot_way == 'TO' or self.shot_way == 'PO')):
			if(self.result):
				raise ValidationError("Result should be null!")
		else:
			if(not self.result):
				raise ValidationError("Result can't be null!")
		return self

class Turnover(models.Model):
	game = models.OneToOneField(Game, primary_key=True)
	stolen = models.PositiveSmallIntegerField(default=0)
	badpass = models.PositiveSmallIntegerField(default=0)
	charging = models.PositiveSmallIntegerField(default=0)
	drop = models.PositiveSmallIntegerField(default=0)
	line = models.PositiveSmallIntegerField(default=0)
	three_second = models.PositiveSmallIntegerField(default=0)
	traveling = models.PositiveSmallIntegerField(default=0)
	team = models.PositiveSmallIntegerField(default=0)
	def __str__(self):
		return str(self.game)

class ShotChart(models.Model):
	game = models.OneToOneField(Game, primary_key=True)
	zone1_made = models.PositiveSmallIntegerField(default=0)
	zone1_attempt = models.PositiveSmallIntegerField(default=0)
	zone1_hit_rate = models.PositiveSmallIntegerField(default=0)
	zone2_made = models.PositiveSmallIntegerField(default=0)
	zone2_attempt = models.PositiveSmallIntegerField(default=0)
	zone2_hit_rate = models.PositiveSmallIntegerField(default=0)
	zone3_made = models.PositiveSmallIntegerField(default=0)
	zone3_attempt = models.PositiveSmallIntegerField(default=0)
	zone3_hit_rate = models.PositiveSmallIntegerField(default=0)
	zone4_made = models.PositiveSmallIntegerField(default=0)
	zone4_attempt = models.PositiveSmallIntegerField(default=0)
	zone4_hit_rate = models.PositiveSmallIntegerField(default=0)
	zone5_made = models.PositiveSmallIntegerField(default=0)
	zone5_attempt = models.PositiveSmallIntegerField(default=0)
	zone5_hit_rate = models.PositiveSmallIntegerField(default=0)
	zone6_made = models.PositiveSmallIntegerField(default=0)
	zone6_attempt = models.PositiveSmallIntegerField(default=0)
	zone6_hit_rate = models.PositiveSmallIntegerField(default=0)
	zone7_made = models.PositiveSmallIntegerField(default=0)
	zone7_attempt = models.PositiveSmallIntegerField(default=0)
	zone7_hit_rate = models.PositiveSmallIntegerField(default=0)
	zone8_made = models.PositiveSmallIntegerField(default=0)
	zone8_attempt = models.PositiveSmallIntegerField(default=0)
	zone8_hit_rate = models.PositiveSmallIntegerField(default=0)
	zone9_made = models.PositiveSmallIntegerField(default=0)
	zone9_attempt = models.PositiveSmallIntegerField(default=0)
	zone9_hit_rate = models.PositiveSmallIntegerField(default=0)
	zone10_made = models.PositiveSmallIntegerField(default=0)
	zone10_attempt = models.PositiveSmallIntegerField(default=0)
	zone10_hit_rate = models.PositiveSmallIntegerField(default=0)
	zone11_made = models.PositiveSmallIntegerField(default=0)
	zone11_attempt = models.PositiveSmallIntegerField(default=0)
	def __str__(self):
		return strself

class Player(models.Model):
	number = models.PositiveSmallIntegerField(primary_key=True)
	name = models.CharField(max_length=200, default='')
	height = models.PositiveSmallIntegerField(default=175)
	weight = models.PositiveSmallIntegerField(default=70)
	USED_HAND_CHOICES = (
		('L', 'Left hand'), ('R', 'Right hand'),
	)
	used_hand = models.CharField(max_length=1, choices=USED_HAND_CHOICES, default='R')
	def __str__(self):
		return 'player ' + str(self.number)

class TimeLine(models.Model):
	game = models.ForeignKey(Game)
	quarter = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(1)])
	substitute = models.BooleanField(default=False)
	player1 = models.ForeignKey(Player, null=True, related_name='player1')
	player2 = models.ForeignKey(Player, null=True, related_name='player2')
	player3 = models.ForeignKey(Player, null=True, related_name='player3')
	player4 = models.ForeignKey(Player, null=True, related_name='player4')
	player5 = models.ForeignKey(Player, null=True, related_name='player5')
	player_get_on = models.ForeignKey(Player, blank=True, null=True, related_name='player_get_on')
	player_get_off = models.ForeignKey(Player, blank=True, null=True, related_name='player_get_off')
	time_min = models.PositiveSmallIntegerField(default=0)
	time_sec = models.PositiveSmallIntegerField(default=0)
	player = models.ForeignKey(Player, blank=True, null=True, related_name='player')
	offense_way = models.CharField(max_length=3, choices=OFFENSE_WAY_CHOICES, null=True, blank=True)
	
	SHOT_WAY_CHOICES = (
		('D', 'Drive'), ('PU', 'Pull Up'), ('SU', 'Spot Up'), ('TO', 'Turnover'),
	)
	shot_way = models.CharField(max_length=2, choices=SHOT_WAY_CHOICES, null=True, blank=True)
	
	RESULT_CHOICES = (
		('M', 'Made'), ('A', 'Attempt'), ('F', 'Foul'), ('N1', 'And One'),
	)
	result = models.CharField(max_length=2, choices=RESULT_CHOICES, null=True, blank=True)
	bonus_made = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
	bonus_attempt = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
	points = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
	def clean(self):
		if(self.substitute):
			if(not(self.player_get_on and self.player_get_off)):
				err_mes = "Player_get_on and Player_get_off is required when substitute is True"
				raise ValidationError(err_mes)
			if(self.player or self.offense_way or self.shot_way or self.result or self.bonus_made or
			   self.bonus_attempt or self.points):
				err_mes1 = "Player, Offense_way, Shot_way, Result, bonus_made, "
				err_mes2 = "bonus_attempt and points should be null when substitute is True"   
				raise ValidationError(err_mes1 + err_mes2)
		else:
			if(self.player_get_on or self.player_get_off):
				err_mes = "Player_get_on and Player_get_off should be null when substitute is False"
				raise ValidationError(err_mes)
			if(not(self.player and self.offense_way and self.shot_way and self.result and self.bonus_made
			   and self.bonus_attmpt and self.points)):
				err_mes1 = "Player, Offense_way, Shot_way, Result, bonus_made, "
				err_mes2 = "bonus_attempt and points are required when substitute is False"   
				raise ValidationError(err_mes1 + err_mes2)
			
			if(not(self.player1 == self.player or self.player2 == self.player or 
				   self.player3 == self.player or self.player4 == self.player or 
				   self.player4 == self.player)):
				mes = "Player should be on floor, that is, the player should be one of playerN.(N=1~5)"
				raise ValidationError(mes)
			if(self.result == 'N1' or self.result == 'F'):
				if(not bonus_made or not bonus_attempt):
					raise ValidationError("Bonus fields are required when result is 'And One' or 'Foul'")
			else:
				if(bonus_made or bonus_attempt):
					err_mes = "Bonus fields shoube be null when result isn't 'And One' nor 'Foul'"
					raise ValidationError(err_mes)
		return self
	def __str__(self):
		time = str(self.time_min).zfill(2)+':'+str(self.time_sec).zfill(2)
		return str(self.game) + '-' + str(self.quarter) + ' ' + time




