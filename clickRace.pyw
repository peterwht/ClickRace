import pygame
import time
import random

pygame.init()

beep_sound = pygame.mixer.Sound("sounds/beep2.wav")
beep_sound2 = pygame.mixer.Sound("sounds/beep4.wav")

display_width = 800
display_height = 600

white = (255,255,255)
black = (0,0,0)

blue = (0, 0, 175)
light_blue = (0,0,220)

red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0, 255, 0)

tan = (254, 241, 169)

grey = (100, 100, 100)
light_grey = (150, 150, 150)

orange = (247, 163, 36)
darkorange = (247, 163, 36)


carspeed = 10

finishLinex = display_width-46
finishLine = display_height/2-80
rectWidth = display_width+20


clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("Rockwell", 25)
medfont = pygame.font.SysFont("Rockwell", 50)
largefont = pygame.font.SysFont("Rockwell", 80)

car = pygame.image.load("images/BlueCar1.png")
car2 = pygame.image.load("images/RedCar.png")
greyCar = pygame.image.load("images/greycar.png") 
greyCarButton = pygame.image.load("images/greyCarButton.png")
redCarButton = pygame.image.load("images/redCarButton.png")
blueCarButton = pygame.image.load("images/blueCarButton.png")

checkered = pygame.image.load("images/checkered.png")

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.toggle_fullscreen()
pygame.display.set_caption("Click Race")

pygame.display.update()

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx +((buttonwidth/2)), buttony+(buttonheight/2)))
    gameDisplay.blit(textSurf, textRect)

def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    
    textRect.center = (display_width/ 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def score(score):

    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def game_intro():
    pygame.time.wait(1)
    intro = False

    while not intro:

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Click Race", blue, -100, "large")
        message_to_screen("Make your car pass the finish line quicker then your opponent", black, -30)

        button("Play", 150, 500, 100, 50, green, light_green, action="Play")
        button("Controls", 350,500,100,50, yellow, light_yellow, action="Controls")
        button("Quit", 550,500,100,50, red, light_red, action="Quit")

        pygame.display.update()
        clock.tick(15)


def multiplayerCarWin(whichPlayer, textColor):

    end_time = pygame.time.get_ticks()

    time_taken = end_time-start_time
    
    win = True

    while win:

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("{} wins!".format(whichPlayer), textColor, -100, "large")
        
        if len(str(time_taken)) == 4: 
            message_to_screen("It took {}:  {}.{} seconds".format(whichPlayer, str(time_taken)[0], str(time_taken)[1:3]), textColor, -30, "medium")
        elif len(str(time_taken)) > 4:
            message_to_screen("It took {}:  {}.{} seconds" .format(whichPlayer, str(time_taken)[0:2], str(time_taken)[1:3]), textColor, -30, "medium")        
       

        button("Play Again", 325, 425, 150, 50, green, light_green, action="Playagain")
        
        button("Quit", 325,500,150,50, red, light_red, action="Quit")

        pygame.display.update()
        clock.tick(15)
        
def car1winC():

    end_time = pygame.time.get_ticks()

    time_taken = end_time-start_time
    
    win = True

    while win:

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Congratulations!", blue, -120, "large")
        message_to_screen("You beat all the levels!", blue, -50, "medium")
        
        if len(str(time_taken)) == 4: 
            message_to_screen("It took you:  " + str(time_taken)[0] + "." + str(time_taken)[1:3]  + " seconds", black, -10, "small")
            message_to_screen(" seconds to beat Level 10.", black, 15, "small")
            
        elif len(str(time_taken)) > 4:
            message_to_screen("It took you:  " + str(time_taken)[0:2] + "." + str(time_taken)[1:3]  + " seconds", black, -10, "small")
            message_to_screen(" seconds to beat Level 10", black, 15, "small")

        message_to_screen("It took you a total of: " + str(totalTime_taken)[0:2] + "." + str(time_taken)[1:3]  + " seconds", black, 40, "small")
        message_to_screen(" seconds to beat all of the levels", black, 70, "small")
            

        button("Play Again", 325, 425, 150, 50, green, light_green, action="Playagain")
        
        button("Quit", 325,500,150,50, red, light_red, action="Quit")

        pygame.display.update()
        clock.tick(15)
        

def computerwin():

    win = True

    while win:

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("The Computer wins",
                          red,
                          -100,
                          "large")
        message_to_screen("You just lost to something that is lifeless.",
                          blue,
                          -30)
        message_to_screen("How does that make you feel?",
                          blue,
                          20)

        button("Play Again", 325, 425, 150, 50, green, light_green, action="Playagain")
        
        button("Quit", 325,500,150,50, red, light_red, action="Quit")

        pygame.display.update()
        clock.tick(15)


def game_controls():
    pygame.time.wait(2)
    gcont = True

    while gcont:

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("How to play", blue, -100,"large")

        message_to_screen("Player 1 is Blue", blue, -30)

        message_to_screen("player 2 is Red", red, 10)

        message_to_screen("To move player 1 forward: A and S",
                          black,50)
        message_to_screen("To move player 2 forward: L and K",black,90)
     

        button("Play", 150, 500, 100, 50, green, light_green, action="Play")
        button("Main", 350,500,100,50, yellow, light_yellow, action="Main")
        button("Quit", 550,500,100,50, red, light_red, action="Quit")

        pygame.display.update()
        clock.tick(15)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if clicked[0] == 1 and action != None:
            if action == "Quit":
                pygame.quit()
                quit()

            if action == "Controls":
                game_controls()
                
                
            if action == "Main":
                game_intro()
                
                
            if action == "Play":
                gameChoice()
                
            if action == "Playagain":
                game_intro()
                
            if action == "Player":
                whichCar()

            if action == "Computer":
                whichCarComputer()
                
            if action == "blueCar":
                countdown(car, car2)

            if action == "redCar":
                countdown(car2, greyCar)

            if action == "greyCar":
                countdown(greyCar, car)

            if action == "blueCar2":
                levelDisplay(car, car2)

            if action == "redCar2":
                levelDisplay(car2, greyCar)

            if action == "greyCar2":
                levelDisplay(greyCar, car)
                
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))
    text_to_button(text, black, x, y, width, height)

