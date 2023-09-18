#imports
import turtle

#classes
class board:
  def __init__(self,x):
    self.turtle = x
    self.peices = [[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1]]
    self.turtle.pu()
    self.turtle.goto(-200,160)
    self.turtle.pd()
    self.turtle.fillcolor('cornsilk')
    self.turtle.color('cornsilk')
    self.turtle.speed(100)
    for x in range(8):
      for y in range(4):
        if x%2 == 0:
          self.turtle.begin_fill()
        self.turtle.left(90)
        self.turtle.fd(50)
        if x%2 != 0:
          self.turtle.end_fill()
        self.turtle.right(90)
        self.turtle.fd(50)
        if x%2 != 0:
          self.turtle.begin_fill()
        self.turtle.right(90)
        self.turtle.fd(50)
        if x%2 == 0:
          self.turtle.end_fill()
        self.turtle.left(90)
        self.turtle.fd(50)
      self.turtle.left(90)
      self.turtle.fd(50)
      if x%2 != 0:
        self.turtle.end_fill()
      self.turtle.right(90)
      self.turtle.bk(400)
      self.turtle.right(90)
      self.turtle.fd(50)
      self.turtle.pu()
      self.turtle.goto(-225,160-x*50)
      self.turtle.color('wheat')
      self.turtle.write(x+1,font=("Arial", 25, "normal"))
      self.turtle.color('cornsilk')
      if x != 7:
        self.turtle.goto(-200,160-(x+1)*50)
      else:
        self.turtle.goto(-200,160-(x)*50)
      self.turtle.left(90)
      self.turtle.pd()
    self.turtle.fd(400)
    self.turtle.pu()
    l = ['a','b','c','d','e','f','g','h']
    for i in range(8):
      self.turtle.goto(-185+50*i,-230)
      self.turtle.color('wheat')
      self.turtle.write(l[i],font=("Arial", 25, "normal"))
    self.turtle.color('cornsilk')
t = turtle.Turtle()
chessboard = board(t)

class peice:
  def __init__(self,x,y,t,s):
    self.turtle = t
    self.turtle.hideturtle()
    self.side = bool(s)
    self.a = True
    self.poss = ('a','b','c','d','e','f','g','h')
    self.pos = (x-1,self.poss.index(y))
    chessboard.peices[x-1][self.poss.index(y)] = self
    self.turtle.pu()
    self.turtle.speed(10000000000000000)
    if self.side:
      self.turtle.color('black')
      self.turtle.fillcolor('white')
    else:
      self.turtle.color('white')
      self.turtle.fillcolor('black')
    self.turtle.goto(-200+self.poss.index(y)*50,160-(x-1)*50)
    self.turtle.pd()
    self.turtle.goto(-200+self.poss.index(y)*50,160-(x-1)*50)
    
  def move(self,x,y):
    chessboard.peices[self.pos[0]][self.pos[1]] = -1
    self.pos = (x-1,self.poss.index(y))
    chessboard.peices[x-1][self.poss.index(y)] = self
    self.turtle.clear()
    self.turtle.pu()
    
    self.turtle.goto(-200+self.poss.index(y)*50,160-(x-1)*50)
    self.turtle.pd()
  def remove(self):
    self.turtle.clear()
    chessboard.peices[self.pos[0]][self.pos[1]] = -1
    self.a = False

