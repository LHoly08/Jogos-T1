import pygame as pg

class Player:
	def __init__(self, Choice_Car:list):
		self.Choice_Car=Choice_Car
		self.ready=False
		self.selection=0

class Car:
	x=456
	y=605
	def __init__(self, speed_aceleration_boost_charge, img):
		self.speed=speed_aceleration_boost_charge[8]
		self.aceleration=speed_aceleration_boost_charge[9]
		self.boost=speed_aceleration_boost_charge[10]
		self.charge=speed_aceleration_boost_charge[11]
		self.car=img
		self.boostvalue=0
		self.boostact=False
		self.boostacttimer=False
		self.innerclock_start=None
		self.boostchargemeter=0
		self.clockrecharge=pg.time.get_ticks()
		self.drift=speed_aceleration_boost_charge[12]
		self.speedvalue=0.1
		self.movement=(self.x, self.y)
		self.do_once_move=True
		self.do_once_stop=False
		self.stopstart=pg.time.get_ticks()
		self.hitbox=(self.car).get_rect()
		self.laps=0
		self.lap_complete=0
		self.cant_right=False
		self.cant_left=False
		self.cant_up=False
		self.cant_down=False
		self.cant_up_p=False
		self.cant_down_p=False
		self.cant_right_p=False
		self.cant_left_p=False
		self.sand=1
		self.sandresist=speed_aceleration_boost_charge[13]
		self.collisionslimit=[
			pg.rect.Rect(self.x-3, self.y-self.hitbox[3]-6, self.hitbox[2]+6, 6),
			pg.rect.Rect(self.x-3, self.y+6, self.hitbox[2]+6, 6),
			pg.rect.Rect(self.x-6, self.y-3, 6, self.hitbox[3]+6),
			pg.rect.Rect(self.x+self.hitbox[2]+6, self.y-3, 6, self.hitbox[3]+6)
		]
		self.sound=True
		
	def boostactive(self, time):
		if time-self.innerclock_start>=2000:
			self.boostvalue=0
			self.boostacttimer=False
			self.clockrecharge=pg.time.get_ticks()

	def boostactivate(self):
		self.boostact=False
		self.boostvalue=player1car.boost
		self.innerclock_start=pg.time.get_ticks()
		self.boostacttimer=True
		self.boostchargemeter=-3

	def boostrecharge(self, timeboost):
		if timeboost-self.clockrecharge>=2000-1500*self.charge:
			self.boostchargemeter+=1
			self.clockrecharge=pg.time.get_ticks()
		if self.boostchargemeter>=10:
			self.boostact=True

	def speedup(self, timespeed):
		if self.sound:
			acceleratingsound.play()
			self.sound=False
		if timespeed-self.speedstart>=1000-1000*self.aceleration and self.speedvalue<self.speed-0.1:
			self.speedvalue+=0.1
			self.speedvalue=round(self.speedvalue, 1)
			self.speedstart=pg.time.get_ticks()

	def stop(self, timestop):
		if timestop-self.stopstart>=1000:
			self.speedvalue=0.1
			self.do_once_move=True
			self.sound=True

	def hitboxchange(self):
		self.hitbox=(self.car).get_rect()
		self.hitbox.topleft=(self.x, self.y)
		self.collisionslimit=[
			pg.rect.Rect(self.x-3, self.y-6, self.hitbox[2]+6, 6),
			pg.rect.Rect(self.x-3, self.y+self.hitbox[3], self.hitbox[2]+6, 6),
			pg.rect.Rect(self.x-6, self.y-3, 6, self.hitbox[3]+6),
			pg.rect.Rect(self.x+self.hitbox[2], self.y-3, 6, self.hitbox[3]+6)
		]

	def move(self, player, numplayer):
		if numplayer==1:
			if keys[pg.K_w] and keys[pg.K_a] and (not (self.cant_up or self.cant_left) and not (self.cant_up_p or self.cant_left_p)):
				self.car=player.Choice_Car[6]
				self.y-=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
				self.x-=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
			elif keys[pg.K_w] and keys[pg.K_d] and (not (self.cant_up or self.cant_right) and not (self.cant_up_p or self.cant_right_p)):
				self.car=player.Choice_Car[4]
				self.y-=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
				self.x+=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
			elif keys[pg.K_s] and keys[pg.K_a] and (not (self.cant_down or self.cant_left) and not (self.cant_down_p or self.cant_left_p)):
				self.car=player.Choice_Car[7]
				self.y+=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
				self.x-=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
			elif keys[pg.K_s] and keys[pg.K_d] and (not (self.cant_down or self.cant_right) and not (self.cant_down_p or self.cant_right_p)):
				self.car=player.Choice_Car[5]
				self.x+=((5*self.speedvalue+9*self.boostvalue+self.drift))/self.sand
				self.y+=((5*self.speedvalue+9*self.boostvalue+self.drift))/self.sand
			elif keys[pg.K_w] and keys[pg.K_s]:
				if self.boostact:
					self.boostactivate()
			elif keys[pg.K_d] and keys[pg.K_a]:
				if self.boostact:
					self.boostactivate()
			elif keys[pg.K_w] and (not self.cant_up and not self.cant_up_p):
				self.car=player.Choice_Car[2]
				self.y-=(5*self.speedvalue+9*self.boostvalue)/self.sand
			elif keys[pg.K_s] and (not self.cant_down and not self.cant_down_p):
				self.car=player.Choice_Car[1]
				self.y+=(5*self.speedvalue+9*self.boostvalue)/self.sand
			elif keys[pg.K_d] and (not self.cant_right and not self.cant_right_p):
				self.car=player.Choice_Car[0]
				self.x+=(5*self.speedvalue+9*self.boostvalue)/self.sand
			elif keys[pg.K_a] and (not self.cant_left and not self.cant_left_p):
				self.car=player.Choice_Car[3]
				self.x-=(5*self.speedvalue+9*self.boostvalue)/self.sand
		elif numplayer==2:
			if keys[pg.K_UP] and keys[pg.K_LEFT] and (not (self.cant_up or self.cant_left) and not (self.cant_up_p or self.cant_left_p)):
				self.car=player.Choice_Car[6]
				self.y-=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
				self.x-=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
			elif keys[pg.K_UP] and keys[pg.K_RIGHT] and (not (self.cant_up or self.cant_right) and not (self.cant_up_p or self.cant_right_p)):
				self.car=player.Choice_Car[4]
				self.y-=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
				self.x+=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
			elif keys[pg.K_DOWN] and keys[pg.K_LEFT] and (not (self.cant_down or self.cant_left) and not (self.cant_down_p or self.cant_left_p)):
				self.car=player.Choice_Car[7]
				self.y+=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
				self.x-=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
			elif keys[pg.K_DOWN] and keys[pg.K_RIGHT] and (not (self.cant_down or self.cant_right) and not (self.cant_down_p or self.cant_right_p)):
				self.car=player.Choice_Car[5]
				self.x+=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
				self.y+=(5*self.speedvalue+9*self.boostvalue+self.drift)/self.sand
			elif keys[pg.K_UP] and keys[pg.K_DOWN]:
				if self.boostact:
					self.boostactivate()
			elif keys[pg.K_RIGHT] and keys[pg.K_LEFT]:
				if self.boostact:
					self.boostactivate()
			elif keys[pg.K_UP] and (not self.cant_up and not self.cant_up_p):
				self.car=player.Choice_Car[2]
				self.y-=(5*self.speedvalue+9*self.boostvalue)/self.sand
			elif keys[pg.K_DOWN] and (not self.cant_down and not self.cant_down_p):
				self.car=player.Choice_Car[1]
				self.y+=(5*self.speedvalue+9*self.boostvalue)/self.sand
			elif keys[pg.K_RIGHT] and (not self.cant_right and not self.cant_right_p):
				self.car=player.Choice_Car[0]
				self.x+=(5*self.speedvalue+9*self.boostvalue)/self.sand
			elif keys[pg.K_LEFT] and (not self.cant_left and not self.cant_left_p):
				self.car=player.Choice_Car[3]
				self.x-=(5*self.speedvalue+9*self.boostvalue)/self.sand
		
	def reset(self, player):
		self.car=player.Choice_Car[0]
		self.speedvalue=0.1
		self.boostact=False
		self.boostchargemeter=-3
		self.x=456
		self.y=605
		self.laps=0
		self.lap_complete=0

	def check1(self):
		if self.lap_complete==0:
			self.lap_complete=1
	
	def check2(self):
		if self.lap_complete==1:
			self.lap_complete=2
	
	def check3(self):
		if self.lap_complete==2:
			self.lap_complete=3

	def startpoint(self):
		if self.lap_complete==3:
			self.laps+=1
			self.lap_complete=0
			
	def won(self, player_won):
		if self.laps==4 and player_won==0:
			return True
		else:
			return False
		
	def progressbar(self, player):
		if player==1:
			if self.boostchargemeter<0:
				screen.blit(progressbarp1[0], (10, 5))
			else:
				screen.blit(progressbarp1[self.boostchargemeter], (10, 5))
		elif player==2:
			if self.boostchargemeter<0:
				screen.blit(progressbarp2[0], (665, 5))
			else:
				screen.blit(progressbarp2[self.boostchargemeter], (665, 5))	

	def lapcounter(self, player):
		countertext=fontLapCounter.render(str(self.laps)+"/3", True, (50, 50, 50))
		if player==1:
			screen.blit(countertext, recttextlapcount1)
		elif player==2:
			screen.blit(countertext, recttextlapcount2)

	def singlelapcounter(self):
		countertext=fontLapCounter.render(str(self.laps)+"/3", True, (50, 50, 50))
		screen.blit(countertext, recttextlapcount1single)

	def identification(self, player):
		if player==1:
			screen.blit(p1id, ((self.x+(self.hitbox[2]/2))-15, (self.y+(self.hitbox[3]/4))-35))
		elif player==2:
			screen.blit(p2id, ((self.x+(self.hitbox[2]/2))-15, (self.y+(self.hitbox[3]/4))-35))

