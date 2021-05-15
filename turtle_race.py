import turtle
import random
import time

def raph_don():
        
    # Screen setup
    screen = turtle.Screen()
    screen.bgcolor('black')

    # Making the first player: Raphael
    raphael = turtle.Turtle()
    raphael.color('red')
    raphael.shape('turtle')
    raphael.penup()
    raphael.goto(-300, 50)

    # Making the second player: Donatello
    donatello = turtle.Turtle()
    donatello.color('magenta')
    donatello.shape('turtle')
    donatello.penup()
    donatello.goto(-300, -50)

    # Making the finish line
    finish_line = turtle.Turtle(visible=False)
    finish_line.goto(300, -240)
    finish_line.color('white')
    finish_line.left(90)
    finish_line.forward(500)
    finish_line.pendown()

    # Making the game: turtles movement
    for pace in range(50):
        if raphael.pos() >= (290, -240):
            print('Raphael Wins!')
            raphael.color('gold')
            break
        elif donatello.pos() >= (290, -240):
            print('Donatello Wins!')
            donatello.color('gold')
            break

        # Turtle movement        
        raphael.forward(random.randint(30, 60)) 
        time.sleep(0.2)
        donatello.forward(random.randint(30, 60))
        time.sleep(0.2)
    
    # Calling the screen
    turtle.done()

def raph_don_leo():
    
    # Screen setup
    screen = turtle.Screen()
    screen.bgcolor('black')

    # Making the first player: Raphael
    raphael = turtle.Turtle()
    raphael.color('red')
    raphael.shape('turtle')
    raphael.penup()
    raphael.goto(-300, 200)

    # Making the second player: Donatello
    donatello = turtle.Turtle()
    donatello.color('magenta')
    donatello.shape('turtle')
    donatello.penup()
    donatello.goto(-300, -200)
    
    # Making the third player: Leonardo
    leonardo = turtle.Turtle()
    leonardo.color('blue')
    leonardo.shape('turtle')
    leonardo.penup()
    leonardo.goto(-300, 0)
    
    # Making the finish line
    finish_line = turtle.Turtle(visible=False)
    finish_line.goto(300, -240)
    finish_line.color('white')
    finish_line.left(90)
    finish_line.forward(500)
    finish_line.pendown()

    # Making the game: turtles movement
    for pace in range(50):
        if raphael.xcor() >= 270:
            print('Raphael Wins!')
            raphael.color('gold')
            break
        elif donatello.xcor() >= 270:
            print('Donatello Wins!')
            donatello.color('gold')
            break
        elif leonardo.xcor() >= 270:
            print('Leonardo Wins!')
            leonardo.color('gold') 
            break   
            
        # Turtle movement        
        raphael.forward(random.randint(30, 60)) 
        time.sleep(0.2)
        donatello.forward(random.randint(30, 60))
        time.sleep(0.2)
        leonardo.forward(random.randint(30, 60))
        time.sleep(0.2)
        
    turtle.done()

def raph_don_leo_mikey():
    
    # Screen setup
    screen = turtle.Screen()
    screen.bgcolor('black')

    # Making the first player: Raphael
    raphael = turtle.Turtle()
    raphael.color('red')
    raphael.shape('turtle')
    raphael.penup()
    raphael.goto(-300, 100)

    # Making the second player: Donatello
    donatello = turtle.Turtle()
    donatello.color('magenta')
    donatello.shape('turtle')
    donatello.penup()
    donatello.goto(-300, 50)
    
    # Making the third player: Leonardo
    leonardo = turtle.Turtle()
    leonardo.color('blue')
    leonardo.shape('turtle')
    leonardo.penup()
    leonardo.goto(-300, -50)
    
    # Making the fourth player: Michelangelo
    michelangelo = turtle.Turtle()
    michelangelo.color('orange')
    michelangelo.shape('turtle')
    michelangelo.penup()
    michelangelo.goto(-300, -100)
     
    
    # Making the finish line
    finish_line = turtle.Turtle(visible=False)
    finish_line.goto(300, -240)
    finish_line.color('white')
    finish_line.left(90)
    finish_line.forward(500)
    finish_line.pendown()

    # Making the game: turtles movement
    for pace in range(50):
        if raphael.xcor() >= 280: 
            print('Raphael Wins!')
            raphael.color('gold')
            break
        elif donatello.xcor() >= 280: 
            print('Donatello Wins!')
            donatello.color('gold')
            break
        elif leonardo.xcor() >= 280: 
            print('Leonardo Wins!')
            leonardo.color('gold') 
            break
        elif michelangelo.xcor() >=280: 
            print('Mchelangelo Wins!')
            michelangelo.color('gold')  
            break     
            
        # Turtle movement        
        raphael.forward(random.randint(30, 60)) 
        time.sleep(0.2)
        donatello.forward(random.randint(30, 60))
        time.sleep(0.2)
        leonardo.forward(random.randint(30, 60))
        time.sleep(0.2)
        michelangelo.forward(random.randint(30, 60))
        time.sleep(0.2)
        
    turtle.done()
        
# Main menu    
print('''               _                      
 _ __ __  ___ | | __  ___  _ __   ___ 
 \ V  V // -_)| |/ _|/ _ \| '  \ / -_)
  \_/\_/ \___||_|\__|\___/|_|_|_|\___|
  
   Please, choose a number:
   
   - 2
   - 3
   - 4
 
''')

# Answering the question you can race
answer = input('>> ')
if answer == str(2):
    raph_don()
elif answer == str(3):
    raph_don_leo()    
elif answer == str(4):
    raph_don_leo_mikey()    
else:
    print('ERROR!')
    print('Please, select the correct number!')    



        