def levelDisplay(whichCarChoice, whichCarChoice2, whatlevel=1):
    levelDisplayExit = False
    howlong = 50

    

    if whatlevel > 1:
            end_time = pygame.time.get_ticks()
            
            
            

    while not levelDisplayExit:

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(gameDisplay, white, [200, 200], howlong)
        howlong += 1

        if whatlevel == 11:
            car1winC()
            
        if howlong >= 80:
            if whatlevel == 1:
                countdown2(whichCarChoice, whichCarChoice2)
            elif whatlevel == 2:
                countdown3(whichCarChoice, whichCarChoice2)
            elif whatlevel == 3:
                countdown4(whichCarChoice, whichCarChoice2)
            elif whatlevel == 4:
                countdown5(whichCarChoice, whichCarChoice2)
            elif whatlevel == 5:
                countdown6(whichCarChoice, whichCarChoice2)
            elif whatlevel == 6:
                countdown7(whichCarChoice, whichCarChoice2)
            elif whatlevel == 7:
                countdown8(whichCarChoice, whichCarChoice2)
            elif whatlevel == 8:
                countdown9(whichCarChoice, whichCarChoice2)
            elif whatlevel == 9:
                countdown10(whichCarChoice, whichCarChoice2)
            elif whatlevel == 10:
                countdown11(whichCarChoice, whichCarChoice2)
        
        gameDisplay.fill(white)
        message_to_screen("Level " + str(whatlevel), black, 0, "large")
        if whatlevel == 1:
            message_to_screen("Super Easy ", green, 80, "medium")
        elif whatlevel == 2:
            message_to_screen("Super Easy ", green, 80, "medium")
        elif whatlevel == 3:
            message_to_screen("Easy", green, 80, "medium")
        elif whatlevel == 4:
            message_to_screen("Easy", green, 80, "medium")
        elif whatlevel == 5:
            message_to_screen("Normal", light_yellow, 80, "medium")
        elif whatlevel == 6:
            message_to_screen("Normal", light_yellow, 80, "medium")
        elif whatlevel == 7:
            message_to_screen("Hard", orange, 80, "medium")
        elif whatlevel == 8:
            message_to_screen("Hard", orange, 80, "medium")
        elif whatlevel == 9:
            message_to_screen("Super Hard", darkorange, 80, "medium")
        elif whatlevel == 10:
            message_to_screen("Impossible", red, 80, "medium")
        

        if whatlevel > 1:
            time_taken = end_time-start_time
            if len(str(time_taken)) == 4:
                    global totalTime_taken
                    totalTime_taken = end_time-start_time
                    message_to_screen("It took you: " + str(time_taken)[0] + "." + str(time_taken)[1:3], black, -270, "small")
                    message_to_screen(" seconds to beat Level " + str(whatlevel-1), black, -240, "small")
            elif len(str(time_taken)) > 4:
                totalTime_taken = end_time-start_time
                message_to_screen("It took you:  " + str(time_taken)[0:2], black, -270, "small")
                message_to_screen(" seconds to beat Level " + str(whatlevel-1), black, -240, "small")


        pygame.display.update()
        clock.tick(10)
    
        
        
    pygame.quit()
    quit()