class PauseMenu:
	def __init__(self, screen_width, screen_height):
		self.width=(screen_width/10)*8
		self.cord_X1=(screen_width/10)
		self.cord_Y1=(screen_height/10)*3
		self.height=(screen_height/10)
		self.cord_Y2=(screen_height/10)*5

class MainMenu:
	def __init__(self, screen_width, screen_height):
		self.width=(screen_width/10*8)
		self.cord_X1=(screen_width/10)
		self.cord_fonty=(screen_height/10)*1
		self.cord_Y1=(screen_height/10)*4
		self.cord_Y2=(screen_height/10)*6
		self.cord_Y3=(screen_height/10)*8
		self.height=(screen_height/10)

class SelectCarMenu:
	def __init__(self, screen_width, screen_height):
		self.width=(screen_width/10)*3
		self.cord_X1=(screen_width/10)
		self.cord_X2=(screen_width/10)*6
		self.cord_Y1=(screen_height/10)
		self.cord_IMG_Y=(screen_height/10)*2.5
		self.cord_Y2=(screen_height/10)*8
		self.height=(screen_height/10)
		self.cord_X_single=(screen_width/10)*4
		self.cord_Bar1_Y=(screen_height/10)*5.5

def timerconfig(timenow, starttime):
	times=(timenow-starttime)//1000
	timem=times//60
	timeh=timem//60
	times-=timem*60
	timem-=timeh*60
	times, timem, timeh=str(times), str(timem), str(timeh)
	if len(timem)==1:
		timem="0"+timem
	if len(times)==1:
		times="0"+times
	if len(timeh)==1:
		timeh="0"+timeh
	return [times, timem, timeh]

def blinkingwinnertext(player_won, timer, starttime):
	if timer-starttime<=1000:
		winnertext=fontWinner.render("Player "+str(player_won)+" Wins", True, (255, 255, 255))
		screen.blit(winnertext, winnertextrect)
	elif timer-starttime>=1500:
		starttime=pg.time.get_ticks()
	return starttime

def blinkingtimertext(timetaken, timer, starttime):
	if timer-starttime<=1000:
		timerwinnertext=fontWinner.render("You took: "+timetaken, True, (255, 255, 255))
		screen.blit(timerwinnertext, timerwinnertextrect)
	elif timer-starttime>=1500:
		starttime=pg.time.get_ticks()
	return starttime

def besttimetaken(timetaken, besttime):
	timetakenint=int(timetaken[0:2])*3600+int(timetaken[3:5])*60+int(timetaken[6:8])
	if besttime==None:
		besttime=timetaken
	besttimeint=int(besttime[0:2])*3600+int(besttime[3:5])*60+int(besttime[6:8])
	if besttimeint>timetakenint:
		besttime=timetaken
	besttimewinnertext=fontSelectNMenu.render("Best Time: "+besttime, True, (255, 255, 255))
	screen.blit(besttimewinnertext, besttimewinnertextrect)
	return besttime

def startheadlight(time, timestart):
	if time-timestart<500:
		screen.blit(headlight[0], (474, 551))
	elif time-timestart<1500:
		screen.blit(headlight[1], (474, 551))
	elif time-timestart<2500:
		screen.blit(headlight[2], (474, 551))
	elif time-timestart<3500:
		screen.blit(headlight[3], (474, 551))
	else:
		screen.blit(headlight[0], (474, 551))
		return False	
	return True

def mainmenuselect(selected):
	for event in pg.event.get():
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_UP or event.key == pg.K_w:
				if selected==2:
					selected=0
				else:
					selected+=1
			if event.key == pg.K_DOWN or event.key == pg.K_s:
				if selected==0:
					selected=2
				else:
					selected-=1
	if selected==0:
		screen.blit(select, (mainmen.cord_X1-2, mainmen.cord_Y3-2))
	elif selected==1:
		screen.blit(select, (mainmen.cord_X1-2, mainmen.cord_Y2-2))
	elif selected==2:
		screen.blit(select, (mainmen.cord_X1-2, mainmen.cord_Y1-2))
	return selected

def pausemenuselect(selected):
	for event in pg.event.get():
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_UP or event.key == pg.K_w:
				if selected==1:
					selected=0
				else:
					selected+=1
			if event.key == pg.K_DOWN or event.key == pg.K_s:
				if selected==0:
					selected=1
				else:
					selected-=1
	if selected==0:
		screen.blit(select, (pausemenu.cord_X1-2, pausemenu.cord_Y2-2))
	elif selected==1:
		screen.blit(select, (pausemenu.cord_X1-2, pausemenu.cord_Y1-2))
	return selected

