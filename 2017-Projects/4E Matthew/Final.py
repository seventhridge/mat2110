import pygame, os

pygame.init()      #initializes pygame


'''
def menu():
    gameMenu = True
    if gameMenu == True:
        menuImage = pygame.image.load('C:/Users/wowba/Desktop/Reach.png')
        gameDisplay.blit(menuImage, (0,0))

      gameMenuClose = False

    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN]:
        gameMenuClose = True


    if gameMenuClose == True:
        image = pygame.image.load('C:/Users/wowba/Desktop/HaloBackground.png').convert_alpha()
        gameDisplay.blit(image, (0, 0))
'''

#Still have a runtime error when I use the menu.

def background():
    image = pygame.image.load('C:/Users/wowba/Desktop/HaloBackground.png').convert_alpha()
    gameDisplay.blit(image, (0,0))

def music():                        #This function plays music as soon as the program opens
    pygame.mixer.music.load("")
    pygame.mixer.music.play(-1,0.0)
                                    #I have a music file specially made for this game


class Player():
    def __index__(self):
        self.image = pygame.image.load('C:/Users/wowba/Desktop/bgbattleship.png')
        #This should load an image to be a sprite for the player to move
        self.x = 540
        self.y = 50
        #Sets the sprite initial position

    def movement(self):
        key = pygame.key.get_pressed()     #This function defines movement keys
        dist = 5                           #This sets movemnt distance to 5 per tick
        if key[pygame.K_UP]:
            self.y -= dist
        elif key[pygame.K_DOWN]:
            self.y += dist

    def draw(self, gameDisplay):
        gameDisplay.blit(self.image, (self.x, self.y))       #This should let my sprite show up on gameDisplay

player = Player()                       #For object based code lower down
clock = pygame.time.Clock()             #For the FPS tick lower down



class Wall():                      #The beginning of the walls. Not testable if program does not run
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1])



#Main or Game loop       gameExit will be set to True and quit when I quit the game.
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            gameExit = True


    gameDisplay = pygame.display.set_mode((1920, 1080))           #Sets resolution
    pygame.display.set_caption('Space Dash')                      #Sets window title

    # menu()

    background()                                                  #Runs background image
    player.draw(gameDisplay)                                      #Draws sprite
    player.movement()                                             #Allows control of sprite

    pygame.display.update()                                       #Updates the display, alowing animation

    clock.tick(60)                                                #Sets FPS to 60



