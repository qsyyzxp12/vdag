import datetime
from django.http import HttpResponse, StreamingHttpResponse
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
		game = Game(date=date, team=team, against=against)
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
	arg = request.POST
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
	ppp.save()
	return HttpResponse(str(ppp))