def gamemodecooldown(time, starttime):
	if time-starttime>1000:
		return False
	return True

def winmenuselect(selected):
	for event in pg.event.get():
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_UP or event.key == pg.K_w:
				if selected==1:
					selected=0
				else:
					selected+=1
			if event.key == pg.K_DOWN or event.key == pg.K_s:
				if selected==0:
					selected=1
				else:
					selected-=1
	if selected==0:
		screen.blit(select, (pausemenu.cord_X1-2, pausemenu.cord_Y2-2))
	elif selected==1:
		screen.blit(select, (pausemenu.cord_X1-2, pausemenu.cord_Y1-2))
	return selected

def delay(time, starttime):
	if time-starttime>4500:
		return True
	return False

def selectCarMen():
	for event in pg.event.get():
		if event.type == pg.KEYDOWN:
			if twoplayers and not p2.ready:
				if event.key == pg.K_RIGHT:
					if p2.selection==len(carnames)-1:
						p2.selection=0
					else:
						p2.selection+=1
				if event.key == pg.K_LEFT:
					if p2.selection==0:
						p2.selection=len(carnames)-1
					else:
						p2.selection-=1
			if not p1.ready:
				if event.key == pg.K_d:
					if p1.selection==len(carnames)-1:
						p1.selection=0
					else:
						p1.selection+=1
				if event.key == pg.K_a:
					if p1.selection==0:
						p1.selection=len(carnames)-1
					else:
						p1.selection-=1

def selectCarMenUI():
	global textcar1, textcar2, p1, p2
	screen.blit(buttonlt, (selectcar.cord_X1, selectcar.cord_Y1+200))
	screen.blit(buttonrt, (selectcar.cord_X1+selectcar.width-46, selectcar.cord_Y1+200))
	screen.blit(buttonlt, (selectcar.cord_X2, selectcar.cord_Y1+200))
	screen.blit(buttonrt, (selectcar.cord_X2+selectcar.width-46, selectcar.cord_Y1+200))
	screen.blit(selectcars[p1.selection], (selectcar.cord_X1+90, selectcar.cord_IMG_Y))
	for i in range(len(carnames)):
		if p1.selection==i:
			textcar1=fontLapCounter.render(carnames[i], True, (25, 25, 25))
			break
	rectcarname1=textcar1.get_rect()
	rectcarname1.center=(selectcar.cord_X1+selectcar.width/2, selectcar.cord_Y1+selectcar.height/2)
	screen.blit(textcar1, rectcarname1)
	screen.blit(selectcars[p2.selection], (selectcar.cord_X2+90, selectcar.cord_IMG_Y))
	for i in range(len(carnames)):
		if p2.selection==i:
			textcar2=fontLapCounter.render(carnames[i], True, (25, 25, 25))
			break
	rectcarname2=textcar2.get_rect()
	rectcarname2.center=(selectcar.cord_X2+selectcar.width/2, selectcar.cord_Y1+selectcar.height/2)
	screen.blit(textcar2, rectcarname2)

def selectrect():
	if p1.ready:
		screen.blit(buttonselectReady, (selectcar.cord_X1, selectcar.cord_Y2-33))
	else:
		screen.blit(buttonselectNotReady, (selectcar.cord_X1, selectcar.cord_Y2-33))
	screen.blit(textbutselectcar1, rectselectcar1)
	if p2.ready:
		screen.blit(buttonselectReady, (selectcar.cord_X2, selectcar.cord_Y2-33))
	else:
		screen.blit(buttonselectNotReady, (selectcar.cord_X2, selectcar.cord_Y2-33))
	screen.blit(textbutselectcar2, rectselectcar2)

def selectcarmenuUISingle():
	global textcarsingle, p1
	screen.blit(buttonlt, (selectcar.cord_X_single, selectcar.cord_Y1+200))
	screen.blit(buttonrt, (selectcar.cord_X_single+selectcar.width-46, selectcar.cord_Y1+200))
	screen.blit(selectcars[p1.selection], (selectcar.cord_X_single+90, selectcar.cord_IMG_Y))
	for i in range(len(carnames)):
		if p1.selection==i:
			textcarsingle=fontLapCounter.render(carnames[i], True, (25, 25, 25))
			break
	rectcarsingle=textcarsingle.get_rect()
	rectcarsingle.center=(selectcar.cord_X_single+selectcar.width/2, selectcar.cord_Y1+selectcar.height/2)
	screen.blit(textcarsingle, rectcarsingle)

def statBarsSingle():
	for speed_bar in range(len(statsbars)):
		if speed_bar == player1car.speed*10:
			screen.blit(statsbars[speed_bar], (selectcar.cord_X_single+100, selectcar.cord_Bar1_Y))
			break
	for acel_bar in range(len(statsbars)):
		if acel_bar == player1car.aceleration*10:
			screen.blit(statsbars[acel_bar], (selectcar.cord_X_single+100, selectcar.cord_Bar1_Y+25))
			break
	for boost_bar in range(len(statsbars)):
		if boost_bar == player1car.boost*10:
			screen.blit(statsbars[boost_bar], (selectcar.cord_X_single+100, selectcar.cord_Bar1_Y+50))
			break
	for charge_bar in range(len(statsbars)):
		if charge_bar == player1car.charge*10:
			screen.blit(statsbars[charge_bar], (selectcar.cord_X_single+100, selectcar.cord_Bar1_Y+75))
			break
	screen.blit(speedBarText, rectspeedBarTextSingle)
	screen.blit(accelBarText, rectaccelBarTextSingle)
	screen.blit(boostBarText, rectboostBarTextSingle)
	screen.blit(chargeBarText, rectchargeBarTextSingle)

def statBarsMain():
	for speed_bar in range(len(statsbars)):
		if speed_bar == player1car.speed*10:
			screen.blit(statsbars[speed_bar], (selectcar.cord_X1+50, selectcar.cord_Bar1_Y))
			break
	for acel_bar in range(len(statsbars)):
		if acel_bar == player1car.aceleration*10:
			screen.blit(statsbars[acel_bar], (selectcar.cord_X1+50, selectcar.cord_Bar1_Y+25))
			break
	for boost_bar in range(len(statsbars)):
		if boost_bar == player1car.boost*10:
			screen.blit(statsbars[boost_bar], (selectcar.cord_X1+50, selectcar.cord_Bar1_Y+50))
			break
	for charge_bar in range(len(statsbars)):
		if charge_bar == player1car.charge*10:
			screen.blit(statsbars[charge_bar], (selectcar.cord_X1+50, selectcar.cord_Bar1_Y+75))
			break
	for speed_bar in range(len(statsbars)):
		if speed_bar == player2car.speed*10:
			screen.blit(statsbars[speed_bar], (selectcar.cord_X2+50, selectcar.cord_Bar1_Y))
			break
	for acel_bar in range(len(statsbars)):
		if acel_bar == player2car.aceleration*10:
			screen.blit(statsbars[acel_bar], (selectcar.cord_X2+50, selectcar.cord_Bar1_Y+25))
			break
	for boost_bar in range(len(statsbars)):
		if boost_bar == player2car.boost*10:
			screen.blit(statsbars[boost_bar], (selectcar.cord_X2+50, selectcar.cord_Bar1_Y+50))
			break
	for charge_bar in range(len(statsbars)):
		if charge_bar == player2car.charge*10:
			screen.blit(statsbars[charge_bar], (selectcar.cord_X2+50, selectcar.cord_Bar1_Y+75))
			break
	screen.blit(speedBarText, rectspeedBarTextMain)
	screen.blit(accelBarText, rectaccelBarTextMain)
	screen.blit(boostBarText, rectboostBarTextMain)
	screen.blit(chargeBarText, rectchargeBarTextMain)

