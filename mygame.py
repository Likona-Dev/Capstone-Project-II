import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image). 

player = pygame.image.load("image.png")
first_enemy = pygame.image.load("enemy.png")
second_enemy = pygame.image.load("monster2.jpg")
third_enemy = pygame.image.load("player2.jpg")
prize = pygame.image.load("prize2.jpg")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

image_height = player.get_height()
image_width = player.get_width()
first_enemy_height = first_enemy.get_height()
first_enemy_width = first_enemy.get_width()
second_enemy_height = second_enemy.get_height()
second_enemy_width = second_enemy.get_width()
third_enemy_height = third_enemy.get_height()
third_enemy_width = third_enemy.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 300

# Make the enemies start off screen and at a random y position.
# Modify (enemyXPosition = screen_width) to (enemyXPosition = screen_width + 490), so that the enemies don't come out at the same time.

first_enemyXPosition =  screen_width 
first_enemyYPosition =  random.randint(0, screen_height - first_enemy_height)
second_enemyXPosition =  screen_width + 490
second_enemyYPosition =  random.randint(0, screen_height - second_enemy_height)
third_enemyXPosition =  screen_width + 1040
third_enemyYPosition =  random.randint(0, screen_height - third_enemy_height)

# prize object, on the x-axis place on the rightmost position and randomise the object on the y-axis.

prizeXPosition = screen_width + 1040
prizeYPosition = random.randint(0, screen_height - prize_height)

# This checks if the up or down key is pressed.
# Since no keys are pressed at this point, store them in bool variables as False.

keyUp= False
keyDown = False
keyLeft = False
keyRight = False


# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play.

while 1:# This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'. In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have. You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(first_enemy, (first_enemyXPosition, first_enemyYPosition))
    screen.blit(second_enemy, (second_enemyXPosition, second_enemyYPosition))
    screen.blit(third_enemy, (third_enemyXPosition, third_enemyYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position, increase the x position to move right.
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_height - image_height:
            playerXPosition += 1
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemies:
    
    first_enemyBox = pygame.Rect(first_enemy.get_rect())
    first_enemyBox.top = first_enemyYPosition
    first_enemyBox.left = first_enemyXPosition

    second_enemyBox = pygame.Rect(second_enemy.get_rect())
    second_enemyBox.top = second_enemyYPosition
    second_enemyBox.left = second_enemyXPosition

    third_enemyBox = pygame.Rect(third_enemy.get_rect())
    third_enemyBox.top = third_enemyYPosition
    third_enemyBox.left = third_enemyXPosition
    
    # Bounding box for the prize:

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    
    # Test collision of the boxes:

    if playerBox.colliderect(first_enemyBox) or playerBox.colliderect(second_enemyBox) or playerBox.colliderect(third_enemyBox):

        # Display losing status to the user:

        print("You lose!")

        # Quit game and exit window:

        pygame.quit()
        exit(0)

    # If the enemy is off the screen the user wins the game:    

    if first_enemyXPosition < 0 - first_enemy_width and second_enemyXPosition < 0 - second_enemy_width and third_enemyXPosition < 0 - third_enemy_width:

        # Display winning status to the user:

        print("You win!")

        # Quit game and exit window:
        pygame.quit()

        exit(0)
        
    # If the player collides with the prize the player, wins    

    if playerBox.colliderect(prizeBox):

        # Display losing status to the user:

        print("You win!")

        # Quit game and exit window:

        pygame.quit()
        exit(0)        
    
 
    
    # Make enemies and the prize approach the player at different speeds.
    
    first_enemyXPosition -= 0.15
    second_enemyXPosition -= 0.15
    third_enemyXPosition -= 0.15
    prizeXPosition -= 0.25
    
    # ================The game loop logic ends here. =============
