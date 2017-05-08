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

def quarterName(quarter):
	if(not quarter):
		return 'Full Game'
	elif(quarter < 5):
		return str(quarter)
	else:
		return 'TO' + str(quarter)

class Game(models.Model):
	team = models.CharField(max_length=200)
	against = models.CharField(max_length=200, default='')
	date = models.DateTimeField('date published')
	def __str__(self):
		return self.team + " vs " + self.against + " " + self.date.strftime("%Y-%m-%d")

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

class PPP(models.Model):
	class Meta:
		unique_together = (('game', 'offense_way', 'shot_way', 'result', 'player'), )
	game = models.ForeignKey(Game)
	isTeamPPP = models.BooleanField(default=False)
	player = models.ForeignKey(Player, blank=True, null=True)
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

		if(self.isTeamPPP and self.player is not None):
			raise ValidationError("Player should be null when 'isTeamPPP' box is checked.")
		elif(not self.isTeamPPP and self.player is None):
			raise ValidationError("Player is required.")
		return self
	def save(self, *args, **kwargs):
		if((self.shot_way == 'TO' or self.shot_way == 'PO')):
			if(self.result):
				raise ValidationError("Result should be null!")
		else:
			if(not self.result):
				raise ValidationError("Result can't be null!")

		if(self.isTeamPPP and self.player is not None):
			raise ValidationError("Player should be null when 'isTeamPPP' box is checked.")
		elif(not self.isTeamPPP and self.player is None):
			raise ValidationError("Player is required.")
		super(PPP, self).save(*args, **kwargs)

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
	class Meta:
		unique_together = (('game', 'isTeamShotChart', 'player'), )
	game = models.ForeignKey(Game)
	isTeamShotChart = models.BooleanField(default=False)
	player = models.ForeignKey(Player, blank=True, null=True)
	zone1_made = models.PositiveSmallIntegerField(default=0)
	zone1_attempt = models.PositiveSmallIntegerField(default=0)
	zone2_made = models.PositiveSmallIntegerField(default=0)
	zone2_attempt = models.PositiveSmallIntegerField(default=0)
	zone3_made = models.PositiveSmallIntegerField(default=0)
	zone3_attempt = models.PositiveSmallIntegerField(default=0)
	zone4_made = models.PositiveSmallIntegerField(default=0)
	zone4_attempt = models.PositiveSmallIntegerField(default=0)
	zone5_made = models.PositiveSmallIntegerField(default=0)
	zone5_attempt = models.PositiveSmallIntegerField(default=0)
	zone6_made = models.PositiveSmallIntegerField(default=0)
	zone6_attempt = models.PositiveSmallIntegerField(default=0)
	zone7_made = models.PositiveSmallIntegerField(default=0)
	zone7_attempt = models.PositiveSmallIntegerField(default=0)
	zone8_made = models.PositiveSmallIntegerField(default=0)
	zone8_attempt = models.PositiveSmallIntegerField(default=0)
	zone9_made = models.PositiveSmallIntegerField(default=0)
	zone9_attempt = models.PositiveSmallIntegerField(default=0)
	zone10_made = models.PositiveSmallIntegerField(default=0)
	zone10_attempt = models.PositiveSmallIntegerField(default=0)
	zone11_made = models.PositiveSmallIntegerField(default=0)
	zone11_attempt = models.PositiveSmallIntegerField(default=0)
	def __str__(self):
		if(self.player is not None):
			return str(self.game) + '__' + str(self.player)
		else:
			return str(self.game)
	def clean(self):
		if self.isTeamShotChart:
			obj = ShotChart.objects.get(game=self.game, isTeamShotChart=True)
			if obj:
				raise ValidationError("This game's team Shot Chart already exists.")
		if(self.zone1_made > self.zone1_attempt):
			raise ValidationError("Zone1_made cannot be more than attempt")
		if(self.zone2_made > self.zone2_attempt):
			raise ValidationError("Zone2_made cannot be more than attempt")
		if(self.zone3_made > self.zone3_attempt):
			raise ValidationError("Zone3_made cannot be more than attempt")
		if(self.zone4_made > self.zone4_attempt):
			raise ValidationError("Zone4_made cannot be more than attempt")
		if(self.zone5_made > self.zone5_attempt):
			raise ValidationError("Zone5_made cannot be more than attempt")
		if(self.zone6_made > self.zone6_attempt):
			raise ValidationError("Zone6_made cannot be more than attempt")
		if(self.zone7_made > self.zone7_attempt):
			raise ValidationError("Zone7_made cannot be more than attempt")
		if(self.zone8_made > self.zone8_attempt):
			raise ValidationError("Zone8_made cannot be more than attempt")
		if(self.zone9_made > self.zone9_attempt):
			raise ValidationError("Zone9_made cannot be more than attempt")
		if(self.zone10_made > self.zone10_attempt):
			raise ValidationError("Zone10_made cannot be more than attempt")
		if(self.zone11_made > self.zone11_attempt):
			raise ValidationError("Zone11_made cannot be more than attempt")
		return self
	
	def save(self, *args, **kwargs):
		if self.isTeamShotChart:
			obj = ShotChart.objects.get(game=self.game, isTeamShotChart=True)
			if obj:
				raise ValidationError("This game's team Shot Chart already exists.")
		if(self.zone1_made > self.zone1_attempt):
			raise ValidationError("Zone1_made cannot be more than attempt")
		if(self.zone2_made > self.zone2_attempt):
			raise ValidationError("Zone2_made cannot be more than attempt")
		if(self.zone3_made > self.zone3_attempt):
			raise ValidationError("Zone3_made cannot be more than attempt")
		if(self.zone4_made > self.zone4_attempt):
			raise ValidationError("Zone4_made cannot be more than attempt")
		if(self.zone5_made > self.zone5_attempt):
			raise ValidationError("Zone5_made cannot be more than attempt")
		if(self.zone6_made > self.zone6_attempt):
			raise ValidationError("Zone6_made cannot be more than attempt")
		if(self.zone7_made > self.zone7_attempt):
			raise ValidationError("Zone7_made cannot be more than attempt")
		if(self.zone8_made > self.zone8_attempt):
			raise ValidationError("Zone8_made cannot be more than attempt")
		if(self.zone9_made > self.zone9_attempt):
			raise ValidationError("Zone9_made cannot be more than attempt")
		if(self.zone10_made > self.zone10_attempt):
			raise ValidationError("Zone10_made cannot be more than attempt")
		if(self.zone11_made > self.zone11_attempt):
			raise ValidationError("Zone11_made cannot be more than attempt")
		super(ShotChart, self).save(*args, **kwargs)