pg.init()

#Car1 Sprites and Stats
car1=[
	pg.image.load("CarRt.png"),
	pg.image.load("CarDn.png"),
	pg.image.load("CarUp.png"),
	pg.image.load("CarLt.png"),
	pg.image.load("CarRtUp.png"),
	pg.image.load("CarRtDn.png"),
	pg.image.load("CarLtUp.png"),
	pg.image.load("CarLtDn.png"),
	0.8,
	0.7,
	0.6,
	0.5,
	0,
	0
]

#Car2 Sprites and Stats
car2=[
	pg.image.load("F1Rt.png"),
	pg.image.load("F1Dn.png"),
	pg.image.load("F1Up.png"),
	pg.image.load("F1Lt.png"),
	pg.image.load("F1RtUp.png"),
	pg.image.load("F1RtDn.png"),
	pg.image.load("F1LtUp.png"),
	pg.image.load("F1LtDn.png"),
	1,
	0.9,
	0.3,
	0.2,
	0,
	0
]

#Car3 Sprites and Stats
car3=[
	pg.image.load("LowRiderRt.png"),
	pg.image.load("LowRiderDn.png"),
	pg.image.load("LowRiderUp.png"),
	pg.image.load("LowRiderLt.png"),
	pg.image.load("LowRiderRtUp.png"),
	pg.image.load("LowRiderRtDn.png"),
	pg.image.load("LowRiderLtUp.png"),
	pg.image.load("LowRiderLtDn.png"),
	0.7,
	0.7,
	1,
	0.8,
	0,
	0
]

#Car4 Sprites and Stats
car4=[
	pg.image.load("DriftRt.png"),
	pg.image.load("DriftDn.png"),
	pg.image.load("DriftUp.png"),
	pg.image.load("DriftLt.png"),
	pg.image.load("DriftRtUp.png"),
	pg.image.load("DriftRtDn.png"),
	pg.image.load("DriftLtUp.png"),
	pg.image.load("DriftLtDn.png"),
	0.8,
	0.7,
	0.7,
	0.6,
	1,
	0
]

#Car5 Sprites and Stats
car5=[
	pg.image.load("RallyRt.png"),
	pg.image.load("RallyDn.png"),
	pg.image.load("RallyUp.png"),
	pg.image.load("RallyLt.png"),
	pg.image.load("RallyRtUp.png"),
	pg.image.load("RallyRtDn.png"),
	pg.image.load("RallyLtUp.png"),
	pg.image.load("RallyLtDn.png"),
	0.8,
	0.7,
	0.5,
	0.4,
	0,
	1
]

#Car6 Sprites and Stats
car6=[
	pg.image.load("MuscleRt.png"),
	pg.image.load("MuscleDn.png"),
	pg.image.load("MuscleUp.png"),
	pg.image.load("MuscleLt.png"),
	pg.image.load("MuscleRtUp.png"),
	pg.image.load("MuscleRtDn.png"),
	pg.image.load("MuscleLtUp.png"),
	pg.image.load("MuscleLtDn.png"),
	0.9,
	0.8,
	0.5,
	0.3,
	0,
	0
]

#Headlight Sprites
headlight=[
	pg.image.load("HeadLightsBasic.png"),
	pg.image.load("HeadLights1.png"),
	pg.image.load("HeadLights2.png"),
	pg.image.load("HeadLights3.png")
]

#Limits
limits=[
	[#limit up
		pg.rect.Rect(9, 66, 711, 6),
		pg.rect.Rect(127, 253, 100, 6),
		pg.rect.Rect(242, 296, 358, 6),
		pg.rect.Rect(403, 423, 323, 6),
		pg.rect.Rect(224, 575, 649, 6),
		pg.rect.Rect(722, 97, 268, 6)
	],
	[#limit down
		pg.rect.Rect(106, 690, 885, 6),
		pg.rect.Rect(243, 538, 601, 6),
		pg.rect.Rect(403, 411, 317, 6),
		pg.rect.Rect(9, 368, 100, 6),
		pg.rect.Rect(841, 230, 32, 6),
		pg.rect.Rect(127, 181, 473, 6)
	],
	[#limit left
		pg.rect.Rect(9, 66, 6, 308),
		pg.rect.Rect(106, 371, 6, 325),
		pg.rect.Rect(243, 296, 6, 248),
		pg.rect.Rect(597, 184, 6, 115),
		pg.rect.Rect(722, 97, 6, 329),
		pg.rect.Rect(870, 233, 6, 345)
	],
	[#limit right
		pg.rect.Rect(114, 184, 6, 72),
		pg.rect.Rect(221, 253, 6, 325),
		pg.rect.Rect(985, 97, 6, 599),
		pg.rect.Rect(838, 233, 6, 311),
		pg.rect.Rect(400, 414, 6, 12),
		pg.rect.Rect(713, 66, 6, 351)
	]
]

#Sand collision
sand=[
	pg.rect.Rect(111, 168, 506, 19),
	pg.rect.Rect(111, 253, 116, 19),
	pg.rect.Rect(243, 525, 601, 19),
	pg.rect.Rect(345, 423, 397, 19),
	pg.rect.Rect(345, 398, 375, 19),
	pg.rect.Rect(243, 296, 373, 19),
	pg.rect.Rect(825, 199, 64, 37),
	pg.rect.Rect(722, 97, 269, 19),
	pg.rect.Rect(208, 575, 681, 19),
	pg.rect.Rect(9, 66, 711, 19),
	pg.rect.Rect(106, 677, 885, 19),
	pg.rect.Rect(9, 355, 116, 19),
	pg.rect.Rect(9, 66, 19, 308),
	pg.rect.Rect(106, 355, 19, 341),
	pg.rect.Rect(111, 168, 19, 104),
	pg.rect.Rect(208, 253, 19, 341),
	pg.rect.Rect(243, 296, 19, 248),
	pg.rect.Rect(345, 398, 61, 44),
	pg.rect.Rect(597, 168, 19, 147),
	pg.rect.Rect(699, 66, 19, 351),
	pg.rect.Rect(722, 97, 19, 345),
	pg.rect.Rect(825, 199, 19, 346),
	pg.rect.Rect(870, 199, 19, 395),
	pg.rect.Rect(972, 97, 19, 599)
]

#Player 1 Progress bar
progressbarp1=[
	pg.image.load("ProgressBar0p1.png"),
	pg.image.load("ProgressBar1p1.png"),
	pg.image.load("ProgressBar2p1.png"),
	pg.image.load("ProgressBar3p1.png"),
	pg.image.load("ProgressBar4p1.png"),
	pg.image.load("ProgressBar5p1.png"),
	pg.image.load("ProgressBar6p1.png"),
	pg.image.load("ProgressBar7p1.png"),
	pg.image.load("ProgressBar8p1.png"),
	pg.image.load("ProgressBar9p1.png"),
	pg.image.load("ProgressBar10p1.png")
]

