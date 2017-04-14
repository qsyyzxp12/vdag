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

class GameAdmin(admin.ModelAdmin):
	list_display = ('date', 'team', 'against')
admin.site.register(Game, GameAdmin)

class PPPAdmin(admin.ModelAdmin):
	list_display = ('game', 'isTeamPPP', 'player', 'offense_way', 'shot_way', 'result', 'value')
admin.site.register(PPP, PPPAdmin)

class TurnoverAdmin(admin.ModelAdmin):
	list_display = ('game', 'stolen', 'badpass', 'charging', 'drop', 'line', 'three_second', 'traveling', 'team')
admin.site.register(Turnover, TurnoverAdmin)

class ShotChartAdmin(admin.ModelAdmin):
	list_display = ('game', 'isTeamShotChart', 'player', 'zone_1', 'zone_2', 'zone_3', 'zone_4', 'zone_5', 'zone_6', 'zone_7', 'zone_8', 'zone_9', 'zone_10', 'zone_11')
	
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
#	list_display = ('game', 'isTeamShotChart', 'player', 'zone1_made', 'zone1_attempt', 'zone1_hit_rate', 'zone2_made', 'zone2_attempt', 'zone2_hit_rate', 'zone3_made', 'zone3_attempt', 'zone3_hit_rate', 'zone4_made', 'zone4_attempt', 'zone4_hit_rate', 'zone5_made', 'zone5_attempt', 'zone5_hit_rate', 'zone6_made', 'zone6_attempt', 'zone6_hit_rate', 'zone7_made', 'zone7_attempt', 'zone7_hit_rate', 'zone8_made', 'zone9_attempt', 'zone9_hit_rate', 'zone10_made', 'zone10_attempt', 'zone10_hit_rate', 'zone11_made', 'zone11_attempt', 'zone11_hit_rate')
admin.site.register(ShotChart, ShotChartAdmin)

admin.site.register(Player)
admin.site.register(TimeLine)
admin.site.register(Defense)
admin.site.register(BoxScore)
