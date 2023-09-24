import pygame
from random import randint
pygame.init() # initiate the pygame
gameDisplay = pygame.display.set_mode((1280,720)) # screen orientation
pygame.display.set_caption("PingPong")  # set the name of the game
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
green = (100,255,130)
red = (255,0,0)
Name = "PLAYER_1= "
Name_2 = "PLAYER_2= "
def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface,textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",35)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (110,25)
    gameDisplay.blit(TextSurf, TextRect)
def player_1 ():
    message_display(Name)
def text_object(text,font):
    textSurface = font.render(text, True, black)
    return textSurface,textSurface.get_rect()
def message_2(text):
    largeText = pygame.font.Font("freesansbold.ttf",35)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = (1120,25)
    gameDisplay.blit(TextSurf, TextRect)
def player_2 ():
    message_2(Name_2)
def text_object(text,font):
    textSurface = font.render(text, True, black)
    return textSurface,textSurface.get_rect()
def message_3(text):
    largeText = pygame.font.Font("freesansbold.ttf",45)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = (640,700)
    gameDisplay.blit(TextSurf, TextRect)
def game_start ():
    message_3("CLICK SPACEBAR TO MOVE BALL")
p1_score = 0
p2_score = 0
def score(count):
    font = pygame.font.Font("freesansbold.ttf",35)
    text = font.render(str(count), True,black)
    gameDisplay.blit(text,(205,10))
def score_2(count):
    font = pygame.font.Font("freesansbold.ttf",35)
    text = font.render(str(count), True,black)
    gameDisplay.blit(text,(1215,10))
def text_object(text,font):
    textSurface = font.render(text, True, black)
    return textSurface,textSurface.get_rect()
def message_4(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = (640,360)
    gameDisplay.blit(TextSurf, TextRect)
def GameOver ():
    message_4("GAME OVER")
def text_object(text,font):
    textSurface = font.render(text, True, black)
    return textSurface,textSurface.get_rect()
def message_5(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = (540,600)
    gameDisplay.blit(TextSurf, TextRect)
def winner_1 ():
    message_5("PLAYER_1 WINS")
def text_object(text,font):
    textSurface = font.render(text, True, black)
    return textSurface,textSurface.get_rect()
def message_6(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = (540,600)
    gameDisplay.blit(TextSurf, TextRect)
def winner_2():
    message_6("PLAYER_2 WINS")
x = 640
y = 360
p1 = 200
p2 = 300
p3 = 1080
p4 =300
step = 40
width = 20
height = 100
ball_width = 25
x_change = 0
y_change = 0
gameOver = False
while not gameOver:
    gameDisplay.fill(white) # set screen background
    line = pygame.draw.rect(gameDisplay,black,(640,50,1,620))
    centre = pygame.draw.circle(gameDisplay,green,(640,360),150)
    paddle = pygame.draw.rect(gameDisplay,black,(p1,p2,width,height)) # draws paddle
    post_1 =  pygame.draw.rect(gameDisplay,green,(0,200,150,10)) # draw post
    post_2 =  pygame.draw.rect(gameDisplay,green,(0,500,150,10)) # draw post
    post_3 =  pygame.draw.rect(gameDisplay,green,(150,200,10,310))  # draw post
    post_4 =  pygame.draw.rect(gameDisplay,green,(1130,200,150,10)) # draw post
    post_5 =  pygame.draw.rect(gameDisplay,green,(1130,500,150,10)) # draw post
    post_6 =  pygame.draw.rect(gameDisplay,green,(1130,200,10,310)) # draw post
    ball = pygame.draw.circle(gameDisplay,red,(x,y),25) # draws ball
    platform = pygame.draw.rect(gameDisplay,green,(0,670,1280,50))
    platform_1 = pygame.draw.rect(gameDisplay,green,(0,0,1280,50))      
    paddle_2 = pygame.draw.rect(gameDisplay,black,(p3,p4,20,100)) # draws paddle
    collide = pygame.Rect.colliderect(paddle,ball)
    collide_2 = pygame.Rect.colliderect(paddle_2,ball)
    collide_3 = pygame.Rect.colliderect(post_3,ball)
    collide_4 = pygame.Rect.colliderect(post_6,ball)
    player_1()
    player_2()
    game_start()
    score(p1_score)
    score_2(p2_score)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE: # moves ball
                y_change = randint(-3,3)
                x_change = randint(-3,3)
        keys = pygame.key.get_pressed() # moves paddle
        if keys[pygame.K_s]:
            p2 += step
        elif keys[pygame.K_w]:
            p2 -= step
        elif keys[pygame.K_KP_8]:
            p4 -= step
        elif keys[pygame.K_KP_2]:
            p4 += step
    x += x_change
    y += y_change
    if collide_4: # counts score
        x = 640
        y = 360
        x_change = 0
        y_change = 0
        p1_score += 1
    if collide_3: # counts score
        x = 640
        y = 360
        x_change = 0
        y_change = 0
        p2_score += 1
    if collide:
        y_change = randint(-5,5)
        x_change = +7
    if collide_2:
        y_change = randint(-5,5)
        x_change = -7
    if p2 < 25:
        p2 += step 
    elif p2 > 1155-p2:
        p2 -= step
    if p4 < 25:
        p4 += step
    elif p4 > 1155-p4:
        p4 -= step
    if x > 1280 - ball_width:
        x_change = -7
    if x < 20:
        x_change = +7
    if y > 670 - ball_width:
        y_change = -7
    if y < 75:
        y_change = +7
    if p1_score == 7:
        GameOver()
        winner_1()
        gameOver = True
    elif p2_score == 7:
        GameOver()
        winner_2()
        gameOver = True
    pygame.display.update()
    clock.tick(60)
pygame.quit() # Game ends
quit()                          
