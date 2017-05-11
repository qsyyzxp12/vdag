import datetime
from django.http import HttpResponse, StreamingHttpResponse
from django.core.exceptions import ValidationError
from vdag.models import Game, PPP, Turnover, ShotChart, Player, TimeLine, Defense, BoxScore
from django.views.decorators.csrf import csrf_exempt

def index(request):
	return HttpResponse("Hello")

def getGame(y, m, d, team, against):
	#check the game exists or not. If it is not, create it. 
	try:
		game = Game.objects.get(date__year=y, date__month=m, date__day=d, team=team, against=against)
	except Game.DoesNotExist:
		dateStr = y + '-' + m + '-' + d
		date = datetime.datetime.strptime(dateStr, "%Y-%m-%d")
		game = Game(
						date=date, 
						team=team, 
						against=against
				   )
		game.save()
	return game

def getPlayer(no):
	try:
		player = Player.objects.get(number=no)
	except Player.DoesNotExist:
		return None
	return player

@csrf_exempt
def addPPP(request):
	if request.method == 'POST':
		arg = request.POST
#		print request.body
#		print str(arg) + '\n'
		game = getGame(arg.get('year'), arg.get('month'), arg.get('day'), arg.get('team'), arg.get('against'))
		player = None
		if arg.get('isTeamPPP') == 'False':
			player = getPlayer(arg.get('player'))
			if not player:
				return HttpResponse("No this player")
		ppp = PPP(
					game = game,
					isTeamPPP = arg.get('isTeamPPP'), 
					player = player, 
					offense_way = arg.get('offense_way'),
					shot_way = arg.get('shot_way'), 
					result = arg.get('result'),
					value = arg.get('value')
				)
		try:
			ppp.save()
		except ValidationError as e:
			print str(e)
			return HttpResponse("Fail")
		return HttpResponse("Success")


@csrf_exempt
def addTurnover(request):
	arg = request.POST
	game = getGame(arg.get('year'), arg.get('month'), arg.get('day'), arg.get('team'), arg.get('against'))
	turnover = Turnover(
							game = game,
							stolen = arg.get('stolen'),
							badpass = arg.get('badpass'),
							charging = arg.get('charging'),
							drop = arg.get('drop'),
							line = arg.get('line'),
							three_second = arg.get('three_second'),
							traveling = arg.get('traveling'),
							team = arg.get('Team')
						)
	try:
		turnover.save()
	except ValidationError as e:
		print str(e)
	return HttpResponse(str(turnover))

@csrf_exempt
def addShotChart(request):
	arg = request.POST
	game = getGame(arg.get('year'), arg.get('month'), arg.get('day'), arg.get('team'), arg.get('against'))
	player = None
	if arg.get('isTeamShotChart') == 'False':
		player = getPlayer(arg.get('player'))
		if not player:
			return HttpResponse("No this player")
	shotchart = ShotChart(
							game = game,
							isTeamShotChart = arg.get('isTeamShotChart'),
							player = player,
							zone1_made = arg.get('zone1_made'),
							zone1_attempt = arg.get('zone1_attempt'),
							zone2_made = arg.get('zone2_made'),
							zone2_attempt = arg.get('zone2_attempt'),
							zone3_made = arg.get('zone3_made'),
							zone3_attempt = arg.get('zone3_attempt'),
							zone4_made = arg.get('zone4_made'),
							zone4_attempt = arg.get('zone4_attempt'),
							zone5_made = arg.get('zone5_made'),
							zone5_attempt = arg.get('zone5_attempt'),
							zone6_made = arg.get('zone6_made'),
							zone6_attempt = arg.get('zone6_attempt'),
							zone7_made = arg.get('zone7_made'),
							zone7_attempt = arg.get('zone7_attempt'),
							zone8_made = arg.get('zone8_made'),
							zone8_attempt = arg.get('zone8_attempt'),
							zone9_made = arg.get('zone9_made'),
							zone9_attempt = arg.get('zone9_attempt'),
							zone10_made = arg.get('zone10_made'),
							zone10_attempt = arg.get('zone10_attempt'),
							zone11_made = arg.get('zone11_made'),
							zone11_attempt = arg.get('zone11_attempt'),
						)
	try:
		shotchart.save()
	except ValidationError as e:
		print str(e)
	return HttpResponse(str(shotchart))