#Player 2 Progress bar
progressbarp2=[
	pg.image.load("ProgressBar0p2.png"),
	pg.image.load("ProgressBar1p2.png"),
	pg.image.load("ProgressBar2p2.png"),
	pg.image.load("ProgressBar3p2.png"),
	pg.image.load("ProgressBar4p2.png"),
	pg.image.load("ProgressBar5p2.png"),
	pg.image.load("ProgressBar6p2.png"),
	pg.image.load("ProgressBar7p2.png"),
	pg.image.load("ProgressBar8p2.png"),
	pg.image.load("ProgressBar9p2.png"),
	pg.image.load("ProgressBar10p2.png")
]

#List of cars
listcars=[
	car1,
	car2,
	car3,
	car4,
	car5,
	car6
]

#Car Images
selectcars=[
	pg.image.load("CarMain.png"),
	pg.image.load("F1Main.png"),
	pg.image.load("LowRiderMain.png"),
	pg.image.load("DriftMain.png"),
	pg.image.load("RallyMain.png"),
	pg.image.load("MuscleMain.png")
]

#Car names
carnames=[
	"Sports Car",
	"Formula 1 Car",
	"Low Rider",
	"Drift Car",
	"Rally Car",
	"Muscle Car"
]

#Stats Bar
statsbars=[
	"",
	pg.image.load("StatsBar1.png"),
	pg.image.load("StatsBar2.png"),
	pg.image.load("StatsBar3.png"),
	pg.image.load("StatsBar4.png"),
	pg.image.load("StatsBar5.png"),
	pg.image.load("StatsBar6.png"),
	pg.image.load("StatsBar7.png"),
	pg.image.load("StatsBar8.png"),
	pg.image.load("StatsBar9.png"),
	pg.image.load("StatsBar10.png"),
]

#Player 1 and Player 2 classes
p1=Player(car1)
p2=Player(car1)
player1car=Car(p1.Choice_Car, p1.Choice_Car[0])
player2car=Car(p2.Choice_Car, p2.Choice_Car[0])
p1id=pg.image.load("P1ID.png")
p2id=pg.image.load("P2ID.png")

#Screen
track=pg.image.load("Track.png")
screen=pg.display.set_mode((1000,700))
screen.fill((120, 120, 120))
pg.display.flip()
pg.display.set_caption("Fast Racer")
button=pg.image.load("Button.png")

#Fonts
fontLapCounter=pg.font.Font("COMEBREAK.ttf", 40)
fontWinner=pg.font.Font("COMEBREAK.ttf", 100)
fontSelectNMenu=pg.font.Font("COMEBREAK.ttf", 60)
fontMainQuit=pg.font.Font("COMEBREAK.ttf", 70)
fontMainMenu=pg.font.Font("Slugs Racer.ttf", 70)
fontMainMenuLabel=pg.font.Font("Slugs Racer.ttf", 100)
fontTimer=pg.font.Font("COMEBREAK.ttf", 50)
fontStatBars=pg.font.Font("COMEBREAK.ttf", 20)

#Pause Menu
textbut1=fontSelectNMenu.render("Resume", True, (30, 30, 30))
textbut2=fontSelectNMenu.render("Main Menu", True, (30, 30, 30))
rectpausemenubut1=textbut1.get_rect()
rectpausemenubut2=textbut2.get_rect()
pausemenu=PauseMenu(screen.get_width(), screen.get_height())
rectpausemenubut1.center=((pausemenu.cord_X1+(pausemenu.width/2)), pausemenu.cord_Y1+(pausemenu.height/2))
rectpausemenubut2.center=((pausemenu.cord_X1+(pausemenu.width/2)), pausemenu.cord_Y2+(pausemenu.height/2))

#WinMenu
textbut1win=fontSelectNMenu.render("Main Menu", True, (30, 30, 30))
textbut2win=fontSelectNMenu.render("Quit", True, (30, 30, 30))
rectwinmenubut1=textbut1win.get_rect()
rectwinmenubut2=textbut2win.get_rect()
rectwinmenubut1.center=((pausemenu.cord_X1+(pausemenu.width/2)), pausemenu.cord_Y1+(pausemenu.height/2))
rectwinmenubut2.center=((pausemenu.cord_X1+(pausemenu.width/2)), pausemenu.cord_Y2+(pausemenu.height/2))

#Lap Counter
textlapcount1=fontLapCounter.render("0/5", True, (50, 50, 50))
textlapcount2=fontLapCounter.render("0/5", True, (50, 50, 50))
recttextlapcount1=textlapcount1.get_rect()
recttextlapcount2=textlapcount2.get_rect()
recttextlapcount1single=textlapcount1.get_rect()
recttextlapcount1.topleft=(345, 5)
recttextlapcount2.topright=(1000-345, 5)
recttextlapcount1single.topright=(990, 5)


#Main Menu
textbut1main=fontMainMenu.render("1  Player", True, (30, 30, 30))
textbut2main=fontMainMenu.render("2  Players", True, (30, 30, 30))
textbut3main=fontMainQuit.render("Quit", True, (30, 30, 30))
mainmenlabel=fontMainMenuLabel.render("Fast  Racers", True, (225, 90, 90))
mainmenlabelrect=mainmenlabel.get_rect()
rectpausemenubut1main=textbut1main.get_rect()
rectpausemenubut2main=textbut2main.get_rect()
rectpausemenubut3main=textbut3main.get_rect()
mainmen=MainMenu(screen.get_width(), screen.get_height())
select=pg.image.load("Select.png")
rectpausemenubut1main.center=((mainmen.cord_X1+(mainmen.width/2)), mainmen.cord_Y1+(mainmen.height/2))
rectpausemenubut2main.center=((mainmen.cord_X1+(mainmen.width/2)), mainmen.cord_Y2+(mainmen.height/2))
rectpausemenubut3main.center=((mainmen.cord_X1+(mainmen.width/2)), mainmen.cord_Y3+(mainmen.height/2))
mainmenlabelrect.center=((mainmen.cord_X1+(mainmen.width/2), mainmen.cord_fonty+(mainmen.height/2)))

#Timer
timertext=fontTimer.render("00:00:00", True, (35, 35, 35))
timerrect=timertext.get_rect()
timerrect.center=((screen.get_width())/2, 25)

#Winner
winnertext=fontWinner.render("Player 1 Wins", True, (200, 200, 200))
winnertextrect=winnertext.get_rect()
winnertextrect.center=((screen.get_width())/2, (screen.get_height())/2)

#Timer Winner
timerwinnertext=fontWinner.render("You took: 00:00:00", True, (200, 200, 200))
timerwinnertextrect=timerwinnertext.get_rect()
timerwinnertextrect.center=((screen.get_width())/2, (screen.get_height())/2)
besttimewinnertext=fontSelectNMenu.render("Best Time: 00:00:00", True, (200, 200, 200))
besttimewinnertextrect=besttimewinnertext.get_rect()
besttimewinnertextrect.center=((screen.get_width())/2, ((screen.get_height())/10)*8)