class TimeLine(models.Model):
	game = models.ForeignKey(Game)
	quarter = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
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
	bonus_made = models.PositiveSmallIntegerField(null=True, blank=True)
	bonus_attempt = models.PositiveSmallIntegerField(null=True, blank=True)
	points = models.PositiveSmallIntegerField(null=True, blank=True)
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
			if(not(self.player and self.offense_way and self.shot_way and self.result 
			   and self.points is not None)):
				err_mes1 = "Player, Offense_way, Shot_way, Result "
				err_mes2 = "and points are required when substitute is False"   
				raise ValidationError(err_mes1 + err_mes2)
			
			if(self.result == 'N1' or self.result == 'F'):
				if(not bonus_made or not bonus_attempt):
					raise ValidationError("Bonus fields are required when result is 'And One' or 'Foul'")
			else:
				if(self.bonus_made or self.bonus_attempt):
					err_mes = "Bonus fields shoube be null when result isn't 'And One' nor 'Foul'"
					raise ValidationError(err_mes)
			players_on_floor = [self.player1,self.player2, self.player3, self.player4, self.player5]
			if(len(players_on_floor) != len(set(players_on_floor))):
				raise ValidationError("Repeated player on the floor.")
			if(self.player not in players_on_floor):
				mes = "Player should be on floor, that is, the player should be one of playerN.(N=1~5)"
				raise ValidationError(mes)
		return self

	def save(self, *args, **kwargs):
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
			if(not(self.player and self.offense_way and self.shot_way and self.result 
			   and self.points is not None)):
				err_mes1 = "Player, Offense_way, Shot_way, Result "
				err_mes2 = "and points are required when substitute is False"   
				raise ValidationError(err_mes1 + err_mes2)
			
			if(self.result == 'N1' or self.result == 'F'):
				if(not bonus_made or not bonus_attempt):
					raise ValidationError("Bonus fields are required when result is 'And One' or 'Foul'")
			else:
				if(self.bonus_made or self.bonus_attempt):
					err_mes = "Bonus fields shoube be null when result isn't 'And One' nor 'Foul'"
					raise ValidationError(err_mes)
			players_on_floor = [self.player1,self.player2, self.player3, self.player4, self.player5]
			if(len(players_on_floor) != len(set(players_on_floor))):
				raise ValidationError("Repeated player on the floor.")
			if(self.player not in players_on_floor):
				mes = "Player should be on floor, that is, the player should be one of playerN.(N=1~5)"
				raise ValidationError(mes)
		super(TimeLine, self).save(*args, **kwargs)
		
	def __str__(self):
		time = str(self.time_min).zfill(2)+':'+str(self.time_sec).zfill(2)
		return str(self.game) + '-' + quarterName(self.quarter) + ' ' + time

