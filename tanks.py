import pygame
import time
import random

red = (200, 0, 0)
light_red = (255, 0, 0) 

black = (0, 0, 0)
white = (225, 225, 225)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (0, 115, 0)
light_green = (0, 225, 0)
    
# calling init()
pygame.init()

# sound
fire_sound = pygame.mixer.Sound("laser.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")

# creating a gamedisplay
gamedisplay = pygame.display.set_mode((800, 600))

display_width = 800
display_hight = 600

# icon and caption
pygame.display.set_caption('tanks')

# ground
groundhight = 35

block_size = 20
FPS = 10

##img = pygame.image.load("snake.png")
##appleimg = pygame.image.load("apple.png")

clock = pygame.time.Clock()

tank_width = 40
tank_hight = 20

turretwidth = 5
wheelwidth = 5

font = pygame.font.SysFont(None, 25)


def score(score):
    text = smallfont.render("score : "+str(score), True, black)
    gamedisplay.blit(text, [0, 0])
        
def pause():
    paused = True
    while paused:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.key == pygame.K_c:
                paused = False

            elif event.key == pygame.K_q:
                pygame.quit()
                quit()

        gamedisplay.fill(white)    
        message_to_gamedisplay("PAUSED",
                          black,
                          -100,
                          size = "large")
        message_to_gamedisplay("press C to continue and Q to quit.",
                          black,
                          25)
        pygame.display.update()
        clock.tick(20)

def explosion(x,y, size=50):
    pygame.mixer.Sound.play(explosion_sound)
    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygaqme.quit()
                quit()

        startpoint = x,y

        colorchoices = [red, light_red, yellow, light_yellow]

        magnitude = 1

        while magnitude < size:

            exploding_bit_x = x + random.randrange(-1*magnitude, magnitude)
            exploding_bit_y = y + random.randrange(-1*magnitude, magnitude)

            pygame.draw.circle(gamedisplay, colorchoices[random.randrange(0, 4)], (exploding_bit_x, exploding_bit_y), random.randrange(0, 5))
            magnitude += 1

            pygame.display.update()
            clock.tick(60)

        explode = False     

def barrier(xlocation, randomhight, barrier_width):    
    pygame.draw.rect(gamedisplay, black, [xlocation, display_hight-randomhight, barrier_width, randomhight])


def fireshell(xy, tankx, tanky, turpos, gun_power, xlocation, barrier_width, randomhight, enemytankx, enemytanky):
    pygame.mixer.Sound.play(fire_sound)
    fire = True
    damage = 0

    startingshell = list(xy)


    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygaqme.quit()
                quit()


        pygame.draw.circle(gamedisplay, green, (startingshell[0], startingshell[1]), 5)
            
        startingshell[0] -= (12 - turpos)*2

        startingshell[1] += int((((startingshell[0]-xy[0])*0.015/(gun_power/50))**2) - (turpos+turpos/(12-turpos)))

        if startingshell[1] > display_hight - groundhight:
            hitx = int((startingshell[0]*display_hight - groundhight)/startingshell[1])
            hity = int(display_hight - groundhight)
            if enemytankx + 15 > hitx > enemytankx - 15:
                damage = 25
            explosion(hitx, hity)
            fire = False

        cheak_x_1 = startingshell[0] <= xlocation + barrier_width
        cheak_x_2 = startingshell[0] >= xlocation

        cheak_y_1 = startingshell[1] <= display_hight
        cheak_y_2 = startingshell[1] >= display_hight - randomhight

        if cheak_x_1 and cheak_x_2 and cheak_y_1 and cheak_y_2:
            hitx = int((startingshell[0]))
            hity = int(startingshell[1])
            explosion(hitx, hity)
            fire = False


                
        pygame.display.update()    
        clock.tick(60)

    return damage        

def e_fireshell(xy, tankx, tanky, turpos, gun_power, xlocation, barrier_width, randomhight, ptankx, ptanky):
    pygame.mixer.Sound.play(fire_sound)
    damage = 0
    current_power = 1
    power_found = False

    while not power_found:
        current_power += 1
        if current_power > 100:
            power_found = True


        fire = True
        startingshell = list(xy)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygaqme.quit()
                    quit()


##            pygame.draw.circle(gamedisplay, red, (startingshell[0], startingshell[1]), 5)
                
            startingshell[0] += (12 - turpos)*2

##            gun_power = random.randrange(int(current_power*0.90), int(current_power*1.10))
            

            startingshell[1] += int((((startingshell[0]-xy[0])*0.015/(current_power/50))**2) - (turpos+turpos/(12-turpos)))

            if startingshell[1] > display_hight - groundhight:
                hitx = int((startingshell[0]*display_hight - groundhight)/startingshell[1])
                hity = int(display_hight - groundhight)