#Select Car Menu
buttonrt=pg.image.load("ButtonSelectRt.png")
buttonlt=pg.image.load("ButtonSelectLt.png")
buttonselectReady=pg.image.load("ButtonSelectReady.png")
buttonselectNotReady=pg.image.load("ButtonSelectNotReady.png")
selectcar=SelectCarMenu(screen.get_width(), screen.get_height())
textbutselectcar1=fontLapCounter.render("Ready", True, (30, 30, 30))
textbutselectcar2=fontLapCounter.render("Ready", True, (30, 30, 30))
textcar1=fontLapCounter.render("Formula 1 Car", True, (25, 25, 25))
textcar2=fontLapCounter.render("Formula 1 Car", True, (25, 25, 25))
rectselectcar1=textbutselectcar1.get_rect()
rectselectcar2=textbutselectcar2.get_rect()
rectcarname1=textcar1.get_rect()
rectcarname2=textcar2.get_rect()
rectselectcar1.center=(selectcar.cord_X1+selectcar.width/2, selectcar.cord_Y2+selectcar.height/2)
rectselectcar2.center=(selectcar.cord_X2+selectcar.width/2, selectcar.cord_Y2+selectcar.height/2)
rectcarname1.center=(selectcar.cord_X1+selectcar.width/2, selectcar.cord_Y1+selectcar.height/2)
rectcarname2.center=(selectcar.cord_X2+selectcar.width/2, selectcar.cord_Y1+selectcar.height/2)
textbutselectcarsingle=fontLapCounter.render("Ready", True, (30, 30, 30))
rectselectcarsingle=textbutselectcarsingle.get_rect()
rectselectcarsingle.center=(selectcar.cord_X_single+selectcar.width/2, selectcar.cord_Y2+selectcar.height/2)
textcarsingle=fontLapCounter.render("Formula 1 Car", True, (25, 25, 25))
rectcarsingle=textcarsingle.get_rect()
rectcarsingle.center=(selectcar.cord_X_single+selectcar.width/2, selectcar.cord_Y1+selectcar.height/2)
speedBarText=fontStatBars.render("Speed", True, (25, 25, 25))
accelBarText=fontStatBars.render("Acceleration", True, (25, 25, 25))
boostBarText=fontStatBars.render("Boost", True, (25, 25, 25))
chargeBarText=fontStatBars.render("Charge", True, (25, 25, 25))
rectspeedBarTextSingle=speedBarText.get_rect()
rectaccelBarTextSingle=accelBarText.get_rect()
rectboostBarTextSingle=boostBarText.get_rect()
rectchargeBarTextSingle=chargeBarText.get_rect()
rectspeedBarTextSingle.center=(selectcar.cord_X_single+25,  selectcar.cord_Bar1_Y+10)
rectaccelBarTextSingle.center=(selectcar.cord_X_single+25,  selectcar.cord_Bar1_Y+35)
rectboostBarTextSingle.center=(selectcar.cord_X_single+25,  selectcar.cord_Bar1_Y+60)
rectchargeBarTextSingle.center=(selectcar.cord_X_single+25,  selectcar.cord_Bar1_Y+85)
rectspeedBarTextMain=speedBarText.get_rect()
rectaccelBarTextMain=accelBarText.get_rect()
rectboostBarTextMain=boostBarText.get_rect()
rectchargeBarTextMain=chargeBarText.get_rect()
rectspeedBarTextMain.center=(selectcar.cord_X_single+100,  selectcar.cord_Bar1_Y+10)
rectaccelBarTextMain.center=(selectcar.cord_X_single+100,  selectcar.cord_Bar1_Y+35)
rectboostBarTextMain.center=(selectcar.cord_X_single+100,  selectcar.cord_Bar1_Y+60)
rectchargeBarTextMain.center=(selectcar.cord_X_single+100,  selectcar.cord_Bar1_Y+85)

#Checkpoints
checkpoint1=pg.rect.Rect(870, 292, 121, 15)
checkpoint2=pg.rect.Rect(487, 296, 15, 121)
checkpoint3=pg.rect.Rect(106, 412, 121, 15)
startpoint=pg.rect.Rect(490, 575, 15, 121)

#Game Variables
GameOn=True
paumen=False
do_once=True
clock = pg.time.Clock()
do_once_music=True
Mainmenu=True
player2car.y=player1car.y+39
twoplayers=False
do_once_main_music=True
timer=pg.time.get_ticks()
timerstart=0
player_Won=0
do_once_winner=True
blinkstarttime=0
headlight_active=True
time_taken="00:00:00"
best_time=None
mainmenuselected=2
pausemenuselected=1
justexited=False
cooldownstarttime=0
menuWin=False
winmenuselected=1
winstarttime=0
selectmenu=True
acceleratingsound=pg.mixer.Sound("Accelerating.mp3")