class pawn(peice):
  def __init__(self,x,y,t,s):
    super().__init__(x,y,t,s)
    self.m = False
    self.pm = []
    self.turtle.pu()
    self.turtle.fd(10)
    self.turtle.left(90)
    self.turtle.fd(7)
    self.turtle.pd()
    self.turtle.begin_fill()
    self.turtle.circle(-7,90)
    self.turtle.circle(5,90)
    self.turtle.fd(5)
    self.turtle.setheading(170)
    self.turtle.circle(-10,320)
    self.turtle.setheading(270)
    self.turtle.fd(5)
    self.turtle.circle(5,90)
    self.turtle.circle(-7,90)
    self.turtle.right(90)
    self.turtle.fd(32)
    self.turtle.end_fill()

  def move (self,x,y):
    if self.side and self.pos[0] > 0:
      if chessboard.peices[self.pos[0]-1][self.pos[1]] == -1:
        self.pm.append((self.pos[0]-1,self.pos[1]))
      if self.m == False and chessboard.peices[self.pos[0]-1][self.pos[1]] == -1 and chessboard.peices[self.pos[0]-2][self.pos[1]] == -1:
        self.pm.append((self.pos[0]-2,self.pos[1]))
      if chessboard.peices[self.pos[0]-1][self.pos[1]-1] == -1 and self.pos[1]-1 >= 0:
        self.pm.append((self.pos[0]-1,self.pos[1]-1))
      if chessboard.peices[self.pos[0]-1][self.pos[1]+1] == -1 and self.pos[1]+1 < 7:
        self.pm.append((self.pos[0]-1, self.pos[1]+1))
    if self.side == 0 and self.pos[0] < 7:
      if chessboard.peices[self.pos[0]+1][self.pos[1]] == -1:
        self.pm.append((self.pos[0]+1,self.pos[1]))
      if self.m == False and chessboard.peices[self.pos[0]+1][self.pos[1]] == -1 and chessboard.peices[self.pos[0]+2][self.pos[1]] == -1:
        self.pm.append((self.pos[0]+2,self.pos[1]))
      if chessboard.peices[self.pos[0]+1][self.pos[1]-1] == -1 and self.pos[1]-1 >= 0:
        self.pm.append((self.pos[0]+1,self.pos[1]-1))
      if chessboard.peices[self.pos[0]+1][self.pos[1]+1] == -1 and self.pos[1]+1 < 7:
        self.pm.append((self.pos[0]+1, self.pos[1]+1))
    if (x-1,self.poss.index(y)) in self.pm:
      self.pm.clear()
      super().move(x,y)
      self.turtle.setheading(0)
      self.turtle.pu()
      self.turtle.fd(10)
      self.turtle.left(90)
      self.turtle.fd(7)
      self.turtle.pd()
      self.turtle.begin_fill()
      self.turtle.circle(-7,90)
      self.turtle.circle(5,90)
      self.turtle.fd(5)
      self.turtle.setheading(170)
      self.turtle.circle(-10,320)
      self.turtle.setheading(270)
      self.turtle.fd(5)
      self.turtle.circle(5,90)
      self.turtle.circle(-7,90)
      self.turtle.right(90)
      self.turtle.fd(32)
      self.turtle.end_fill()
      self.m = True
      return True
    else:
      return False
  def checkpm (self,x,y):
    if self.side and self.pos[0] < 7:
      if chessboard.peices[self.pos[0]-1][self.pos[1]] == -1:
        self.pm.append((self.pos[0]-1,self.pos[1]))
      if self.m == False and chessboard.peices[self.pos[0]-1][self.pos[1]] == -1 and chessboard.peices[self.pos[0]-2][self.pos[1]] == -1:
        self.pm.append((self.pos[0]-2,self.pos[1]))
      if chessboard.peices[self.pos[0]-1][self.pos[1]-1] != -1 and self.pos[1]-1 >= 0:
        self.pm.append((self.pos[0]-1,self.pos[1]-1))
      if chessboard.peices[self.pos[0]-1][self.pos[1]+1] != -1 and self.pos[1]+1 < 7:
        self.pm.append((self.pos[0]-1, self.pos[1]+1))
    if self.side == 0 and self.pos[0] < 7:
      if chessboard.peices[self.pos[0]+1][self.pos[1]] == -1:
        self.pm.append((self.pos[0]+1,self.pos[1]))
      if self.m == False and chessboard.peices[self.pos[0]+1][self.pos[1]] == -1 and chessboard.peices[self.pos[0]+2][self.pos[1]] == -1:
        self.pm.append((self.pos[0]+2,self.pos[1]))
      if chessboard.peices[self.pos[0]+1][self.pos[1]-1] != -1 and self.pos[1]-1 >= 0:
        self.pm.append((self.pos[0]+1,self.pos[1]-1))
      if chessboard.peices[self.pos[0]+1][self.pos[1]+1] != -1 and self.pos[1]+1 < 7:
        self.pm.append((self.pos[0]+1, self.pos[1]+1))
    return(x-1,self.poss.index(y)) in self.pm
