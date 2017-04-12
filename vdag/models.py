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
#	game = models.AutoField(primary_key=True, blank=True)
	OFFENSE_WAY_CHOICES = (
		('F', 'Fast'), ('I', 'Isolation'), ('OS', 'Off-ball Screen'), ('DK', 'Driving Kick'), ('C', 'Cut'), ('O', 'Other'),
		('PNR', 'Pick and Roll'), ('S', 'Second'), ('PU', 'Post Up'), ('HU', 'High Post'),
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
#		string = Game.objects.select_related().filter(id = self.game).team
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

#class Turnover(models.Model):
#	game = models.OneToOneField(Game, primary_key=True)
	
