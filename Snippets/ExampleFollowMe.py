import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
'''
The above two lines of code are a hack inorder to keep gamelib in a common
location where it can be updated it for all games.  If you copy gamelib.py
into the same folder as the game then you don't need these lines and can
simply delete them.
'''

from gamelib import *

game = Game(650,450,"FollowMe")
plasma = Animation("images\\plasmaball1.png",11,game,32,32,frate=3)
alien = Image("images\\alien2 39.gif",game)
oldx, oldy = 0,0 #Syntax for assigning multiple values to multiple variables in one line
locations = []

while not game.over:
    game.processInput()
    game.clearBackground(black)

    alien.move()
    plasma.draw()

    #Standard code just for moving the alien
    if keys.Pressed[K_LEFT]:
        alien.rotateBy(2,"left")
    elif keys.Pressed[K_RIGHT]:
        alien.rotateBy(2,"right")
    else:
        alien.rotateBy(0,"still")
    if keys.Pressed[K_UP]:
        alien.forward(-2)
    else:
        alien.speed *= 0.99

    #If there is a change in the x and y location of the alien as
    #compared to where it was, lets store that location and set its old location
    #to its current
    if oldx != alien.x or oldy != alien.y:
        locations.append( {"x":alien.x,"y":alien.y} )
        oldx = alien.x
        oldy = alien.y

    #We start moving the plasma to the oldest location stored after we have
    #stored more than 50 locations of the alien
    if len(locations) > 50:
        location = locations.pop(0)
        plasma.moveTo(location["x"],location["y"])
         
    game.update(60)


game.quit()