class rook(peice):
  def __init__(self,x,y,t,s):
    super().__init__(x,y,t,s)
    self.pm = []
    self.m = False
    self.turtle.pu()
    self.turtle.fd(10)
    self.turtle.left(90)
    self.turtle.fd(7)
    self.turtle.pd()
    self.turtle.begin_fill()
    self.turtle.circle(-7,90)
    self.turtle.left(90)
    self.turtle.fd(15)
    self.turtle.left(90)
    self.turtle.fd(7)
    self.turtle.right(90)
    self.turtle.fd(10)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(10)
    self.turtle.right(90)
    self.turtle.fd(7)
    self.turtle.left(90)
    self.turtle.fd(15)
    self.turtle.left(90)
    self.turtle.circle(-7,90)
    self.turtle.setheading(180)
    self.turtle.fd(24)
    self.turtle.end_fill()

  def move(self,x,y):
    for i in range(self.pos[0]-1,-1,-1):
      if chessboard.peices[i][self.pos[1]] == -1:
        self.pm.append((i,self.pos[1]))
      else:
        self.pm.append((i,self.pos[1]))
        break
    for i in range(self.pos[0]+1,8):
      if chessboard.peices[i][self.pos[1]] == -1:
        self.pm.append((i,self.pos[1]))
      else:
        self.pm.append((i,self.pos[1]))
        break
    for i in range(self.pos[1]-1,-1,-1):
      if chessboard.peices[self.pos[0]][i] == -1:
        self.pm.append((self.pos[0],i))
      else:
        self.pm.append((self.pos[0],i))
        break
    for i in range(self.pos[1]+1,8):
      if chessboard.peices[self.pos[0]][i] == -1:
        self.pm.append((self.pos[0],i))
      else:
        self.pm.append((self.pos[0],i))
        break
    if (x-1,self.poss.index(y)) in self.pm:
      self.pm.clear()
      super().move(x,y)
      self.turtle.setheading(0)
      self.turtle.pu()
      self.turtle.fd(10)
      self.turtle.left(90)
      self.turtle.fd(7)
      self.turtle.pd()
      self.turtle.begin_fill()
      self.turtle.circle(-7,90)
      self.turtle.left(90)
      self.turtle.fd(15)
      self.turtle.left(90)
      self.turtle.fd(7)
      self.turtle.right(90)
      self.turtle.fd(10)
      self.turtle.right(90)
      self.turtle.fd(5)
      self.turtle.right(90)
      self.turtle.fd(5)
      self.turtle.left(90)
      self.turtle.fd(5)
      self.turtle.left(90)
      self.turtle.fd(5)
      self.turtle.right(90)
      self.turtle.fd(5)
      self.turtle.right(90)
      self.turtle.fd(5)
      self.turtle.left(90)
      self.turtle.fd(5)
      self.turtle.left(90)
      self.turtle.fd(5)
      self.turtle.right(90)
      self.turtle.fd(5)
      self.turtle.right(90)
      self.turtle.fd(10)
      self.turtle.right(90)
      self.turtle.fd(7)
      self.turtle.left(90)
      self.turtle.fd(15)
      self.turtle.left(90)
      self.turtle.circle(-7,90)
      self.turtle.setheading(180)
      self.turtle.fd(24)
      self.turtle.end_fill()
      self.m = True
      return True
    else:
      return False

  def castle(self,x,y):
    self.pm.clear()
    super().move(x,y)
    self.turtle.setheading(0)
    self.turtle.pu()
    self.turtle.fd(10)
    self.turtle.left(90)
    self.turtle.fd(7)
    self.turtle.pd()
    self.turtle.begin_fill()
    self.turtle.circle(-7,90)
    self.turtle.left(90)
    self.turtle.fd(15)
    self.turtle.left(90)
    self.turtle.fd(7)
    self.turtle.right(90)
    self.turtle.fd(10)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(10)
    self.turtle.right(90)
    self.turtle.fd(7)
    self.turtle.left(90)
    self.turtle.fd(15)
    self.turtle.left(90)
    self.turtle.circle(-7,90)
    self.turtle.setheading(180)
    self.turtle.fd(24)
    self.turtle.end_fill()
    self.m = True

  def checkpm (self,x,y):
    for i in range(self.pos[0]-1,-1,-1):
      if chessboard.peices[i][self.pos[1]] == -1:
        self.pm.append((i,self.pos[1]))
      else:
        self.pm.append((i,self.pos[1]))
        break
    for i in range(self.pos[0]+1,8):
      if chessboard.peices[i][self.pos[1]] == -1:
        self.pm.append((i,self.pos[1]))
      else:
        self.pm.append((i,self.pos[1]))
        break
    for i in range(self.pos[1]-1,-1,-1):
      if chessboard.peices[self.pos[0]][i] == -1:
        self.pm.append((self.pos[0],i))
      else:
        self.pm.append((self.pos[0],i))
        break
    for i in range(self.pos[1]+1,8):
      if chessboard.peices[self.pos[0]][i] == -1:
        self.pm.append((self.pos[0],i))
      else:
        self.pm.append((self.pos[0],i))
        break
    return(x-1,self.poss.index(y)) in self.pm
        