##                explosion(hitx, hity)
                if ptankx+15 > hitx > ptankx-15:
                    power_found = True
                    
                fire = False

            cheak_x_1 = startingshell[0] <= xlocation + barrier_width
            cheak_x_2 = startingshell[0] >= xlocation

            cheak_y_1 = startingshell[1] <= display_hight
            cheak_y_2 = startingshell[1] >= display_hight - randomhight

            if cheak_x_1 and cheak_x_2 and cheak_y_1 and cheak_y_2:
                hitx = int((startingshell[0]))
                hity = int(startingshell[1])
##                explosion(hitx, hity)
                fire = False
                

    fire = True
    startingshell = list(xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygaqme.quit()
                quit()

        pygame.draw.circle(gamedisplay, red, (startingshell[0], startingshell[1]), 5)
        startingshell[0] += (12 - turpos)*2


        
        gun_power = random.randrange(int(current_power*0.90), int(current_power*1.10))
        
        startingshell[1] += int((((startingshell[0]-xy[0])*0.015/(gun_power/50))**2) - (turpos+turpos/(12-turpos)))

        if startingshell[1] > display_hight - groundhight:
            hitx = int((startingshell[0]*display_hight - groundhight)/startingshell[1])
            hity = int(display_hight - groundhight)
            if ptankx + 15 > hitx > ptankx - 15:
                damage = 25
            explosion(hitx, hity)
            fire = False

        cheak_x_1 = startingshell[0] <= xlocation + barrier_width
        cheak_x_2 = startingshell[0] >= xlocation

        cheak_y_1 = startingshell[1] <= display_hight
        cheak_y_2 = startingshell[1] >= display_hight - randomhight

        if cheak_x_1 and cheak_x_2 and cheak_y_1 and cheak_y_2:
            hitx = int((startingshell[0]))
            hity = int(startingshell[1])
            explosion(hitx, hity)
            fire = False
          
        pygame.display.update()    
        clock.tick(60)

    return damage        

def power(level):
    text = smallfont.render("level: "+str(level)+("%"), True, black)
    gamedisplay.blit(text, [display_width/2,0])

def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gamedisplay.fill(white)

        message_to_gamedisplay("welcome to, tanks",green,-100,"large")
        message_to_gamedisplay("the objective is to distroy enemy",black,-30)        
        message_to_gamedisplay("before they distroy you !",black,10)  
        message_to_gamedisplay("more enemy you distroy , they get harder !",black,50)

   
        button("play", 150, 500, 100, 50, green, light_green, action="play")
        button("controls", 325, 500, 150, 50, yellow, light_yellow, action="controls")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")

        text_to_button("play", black, 175, 472, 100, 50)
        text_to_button("controls", black, 375, 472, 100, 50)
        text_to_button("quit", black, 575, 472, 100, 50)
        
        pygame.display.update()
        clock.tick(15)

# display message

smallfont = pygame.font.SysFont("comicsansms", 25)
midfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 60)


def tank(x, y, torpos):
    x = int(x)
    y = int(y)

    possibleturret = [(x-27, y-2),
                      (x-26, y-5),
                      (x-25, y-8),
                      (x-23, y-12),
                      (x-20, y-14),
                      (x-18, y-15),
                      (x-15, y-17),
                      (x-13, y-19),
                      (x-11, y-21)
                      ]


    
    pygame.draw.circle(gamedisplay, black, (x, y),int(tank_hight/2))
    pygame.draw.rect(gamedisplay, black, (x-tank_hight, y, tank_width, tank_hight))
    
    pygame.draw.line(gamedisplay, black, (x,y), possibleturret[torpos], turretwidth)    

    pygame.draw.circle(gamedisplay, black, (x-15, y+20), wheelwidth)
    pygame.draw.circle(gamedisplay, black, (x-10, y+20), wheelwidth)
    pygame.draw.circle(gamedisplay, black, (x-5, y+20), wheelwidth)
    pygame.draw.circle(gamedisplay, black, (x, y+20), wheelwidth)
    pygame.draw.circle(gamedisplay, black, (x+5, y+20), wheelwidth)
    pygame.draw.circle(gamedisplay, black, (x+10, y+20), wheelwidth)
    pygame.draw.circle(gamedisplay, black, (x+15, y+20), wheelwidth)

    return possibleturret[torpos]

