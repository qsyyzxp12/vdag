from django.contrib import admin
from .models import Game, PPP, Turnover, ShotChart, TimeLine, Player, Defense, BoxScore

#class ChoiceInline(admin.TabularInline):  # or StackedInline
#	model = Choice
#	extra = 3

#class QuestionAdmin(admin.ModelAdmin):
#	fieldsets = [
#		(None,					{'fields': ['question_text']}),
#		('Date information', 	{'fields': ['pub_date'], 'classes': ['collapse']}),
#	]
#	inlines = [ChoiceInline]
#	list_display = ('question_text', 'pub_date')
#	list_filter = ['pub_date']
#	search_fields = ['question_text']

#admin.site.register(Question, QuestionAdmin)

class PPPInline(admin.TabularInline):
	model = PPP
	extra = 0

class TurnoverInline(admin.TabularInline):
	model = Turnover
	extra = 0

class ShotChartInline(admin.TabularInline):
	model = ShotChart
	extra = 0

class TimeLineInline(admin.TabularInline):
	model = TimeLine
	extra = 0

class DefenseInline(admin.TabularInline):
	model = Defense
	extra = 0

class BoxScoreInline(admin.TabularInline):
	model = BoxScore
	extra = 0

class GameAdmin(admin.ModelAdmin):
	inlines = [PPPInline, ShotChartInline, TurnoverInline, TimeLineInline, DefenseInline, BoxScoreInline]
	list_display = ('date', 'team', 'against')

class PPPAdmin(admin.ModelAdmin):
	list_display = ('game', 'Player', 'offense_way', 'shot_way', 'result', 'value')
	def Player(self, obj):
		if(obj.isTeamPPP):
			return 'Team'
		else:
			return obj.player

class TurnoverAdmin(admin.ModelAdmin):
	list_display = ('game', 'stolen', 'badpass', 'charging', 'drop', 'line', 'three_second', 'traveling', 'team')

class ShotChartAdmin(admin.ModelAdmin):
	list_display = ('game', 'Player', 'zone_1', 'zone_2', 'zone_3', 
					'zone_4', 'zone_5', 'zone_6', 'zone_7', 'zone_8', 'zone_9', 'zone_10', 
					'zone_11')
	
	def Player(self, obj):
		if(obj.isTeamShotChart):
			return 'Team'
		else:
			return obj.player
	def zone_1(self, obj):
		hit_rate = 0
		if(obj.zone1_attempt):
			hit_rate = obj.zone1_made*100 / obj.zone1_attempt
		return str(obj.zone1_made) + '/' + str(obj.zone1_attempt) + '  ' + str(hit_rate) + '%'
	
	def zone_2(self, obj):
		hit_rate = 0
		if(obj.zone2_attempt):
			hit_rate = obj.zone2_made*100 / obj.zone2_attempt
		return str(obj.zone2_made) + '/' + str(obj.zone2_attempt) + '  ' + str(hit_rate) + '%'	
	
	def zone_3(self, obj):
		hit_rate = 0
		if(obj.zone3_attempt):
			hit_rate = obj.zone3_made*100 / obj.zone3_attempt
		return str(obj.zone3_made) + '/' + str(obj.zone3_attempt) + '  ' + str(hit_rate) + '%'
	
	def zone_4(self, obj):
		hit_rate = 0
		if(obj.zone4_attempt):
			hit_rate = obj.zone4_made*100 / obj.zone4_attempt
		return str(obj.zone4_made) + '/' + str(obj.zone4_attempt) + '  ' + str(hit_rate) + '%'
	
	def zone_5(self, obj):
		hit_rate = 0
		if(obj.zone5_attempt):
			hit_rate = obj.zone5_made*100 / obj.zone5_attempt
		return str(obj.zone5_made) + '/' + str(obj.zone5_attempt) + '  ' + str(hit_rate) + '%'
	
	def zone_6(self, obj):
		hit_rate = 0
		if(obj.zone6_attempt):
			hit_rate = obj.zone6_made*100 / obj.zone6_attempt
		return str(obj.zone6_made) + '/' + str(obj.zone6_attempt) + '  ' + str(hit_rate) + '%'
	
	def zone_7(self, obj):
		hit_rate = 0
		if(obj.zone7_attempt):
			hit_rate = obj.zone7_made*100 / obj.zone7_attempt
		return str(obj.zone7_made) + '/' + str(obj.zone7_attempt) + '  ' + str(hit_rate) + '%'
	
	def zone_8(self, obj):
		hit_rate = 0
		if(obj.zone8_attempt):
			hit_rate = obj.zone8_made*100 / obj.zone8_attempt
		return str(obj.zone8_made) + '/' + str(obj.zone8_attempt) + '  ' + str(hit_rate) + '%'
	
	def zone_9(self, obj):
		hit_rate = 0
		if(obj.zone9_attempt):
			hit_rate = obj.zone9_made*100 / obj.zone9_attempt
		return str(obj.zone9_made) + '/' + str(obj.zone9_attempt) + '  ' + str(hit_rate) + '%'
	
	def zone_10(self, obj):
		hit_rate = 0
		if(obj.zone10_attempt):
			hit_rate = obj.zone10_made*100 / obj.zone10_attempt
		return str(obj.zone10_made) + '/' + str(obj.zone10_attempt) + '  ' + str(hit_rate) + '%'
	
	def zone_11(self, obj):
		hit_rate = 0
		if(obj.zone11_attempt):
			hit_rate = obj.zone11_made*100 / obj.zone11_attempt
		return str(obj.zone11_made) + '/' + str(obj.zone11_attempt) + '  ' + str(hit_rate) + '%'