class knight(peice):
  def __init__(self,x,y,t,s):
    super().__init__(x,y,t,s)
    self.pm = []
    self.turtle.pu()
    self.turtle.fd(10)
    self.turtle.left(90)
    self.turtle.fd(7)
    self.turtle.pd()
    self.turtle.begin_fill()
    self.turtle.circle(-7,90)
    self.turtle.setheading(80)
    self.turtle.fd(10)
    self.turtle.circle(10,30)
    self.turtle.circle(1,120)
    self.turtle.fd(10)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.right(75)
    self.turtle.fd(15)
    self.turtle.left(70)
    self.turtle.fd(5)
    self.turtle.right(150)
    self.turtle.fd(7)
    self.turtle.circle(-20,90)
    self.turtle.fd(2)
    self.turtle.setheading(0)
    self.turtle.circle(-7,90)
    self.turtle.right(90)
    self.turtle.fd(25)
    self.turtle.end_fill()

  def move(self,x,y):
    if self.pos[0]-2 >= 0 and self.pos[1]-1 >= 0:
      self.pm.append((self.pos[0]-2,self.pos[1]-1))
    if self.pos[0]-1 >= 0 and self.pos[1]-2 >= 0:
      self.pm.append((self.pos[0]-1,self.pos[1]-2))
    if self.pos[0]-2 >= 0 and self.pos[1]+1 <= 7:
      self.pm.append((self.pos[0]-2,self.pos[1]+1))
    if self.pos[0]-1 >= 0 and self.pos[1]+2 <= 7:
      self.pm.append((self.pos[0]-1,self.pos[1]+2))
    if self.pos[0]+2 <= 7 and self.pos[1]-1 >= 0:
      self.pm.append((self.pos[0]+2,self.pos[1]-1))
    if self.pos[0]+1 <= 7 and self.pos[1]-2 >= 0:
      self.pm.append((self.pos[0]+1,self.pos[1]-2))
    if self.pos[0]+2 <= 7 and self.pos[1]+1 <= 7:
      self.pm.append((self.pos[0]+2,self.pos[1]+1))
    if self.pos[0]+1 <= 7 and self.pos[1]+2 <= 7:
      self.pm.append((self.pos[0]+1,self.pos[1]+2))
    if (x-1,self.poss.index(y)) in self.pm:
      self.pm.clear()
      super().move(x,y)
      self.turtle.setheading(0)
      self.turtle.pu()
      self.turtle.fd(10)
      self.turtle.left(90)
      self.turtle.fd(7)
      self.turtle.pd()
      self.turtle.begin_fill()
      self.turtle.circle(-7,90)
      self.turtle.setheading(80)
      self.turtle.fd(10)
      self.turtle.circle(10,30)
      self.turtle.circle(1,120)
      self.turtle.fd(10)
      self.turtle.right(90)
      self.turtle.fd(5)
      self.turtle.right(75)
      self.turtle.fd(15)
      self.turtle.left(70)
      self.turtle.fd(5)
      self.turtle.right(150)
      self.turtle.fd(7)
      self.turtle.circle(-20,90)
      self.turtle.fd(2)
      self.turtle.setheading(0)
      self.turtle.circle(-7,90)
      self.turtle.right(90)
      self.turtle.fd(25)
      self.turtle.end_fill()
      return True
    else:
      return False

  def checkpm(self,x,y):
    if self.pos[0]-2 >= 0 and self.pos[1]-1 >= 0:
      self.pm.append((self.pos[0]-2,self.pos[1]-1))
    if self.pos[0]-1 >= 0 and self.pos[1]-2 >= 0:
      self.pm.append((self.pos[0]-1,self.pos[1]-2))
    if self.pos[0]-2 >= 0 and self.pos[1]+1 <= 7:
      self.pm.append((self.pos[0]-2,self.pos[1]+1))
    if self.pos[0]-1 >= 0 and self.pos[1]+2 <= 7:
      self.pm.append((self.pos[0]-1,self.pos[1]+2))
    if self.pos[0]+2 <= 7 and self.pos[1]-1 >= 0:
      self.pm.append((self.pos[0]+2,self.pos[1]-1))
    if self.pos[0]+1 <= 7 and self.pos[1]-2 >= 0:
      self.pm.append((self.pos[0]+1,self.pos[1]-2))
    if self.pos[0]+2 <= 7 and self.pos[1]+1 <= 7:
      self.pm.append((self.pos[0]+2,self.pos[1]+1))
    if self.pos[0]+1 <= 7 and self.pos[1]+2 <= 7:
      self.pm.append((self.pos[0]+1,self.pos[1]+2))
    return(x-1,self.poss.index(y)) in self.pm