class Defense(models.Model):
	class Meta:
		unique_together = (('game', 'player', 'quarter'), )
	game = models.ForeignKey(Game)
	isTeamDefense = models.BooleanField(default=False)
	player = models.ForeignKey(Player, null=True, blank=True)
	quarter = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
	tip = models.PositiveSmallIntegerField(default=0)
	close_out = models.PositiveSmallIntegerField(default=0)
	stop_ball = models.PositiveSmallIntegerField(default=0)
	block = models.PositiveSmallIntegerField(default=0)
	steal = models.PositiveSmallIntegerField(default=0)
	eight_24 = models.PositiveSmallIntegerField(default=0)
	double_team = models.PositiveSmallIntegerField(default=0)
	loose_ball = models.PositiveSmallIntegerField(default=0)
	off_reb = models.PositiveSmallIntegerField(default=0)
	def_reb = models.PositiveSmallIntegerField(default=0)
	off_reb_tip = models.PositiveSmallIntegerField(default=0)
	assist = models.PositiveSmallIntegerField(default=0)
	turnover = models.PositiveSmallIntegerField(default=0)
	wide_open = models.PositiveSmallIntegerField(default=0)
	no_blow_out = models.PositiveSmallIntegerField(default=0)
	def_assist = models.PositiveSmallIntegerField(default=0)
	blown_by = models.PositiveSmallIntegerField(default=0)
	
	def __str__(self):
		if(self.player is not None):
			return str(self.game) + '-' + quarterName(self.quarter) + '__' + str(self.player)
		else:
			return str(self.game) + '-' + quarterName(self.quarter)
	def clean(self):
		if(self.isTeamDefense and self.player is not None):
			raise ValidationError("Player should be null when 'isTeamDefense' box is checked.")
		elif(not self.isTeamDefense and self.player is None):
			raise ValidationError("Player is required.")
		return self
	def save(self, *args, **kwargs):
		if(self.isTeamDefense and self.player is not None):
			raise ValidationError("Player should be null when 'isTeamDefense' box is checked.")
		elif(not self.isTeamDefense and self.player is None):
			raise ValidationError("Player is required.")
		super(Defense, self).save(*arg, **kwargs)

class BoxScore(models.Model):
	class Meta:
		unique_together = (('game', 'player', 'quarter'), )
	game = models.ForeignKey(Game)
	isTeamBoxScore = models.BooleanField(default=False)
	player = models.ForeignKey(Player, null=True, blank=True)
	quarter = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
	time = models.PositiveSmallIntegerField(default=0)
	two_pts_made = models.PositiveSmallIntegerField(default=0)
	two_pts_attempt = models.PositiveSmallIntegerField(default=0)
	three_pts_made = models.PositiveSmallIntegerField(default=0)
	three_pts_attempt = models.PositiveSmallIntegerField(default=0)
	ft_made = models.PositiveSmallIntegerField(default=0)
	ft_attempt = models.PositiveSmallIntegerField(default=0)
	off_reb = models.PositiveSmallIntegerField(default=0)
	def_reb = models.PositiveSmallIntegerField(default=0)
	total_reb = models.PositiveSmallIntegerField(default=0)
	assist = models.PositiveSmallIntegerField(default=0)
	steal = models.PositiveSmallIntegerField(default=0)
	block = models.PositiveSmallIntegerField(default=0)
	turnover = models.PositiveSmallIntegerField(default=0)
	foul = models.PositiveSmallIntegerField(default=0)
	pts = models.PositiveSmallIntegerField(default=0)
	
	def __str__(self):
		if(self.player is not None):
			return str(self.game) + '-' + quarterName(self.quarter) + '__' + str(self.player)
		else:
			return str(self.game) + '-' + quarterName(self.quarter) 
	def clean(self):
		if(self.isTeamBoxScore and self.player is not None):
			raise ValidationError("Player should be null when 'isTeamBoxScore' box is checked.")
		elif(not self.isTeamBoxScore and self.player is None):
			raise ValidationError("Player is required.")
		return self
	def save(self, *args, **kwargs):
		if(self.isTeamBoxScore and self.player is not None):
			raise ValidationError("Player should be null when 'isTeamBoxScore' box is checked.")
		elif(not self.isTeamBoxScore and self.player is None):
			raise ValidationError("Player is required.")
		super(BoxScore, self).save(*args, **kwargs)
	