while GameOn:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			GameOn=False
	keys=pg.key.get_pressed()
	mouse=pg.mouse.get_pos()
	mouseclick=pg.mouse.get_pressed()
	screen.blit(track, (0, 0))
	if Mainmenu:
		#Main Menu
		if do_once_main_music:
			do_once_main_music=False
			pg.mixer.music.load("Start Menu.mp3")
			pg.mixer_music.play(-1)
		screen.blit(button, (mainmen.cord_X1, mainmen.cord_Y1))
		screen.blit(button, (mainmen.cord_X1, mainmen.cord_Y2))
		screen.blit(button, (mainmen.cord_X1, mainmen.cord_Y3))
		mainmenuselected=mainmenuselect(mainmenuselected)
		screen.blit(textbut1main, rectpausemenubut1main)
		screen.blit(textbut2main, rectpausemenubut2main)
		screen.blit(textbut3main, rectpausemenubut3main)
		screen.blit(mainmenlabel, mainmenlabelrect)

		if justexited:
			justexited=gamemodecooldown(pg.time.get_ticks(), cooldownstarttime)
		else:
			#Select Main Menu Button
			if keys[pg.K_d] or keys[pg.K_RIGHT]:
				if mainmenuselected==0:
					GameOn=False
				elif mainmenuselected==1:
					Mainmenu=False
					twoplayers=True
					do_once_main_music=True
					do_once_winner=True
					player_Won=0
					menuWin=False
					p2.ready=False
					p1.ready=False
					selectmenu=True
				elif mainmenuselected==2:
					Mainmenu=False
					twoplayers=False
					do_once_main_music=True
					player_Won=0
					menuWin=False
					selectmenu=True

		#Check Mouse Click
		if mouseclick[0]:
			if mainmen.cord_X1<=mouse[0]<=mainmen.cord_X1+mainmen.width and mainmen.cord_Y1<=mouse[1]<=mainmen.cord_Y1+mainmen.height:
				Mainmenu=False
				twoplayers=False
				do_once_main_music=True
				player_Won=0
				menuWin=False
				selectmenu=True
			if mainmen.cord_X1<=mouse[0]<=mainmen.cord_X1+mainmen.width and mainmen.cord_Y2<=mouse[1]<=mainmen.cord_Y2+mainmen.height:
				Mainmenu=False
				twoplayers=True
				do_once_main_music=True
				do_once_winner=True
				timeheadlightstart=pg.time.get_ticks()
				player_Won=0
				menuWin=False
				p1.ready=False
				p2.ready=False
				selectmenu=True
			if mainmen.cord_X1<=mouse[0]<=mainmen.cord_X1+mainmen.width and mainmen.cord_Y3<=mouse[1]<=mainmen.cord_Y3+mainmen.height:
				GameOn=False
		
	elif paumen:
		#Pause Menu
		if do_once:
			pg.mixer.music.load("Pause Menu.mp3") 
			pg.mixer.music.play(-1)
			do_once=False
		screen.blit(button, (pausemenu.cord_X1, pausemenu.cord_Y1))
		screen.blit(button, (pausemenu.cord_X1, pausemenu.cord_Y2))
		pausemenuselected=pausemenuselect(pausemenuselected)
		screen.blit(textbut1, rectpausemenubut1)
		screen.blit(textbut2, rectpausemenubut2)

		#Select Pause Menu Button
		if keys[pg.K_d] or keys[pg.K_RIGHT]:
			if pausemenuselected==0:
				paumen=False
				Mainmenu=True
				do_once=True
				headlight_active=True
				justexited=True
				cooldownstarttime=pg.time.get_ticks()
			elif pausemenuselected==1:
				paumen=False
				do_once=True

		#Check Mouse Click
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					paumen=False
					do_once=True
		if mouseclick[0]: 
			if pausemenu.cord_X1<=mouse[0]<=pausemenu.cord_X1+pausemenu.width  and pausemenu.cord_Y1<=mouse[1]<=pausemenu.cord_Y1+pausemenu.height:
				paumen=False
				do_once=True
			if pausemenu.cord_X1<=mouse[0]<=pausemenu.cord_X1+pausemenu.width  and pausemenu.cord_Y2<=mouse[1]<=pausemenu.cord_Y2+pausemenu.height:
				paumen=False
				Mainmenu=True
				do_once=True
				headlight_active=True
				justexited=True
				cooldownstarttime=pg.time.get_ticks()
					
	else:
		if selectmenu:
			if twoplayers:
				#2 Player Select Car Menu
				if keys[pg.K_DOWN] and not p2.ready:
					p2.ready=True	
				elif keys[pg.K_UP] and p2.ready:
					p2.ready=False
				if keys[pg.K_s] and not p1.ready:
					p1.ready=True
				elif keys[pg.K_w] and p1.ready:
					p1.ready=False
				selectCarMen()
				selectCarMenUI()
				selectrect()
				for i in range(len(listcars)):
					if p1.selection==i:
						p1.Choice_Car=listcars[i]
					if p2.selection==i:
						p2.Choice_Car=listcars[i]
				player1car=Car(p1.Choice_Car, p1.Choice_Car[0])
				player2car=Car(p2.Choice_Car, p2.Choice_Car[0])
				statBarsMain()
				if p1.ready and p2.ready:
					selectmenu=False
					headlight_active=True
					timeheadlightstart=pg.time.get_ticks()
					player1car.clockrecharge=pg.time.get_ticks()
					player2car.clockrecharge=pg.time.get_ticks()
					player1car.reset(p1)
					player2car.reset(p2)
					player2car.y=player1car.y+46
			else:
				#Single Player Select Car Menu
				selectCarMen()
				selectcarmenuUISingle()
				screen.blit(buttonselectNotReady, (selectcar.cord_X_single, selectcar.cord_Y2-33))
				screen.blit(textbutselectcarsingle, rectselectcarsingle)
				for i in range(len(listcars)):
					if p1.selection==i:
						p1.Choice_Car=listcars[i]
						break
				player1car=Car(p1.Choice_Car, p1.Choice_Car[0])
				statBarsSingle()
				if keys[pg.K_s]:
					selectmenu=False
					headlight_active=True
					timeheadlightstart=pg.time.get_ticks()
					player1car.clockrecharge=pg.time.get_ticks()
					player1car.reset(p1)

		else:
			if do_once_music:
				pg.mixer.music.load("Smart Race.mp3")
				pg.mixer.music.play(-1)
				do_once_music=False

			for event in pg.event.get():
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_ESCAPE:
						paumen=True
						do_once_music=True
			if headlight_active:
				headlight_active=startheadlight(pg.time.get_ticks(), timeheadlightstart)
				if not headlight_active:
					timerstart=pg.time.get_ticks()
					player1car.clockrecharge=pg.time.get_ticks()
					if twoplayers:
						player2car.clockrecharge=pg.time.get_ticks()
				screen.blit(player1car.car, (player1car.x, player1car.y))
				if twoplayers:
					screen.blit(player2car.car, (player2car.x, player2car.y))
			else:
				screen.blit(headlight[0], (474, 551))
				if player_Won==0:

					#Player 1 with Player 2 collision
					if twoplayers:
						for i in range(len(player2car.collisionslimit)):
							collide=(player2car.collisionslimit[i]).colliderect(player1car.hitbox)
							if collide:
								if i == 0:
									player1car.cant_down_p=True
								elif i == 1:
									player1car.cant_up_p=True
								elif i == 2:
									player1car.cant_right_p=True
								elif i == 3:
									player1car.cant_left_p=True
							else:
								if i == 0:
									player1car.cant_down_p=False
								elif i == 1:
									player1car.cant_up_p=False
								elif i == 2:
									player1car.cant_right_p=False
								elif i == 3:
									player1car.cant_left_p=False
					
					#Check collision with limits
					for limitcheck in range(len(limits)):
						for limit in limits[limitcheck]:
							collidelimit=limit.colliderect(player1car.hitbox)
							if collidelimit:
								if limitcheck==0:
									player1car.cant_up=True
									break
								elif limitcheck==1:
									player1car.cant_down=True
									break
								elif limitcheck==2:
									player1car.cant_left=True
									break
								elif limitcheck==3:
									player1car.cant_right=True
									break
							if limitcheck==0:
								player1car.cant_up=False
							elif limitcheck==1:
								player1car.cant_down=False
							elif limitcheck==2:
								player1car.cant_left=False
							elif limitcheck==3:
								player1car.cant_right=False

					#Check collision with sand
					for sandcheck in sand:
						collidesand=sandcheck.colliderect(player1car.hitbox)
						if collidesand and player1car.sandresist==0:
							player1car.sand=2
							break
						player1car.sand=1
					
					#movement and boost player 1
					player1car.movement=(player1car.x, player1car.y)
					player1car.move(p1, 1)
					if (player1car.x, player1car.y)!=player1car.movement:
						if player1car.do_once_move:
							player1car.speedstart=pg.time.get_ticks()
							player1car.do_once_move=False
						player1car.do_once_stop=True
						player1car.speedup(pg.time.get_ticks())
					else:
						if player1car.do_once_stop:
							player1car.stopstart=pg.time.get_ticks()
							player1car.do_once_stop=False
						player1car.stop(pg.time.get_ticks())
					if player1car.boostacttimer:
						player1car.boostactive(pg.time.get_ticks())
					if not player1car.boostact:
						player1car.boostrecharge(pg.time.get_ticks())
					player1car.progressbar(1)
					screen.blit(player1car.car, (player1car.x, player1car.y))
					player1car.hitboxchange()

					#Collision Checkpoints player 1
					collidecheck1=(player1car.hitbox).colliderect(checkpoint1)
					if collidecheck1:
						player1car.check1()
					collidecheck2=(player1car.hitbox).colliderect(checkpoint2)
					if collidecheck2:
						player1car.check2()
					collidecheck3=(player1car.hitbox).colliderect(checkpoint3)
					if collidecheck3:
						player1car.check3()
					collidecheckstart=(player1car.hitbox).colliderect(startpoint)
					if collidecheckstart:
						player1car.startpoint()

					if twoplayers:

						#Player 2 with Player 1 collision
						for i in range(len(player1car.collisionslimit)):
							collide=(player1car.collisionslimit[i]).colliderect(player2car.hitbox)
							if collide:
								if i == 0:
									player2car.cant_down_p=True
								elif i == 1:
									player2car.cant_up_p=True
								elif i == 2:
									player2car.cant_right_p=True
								elif i == 3:
									player2car.cant_left_p=True
							else:
								if i == 0:
									player2car.cant_down_p=False
								elif i == 1:
									player2car.cant_up_p=False
								elif i == 2:
									player2car.cant_right_p=False
								elif i == 3:
									player2car.cant_left_p=False

						#Check collision with limits
						for limitcheck in range(len(limits)):
							for limit in limits[limitcheck]:
								collidelimit=limit.colliderect(player2car.hitbox)
								if collidelimit:
									if limitcheck==0:
										player2car.cant_up=True
										break
									elif limitcheck==1:
										player2car.cant_down=True
										break
									elif limitcheck==2:
										player2car.cant_left=True
										break
									elif limitcheck==3:
										player2car.cant_right=True
										break
								if limitcheck==0:
									player2car.cant_up=False
								elif limitcheck==1:
									player2car.cant_down=False
								elif limitcheck==2:
									player2car.cant_left=False
								elif limitcheck==3:
									player2car.cant_right=False

						#Check collision with sand
						for sandcheck in sand:
							collidesand=sandcheck.colliderect(player2car.hitbox)
							if collidesand and player2car.sandresist==0:
								player2car.sand=2
								break
							player2car.sand=1

						#movement and boost player 2
						player2car.movement=(player2car.x, player2car.y)
						player2car.move(p2, 2)
						if (player2car.x, player2car.y)!=player2car.movement:
							if player2car.do_once_move:
								player2car.speedstart=pg.time.get_ticks()
								player2car.do_once_move=False
							player2car.do_once_stop=True
							player2car.speedup(pg.time.get_ticks())
						else:
							if player2car.do_once_stop:
								player2car.stopstart=pg.time.get_ticks()
								player2car.do_once_stop=False
							player2car.stop(pg.time.get_ticks())
						if player2car.boostacttimer:
							player2car.boostactive(pg.time.get_ticks())
						if not player2car.boostact:
							player2car.boostrecharge(pg.time.get_ticks())
						player2car.progressbar(2)
						screen.blit(player2car.car, (player2car.x, player2car.y))
						player2car.hitboxchange()

						#Player Identification
						player1car.identification(1)
						player2car.identification(2)

						#Collision Checkpoints player 2
						collidecheck1=(player2car.hitbox).colliderect(checkpoint1)
						if collidecheck1:
							player2car.check1()
						collidecheck2=(player2car.hitbox).colliderect(checkpoint2)
						if collidecheck2:
							player2car.check2()
						collidecheck3=(player2car.hitbox).colliderect(checkpoint3)
						if collidecheck3:
							player2car.check3()
						collidecheckstart=(player2car.hitbox).colliderect(startpoint)
						if collidecheckstart:
							player2car.startpoint()
						
						#Lap counter
						player1car.lapcounter(1)
						player2car.lapcounter(2) 
													
						#Check if player 1 or player 2 won
						if player1car.won(player_Won):
							player_Won=1
						elif player2car.won(player_Won):
							player_Won=2

					else:
						#Single Player Timer
						timer=pg.time.get_ticks()
						time=timerconfig(timer, timerstart)
						timertext=fontTimer.render(time[2]+":"+time[1]+":"+time[0], True, (35, 35, 35))
						screen.blit(timertext, timerrect)

						#Lap counter
						player1car.singlelapcounter()

						#Check if player completed race
						if player1car.won(player_Won):
							player_Won=1
							time_taken=time[2]+":"+time[1]+":"+time[0]
				else:
					if do_once_winner:
						do_once_winner=False
						blinkstarttime=pg.time.get_ticks()
						winstarttime=pg.time.get_ticks()
					if twoplayers:
						if menuWin:
							screen.blit(button, (pausemenu.cord_X1, pausemenu.cord_Y1))
							screen.blit(button, (pausemenu.cord_X1, pausemenu.cord_Y2))
							winmenuselected=pausemenuselect(winmenuselected)
							screen.blit(textbut1win, rectwinmenubut1)
							screen.blit(textbut2win, rectwinmenubut2)

							#Select Pause Menu Button
							if keys[pg.K_d] or keys[pg.K_RIGHT]:
								if winmenuselected==0:
									GameOn=False
								elif winmenuselected==1:
									paumen=False
									Mainmenu=True
									do_once=True
									headlight_active=True
									justexited=True
									cooldownstarttime=pg.time.get_ticks()

							#Check Mouse Click
							if mouseclick[0]: 
								if pausemenu.cord_X1<=mouse[0]<=pausemenu.cord_X1+pausemenu.width  and pausemenu.cord_Y1<=mouse[1]<=pausemenu.cord_Y1+pausemenu.height:
									Mainmenu=True
									do_once=True
									headlight_active=True
									menuWin=False
									justexited=True
									cooldownstarttime=pg.time.get_ticks()
								if pausemenu.cord_X1<=mouse[0]<=pausemenu.cord_X1+pausemenu.width  and pausemenu.cord_Y2<=mouse[1]<=pausemenu.cord_Y2+pausemenu.height:
									GameOn=False
						else:
							#Winner Text
							blinkstarttime=blinkingwinnertext(player_Won, pg.time.get_ticks(), blinkstarttime)
							menuWin=delay(pg.time.get_ticks(), winstarttime)
					else:
						if menuWin:
							screen.blit(button, (pausemenu.cord_X1, pausemenu.cord_Y1))
							screen.blit(button, (pausemenu.cord_X1, pausemenu.cord_Y2))
							winmenuselected=pausemenuselect(winmenuselected)
							screen.blit(textbut1win, rectwinmenubut1)
							screen.blit(textbut2win, rectwinmenubut2)

							#Select Pause Menu Button
							if keys[pg.K_d] or keys[pg.K_RIGHT]:
								if winmenuselected==0:
									GameOn=False
								elif winmenuselected==1:
									paumen=False
									Mainmenu=True
									do_once=True
									headlight_active=True
									justexited=True
									cooldownstarttime=pg.time.get_ticks()
									do_once_music=True

							#Check Mouse Click
							if mouseclick[0]:
								if pausemenu.cord_X1<=mouse[0]<=pausemenu.cord_X1+pausemenu.width  and pausemenu.cord_Y1<=mouse[1]<=pausemenu.cord_Y1+pausemenu.height:
									Mainmenu=True
									do_once=True
									headlight_active=True
									justexited=True
									cooldownstarttime=pg.time.get_ticks()
									do_once_music=True
								if pausemenu.cord_X1<=mouse[0]<=pausemenu.cord_X1+pausemenu.width  and pausemenu.cord_Y2<=mouse[1]<=pausemenu.cord_Y2+pausemenu.height:
									GameOn=False
						else:
							menuWin=delay(pg.time.get_ticks(), winstarttime)
							#Time taken Text
							blinkstarttime=blinkingtimertext(time_taken, pg.time.get_ticks(), blinkstarttime)
							best_time=besttimetaken(time_taken, best_time)

	pg.display.update()
	clock.tick(60)
pg.quit()