class bishop(peice):
  def __init__(self,x,y,t,s):
    super().__init__(x,y,t,s)
    self.pm = []
    self.turtle.pu()
    self.turtle.fd(10)
    self.turtle.left(90)
    self.turtle.fd(7)
    self.turtle.pd()
    self.turtle.begin_fill()
    self.turtle.circle(-7,90)
    self.turtle.setheading(150)
    self.turtle.circle(-15,90)
    self.turtle.fd(10)
    self.turtle.circle(-5,90)
    self.turtle.setheading(270)
    self.turtle.fd(15)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(10)
    self.turtle.setheading(320)
    self.turtle.circle(-15,80)
    self.turtle.fd(8)
    self.turtle.setheading(0)
    self.turtle.circle(-7,90)
    self.turtle.right(90)
    self.turtle.fd(25)
    self.turtle.end_fill()

  def move(self,x,y):
    for i in range(1,min(self.pos[0]+1,self.pos[1]+1)):
      if chessboard.peices[self.pos[0]-i][self.pos[1]-i] == -1:
        self.pm.append((self.pos[0]-i,self.pos[1]-i))
      else:
        self.pm.append((self.pos[0]-i,self.pos[1]-i))
        break
    for i in range(1,min(self.pos[0]+1,8-self.pos[1])):
      if chessboard.peices[self.pos[0]-i][self.pos[1]+i] == -1:
        self.pm.append((self.pos[0]-i,self.pos[1]+i))
      else:
        self.pm.append((self.pos[0]-i,self.pos[1]+i))
        break
    for i in range(1,min(8-self.pos[0],self.pos[1]+1)):
      if chessboard.peices[self.pos[0]+i][self.pos[1]-i] == -1:
        self.pm.append((self.pos[0]+i,self.pos[1]-i))
      else:
        self.pm.append((self.pos[0]+i,self.pos[1]-i))
        break
    for i in range(1,min(8-self.pos[0],8-self.pos[1])):
      if chessboard.peices[self.pos[0]+i][self.pos[1]+i] == -1:
        self.pm.append((self.pos[0]+i,self.pos[1]+i))
      else:
        self.pm.append((self.pos[0]+i,self.pos[1]+i))
        break
    if (x-1,self.poss.index(y)) in self.pm:
      self.pm.clear()
      super().move(x,y)
      self.turtle.setheading(0)
      self.turtle.pu()
      self.turtle.fd(10)
      self.turtle.left(90)
      self.turtle.fd(7)
      self.turtle.pd()
      self.turtle.begin_fill()
      self.turtle.circle(-7,90)
      self.turtle.setheading(150)
      self.turtle.circle(-15,90)
      self.turtle.fd(10)
      self.turtle.circle(-5,90)
      self.turtle.setheading(270)
      self.turtle.fd(15)
      self.turtle.left(90)
      self.turtle.fd(5)
      self.turtle.left(90)
      self.turtle.fd(10)
      self.turtle.setheading(320)
      self.turtle.circle(-15,80)
      self.turtle.fd(8)
      self.turtle.setheading(0)
      self.turtle.circle(-7,90)
      self.turtle.right(90)
      self.turtle.fd(25)
      self.turtle.end_fill()
      return True
    else:
      return False

  def checkpm(self,x,y):
    for i in range(1,min(self.pos[0]+1,self.pos[1]+1)):
      if chessboard.peices[self.pos[0]-i][self.pos[1]-i] == -1:
        self.pm.append((self.pos[0]-i,self.pos[1]-i))
      else:
        self.pm.append((self.pos[0]-i,self.pos[1]-i))
        break
    for i in range(1,min(self.pos[0]+1,8-self.pos[1])):
      if chessboard.peices[self.pos[0]-i][self.pos[1]+i] == -1:
        self.pm.append((self.pos[0]-i,self.pos[1]+i))
      else:
        self.pm.append((self.pos[0]-i,self.pos[1]+i))
        break
    for i in range(1,min(8-self.pos[0],self.pos[1]+1)):
      if chessboard.peices[self.pos[0]+i][self.pos[1]-i] == -1:
        self.pm.append((self.pos[0]+i,self.pos[1]-i))
      else:
        self.pm.append((self.pos[0]+i,self.pos[1]-i))
        break
    for i in range(1,min(8-self.pos[0],8-self.pos[1])):
      if chessboard.peices[self.pos[0]+i][self.pos[1]+i] == -1:
        self.pm.append((self.pos[0]+i,self.pos[1]+i))
      else:
        self.pm.append((self.pos[0]+i,self.pos[1]+i))
        break
    return(x-1,self.poss.index(y)) in self.pm

