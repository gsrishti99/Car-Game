import pygame
import time
import random
import sys
pygame.init()
pygame.font.init()
charcoal = (70,70,70)
black = (0,0,0)
red = (255,0,0)
bright_red = (255, 63, 0)
blue = (0,0,255)
bright_blue = (65, 105, 225)
green = (0,200,0)
bright_green = (0,255,0)
yellow = (237,237,45)
display_width = 900
display_height = 700
car_width = 78
car_height = 154
pause = False
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()
carimg = pygame.image.load('lambo2_burned.png')
grassimg = pygame.image.load('grass.jpg')
roadimg = pygame.image.load('highway.jpg')
roadimg = pygame.transform.scale(roadimg, (700, 400))
background = pygame.image.load("bg.jpg")

# Front Page
def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(background,(0,0))
        largetext = pygame.font.Font("Xcelsion Italic.ttf",115)
        TextSurf,TextRect = text_objects("CAR GAME",largetext)
        TextRect.center = (450,100)
        gamedisplays.blit(TextSurf,TextRect)
        button("START",700,200,110,50,green,bright_green,"play")
        button("QUIT",700,400,100,50,red,bright_red,"quit") 
        button("INSTRUCTIONS",630,300,250,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)

# Set background for countdown before starting the new game
def countdown_background():
    font = pygame.font.SysFont(None,25)
    x = (display_width*0.45)
    y = (display_height*0.75)
    gamedisplays.blit(grassimg,(0,0))
    gamedisplays.blit(grassimg,(0,400))
    gamedisplays.blit(grassimg,(807,0))
    gamedisplays.blit(grassimg,(807,400))
    gamedisplays.blit(roadimg,(100,0))
    gamedisplays.blit(roadimg,(100,400))
    gamedisplays.blit(carimg,(int(x),int(y)))
    text=font.render("Passed: 0",True,red)
    score=font.render("Score: 0",True,red)
    gamedisplays.blit(text,(100,50))
    gamedisplays.blit(score,(100,30))
    button("PAUSE",650,0,150,50,blue,bright_blue,"pause")

# Countdown Function
def countdown():
    countdown = True
    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.fill(charcoal)
        countdown_background()
        largetext = pygame.font.Font("Xcelsion Italic.ttf",115)
        TextSurf,TextRect = text_objects("3", largetext)
        TextRect.center = ((int(display_width/2)), (int(display_height/2)))
        gamedisplays.blit(TextSurf,TextRect) 
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(charcoal)
        countdown_background()
        largetext = pygame.font.Font("Xcelsion Italic.ttf",115)
        TextSurf,TextRect = text_objects("2", largetext)
        TextRect.center = ((int(display_width/2)), (int(display_height/2)))
        gamedisplays.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(charcoal)
        countdown_background()
        largetext = pygame.font.Font("Xcelsion Italic.ttf",115)
        TextSurf,TextRect = text_objects("1", largetext)
        TextRect.center = ((int(display_width/2)), (int(display_height/2)))
        gamedisplays.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(charcoal)
        countdown_background()
        largetext = pygame.font.Font("Xcelsion Italic.ttf",115)
        TextSurf,TextRect = text_objects("GO!!", largetext)
        TextRect.center = ((int(display_width/2)), (int(display_height/2)))
        gamedisplays.blit(TextSurf,TextRect)
        pygame.display.update()
        clock.tick(1)
        game_loop()

# To pause the game
def paused():
    global pause
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(background,(0,0))
        largetext = pygame.font.Font("Xcelsion Italic.ttf",110)
        TextSurf,TextRect = text_objects("PAUSED", largetext)
        TextRect.center = (450,100)
        gamedisplays.blit(TextSurf,TextRect)
        button("CONTINUE",660,200,160,50,green,bright_green,"unpause")
        button("RESTART",660,300,150,50,blue,bright_blue,"play")
        button("MAIN MENU",635,400,200,50,red,bright_red,"menu")
        pygame.display.update()
        clock.tick(30)

# To unpause the game
def unpaused():
    global pause
    pause = False

# Apply buttons on the screen
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gamedisplays,ac, (x,y,w,h))
        if click[0] == 1 and action!= None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
            elif action=="intro":
                introduction()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                paused()
            elif action == "unpause":
                unpaused()
        
    else:
        pygame.draw.rect(gamedisplays, ic, (x,y,w,h))
    smalltext = pygame.font.Font("Xcelsion Italic.ttf", 20)
    textsurf,textrect = text_objects(msg, smalltext)
    textrect.center = ((int(x+(w/2))), (int(y+(h/2))))
    gamedisplays.blit(textsurf, textrect)

# For Introduction and Rules of the game
def introduction():
    introduction = True
    while introduction:
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                quit.exit()
        gamedisplays.blit(background, (0,0))
        largetext = pygame.font.Font("Xcelsion Italic.ttf", 70)
        smalltext = pygame.font.Font("Yellowjacket Condensed.ttf", 30)
        mediumtext = pygame.font.Font("Xcelsion Italic.ttf", 50)
        textSurf,textRect = text_objects("This is a car game in which you need dodge the coming cars.", smalltext)
        textRect.center = ((370), (200))
        TextSurf,TextRect = text_objects("INSTRUCTION", largetext)
        TextRect.center = ((450),(100))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        stextSurf,stextRect = text_objects("ARROW LEFT: LEFT TURN", smalltext)
        stextRect.center = ((150),(400))
        hTextSurf,hTextRect = text_objects("ARROW RIGHT: RIGHT TURN", smalltext)
        hTextRect.center = ((150),(450))
        atextSurf,atextRect = text_objects("F: ACCELERATOR", smalltext)
        atextRect.center = ((150),(500))
        rtextSurf,rtextRect = text_objects("S: BREAK", smalltext)
        rtextRect.center = ((150),(550))
        ptextSurf,ptextRect = text_objects("P: PAUSE", smalltext)
        ptextRect.center = ((150),(350))
        sTextSurf,sTextRect = text_objects("CONTROLS", mediumtext)
        sTextRect.center = ((350),(300))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        gamedisplays.blit(atextSurf,atextRect)
        gamedisplays.blit(rtextSurf,rtextRect)
        gamedisplays.blit(ptextSurf,ptextRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)
    