def countdown(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 1.5
    carx = 0
    car2x = 0

    circletimerred = 50
    circletimeryellow = 50
    circletimergreen = 50
    
    pygame.mixer.Sound.play(beep_sound)
    
    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
        circletimerred += 1
        
        if circletimerred >= 52:
            pygame.mixer.Sound.play(beep_sound)
            
            pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
            circletimerred = 51
            
            
            pygame.draw.circle(gameDisplay, light_yellow, [350, 100], circletimeryellow)
            circletimeryellow += 1
            
            if circletimeryellow >= 52:
                
                circletimeryellow = 52
                
                pygame.draw.circle(gameDisplay, green, [500, 100], circletimergreen)
                circletimergreen += 1
                
                if circletimergreen >= 52:
                    pygame.mixer.Sound.play(beep_sound2)
                    if whichCarChoice == car:
                        gameLoop(car, car2)
                        
                    if whichCarChoice == car2:
                        gameLoop(car2, greyCar)
                        
                    if whichCarChoice == greyCar:
                        gameLoop(greyCar, car)
                
                
        
        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))
        
        
        
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def countdown2(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 1.5
    carx = 0
    car2x = 0

    circletimerred = 50
    circletimeryellow = 50
    circletimergreen = 50
    
    pygame.mixer.Sound.play(beep_sound)
    
    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
        circletimerred += 1
        
        if circletimerred >= 52:
            pygame.mixer.Sound.play(beep_sound)
            
            pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
            circletimerred = 51
            
            
            pygame.draw.circle(gameDisplay, light_yellow, [350, 100], circletimeryellow)
            circletimeryellow += 1
            
            if circletimeryellow >= 52:
                
                circletimeryellow = 52
                
                pygame.draw.circle(gameDisplay, green, [500, 100], circletimergreen)
                circletimergreen += 1
                
                if circletimergreen >= 52:
                    pygame.mixer.Sound.play(beep_sound2)
                    level1(whichCarChoice, whichCarChoice2)
                
                
        
        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def countdown3(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 1.5
    carx = 0
    car2x = 0

    circletimerred = 50
    circletimeryellow = 50
    circletimergreen = 50
    
    pygame.mixer.Sound.play(beep_sound)
    
    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
        circletimerred += 1
        
        if circletimerred >= 52:
            pygame.mixer.Sound.play(beep_sound)
            
            pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
            circletimerred = 51
            
            
            pygame.draw.circle(gameDisplay, light_yellow, [350, 100], circletimeryellow)
            circletimeryellow += 1
            
            if circletimeryellow >= 52:
                
                circletimeryellow = 52
                
                pygame.draw.circle(gameDisplay, green, [500, 100], circletimergreen)
                circletimergreen += 1
                
                if circletimergreen >= 52:
                    pygame.mixer.Sound.play(beep_sound2)
                    level2(whichCarChoice, whichCarChoice2)
                
                
        
        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()
def countdown4(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 1.5
    carx = 0
    car2x = 0

    circletimerred = 50
    circletimeryellow = 50
    circletimergreen = 50
    
    pygame.mixer.Sound.play(beep_sound)
    
    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
        circletimerred += 1
        
        if circletimerred >= 52:
            pygame.mixer.Sound.play(beep_sound)
            
            pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
            circletimerred = 51
            
            
            pygame.draw.circle(gameDisplay, light_yellow, [350, 100], circletimeryellow)
            circletimeryellow += 1
            
            if circletimeryellow >= 52:
                
                circletimeryellow = 52
                
                pygame.draw.circle(gameDisplay, green, [500, 100], circletimergreen)
                circletimergreen += 1
                
                if circletimergreen >= 52:
                    pygame.mixer.Sound.play(beep_sound2)
                    level3(whichCarChoice, whichCarChoice2)
                
                
        
        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()


def countdown5(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 1.5
    carx = 0
    car2x = 0

    circletimerred = 50
    circletimeryellow = 50
    circletimergreen = 50
    
    pygame.mixer.Sound.play(beep_sound)
    
    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
        circletimerred += 1
        
        if circletimerred >= 52:
            pygame.mixer.Sound.play(beep_sound)
            
            pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
            circletimerred = 51
            
            
            pygame.draw.circle(gameDisplay, light_yellow, [350, 100], circletimeryellow)
            circletimeryellow += 1
            
            if circletimeryellow >= 52:
                
                circletimeryellow = 52
                
                pygame.draw.circle(gameDisplay, green, [500, 100], circletimergreen)
                circletimergreen += 1
                
                if circletimergreen >= 52:
                    pygame.mixer.Sound.play(beep_sound2)
                    level4(whichCarChoice, whichCarChoice2)
                
                
        
        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def countdown6(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 1.5
    carx = 0
    car2x = 0

    circletimerred = 50
    circletimeryellow = 50
    circletimergreen = 50
    
    pygame.mixer.Sound.play(beep_sound)
    
    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
        circletimerred += 1
        
        if circletimerred >= 52:
            pygame.mixer.Sound.play(beep_sound)
            
            pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
            circletimerred = 51
            
            
            pygame.draw.circle(gameDisplay, light_yellow, [350, 100], circletimeryellow)
            circletimeryellow += 1
            
            if circletimeryellow >= 52:
                
                circletimeryellow = 52
                
                pygame.draw.circle(gameDisplay, green, [500, 100], circletimergreen)
                circletimergreen += 1
                
                if circletimergreen >= 52:
                    pygame.mixer.Sound.play(beep_sound2)
                    level5(whichCarChoice, whichCarChoice2)
                
                
        
        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def countdown7(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 1.5
    carx = 0
    car2x = 0

    circletimerred = 50
    circletimeryellow = 50
    circletimergreen = 50
    
    pygame.mixer.Sound.play(beep_sound)
    
    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
        circletimerred += 1
        
        if circletimerred >= 52:
            pygame.mixer.Sound.play(beep_sound)
            
            pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
            circletimerred = 51
            
            
            pygame.draw.circle(gameDisplay, light_yellow, [350, 100], circletimeryellow)
            circletimeryellow += 1
            
            if circletimeryellow >= 52:
                
                circletimeryellow = 52
                
                pygame.draw.circle(gameDisplay, green, [500, 100], circletimergreen)
                circletimergreen += 1
                
                if circletimergreen >= 52:
                    pygame.mixer.Sound.play(beep_sound2)
                    level6(whichCarChoice, whichCarChoice2)
                
                
        
        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def countdown8(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 1.5
    carx = 0
    car2x = 0

    circletimerred = 50
    circletimeryellow = 50
    circletimergreen = 50
    
    pygame.mixer.Sound.play(beep_sound)
    
    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
        circletimerred += 1
        
        if circletimerred >= 52:
            pygame.mixer.Sound.play(beep_sound)
            
            pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
            circletimerred = 51
            
            
            pygame.draw.circle(gameDisplay, light_yellow, [350, 100], circletimeryellow)
            circletimeryellow += 1
            
            if circletimeryellow >= 52:
                
                circletimeryellow = 52
                
                pygame.draw.circle(gameDisplay, green, [500, 100], circletimergreen)
                circletimergreen += 1
                
                if circletimergreen >= 52:
                    pygame.mixer.Sound.play(beep_sound2)
                    level7(whichCarChoice, whichCarChoice2)
                
                
        
        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()
    

def countdown9(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 1.5
    carx = 0
    car2x = 0

    circletimerred = 50
    circletimeryellow = 50
    circletimergreen = 50
    
    pygame.mixer.Sound.play(beep_sound)
    
    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
        circletimerred += 1
        
        if circletimerred >= 52:
            pygame.mixer.Sound.play(beep_sound)
            
            pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
            circletimerred = 51
            
            
            pygame.draw.circle(gameDisplay, light_yellow, [350, 100], circletimeryellow)
            circletimeryellow += 1
            
            if circletimeryellow >= 52:
                
                circletimeryellow = 52
                
                pygame.draw.circle(gameDisplay, green, [500, 100], circletimergreen)
                circletimergreen += 1
                
                if circletimergreen >= 52:
                    pygame.mixer.Sound.play(beep_sound2)
                    level8(whichCarChoice, whichCarChoice2)
                
                
        
        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def countdown10(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 1.5
    carx = 0
    car2x = 0

    circletimerred = 50
    circletimeryellow = 50
    circletimergreen = 50
    
    pygame.mixer.Sound.play(beep_sound)
    
    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
        circletimerred += 1
        
        if circletimerred >= 52:
            pygame.mixer.Sound.play(beep_sound)
            
            pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
            circletimerred = 51
            
            
            pygame.draw.circle(gameDisplay, light_yellow, [350, 100], circletimeryellow)
            circletimeryellow += 1
            
            if circletimeryellow >= 52:
                
                circletimeryellow = 52
                
                pygame.draw.circle(gameDisplay, green, [500, 100], circletimergreen)
                circletimergreen += 1
                
                if circletimergreen >= 52:
                    pygame.mixer.Sound.play(beep_sound2)
                    level9(whichCarChoice, whichCarChoice2)
                
                
        
        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def countdown11(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 1.5
    carx = 0
    car2x = 0

    circletimerred = 50
    circletimeryellow = 50
    circletimergreen = 50
    
    pygame.mixer.Sound.play(beep_sound)
    
    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
        circletimerred += 1
        
        if circletimerred >= 52:
            pygame.mixer.Sound.play(beep_sound)
            
            pygame.draw.circle(gameDisplay, red, [200, 100], circletimerred)
            circletimerred = 51
            
            
            pygame.draw.circle(gameDisplay, light_yellow, [350, 100], circletimeryellow)
            circletimeryellow += 1
            
            if circletimeryellow >= 52:
                
                circletimeryellow = 52
                
                pygame.draw.circle(gameDisplay, green, [500, 100], circletimergreen)
                circletimergreen += 1
                
                if circletimergreen >= 52:
                    pygame.mixer.Sound.play(beep_sound2)
                    level10(whichCarChoice, whichCarChoice2)
                
                
        
        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()
    
def gameChoice():
    gameChoiceExit = False

    while not gameChoiceExit:

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Do you want to play against a", black, -100, "medium")
        message_to_screen("computer that gets harder?", black, -50, "medium")
        message_to_screen("or, against another player?", black, 0, "medium")

        button("Player", 325, 425, 150, 50, green, light_green, action="Player")
        button("Computer", 325,500,150,50, yellow, light_yellow, action="Computer")

        pygame.display.update()
        clock.tick(15)
        
    pygame.quit()
    quit()
    
    
def level1(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 15
    carx = 0
    car2x = 0
    global start_time
    start_time = pygame.time.get_ticks()
   
    

    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     pass
                if event.key == pygame.K_a:
                    carx += carspeed
                elif event.key == pygame.K_s:
                    carx += carspeed
        car2x += 3
                

        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        if carx >= 660:
            levelDisplay(whichCarChoice, whichCarChoice2, whatlevel=2)
        if car2x >= 660:
            computerwin()
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def level2(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 15
    carx = 0
    car2x = 0
    global start_time
    start_time = pygame.time.get_ticks()
   
    

    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     pass
                if event.key == pygame.K_a:
                    carx += carspeed
                elif event.key == pygame.K_s:
                    carx += carspeed
        car2x += 3
                

        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        if carx >= 660:
            levelDisplay(whichCarChoice, whichCarChoice2, whatlevel=3)
        if car2x >= 660:
            computerwin()
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()
    
def level3(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 15
    carx = 0
    car2x = 0
    global start_time
    start_time = pygame.time.get_ticks()
   
    

    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     pass
                if event.key == pygame.K_a:
                    carx += carspeed
                elif event.key == pygame.K_s:
                    carx += carspeed
        car2x += 3
                

        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        if carx >= 660:
            levelDisplay(whichCarChoice, whichCarChoice2, whatlevel=4)
        if car2x >= 660:
            computerwin()
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def level4(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 15
    carx = 0
    car2x = 0
    global start_time
    start_time = pygame.time.get_ticks()
   
    

    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     pass
                if event.key == pygame.K_a or event.key == pygame.K_s:
                    carx += carspeed
        car2x += 4
                

        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        if carx >= 660:
            levelDisplay(whichCarChoice, whichCarChoice2, whatlevel=5)
        if car2x >= 660:
            computerwin()
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def level5(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 15
    carx = 0
    car2x = 0
    global start_time
    start_time = pygame.time.get_ticks()
   
    

    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     pass
                if event.key == pygame.K_a:
                    carx += carspeed
                elif event.key == pygame.K_s:
                    carx += carspeed
        car2x += 5
                

        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        if carx >= 660:
            levelDisplay(whichCarChoice, whichCarChoice2, whatlevel=6)
        if car2x >= 660:
            computerwin()
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def level6(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 15
    carx = 0
    car2x = 0
    global start_time
    start_time = pygame.time.get_ticks()
   
    

    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     pass
                if event.key == pygame.K_a:
                    carx += carspeed
                elif event.key == pygame.K_s:
                    carx += carspeed
        car2x += 6
                

        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        if carx >= 660:
            levelDisplay(whichCarChoice, whichCarChoice2, whatlevel=7)
        if car2x >= 660:
            computerwin()
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()
def level7(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 15
    carx = 0
    car2x = 0
    global start_time
    start_time = pygame.time.get_ticks()
   
    

    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     pass
                if event.key == pygame.K_a:
                    carx += carspeed
                elif event.key == pygame.K_s:
                    carx += carspeed
        car2x += 7
                

        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        if carx >= 660:
            levelDisplay(whichCarChoice, whichCarChoice2, whatlevel=8)
        if car2x >= 660:
            car2win()
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def level8(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 15
    carx = 0
    car2x = 0
    global start_time
    start_time = pygame.time.get_ticks()
   
    

    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     pass
                if event.key == pygame.K_a:
                    carx += carspeed
                elif event.key == pygame.K_s:
                    carx += carspeed
        car2x += 8
                

        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        if carx >= 660:
            levelDisplay(whichCarChoice, whichCarChoice2, whatlevel=9)
        if car2x >= 660:
            computerwin()
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def level9(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 15
    carx = 0
    car2x = 0
    global start_time
    start_time = pygame.time.get_ticks()
   
    

    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     pass
                if event.key == pygame.K_a:
                    carx += carspeed
                elif event.key == pygame.K_s:
                    carx += carspeed
        car2x += 9
                

        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        if carx >= 660:
            levelDisplay(whichCarChoice, whichCarChoice2, whatlevel=10)
        if car2x >= 660:
            computerwin()
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

def level10(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 15
    carx = 0
    car2x = 0
    global start_time
    start_time = pygame.time.get_ticks()
   
    

    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     pass
                if event.key == pygame.K_a:
                    carx += carspeed
                elif event.key == pygame.K_s:
                    carx += carspeed
        car2x += 10
                

        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        gameDisplay.blit(whichCarChoice, (carx, 240))
        gameDisplay.blit(whichCarChoice2, (car2x, 350))

        if carx >= 660:
            levelDisplay(whichCarChoice, whichCarChoice2, whatlevel=11)
        if car2x >= 660:
            computerwin()
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()


def whichCar():
    gameChoiceExit = False

    while not gameChoiceExit:

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)

        message_to_screen("PLAYER 1", blue, -275, "medium")
        message_to_screen("Choose your car color", black, -200, "medium")
        button(" ", 20, display_height/2-50, 200, 100, blue, light_blue, action="blueCar")
        button(" ", 300, display_height/2-50, 200, 100, red, light_red, action="redCar")
        button(" ", 800 - 200-20, display_height/2-50, 200, 100, grey, light_grey, action="greyCar")
        gameDisplay.blit(greyCarButton, (800-200-20, display_height/2-50))
        gameDisplay.blit(redCarButton, (300, display_height/2-50))
        gameDisplay.blit(blueCarButton, (20, display_height/2-50))
        clock.tick(30)
        pygame.display.update()
    pygame.quit()
    quit()

def whichCarComputer():
    gameChoiceExit = False

    while not gameChoiceExit:

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)

        message_to_screen("PLAYER 1", blue, -275, "medium")
        message_to_screen("Choose your car color", black, -200, "medium")
        button(" ", 20, display_height/2-50, 200, 100, blue, light_blue, action="blueCar2")
        button(" ", 300, display_height/2-50, 200, 100, red, light_red, action="redCar2")
        button(" ", 800 - 200-20, display_height/2-50, 200, 100, grey, light_grey, action="greyCar2")
        gameDisplay.blit(greyCarButton, (800-200-20, display_height/2-50))
        gameDisplay.blit(redCarButton, (300, display_height/2-50))
        gameDisplay.blit(blueCarButton, (20, display_height/2-50))
        
        clock.tick(30)
        pygame.display.update()
    pygame.quit()
    quit()
    

def gameLoop(whichCarChoice, whichCarChoice2):
    gameExit = False
    FPS = 15
    carx = 0
    car2x = 0

    global start_time
    start_time = pygame.time.get_ticks()

    """for i in range(0,30):
        clock.tick(30)"""
    
    

    while not gameExit:

        gameDisplay.fill(tan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    pass
                if event.key == pygame.K_a:
                    carx += carspeed
                elif event.key == pygame.K_s:
                    carx += carspeed
                elif event.key == pygame.K_l:
                    car2x += carspeed
                elif event.key == pygame.K_k:
                    car2x += carspeed               

        pygame.draw.rect(gameDisplay, grey, [0, 220, rectWidth, 200])
        message_to_screen("PLAYER 1", blue, -100, "medium")
        message_to_screen("PLAYER 2", red, 140, "medium")
        pygame.draw.rect(gameDisplay, light_yellow, [-10, 310, 820, 20], 5)
        gameDisplay.blit(checkered, [finishLinex, finishLine])
        
        
        gameDisplay.blit(whichCarChoice, (carx, display_height-360))
        gameDisplay.blit(whichCarChoice2, (car2x, display_height-250))

        if carx >= 660:
            multiplayerCarWin("Player 1", blue)
        if car2x >= 660:
            multiplayerCarWin("Player 2", red)
        
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()




