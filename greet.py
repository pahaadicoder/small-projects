#Write your code below this line 👇
import math

def number_of_can(height,width,cover):
  area= height * width
  can=(math.ceil(area/cover))
  print(can)
h= int(input("what is the height of the wall:?\n"))
w= int(input("what is the width of the wall:?\n"))
coverage=5
number_of_can(height=h, width=w, cover=coverage)