def enemy_tank(x, y, torpos):
    x = int(x)
    y = int(y)

    possibleturret = [(x+27, y-2),
                      (x+26, y-5),
                      (x+25, y-8),
                      (x+23, y-12),
                      (x+20, y-14),
                      (x+18, y-15),
                      (x+15, y-17),
                      (x+13, y-19),
                      (x+11, y-21)
                      ]


    
    pygame.draw.circle(gamedisplay, black, (x, y),int(tank_hight/2))
    pygame.draw.rect(gamedisplay, black, (x-tank_hight, y, tank_width, tank_hight))
    pygame.draw.line(gamedisplay, black, (x,y), possibleturret[torpos], turretwidth)    

    pygame.draw.circle(gamedisplay, black, (x-15, y+20), wheelwidth)
    pygame.draw.circle(gamedisplay, black, (x-10, y+20), wheelwidth)
    pygame.draw.circle(gamedisplay, black, (x-5, y+20), wheelwidth)
    pygame.draw.circle(gamedisplay, black, (x, y+20), wheelwidth)
    pygame.draw.circle(gamedisplay, black, (x+5, y+20), wheelwidth)
    pygame.draw.circle(gamedisplay, black, (x+10, y+20), wheelwidth)
    pygame.draw.circle(gamedisplay, black, (x+15, y+20), wheelwidth)

    return possibleturret[torpos]


def game_controls():
    
    gcont = True

    while gcont:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamedisplay.fill(white)
        message_to_gamedisplay("controls",green,-100,"large")
        message_to_gamedisplay("fire :: space bar",black,-30)        
        message_to_gamedisplay("move turret :: up and down arrow key",black,10)  
        message_to_gamedisplay("move tank :: left and right arrow key",black,50)
        message_to_gamedisplay("pause :: p",black,90)
        message_to_gamedisplay("main menu :: m",black,130)

   
        button("play", 150, 500, 100, 50, green, light_green, action="play")
        button("controls", 325, 500, 150, 50, yellow, light_yellow, action="main menu")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")

        text_to_button("play", black, 175, 472, 100, 50)
        text_to_button("main menu", black, 375, 472, 100, 50)
        text_to_button("quit", black, 575, 472, 100, 50)
        
        pygame.display.update()
        clock.tick(15)



def game_over():
    
    game_over = True

    while game_over:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamedisplay.fill(white)
        message_to_gamedisplay("game over",green,-100,"large")
        message_to_gamedisplay("you lose",black,-30)        
  
        button("play", 125, 500, 150, 50, green, light_green, action="play")
        button("controls", 325, 500, 150, 50, yellow, light_yellow, action="main menu")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")

        text_to_button("play again", black, 175, 472, 100, 50)
        text_to_button("main menu", black, 375, 472, 100, 50)
        text_to_button("quit", black, 575, 472, 100, 50)
        
        pygame.display.update()
        clock.tick(15)

def you_win():
    
    you_win = True

    while you_win:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gamedisplay.fill(white)
        message_to_gamedisplay("you win",green,-100,"large")
        message_to_gamedisplay("congratulations",black,-30)        
  
        button("play", 125, 500, 150, 50, green, light_green, action="play")
        button("controls", 325, 500, 150, 50, yellow, light_yellow, action="main menu")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")

        text_to_button("play again", black, 175, 472, 100, 50)
        text_to_button("main menu", black, 375, 472, 100, 50)
        text_to_button("quit", black, 575, 472, 100, 50)
        
        pygame.display.update()
        clock.tick(15)       
    
def button(text, x, y, width, hight, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+width > cur[0] > x and y+hight > cur[1] > y:  
        pygame.draw.rect(gamedisplay, active_color, (x, y, width, hight))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_controls()

            if action == "play":

                gameloop()
                
            if action == "main menu":
                game_intro()



                
    else:
        pygame.draw.rect(gamedisplay, inactive_color, (x, y, width, hight))
    
def text_objects(text, color, size):
    if size == "small":
        textsurface = smallfont.render(text, True, color)
    elif size == "medium":
        textsurface = midfont.render(text, True, color)
    elif size == "large":
        textsurface = largefont.render(text, True, color)

        
    return textsurface, textsurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonhight, buttonwidth, size="small"):
    textsurf, textrect = text_objects(msg, color, size)    
    textrect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonhight/2))
    gamedisplay.blit(textsurf, textrect)

    
def message_to_gamedisplay(msg, color, y_displace=0, size = "small"):
    textsurf, textrect = text_objects(msg, color, size)
    textrect.center = int(display_width / 2), int(display_hight / 2)+y_displace
    gamedisplay.blit(textsurf, textrect)