class PlayerAdmin(admin.ModelAdmin):
	list_display = ('name', 'number', 'height', 'used_hand')

class TimeLineAdmin(admin.ModelAdmin):
	list_display = ('game', 'quarter', 'player_on_floor', 'player_get_on', 'player_get_off', 
					'time', 'player', 'offense_way', 'shot_way', 'result', 'bonus_made', 
					'bonus_attempt', 'points')
	def player_on_floor (self, obj):
		tmp = str(obj.player1.number)+', '+str(obj.player2.number)+', '+str(obj.player3.number)+', '
		return tmp+str(obj.player4.number)+', '+str(obj.player5.number)
	def time(self, obj):
		return str(obj.time_min).zfill(2) + ':' + str(obj.time_sec).zfill(2)

class DefenseAdmin(admin.ModelAdmin):
	deflection_set = ['tip', 'close_out', 'stop_ball', 'block', 'steal', 'eight_24', 'double_team', 'loose_ball']
	good_set = ['off_reb', 'def_reb', 'off_reb_tip', 'assist']
	bad_set = ['turnover', 'wide_open', 'no_blow_out', 'def_assist', 'blown_by']
	fieldsets = [
		(None,			{'fields': ['game', 'isTeamDefense', 'player', 'quarter']}),
		('Deflection', 	{'fields': deflection_set}),
		('Good', 		{'fields': good_set}),
		('Bad',			{'fields': bad_set}),
	]
	list_display = ('game', 'Player', 'Quarter', 'tip', 'close_out', 'stop_ball', 'block', 
					'steal', 'eight_24', 'double_team', 'loose_ball', 'off_reb', 'def_reb', 
					'off_reb_tip', 'assist', 'turnover', 'wide_open', 'no_blow_out', 'def_assist', 
					'blown_by', 'total', 'deflections')
	def Quarter(self, obj):
		if(not obj.quarter):
			return 'Full Game'
		elif(obj.quarter < 5):
			return obj.quarter
		else:
			return 'OT ' + str(obj.quarter-4)
	def Player(self, obj):
		if(obj.isTeamDefense):
			return 'Team'
		else:
			return obj.player
	def total(self, obj):
		deflection = obj.tip + obj.close_out + obj.stop_ball + obj.block + obj.steal + obj.eight_24 + obj.double_team + obj.loose_ball
		good = obj.off_reb + obj.def_reb + obj.off_reb_tip + obj.assist
		bad = obj.turnover + obj.wide_open + obj.no_blow_out + obj.assist + obj.blown_by
		return deflection + good - bad
	def deflections(self, obj):
		deflection = obj.tip + obj.close_out + obj.stop_ball + obj.block + obj.steal + obj.eight_24 + obj.double_team + obj.loose_ball
		return deflection

class BoxScoreAdmin(admin.ModelAdmin):
	list_display = ('game', 'Quarter', 'Player', 'two_pts_made', 'two_pts_attempt', 
					'three_pts_made', 'three_pts_attempt', 'ft_made', 'ft_attempt', 
					'off_reb', 'def_reb', 'total_reb', 'assist', 'steal', 'block', 
					'turnover', 'foul', 'pts')
	def Quarter(self, obj):
		if(not obj.quarter):
			return 'Full Game'
		elif(obj.quarter < 5):
			return obj.quarter
		else:
			return 'OT ' + str(obj.quarter-4)
	
	def Player(self, obj):
		if(obj.isTeamBoxScore):
			return 'Team'
		else:
			return obj.player
		
admin.site.register(Game, GameAdmin)
admin.site.register(PPP, PPPAdmin)
admin.site.register(Turnover, TurnoverAdmin)
admin.site.register(ShotChart, ShotChartAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(TimeLine, TimeLineAdmin)
admin.site.register(Defense, DefenseAdmin)
admin.site.register(BoxScore, BoxScoreAdmin)
