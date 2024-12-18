import pygame
import random
import sys
import os
import math
from pygame._sdl2 import Window

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
pygame.init()

programIcon = pygame.image.load(resource_path('assets/iconic.png'))

pygame.display.set_icon(programIcon)

clock = pygame.time.Clock()

height = 250
width = 550

screen = pygame.display.set_mode((width, height),flags = pygame.NOFRAME)
run = True
window = Window.from_display_module()
windex, windey = window.position

bg_img = pygame.image.load(resource_path('assets/betBG.png')).convert()
bt_img = pygame.image.load(resource_path('assets/Butonen.png')).convert()
ex_img = pygame.image.load(resource_path('assets/eee.png')).convert()
def background(image):
    sized = pygame.transform.smoothscale(image,(550, 250))
    screen.blit(sized, (0,0))

fontSize = 25
font = pygame.font.Font(resource_path('assets/fontle.ttf'), fontSize)

titleFontSize = 32
titleFont = pygame.font.Font(resource_path('assets/fontle.ttf'), titleFontSize)
descFontSize = 25
descFont = pygame.font.Font(resource_path('assets/fontle.ttf'), descFontSize)

setup = {
    1: [150, 190, 0.1, "Yes", 300, 190, 0.1, "No"],
    2: [225, 190, 0.1, "Begin", 600, 60, 0.1, "No"]
}
diff0 = {
    1: [300, 190, 0.1, "Cancel", 150, 190, 0.1, "Agree"],
    2: [150, 190, 0.1, "Cancel", 300, 190, 0.1, "Agree"]
}
diff1 = {
    1: [300, 190, 0.1, "Cancel", 150, 190, 0.1, "Agree"],
    2: [150, 190, 0.1, "Cancel", 300, 190, 0.1, "Agree"],
    3: [150, 190, 0.1, "Cancel", 300, 190, 0.1, "Cancle"],
    4: [300, 190, 0.1, "Cancel", 150, 190, 0.1, "Cancle"],
    5: [150, 190, 0.1, "Cancel", 300, 190, 0.1, "Cancal"],
    6: [300, 190, 0.1, "Cancel", 150, 190, 0.1, "Cancal"],
    7: [150, 190, 0.1, "Cancel", 300, 190, 0.1, "Dancel"],
    8: [300, 190, 0.1, "Cancel", 150, 190, 0.1, "Dancel"]
}

#TODO: Improve, make proceduraly generated from a dictionary
diff2 = {
    1: [300, 190, 0.1, "Cancel", 150, 190, 0.1, "Cancal"],
    2: [150, 190, 0.1, "Cancel", 300, 190, 0.1, "Cancle"],
    3: [300, 190, 0.1, "Cancel", 150, 190, 0.1, "Cancle"],
    4: [10, 150, 0.1, "Cancel", 150, 190, 0.1, "Agree"],
    5: [400, 50, 0.1, "Cancel", 10, 150, 0.1, "Cancal"],
    6: [300, 190, 0.085, "Cancel", 150, 190, 0.125, "Agree"],
    7: [150, 190, 0.1, "Cancel", 300, 190, 0.1, "Agree"],
    8: [300, 190, 0.085, "Cancel", 150, 190, 0.125, "Agree"],
    9: [10, 150, 0.085, "Cancel", 150, 190, 0.1, "Cancal"],
    10: [400, 50, 0.085, "Cancel", 150, 190, 0.1, "Agree"],
    11: [10, 150, 0.1, "Cancel", 150, 190, 0.1, "CLICK"],
    12: [400, 50, 0.1, "Cancel", 400, 190, 0.1, "CLICK"],
    13: [300, 190, 0.085, "Cancel", 150, 190, 0.125, "CLICK"],
    14: [150, 190, 0.1, "Cancel", 300, 190, 0.1, "CLICK"],
    15: [300, 190, 0.085, "Cancel", 150, 190, 0.125, "CLICK"],
    16: [10, 150, 0.085, "Cancel", 150, 190, 0.1, "CLICK"],
    17: [400, 50, 0.085, "Cancel", 150, 190, 0.1, "CLICK"],
    18: [10, 150, 0.1, "Cancel", 150, 190, 0.1, "Cancle"],
    19: [400, 50, 0.1, "Cancel", 150, 190, 0.1, "Cancle"],
    20: [300, 190, 0.085, "Cancel", 150, 190, 0.125, "Cancle"],
    21: [150, 190, 0.1, "Cancel", 300, 190, 0.1, "Cancle"],
    22: [300, 190, 0.085, "Cancel", 150, 190, 0.125, "Cancle"],
    23: [10, 150, 0.085, "Cancel", 150, 190, 0.1, "Cancle"],
    24: [150, 190, 0.085, "Cancel", 400, 50, 0.1, "Cancle"],
    25: [10, 150, 0.1, "Cancel", 150, 190, 0.1, "Yes"],
    26: [400, 50, 0.1, "Cancel", 150, 190, 0.1, "Yes"],
    27: [300, 190, 0.085, "Cancel", 150, 190, 0.125, "Yes"],
    28: [150, 150, 0.1, "Cancel", 300, 190, 0.1, "Yes"],
    29: [300, 190, 0.085, "Cancel", 150, 190, 0.125, "Yes"],
    30: [400, 200, 0.085, "Cancel", 150, 190, 0.1, "Yes"],
    31: [400, 50, 0.085, "Cancel", 150, 190, 0.1, "Yes"],
}

