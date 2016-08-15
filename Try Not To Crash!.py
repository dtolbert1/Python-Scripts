import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

#Color is measured using RGB(Red, Blue, Green)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_color = (53, 115 , 255)

#Variable used to know where both edges of the car are
car_width = 150

#This sets our game display and display size
gameDisplay = pygame.display.set_mode((display_width,display_height))

#Give the game a title
pygame.display.set_caption('Try Not To Crash!')
clock = pygame.time.Clock()

#Car Image (Make sure it is in the same directory as your script)
carImg = pygame.image.load('racecar.png')

#This is a text displaying function that will display how many objects that we've avoided
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Objects dodged: " + str(count), True, black)
    gameDisplay.blit(text,(0,0))

#This function is how we will draw the objects on our game
#It takes x,y starting points, width and height variables, and finally color
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

#Car function to display the car image
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

#How to create our invisible rectangle
def text_objects(text, font,):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#This is the message displaying function
#We define the large text, then we define the tet and the rectable that would encompass it
#We then center the text using our width and height variables
#Then we blit this to the surface, remembering this only draws it in the background
#We need to call "pygame.display.update"
#After the display, we need to run back the game loop

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

#Make a crash function to be able to make a crash more elaborate in the future
def crash():
    message_display("You crashed!")

def game_loop():
    x = (display_width * 0.45)
    y = (display_height *0.8)

    x_change = 0

    #We want the starting position of the object to be random in its x range, between 0 and the width of the display
    #Then we define the y position with thing_starty;
    #We use -600 so the player has time to get situated before the block appears on the screen
    #Then we specify the objects speed; This is how many pixels at a time it will move
    #We then define the blocks width and height
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 3
    thing_width = 100
    thing_height = 100

    dodged = 0

    #Event handling loop

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            #Saying what will happen if a key is pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            #Saying what will happen if the key is released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        #Changes the x variable of the car
        x += x_change
        gameDisplay.fill(white)

        #things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        #This is the logic for whether or not the car has crossed over the left or right boundaries
        if x > display_width - car_width or x < 0:
            crash()

        #The code block to create another block once one has moved off of the screen
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

        #Everytime we dodge a block, the speed increases and the width of the block increases
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        #We're asking if y, the car's top left, has crossed the object's y + height, meaning the bottom left.
        #If it has, we print that y crossover has occured.
        #This doesn't mean there's necessarily overlap, maybe the x coordinates are vastly different and we're on opposite sides.
        #We then need to ask if the objects are anywhere within each other's boundaries.
        if y < thing_starty + thing_height:
            print("y crossover")

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print("x crossover")
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()