class queen(peice):
  def __init__(self,x,y,t,s):
    super().__init__(x,y,t,s)
    self.pm = []
    self.turtle.pu()
    self.turtle.fd(10)
    self.turtle.left(90)
    self.turtle.fd(7)
    self.turtle.pd()
    self.turtle.begin_fill()
    self.turtle.circle(-7,90)
    self.turtle.left(110)
    self.turtle.fd(23)
    self.turtle.left(90)
    self.turtle.circle(-2,340)
    self.turtle.left(90)
    self.turtle.fd(15)
    self.turtle.left(130)
    self.turtle.fd(15)
    self.turtle.left(90)
    self.turtle.circle(-2,340)
    self.turtle.left(90)
    self.turtle.fd(15)
    self.turtle.left(130)
    self.turtle.fd(15)
    self.turtle.left(90)
    self.turtle.circle(-2,340)
    self.turtle.left(90)
    self.turtle.fd(23)
    self.turtle.setheading(0)
    self.turtle.circle(-7,90)
    self.turtle.right(90)
    self.turtle.fd(25)
    self.turtle.end_fill()

  def move(self,x,y):
    for i in range(self.pos[0]-1,-1,-1):
      if chessboard.peices[i][self.pos[1]] == -1:
        self.pm.append((i,self.pos[1]))
      else:
        self.pm.append((i,self.pos[1]))
        break
    for i in range(self.pos[0]+1,8):
      if chessboard.peices[i][self.pos[1]] == -1:
        self.pm.append((i,self.pos[1]))
      else:
        self.pm.append((i,self.pos[1]))
        break
    for i in range(self.pos[1]-1,-1,-1):
      if chessboard.peices[self.pos[0]][i] == -1:
        self.pm.append((self.pos[0],i))
      else:
        self.pm.append((self.pos[0],i))
        break
    for i in range(self.pos[1]+1,8):
      if chessboard.peices[self.pos[0]][i] == -1:
        self.pm.append((self.pos[0],i))
      else:
        self.pm.append((self.pos[0],i))
        break
    for i in range(1,min(self.pos[0]+1,self.pos[1]+1)):
      if chessboard.peices[self.pos[0]-i][self.pos[1]-i] == -1:
        self.pm.append((self.pos[0]-i,self.pos[1]-i))
      else:
        self.pm.append((self.pos[0]-i,self.pos[1]-i))
        break
    for i in range(1,min(self.pos[0]+1,8-self.pos[1])):
      if chessboard.peices[self.pos[0]-i][self.pos[1]+i] == -1:
        self.pm.append((self.pos[0]-i,self.pos[1]+i))
      else:
        self.pm.append((self.pos[0]-i,self.pos[1]+i))
        break
    for i in range(1,min(8-self.pos[0],self.pos[1]+1)):
      if chessboard.peices[self.pos[0]+i][self.pos[1]-i] == -1:
        self.pm.append((self.pos[0]+i,self.pos[1]-i))
      else:
        self.pm.append((self.pos[0]+i,self.pos[1]-i))
        break
    for i in range(1,min(8-self.pos[0],8-self.pos[1])):
      if chessboard.peices[self.pos[0]+i][self.pos[1]+i] == -1:
        self.pm.append((self.pos[0]+i,self.pos[1]+i))
      else:
        self.pm.append((self.pos[0]+i,self.pos[1]+i))
        break
    if (x-1,self.poss.index(y)) in self.pm:
      self.pm.clear()
      super().move(x,y)
      self.turtle.setheading(0)
      self.turtle.pu()
      self.turtle.fd(10)
      self.turtle.left(90)
      self.turtle.fd(7)
      self.turtle.pd()
      self.turtle.begin_fill()
      self.turtle.circle(-7,90)
      self.turtle.left(110)
      self.turtle.fd(23)
      self.turtle.left(90)
      self.turtle.circle(-2,340)
      self.turtle.left(90)
      self.turtle.fd(15)
      self.turtle.left(130)
      self.turtle.fd(15)
      self.turtle.left(90)
      self.turtle.circle(-2,340)
      self.turtle.left(90)
      self.turtle.fd(15)
      self.turtle.left(130)
      self.turtle.fd(15)
      self.turtle.left(90)
      self.turtle.circle(-2,340)
      self.turtle.left(90)
      self.turtle.fd(23)
      self.turtle.setheading(0)
      self.turtle.circle(-7,90)
      self.turtle.right(90)
      self.turtle.fd(25)
      self.turtle.end_fill()
      return True
    else:
      return False

  def checkpm(self,x,y):
    for i in range(self.pos[0]-1,-1,-1):
      if chessboard.peices[i][self.pos[1]] == -1:
        self.pm.append((i,self.pos[1]))
      else:
        self.pm.append((i,self.pos[1]))
        break
    for i in range(self.pos[0]+1,8):
      if chessboard.peices[i][self.pos[1]] == -1:
        self.pm.append((i,self.pos[1]))
      else:
        self.pm.append((i,self.pos[1]))
        break
    for i in range(self.pos[1]-1,-1,-1):
      if chessboard.peices[self.pos[0]][i] == -1:
        self.pm.append((self.pos[0],i))
      else:
        self.pm.append((self.pos[0],i))
        break
    for i in range(self.pos[1]+1,8):
      if chessboard.peices[self.pos[0]][i] == -1:
        self.pm.append((self.pos[0],i))
      else:
        self.pm.append((self.pos[0],i))
        break
    for i in range(1,min(self.pos[0]+1,self.pos[1]+1)):
      if chessboard.peices[self.pos[0]-i][self.pos[1]-i] == -1:
        self.pm.append((self.pos[0]-i,self.pos[1]-i))
      else:
        self.pm.append((self.pos[0]-i,self.pos[1]-i))
        break
    for i in range(1,min(self.pos[0]+1,8-self.pos[1])):
      if chessboard.peices[self.pos[0]-i][self.pos[1]+i] == -1:
        self.pm.append((self.pos[0]-i,self.pos[1]+i))
      else:
        self.pm.append((self.pos[0]-i,self.pos[1]+i))
        break
    for i in range(1,min(8-self.pos[0],self.pos[1]+1)):
      if chessboard.peices[self.pos[0]+i][self.pos[1]-i] == -1:
        self.pm.append((self.pos[0]+i,self.pos[1]-i))
      else:
        self.pm.append((self.pos[0]+i,self.pos[1]-i))
        break
    for i in range(1,min(8-self.pos[0],8-self.pos[1])):
      if chessboard.peices[self.pos[0]+i][self.pos[1]+i] == -1:
        self.pm.append((self.pos[0]+i,self.pos[1]+i))
      else:
        self.pm.append((self.pos[0]+i,self.pos[1]+i))
        break
    return(x-1,self.poss.index(y)) in self.pm