nomines = {
    1: "Accept",
    2: "Cance1",
    3: "Cancle",
    4: "Cancal",
    5: "Dancel",
    6: "Click",
    7: "SUBMIT",
    8: "REEEE",
    9: "Yes",
    10: "No ;)",
    11: "Cancel*"
}

puntos = {
1: [300, 190, 30, 150, 190, 30],
2: [150, 190, 30, 300, 190, 30],
3: [400, 50, 10, 10, 200, 10],
4: [10, 50, 10, 400, 200, 10],
5: [450, 190, 15, 50, 190, 15],
6: [50, 190, 15, 450, 190, 15],
7: [220, 130, 100, 240, 130, 100],
8: [220, 130, 100, 240, 130, 100],
9: [220, 130, 100, 240, 130, 100],
10: [220, 130, 100, 240, 130, 100],
11: [220, 130, 100, 240, 130, 100],
12: [220, 130, 100, 240, 130, 100]
}
fluctos = {
    1: [100,100,0.5],
    2: [20,20,2],
    3: [20,20,1]
}
oposex = 0
oposey = 0
engaged = False
anPosex = 0
anPosey = 0
NowPosex = 0
NowPosey = 0

points = 0
pagina = 0
gameRunning = True
temporg = 1000
timestart = False
timetrip = False
timeLeft = 0
increment = 30
lost = False
stop = False
realponts = 0
totalWdith = 500
ticker = 0

class Button():
    def __init__(self, x, y, image, scale, text):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.smoothscale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.text = font.render(text, True, "#262626", None)
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        elif pygame.mouse.get_pressed()[0]:
            self.clicked = True

        screen.blit(self.image, self.rect)
        screen.blit(self.text, (self.rect.x + 7, self.rect.y+4))
        return action
    

#exit_button = Button(496,4, ex_img, 0.0515, "")
exit_button = Button(502,9, ex_img, 0.04, "")