@csrf_exempt
def addTimeLine(request):
	arg = request.POST
	game = getGame(arg.get('year'), arg.get('month'), arg.get('day'), arg.get('team'), arg.get('against'))
	try:
		player1 = Player.objects.get(number=arg.get('player1'))
		player2 = Player.objects.get(number=arg.get('player2'))
		player3 = Player.objects.get(number=arg.get('player3'))
		player4 = Player.objects.get(number=arg.get('player4'))
		player5 = Player.objects.get(number=arg.get('player5'))
		if arg.get('substitute') == 'True':
			player_get_on = Player.objects.get(number=arg.get('player_get_on'))
			player_get_off = Player.objects.get(number=arg.get('player_get_off'))
		else:
			player = Player.objects.get(number=arg.get('player'))
	except Player.DoesNotExist:
		return HttpResponse("No such player")
	
	timeline = TimeLine(
							game = game,
							quarter = arg.get('quarter'),
							substitute = arg.get('substitute'),
							player1 = player1,
							player2 = player2,
							player3 = player3,
							player4 = player4,
							player5 = player5,
							player_get_on = player_get_on,
							player_get_off = player_get_off,
							time_min = arg.get('time_min'),
							time_sec = arg.get('time_sec'),
							player = player,
							offense_way = arg.get('offense_way'),
							shot_way = arg.get('shot_way'),
							result = arg.get('result'),
							bonus_made = arg.get('bonus_made'),
							bonus_attempt = arg.get('bonus_attempt'),
							points = arg.get('points'),
						)
	try:
		timeline.save()
	except ValidationError as e:
		print str(e)
	return HttpResponse(str(timeline))

@csrf_exempt
def addDefense(request):
	arg = request.POST
	game = getGame(arg.get('year'), arg.get('month'), arg.get('day'), arg.get('team'), arg.get('against'))
	player = None
	if arg.get('isTeamDefense') == 'False':
		player = getPlayer(arg.get('player'))
		if not player :
			return HttpResponse("No this player")
	defense = Defense(
						game = game,
						isTeamDefense = arg.get('isTeamDefense'),
						player = player,
						quarter = arg.get('quarter'),
						tip = arg.get('tip'),
						close_out = arg.get('close_out'),
						stop_ball = arg.get('stop_ball'),
						block = arg.get('block'),
						steal = arg.get('steal'),
						eight_24 = arg.get('eight_24'),
						double_team = arg.get('double_team'),
						loose_ball = arg.get('loose_ball'),
						off_reb = arg.get('off_reb'),
						def_reb = arg.get('def_reb'),
						off_reb_tip = arg.get('off_reb_tip'),
						assist = arg.get('assist'),
						turnover = arg.get('turnover'),
						wide_open = arg.get('wide_open'),
						no_blow_out = arg.get('no_blow_out'),
						def_assist = arg.get('def_assist'),
						blown_by = arg.get('blown_by'),
					 )
	try:
		defense.save()
	except ValidationError as e:
		print str(e)
	return HttpResponse(str(defense))

@csrf_exempt
def addBoxScore(request):
	arg = request.POST
	game = getGame(arg.get('year'), arg.get('month'), arg.get('day'), arg.get('team'), arg.get('against'))
	player = None
	if arg.get('isTeamBoxScore') == 'False':
		player = getPlayer(arg.get('player'))
		if not player :
			return HttpResponse("No this player")
	boxscore = BoxScore(
							game = game,
							isTeamBoxScore = arg.get('isTeamBoxScore'),
							player = player,
							quarter = arg.get('quarter'),
							time = arg.get('time'),
							two_pts_made = arg.get('two_pts_made'),
							two_pts_attempt = arg.get('two_pts_attempt'),
							three_pts_made = arg.get('three_pts_made'),
							three_pts_attempt = arg.get('three_pts_attempt'),
							ft_made = arg.get('ft_made'),
							ft_attempt = arg.get('ft_attempt'),
							off_reb = arg.get('off_reb'),
							def_reb = arg.get('def_reb'),
							total_reb = arg.get('total_reb'),
							assist = arg.get('assist'),
							steal = arg.get('steal'),
							block = arg.get('block'),
							turnover = arg.get('turnover'),
							foul = arg.get('foul'),
							pts = arg.get('pts'),
					   )
	try:
		boxscore.save()
	except ValidationError as e:
		print str(e)
	return HttpResponse(str(boxscore))
