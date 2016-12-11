from gamelib import *
from EarthDefendFunctions import *

game = Game(800,600,"Game")

earth = Image("images\\earth.png",game)
earth.resizeTo(150,150)

asteroids = [] #Empty List

for times in range(20):
    asteroids.append( Animation("images\\asteroid1t.gif",41,game,371/7,312/6) )

positionAsteroids(asteroids,earth,game)
'''
positionAsteroids is function from myAsteroidFunctions that randomly
positions asteroids off the screen and sets their angle to the direction of the
earth.  There is some trigonometry that might be unfamiliar.  That's ok!
As a programmer, sometimes its enough just to understand what is being
done for you and not necessarily how.
'''

hero = Image("images\\hero.gif",game)

explode = Animation("images\\explosion.png",22,game, 285/5, 320/5)
explode.visible = False
plasma = Animation("images\\plasmaball1.png",11,game,352/11,32)
plasma.visible = False

bk = Animation("images\\field_5.png",5,game,1000,1000)
game.setBackground(bk)

fires = []

while not game.over:
    game.processInput()
    game.drawBackground()
    
    earth.draw()
    hero.move()
    for a in asteroids:
        a.move()
    for f in fires:
        f.draw()
    explode.draw(False)
    plasma.move()
    
    if keys.Pressed[K_LEFT]:
        hero.rotateBy(2,"left")
    elif keys.Pressed[K_RIGHT]:
        hero.rotateBy(2,"right")
    else:
        hero.rotateBy(0,"still")
        
    if keys.Pressed[K_UP]:
        hero.forward(2)
    else:
        hero.speed *= 0.99
        
    if keys.Pressed[K_SPACE]:
        plasma.visible = True
        plasma.moveTo(hero.x,hero.y)
        plasma.setSpeed(10 , hero.getAngle())

    for a in asteroids:
        if a.collidedWith(earth):
            a.visible = False
            explode.moveTo(a.x,a.y)
            explode.visible = True
            fires.append(Animation("images\\explosion.png",22,game, 285/5, 320/5))
            fires[len(fires)-1].moveTo(a.x,a.y)
        if a.collidedWith(plasma):
            a.visible = False
            explode.moveTo(a.x,a.y)
            explode.visible = True

    game.update(100)
    
game.quit()