title = titleFont.render("Welcome!", True, "#bebebe", None)
titleRect = title.get_rect()
titleRect.topleft = (17, 10)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            oposex, oposey = pygame.mouse.get_pos()
            if oposey < 55:
                engaged = True
                NowPosex = oposex
                NowPosey = oposey
        if event.type == pygame.MOUSEBUTTONUP:
            engaged = False

        if engaged:
            oposex, oposey = pygame.mouse.get_pos()
            distex = NowPosex - oposex
            distey = NowPosey - oposey
            windex -= distex
            windey -= distey
            window.position = (windex, windey)

    screen.fill('#bebebe')
    background(bg_img)
    #Title
    #Description

   
    if not gameRunning:
        #print("points: " + str(points))
        gen = True
        if pygame.mouse.get_pressed()[0] == 0:
            gameRunning = True
    if gameRunning:
        if pagina == -2:
            timestart = False
            if points == -1:
                run = False
            else:
                pagina = 2
                timetrip = False
        if pagina == 0:
            points = pagina
            if points == -1:
                run = False
            else:
                desc = descFont.render("Welcome! Do you want to play a game?", True, "#262626", None)
                good_button = Button(setup[1][0], setup[1][1], bt_img, setup[1][2], setup[1][3])
                bad_button = Button(setup[1][4], setup[1][5], bt_img, setup[1][6], setup[1][7])
        elif pagina == 1:
            if points == -1:
                run = False
            else:
                desc = descFont.render("The game is simple. You must click \'Cancel\' to \n deny the Terms and conditions", True, "#262626", None)
                good_button = Button(setup[2][0], setup[2][1], bt_img, setup[2][2], setup[2][3])
                bad_button = Button(setup[2][4], setup[2][5], bt_img, setup[2][6], setup[2][7])
        elif pagina == 2:
            realponts = 0
            lost = False
            points = 0
            stop = False
            timestart = True
            desc = descFont.render("Do you accept the Terms and Conditions?", True, "#262626", None)
            good_button = Button(diff0[1][0], diff0[1][1], bt_img, diff0[1][2], diff0[1][3])
            bad_button = Button(diff0[1][4], diff0[1][5], bt_img, diff0[1][6], diff0[1][7])
        elif pagina == 3:
            if points +2 == pagina:
                if gen:
                    timeLeft += increment
                    realponts +=1
                    shuwaz = random.randint(1, len(diff0))
                    gen = False
                good_button = Button(diff0[shuwaz][0], diff0[shuwaz][1], bt_img, diff0[shuwaz][2], diff0[shuwaz][3])
                bad_button = Button(diff0[shuwaz][4], diff0[shuwaz][5], bt_img, diff0[shuwaz][6], diff0[shuwaz][7])
            else:
                desc = descFont.render("Oh No! You accepted the Terms and Conditions! \n Your final score is: "+ str(realponts) +"\n Play again?", True, "#262626", None)
                good_button = Button(setup[2][0], setup[2][1], bt_img, setup[2][2], setup[2][3])
                bad_button = Button(setup[2][4], setup[2][5], bt_img, setup[2][6], setup[2][7])
                pagina = -3
                points = 1
                timeLeft = 0
                stop = True
                #lost = True
        elif pagina > 3 and pagina < 6:
            if points +2 == pagina:
                if gen:
                    timeLeft += increment
                    realponts += 1
                    shuwaz = random.randint(1, len(diff1))
                    gen = False
                good_button = Button(diff1[shuwaz][0], diff1[shuwaz][1], bt_img, diff1[shuwaz][2], diff1[shuwaz][3])
                bad_button = Button(diff1[shuwaz][4], diff1[shuwaz][5], bt_img, diff1[shuwaz][6], diff1[shuwaz][7])
            else:
                desc = descFont.render("Oh No! You accepted the Terms and Conditions! \n Your final score is: "+ str(realponts) +"\n Play again?", True, "#262626", None)
                good_button = Button(setup[2][0], setup[2][1], bt_img, setup[2][2], setup[2][3])
                bad_button = Button(setup[2][4], setup[2][5], bt_img, setup[2][6], setup[2][7])
                pagina = -3
                points = 1
                timeLeft = 0
                stop = True
                #lost = True
        
    # elif pagina >= 6:
    #     if points +2 == pagina:
                
        #         if gen:
        #             timeLeft += 20
        #             realponts += 1
        #             shuwaz = random.randint(1, len(diff2))
        #             gen = False
        #         good_button = Button(diff2[shuwaz][0], diff2[shuwaz][1], bt_img, diff2[shuwaz][2], diff2[shuwaz][3])
        #         bad_button = Button(diff2[shuwaz][4], diff2[shuwaz][5], bt_img, diff2[shuwaz][6], diff2[shuwaz][7])
    #     else:
                desc = descFont.render("Oh No! You accepted the Terms and Conditions! \n Your final score is: "+ str(realponts) +"\n Play again?", True, "#262626", None)
                good_button = Button(setup[2][0], setup[2][1], bt_img, setup[2][2], setup[2][3])
                bad_button = Button(setup[2][4], setup[2][5], bt_img, setup[2][6], setup[2][7])
                pagina = -3
                points = 1
                timeLeft = 0
                stop = True
                #lost = True
        elif pagina >= 6 and pagina < 15:
            if points +2 == pagina:
                if gen:
                    timeLeft += 10
                    realponts += 1
                    punchose = random.randint(1, len(puntos))
                    nomchose = random.randint(1, len(nomines))
                    varGx = random.randint(-puntos[punchose][2], puntos[punchose][2])
                    varGy = random.randint(-puntos[punchose][2], puntos[punchose][2])
                    varBx = random.randint(-puntos[punchose][5], puntos[punchose][5])
                    varBy = random.randint(-puntos[punchose][5], puntos[punchose][5])
                    gen = False
                good_button = Button(puntos[punchose][0]+varGx, puntos[punchose][1]+varGy, bt_img, 0.1, "Cancel")
                bad_button = Button(puntos[punchose][3]+varBx, puntos[punchose][4]+varBy, bt_img, 0.1, nomines[nomchose])
            else:
                desc = descFont.render("Oh No! You accepted the Terms and Conditions! \n Your final score is: "+ str(realponts) +"\n Play again?", True, "#262626", None)
                good_button = Button(setup[2][0], setup[2][1], bt_img, setup[2][2], setup[2][3])
                bad_button = Button(setup[2][4], setup[2][5], bt_img, setup[2][6], setup[2][7])
                pagina = -3
                points = 1
                timeLeft = 0
                stop = True
        elif pagina >= 15:
            if points +2 == pagina:
                if gen:
                    tick = 1
                    timeLeft += 10
                    realponts += 1
                    punchose = random.randint(1, len(puntos))
                    nomchose = random.randint(1, len(nomines))
                    flucGchose = random.randint(1, len(fluctos))
                    flucBchose = random.randint(1, len(fluctos))
                    varGx = random.randint(-puntos[punchose][2], puntos[punchose][2])
                    varGy = random.randint(-puntos[punchose][2], puntos[punchose][2])
                    varBx = random.randint(-puntos[punchose][5], puntos[punchose][5])
                    varBy = random.randint(-puntos[punchose][5], puntos[punchose][5])
                    ampGx = random.randint(-fluctos[flucGchose][0], fluctos[flucGchose][0])
                    ampGy = random.randint(-fluctos[flucGchose][1], fluctos[flucGchose][1])
                    ampBx = random.randint(-fluctos[flucBchose][0], fluctos[flucBchose][0])
                    ampBy = random.randint(-fluctos[flucGchose][1], fluctos[flucGchose][1])
                    perG = random.uniform(-fluctos[flucGchose][2], fluctos[flucGchose][2])
                    perB = random.uniform(-fluctos[flucGchose][2], fluctos[flucGchose][2])
                    gen = False
                
                vibeGx = ampGx * math.sin(tick * perG)
                vibeGy = ampGy * math.sin(tick * perG)
                vibeBx = ampBx * math.sin(tick * perB)
                vibeBy = ampBy * math.sin(tick * perB)

                good_button = Button(puntos[punchose][0]+varGx+vibeGx, puntos[punchose][1]+varGy+vibeGy, bt_img, 0.1, "Cancel")
                bad_button = Button(puntos[punchose][3]+varBx+vibeBx, puntos[punchose][4]+varBy+vibeBy, bt_img, 0.1, nomines[nomchose])
                tick += 0.5
            else:
                desc = descFont.render("Oh No! You accepted the Terms and Conditions! \n Your final score is: "+ str(realponts) +"\n Play again?", True, "#262626", None)
                good_button = Button(setup[2][0], setup[2][1], bt_img, setup[2][2], setup[2][3])
                bad_button = Button(setup[2][4], setup[2][5], bt_img, setup[2][6], setup[2][7])
                pagina = -3
                points = 1
                timeLeft = 0
                stop = True
    if timestart and not timetrip:
        timetrip = True
        timeLeft = temporg
    if timeLeft >= 0 and timestart:
        #print(timeLeft)
        timeLeft -= 1
        if not stop:
            title = titleFont.render("Score: " + str(realponts), True, "#bebebe", None)
            widit = totalWdith - (totalWdith * (timeLeft/temporg))
            pygame.draw.rect(screen, "#262626", pygame.Rect(20, 115, totalWdith + 10, 45), border_radius=5)
            pygame.draw.rect(screen, "#0001a4", pygame.Rect(25, 120, widit, 35), border_radius=5)
    if timeLeft < 0 and timestart:
        lost = True
    if lost:
        timestart = False
        title = titleFont.render("Game Over!", True, "#bebebe", None)
        if timeLeft < 0 and not stop:
            desc = descFont.render("Oh No! You ran out of time! \n Your final score is: "+ str(realponts) +"\n Play again?", True, "#262626", None)
        good_button = Button(setup[2][0], setup[2][1], bt_img, setup[2][2], setup[2][3])
        bad_button = Button(setup[2][4], setup[2][5], bt_img, setup[2][6], setup[2][7])
        pagina = -3
        points = 0
    
    descRect = desc.get_rect()
    descRect.topleft = (15, 75)
    screen.blit(desc, descRect)
    
    screen.blit(title, titleRect)

    
    if good_button.draw():
        gameRunning = False
        points += 1
        pagina +=1
    if bad_button.draw():
        gameRunning = False
        points -= 1
        pagina += 1
    if exit_button.draw():
        run = False
    pygame.display.update()
    clock.tick(60)
    #print(clock.get_fps())
pygame.quit()