def health_bars(player_health, enemy_health):

    if player_health > 75:
        player_health_color = light_green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red

    if enemy_health > 75:
        enemy_health_color = light_green
    elif enemy_health > 50:
        enemy_health_color = yellow
    else:
        enemy_health_color = red

    pygame.draw.rect(gamedisplay, player_health_color, [680, 25, player_health, 25])
    pygame.draw.rect(gamedisplay, enemy_health_color, [20, 25, enemy_health, 25])


# game loop
def gameloop():

    game_exit = True
    gameover = False

    maintankx = display_width * 0.9
    maintanky = display_hight * 0.9
    tankmove = 0

    enemytankx = display_width * 0.1
    enemytanky = display_hight * 0.9

    xlocation = (display_width/2) + random.randint(-0.1*display_width, 0.1*display_width)
    randomhight = random.randrange(display_hight*0.1, display_hight*0.6)

    barrier_width = 50

    currentturpos = 0
    changetur = 0

    fire_power = 50
    power_change = 0

    player_health = 100
    enemy_health = 100

    while game_exit:
    
        if gameover == True:
            gamedisplay.fill((225, 225, 255))
            message_to_gamedisplay("game over",
                              red, -50,
                              size = "large")
            message_to_gamedisplay("press C to play again and Q to exit",
                              black,
                              50,
                              size = "medium")
            pygame.display.update()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = False
                    break
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = False
                        gameover = False
                    if event.key == pygame.K_c:
                        gameloop()

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankmove = -5
                elif event.key == pygame.K_RIGHT:
                    tankmove = +5
                elif event.key == pygame.K_x:
                    changetur = 1
                elif event.key == pygame.K_z:
                    changetur = -1
                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_m:
                    game_intro()

                elif event.key == pygame.K_SPACE:
                    
                    damage = fireshell(gun, maintankx, maintanky, currentturpos, fire_power, xlocation, barrier_width, randomhight, enemytankx, enemytanky)
                    enemy_health -= damage


                    possiblemovement = ['f','r']
                    moveindex = random.randrange(0,2)

                    for x in range(random.randrange(0,10)):

                        if display_width * 0.3 > enemytankx > display_width * 0.03:
                            
                            if possiblemovement[moveindex] == 'f':
                                enemytankx += 5
                            elif possiblemovement[moveindex] == 'r':
                                enemytankx -= 5

                            gamedisplay.fill(white)
                            health_bars(player_health, enemy_health)
                            gun = tank(maintankx, maintanky, currentturpos)
                            enemy_gun = enemy_tank(enemytankx, enemytanky, 8)
                            fire_power += power_change
                            power(fire_power)
                            barrier(xlocation, randomhight, barrier_width)
                            gamedisplay.fill(green, rect=[0, display_hight-groundhight, display_width, groundhight])
                            pygame.display.update()
                            
                            clock.tick(FPS)


                    damage = e_fireshell(enemy_gun, enemytankx, enemytanky, 8, 50, xlocation, barrier_width, randomhight, maintankx, maintanky)
                    player_health -= damage
                    
                elif event.key == pygame.K_a:
                    power_change = -1

                elif event.key == pygame.K_s:
                    power_change = 1    

            if event.type == pygame.KEYUP:
                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                     tankmove = 0
                 if event.key == pygame.K_z or event.key == pygame.K_x:
                     changetur = 0
                 if event.key == pygame.K_a or event.key == pygame.K_s:
                    power_change = 0

        maintankx += tankmove
        currentturpos += changetur

        if currentturpos > 8:
            currentturpos = 8
        elif currentturpos < 0:
            currentturpos = 0

        
        if maintankx - (tank_width/2) <  xlocation+barrier_width:
             maintankx += 5
             
        gamedisplay.fill(white)
        health_bars(player_health, enemy_health)
        gun = tank(maintankx, maintanky, currentturpos)
        enemy_gun = enemy_tank(enemytankx, enemytanky, 8)
        fire_power += power_change

        if fire_power > 100:
            fire_power = 100

        elif fire_power < 1:
            fire_power = 1


        
        power(fire_power)
        barrier(xlocation, randomhight, barrier_width)
        gamedisplay.fill(green, rect=[0, display_hight-groundhight, display_width, groundhight])
        pygame.display.update()

        if player_health < 1:
            game_over()
        elif enemy_health < 1:
            you_win()

        elif enemy_health < 1 and player_health < 1:
            game_over()
        
        clock.tick(FPS)

    # quit game
    pygame.quit()
    quit()

game_intro()
gameloop()



 



    

