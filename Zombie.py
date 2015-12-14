from gamelib import *

game = Game(800,600,"Zombie Attack!",60)
bk  = Image("images\\Zbk.jpg",game)
bk.resizeTo(800,600)
zombie = Image("images\\zombie.png",game)
zombie.resizeTo(150,150)
zombie.setSpeed(4,60)
turkey = Image("images\\turkey.gif",game)
turkey.resizeBy(-50)
turkey.setSpeed(6,45)
gun = Sound("sound\\Gun2.wav",1)
chomp = Sound("sound\\ZombieChomp.wav",2)
gobble = Sound("sound\\TurkeyGooble.wav",3)
die = Sound("sound\\ZombieDie.wav",4)
scope = Image("images\\crosshair.png",game)

while not game.over:
    game.processInput()

    bk.draw()
   
    zombie.move(True)
    turkey.move(True)
    turkey.resizeBy(1)
    scope.moveTo(mouse.x,mouse.y)
    if mouse.LeftButton:
        gun.play()
    if zombie.collidedWith(mouse) and mouse.LeftButton:
        zombie.resizeBy(-2)
        x = randint(zombie.width,game.width-zombie.width)
        y = randint(zombie.height,game.height-zombie.height)
        zombie.moveTo(x,y)
        zombie.speed += 2        
        game.score += 10
        die.play()
        
    if zombie.collidedWith(turkey):
        turkey.resizeTo(150,150)
        x = randint(turkey.width,game.width-turkey.width)
        y = randint(turkey.height,game.height-turkey.height)
        turkey.moveTo(x,y)
        game.score -= 10
        chomp.play()
        gobble.play()

    if turkey.width >= 250:
        turkey.resizeTo(150,150) 
        x = randint(turkey.width,game.width-turkey.width)
        y = randint(turkey.height,game.height-turkey.height)
        turkey.moveTo(x,y)
        game.score += 10
        gobble.play()
    
    if turkey.collidedWith(mouse) and mouse.LeftButton:
        gobble.play()
        game.time -= 10

    if game.time <= 0:
        game.over = True
    game.displayTime(150,5)
    game.displayScore()
    game.update(20)
game.quit()