# Put obstacles for the car
def obstacle(obs_startx,obs_starty,obs):
    if obs == 0:
        obs_pic = pygame.image.load("obs6_burned.png")
    if obs == 1:
        obs_pic = pygame.image.load("obs5_burned.png")
    if obs == 2:
        obs_pic = pygame.image.load("obs2_burned.png")
    if obs == 3:
        obs_pic = pygame.image.load("obs7_burned.png")
    if obs == 4:
        obs_pic = pygame.image.load("obs1_burned.png")
    if obs == 5:
        obs_pic = pygame.image.load("obs4_burned.png")
    gamedisplays.blit(obs_pic,(int(obs_startx),int(obs_starty)))

# Display Score
def score_system(passed_car,score):
    font=pygame.font.SysFont(None,35)
    text=font.render("Passed: " + str(passed_car),True,red)
    score=font.render("Score: " + str(score),True,red)
    gamedisplays.blit(text,(100,50))
    gamedisplays.blit(score,(100,30))

# Blit car
def car(x,y):
    gamedisplays.blit(carimg,(int(x),int(y)))

# Blit road
def road():
    gamedisplays.blit(roadimg,(100,0))
    gamedisplays.blit(roadimg,(100,400))

# Blit grass    
def grass():
    gamedisplays.blit(grassimg,(0,0))
    gamedisplays.blit(grassimg,(0,400))
    gamedisplays.blit(grassimg,(807,0))
    gamedisplays.blit(grassimg,(807,400))

# Set font and color for text
def text_objects(text,font):
    textsurface = font.render(text,True,yellow)
    return textsurface,textsurface.get_rect()

# This function called when car crashes
def message(text):
    largetext = pygame.font.Font("Xcelsion Italic.ttf",80)
    textsurf,textrect = text_objects(text,largetext)
    textrect.center = ((int(display_width/2)),(int(display_height/2)))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

# Display message when the car crashes with other obstcles
def crash():
    message("CRASHED")

# Main Function
def game_loop():
    global pause
    x = (display_width*0.45)
    y = (display_height*0.75)
    x_change = 0
    obstacle_speed = 12
    obs = 0
    y_change = 0
    obs_startx = random.randrange(100,(display_width-200))
    obs_starty = -850
    obs_width = 65
    obs_height = 145
    passed_car = 0
    level = 0
    score = 0
    y2 = 7
    
    cross = False
    while not cross:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_f:
                    obstacle_speed+=2
                if event.key == pygame.K_s:
                    obstacle_speed-=2
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x+=x_change
        pause = True
        gamedisplays.fill(charcoal)
        
        rel_y = y2 % grassimg.get_rect().width
        int(rel_y)
        gamedisplays.blit(grassimg,(0,int(rel_y-grassimg.get_rect().width)))
        gamedisplays.blit(grassimg,(807,int(rel_y-grassimg.get_rect().width)))
        if rel_y < 700:
            gamedisplays.blit(grassimg,(0,int(rel_y)))
            gamedisplays.blit(grassimg,(807,int(rel_y)))
            gamedisplays.blit(grassimg,(0,int(rel_y)+400))
            gamedisplays.blit(grassimg,(807,int(rel_y)+400))
            gamedisplays.blit(roadimg,(100,int(rel_y)+100))
            gamedisplays.blit(roadimg,(100,int(rel_y)+200))
            gamedisplays.blit(roadimg,(100,int(rel_y)+300))
            gamedisplays.blit(roadimg,(100,int(rel_y)+400))
            gamedisplays.blit(roadimg,(100,int(rel_y)-100))

        y2+=obstacle_speed

        obs_starty -= (obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed_car,score)
        if x>745-car_width or x<165:
            crash()    
        if x>display_width-(car_width+165) or x<165:
            crash()
        if obs_starty>display_height:
            obs_starty = 0-obs_height
            obs_startx = random.randrange(180,(display_width-280))
            obs = random.randrange(0,6)
            passed_car+=1
            score=passed_car*10
            if (passed_car)%11==0:
                level+=1 
                obstacle_speed+=2
                largetext = pygame.font.Font("Xcelsion Italic.ttf",80)
                textsurf,textrect = text_objects("level"+str(level),largetext)
                textrect.center = ((int(display_width/2)),(int(display_height/2)))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(2)
        if y<obs_starty+obs_height:
            if x>obs_startx and x<obs_startx + obs_width or x+car_width>obs_startx and x+car_width<obs_startx+obs_width:
                crash()       
        button("PAUSE",650,0,150,50,blue,bright_blue,"pause")  
        pygame.display.update()
        clock.tick(60)
intro_loop()
game_loop()
pygame.quit()
quit()
