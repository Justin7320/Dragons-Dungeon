
#The Gamers!
#Dragons Dungeon
#Kyle Afzali, Kenny Burgos, and Justin M.
#You have to get through the maze, to the queen and pass the dragons minions.


from gamelib import*#import game library
#Creat variable
game = Game(1000, 800,"Dragons Dungeon")
bk = Image("images\\background.jpg",game)
bk.resizeTo(1000, 800)

play = Image("images\\play.png",game)
play.moveTo(550,410)
play.resizeTo(350,420)

title = Image("images\\title.png",game)
title.resizeTo(1000, 800)




bks = Sound("bk.wav",1)


#title sccreen

while not game.over:
   game.processInput()

   bk.draw()
   title.draw()
   play.draw()
   bks.play()




   if play.collidedWith(mouse) and mouse.LeftButton:
       game.over = True

   game.update(10)








#Level One game loop


king = Animation("images\\upk.png",4,game,128/4,41)
maze = Image("Images\\maze.jpg",game)
key = Image("Images\\key.png",game)
health = Image("Images\\heart.png",game)
health2 = Image("Images\\h2.png",game)
health3 = Image("Images\\h3.png",game)
cage = Image("Images\\cage.jpg",game)
goblin= Animation("Images\\goblin.png",3,game,31,113/3)
Q = Animation("images\\q.png",3,game,39,169/3)
winter = Image("images\\winter.png",game)
BM = Image("Images\\bk maze.png",game)
#move/resize
winter.resizeTo(750, 800)
health.resizeTo(50,50)
health2.resizeTo(50,50)
health3.resizeTo(50,50)
maze.resizeTo(700,600)
BM.resizeTo(700,600)
king.resizeTo(30,30)
key.resizeTo(25,25)
goblin.moveTo(350,235)
king.moveTo(550,250)
cage.moveTo(195,300)
Q.moveTo(200,300)
key.moveTo(800,145)
cage.resizeTo(150,150)
health.moveTo(30,50)
health2.moveTo(75,50)
health3.moveTo(120,50)



win = Sound("win.wav",2)
lose = Sound("lavendertown.wav",3)



#goblin = []
#for index in range(8):
    #goblin.append(Animation("images\\goblin.png",12,game,31,113/3,use_alpha=False))    

#for index in range(8):
         #x = randint(100,800)
         #y = randint(100,800)
         #goblin[index].moveTo(x, -y)
         #goblin[index].setSpeed(4,7)





game.over = False
while not game.over:
   game.processInput()
   bk.draw()
   maze.draw()
   Q.draw()
   cage.draw()
   health3.draw()
   health2.draw()
   health.draw()
   goblin.draw()
   key.draw()
   BM.draw()
   king.draw()
   bks.play()

   #def moveTowards(goblin,king,):
   goblin.setSpeed(3,goblin.angleTo(king))
   goblin.move()

  
   if goblin.collidedWith(king) :
       health.visible = False
       health2.visible = False
       health3.visible = False




   if king.collidedWith(cage) :
       cage.visible = False
       key.visible = False


   if key.collidedWith(king) :
      key.moveTo(700,50)
      key.resizeTo(80,80)


      
   if keys.Pressed[K_UP]:

                   king.y -=4
   if keys.Pressed[K_DOWN]:
                    king.y +=4
                   
   if keys.Pressed[K_RIGHT]:
                   king.x +=4

   if keys.Pressed[K_LEFT]:
                   king.x -=4


   if Q.collidedWith(king): 
      
      game.over=True


   #if  not health3.visible = False :
      #game.over=True



   game.update(30)



#win screen

  



winter = Image("images\\winter.png",game)
winter.resizeTo(750, 800)
game.over = False

while not game.over:
   game.processInput()


   win.play()
   bk.draw()
   winter.draw()

   game.update(100)
   game.wait(K_RETURN)
   game.quit()





gameover = Image("images\\gameover.jpg",game)
gameover.resizeTo(1000, 800)




while not game.over:
   game.processInput()                   


bk.draw()
gameover.draw()
lose.play()





game.update(20)
game.wait(K_RETURN)
game.quit()
