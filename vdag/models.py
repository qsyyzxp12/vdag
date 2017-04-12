import datetime
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

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
	OFFENSE_WAY_CHOICES = (
		('F', 'Fast'), ('I', 'Isolation'), ('OS', 'Off-ball Screen'), ('DK', 'Driving Kick'),
		('C', 'Cut'), ('O', 'Other'), ('PNR', 'Pick and Roll'), ('S', 'Second'), ('PU', 'Post Up'), 
		('HU', 'High Post'),
	)
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
		return str(self.game)