class king(peice):
  def __init__(self,x,y,t,s):
    super().__init__(x,y,t,s)
    self.pm = []
    self.m = False
    self.turtle.pu()
    self.turtle.fd(10)
    self.turtle.left(90)
    self.turtle.fd(7)
    self.turtle.pd()
    self.turtle.begin_fill()
    self.turtle.circle(-7,90)
    self.turtle.fd(1)
    self.turtle.setheading(180)
    self.turtle.circle(-8,180)
    self.turtle.setheading(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.right(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.fd(5)
    self.turtle.left(90)
    self.turtle.circle(-8,180)
    self.turtle.fd(1)
    self.turtle.setheading(0)
    self.turtle.circle(-7,90)
    self.turtle.right(90)
    self.turtle.fd(20)
    self.turtle.end_fill()

  def move(self,x,y):
    if self.pos[0] > 0 and self.pos[1] > 0:
      self.pm.append((self.pos[0]-1,self.pos[1]-1))
    if self.pos[0] > 0:
      self.pm.append((self.pos[0]-1,self.pos[1]))
    if self.pos[0] > 0 and self.pos[1] < 7:
      self.pm.append((self.pos[0]-1,self.pos[1]+1))
    if self.pos[1] > 0:
      self.pm.append((self.pos[0],self.pos[1]-1))
    if self.pos[1] < 7:
      self.pm.append((self.pos[0],self.pos[1]+1))
    if self.pos[0] < 7 and self.pos[1] > 0:
      self.pm.append((self.pos[0]+1,self.pos[1]-1))
    if self.pos[0] < 7:
      self.pm.append((self.pos[0]+1,self.pos[1]))
    if self.pos[0] < 7 and self.pos[1] < 7:
      self.pm.append((self.pos[0]+1,self.pos[1]+1))
    if self.m == False:
      if chessboard.peices[self.pos[0]][self.pos[1]-2]:
        self.pm.append((self.pos[0],self.pos[1]-2))
      if chessboard.peices[self.pos[0]][self.pos[1]+2]:
        self.pm.append((self.pos[0],self.pos[1]+2))
    if (x-1,self.poss.index(y)) in self.pm:
      self.pm.clear()
      super().move(x,y)
      self.turtle.setheading(0)
      self.turtle.pu()
      self.turtle.fd(10)
      self.turtle.left(90)
      self.turtle.fd(7)
      self.turtle.pd()
      self.turtle.begin_fill()
      self.turtle.circle(-7,90)
      self.turtle.fd(1)
      self.turtle.setheading(180)
      self.turtle.circle(-8,180)
      self.turtle.setheading(90)
      self.turtle.fd(5)
      self.turtle.left(90)
      self.turtle.fd(5)
      self.turtle.right(90)
      self.turtle.fd(5)
      self.turtle.right(90)
      self.turtle.fd(5)
      self.turtle.left(90)
      self.turtle.fd(5)
      self.turtle.right(90)
      self.turtle.fd(5)
      self.turtle.right(90)
      self.turtle.fd(5)
      self.turtle.left(90)
      self.turtle.fd(5)
      self.turtle.right(90)
      self.turtle.fd(5)
      self.turtle.right(90)
      self.turtle.fd(5)
      self.turtle.left(90)
      self.turtle.fd(5)
      self.turtle.left(90)
      self.turtle.circle(-8,180)
      self.turtle.fd(1)
      self.turtle.setheading(0)
      self.turtle.circle(-7,90)
      self.turtle.right(90)
      self.turtle.fd(20)
      self.turtle.end_fill()
      self.m = True
      return True
    else:
      return False

  def checkpm(self,x,y):
    if self.pos[0] > 0 and self.pos[1] > 0:
      self.pm.append((self.pos[0]-1,self.pos[1]-1))
    if self.pos[0] > 0:
      self.pm.append((self.pos[0]-1,self.pos[1]))
    if self.pos[0] > 0 and self.pos[1] < 7:
      self.pm.append((self.pos[0]-1,self.pos[1]+1))
    if self.pos[1] > 0:
      self.pm.append((self.pos[0],self.pos[1]-1))
    if self.pos[1] < 7:
      self.pm.append((self.pos[0],self.pos[1]+1))
    if self.pos[0] < 7 and self.pos[1] > 0:
      self.pm.append((self.pos[0]+1,self.pos[1]-1))
    if self.pos[0] < 7:
      self.pm.append((self.pos[0]+1,self.pos[1]))
    if self.pos[0] < 7 and self.pos[1] < 7:
      self.pm.append((self.pos[0]+1,self.pos[1]+1))
    if self.m == False:
      if chessboard.peices[self.pos[0]][self.pos[1]-2]:
        self.pm.append((self.pos[0],self.pos[1]-2))
      if chessboard.peices[self.pos[0]][self.pos[1]+2]:
        self.pm.append((self.pos[0],self.pos[1]+2))
    return(x-1,self.poss.index(y)) in self.pm
      
#start up
tp11 = turtle.Turtle()
p11 = pawn(7,'a',tp11,1)
tp21 = turtle.Turtle()
p21 = pawn(7,'b',tp21,1)
tp31 = turtle.Turtle()
p31 = pawn(7,'c',tp31,1)
tp41 = turtle.Turtle()
p41 = pawn(7,'d',tp41,1)
tp51 = turtle.Turtle()
p51 = pawn(7,'e',tp51,1)
tp61 = turtle.Turtle()
p61 = pawn(7,'f',tp61,1)
tp71 = turtle.Turtle()
p71 = pawn(7,'g',tp71,1)
tp81 = turtle.Turtle()
p81 = pawn(7,'h',tp81,1)
tr11 = turtle.Turtle()
r11 = rook(8,'a',tr11,1)
tr21 = turtle.Turtle()
r21 = rook(8,'h',tr21,1)
tk11 = turtle.Turtle()
k11 = knight(8,'b',tk11,1)
tk21 = turtle.Turtle()
k21 = knight(8,'g',tk21,1)
tb11 = turtle.Turtle()
b11 = bishop(8,'c',tb11,1)
tb21 = turtle.Turtle()
b21 = bishop(8,'f',tb21,1)
tq1 = turtle.Turtle()
q1 = queen(8,'d',tq1,1)
tki1 = turtle.Turtle()
ki1 = king(8,'e',tki1,1)

tp12 = turtle.Turtle()
p12 = pawn(2,'a',tp12,0)
tp22 = turtle.Turtle()
p22 = pawn(2,'b',tp22,0)
tp32 = turtle.Turtle()
p32 = pawn(2,'c',tp32,0)
tp42 = turtle.Turtle()
p42 = pawn(2,'d',tp42,0)
tp52 = turtle.Turtle()
p52 = pawn(2,'e',tp52,0)
tp62 = turtle.Turtle()
p62 = pawn(2,'f',tp62,0)
tp72 = turtle.Turtle()
p72 = pawn(2,'g',tp72,0)
tp82 = turtle.Turtle()
p82 = pawn(2,'h',tp82,0)
tr12 = turtle.Turtle()
r12 = rook(1,'a',tr12,0)
tr22 = turtle.Turtle()
r22 = rook(1,'h',tr22,0)
tk12 = turtle.Turtle()
k12 = knight(1,'b',tk12,0)
tk22 = turtle.Turtle()
k22 = knight(1,'g',tk22,0)
tb12 = turtle.Turtle()
b12 = bishop(1,'c',tb12,0)
tb22 = turtle.Turtle()
b22 = bishop(1,'f',tb22,0)
tq2 = turtle.Turtle()
q2 = queen(1,'d',tq2,0)
tki2 = turtle.Turtle()
ki2 = king(1,'e',tki2,0)

#game proccess
turn = 1
poss = ('a','b','c','d','e','f','g','h')
while(ki1.a and ki2.a):
  if turn == 1:
    print("White's turn")
  else:
    print("Black's turn")
  print('Possible peices positions: ',end='')
  for i in range(8):
    for e in range(8):
      if chessboard.peices[i][e] != -1:
        if chessboard.peices[i][e].side == turn:
          print(str(i+1)+poss[e],end=' ')
  print('')
  p = input('Position of selected piece(e.g. 7a): ')
  p = (int(p[0])-1,poss.index(p[1]))
  print("Possible moves: ",end='')
  chessboard.peices[p[0]][p[1]].checkpm(1,'a')
  for i in range(len(chessboard.peices[p[0]][p[1]].pm)):
    print(str(chessboard.peices[p[0]][p[1]].pm[i][0]+1)+poss[chessboard.peices[p[0]][p[1]].pm[i][1]],end=" ")
  print('')
  m = input('Move to (e.g 2c): ')
  if chessboard.peices[int(p[0])][p[1]].checkpm(int(m[0]),m[1]):
    if chessboard.peices[int(m[0])-1][poss.index(m[1])] != -1:
      if chessboard.peices[int(m[0])-1][poss.index(m[1])].side != turn:
        chessboard.peices[int(m[0])-1][poss.index(m[1])].remove()
        chessboard.peices[p[0]][p[1]].move(int(m[0]),m[1])
    else:
      if type(chessboard.peices[p[0]][p[1]]) is king:
        if int(m[0])-1 == chessboard.peices[p[0]][p[1]].pos[0] and poss.index(m[1])+4 == chessboard.peices[p[0]][p[1]].pos[1] and chessboard.peices[p[0]][p[1]].side == 1 and chessboard.peices[7][0].m == False:
          chessboard.peices[7][0].castle(8,'d')
        if int(m[0])-1 == chessboard.peices[p[0]][p[1]].pos[0] and poss.index(m[1])-3 == chessboard.peices[p[0]][p[1]].pos[1] and chessboard.peices[p[0]][p[1]].side == 1 and chessboard.peices[7][7].m == False:
          chessboard.peices[7][7].castle(8,'f')
        if int(m[0])-1 == chessboard.peices[p[0]][p[1]].pos[0] and poss.index(m[1])+4 == chessboard.peices[p[0]][p[1]].pos[1] and chessboard.peices[p[0]][p[1]].side == 0 and chessboard.peices[0][0].m == False:
          chessboard.peices[0][0].castle(0,'d')
        if int(m[0])-1 == chessboard.peices[p[0]][p[1]].pos[0] and poss.index(m[1])-3 == chessboard.peices[p[0]][p[1]].pos[1] and chessboard.peices[p[0]][p[1]].side == 1 and chessboard.peices[0][7].m == False:
          chessboard.peices[0][7].castle(0,'f')
      
      if chessboard.peices[p[0]][p[1]].move(int(m[0]),m[1]):
        if turn == 1:
          turn = 0
        else:
          turn = 1
      else:
        print('invalid movement')
        
    