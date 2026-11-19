def code():
  for i in range(3):
    for j in range(4):
      print("*",end=" ")
    print(" ")
code()


def code():
  for i in range(5):
    for j in range(4):
      if   i==2  or j==0 or  j==3:
        print("*",end=" ")
      else:
        print(" " , end=" ")
    print(" ")
code()
#i is row , j is column


def code ():
  for i in range(5):
    for j in range(5):
      if i+j==4  :
        print('*',end=" ")
      else:
        print(' ', end= " ")
    print(" ")
code()



def code ():
  x=0
  for i in range(6):
    x+=1 #x=0+1=1*
    for j in range(x):
      
      print('*' , end = " ")
    print(" ")
code()



def code ():
  x=6
  for i in range(6):
    x-=1 #x=0+1=1*
    for j in range(x):  
      print('*' , end = " ")
    print(" ")
code()




def code ():
  x=6
  for i in range(6):
    x-=1 #x=0+1=1*
    for j in range(x):  
      if i==1 and j==2:
        print('@',end=" ")
      elif  i==3 and j==0:
        print('$', end=" ")
      else:
        print('*' , end = " ")
    print(" ")
code()




def code():
  s=0
  sp=5
  for i in range(5):
    s+=1
    sp-=1
    for j in range(sp):
      print(" ",end=" ")
    for k in range(s):
      print("*",end=" ")
    print(" ")
code()


def code ():
  st=-1
  sp=5
  for i in range(6):
    for j in range(sp):
      print(" ",end=" ")
    for k in range(st):
      print("*",end=" ")
    print()
    st+=2
    sp-=1
code()

