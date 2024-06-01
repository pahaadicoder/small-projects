HACKERRANK
USE "ASKPYTHON.COM" FOR FURTHER QUIERIES AND DOUBTS.
#double quote basically shows begining and end of the characters (its not code just some text that i want to print out!)
#just when u get a syntax error just copy it and paste it on google (stackoverallflow.com)
#syntax highlighting
#in python spaces are much important(indentation error)
#program 1st letter always counted as 0

#we can write codes on new line using [/n {key above enter key}] after one line instead of using print command in seperate lines.
print("hi how are u ?\nim fine thank you")
#if u want to add space b/w strings there are 3 ways:-(1st string + " "+ 2nd string)easiest one.


#input( ) this function gives prompt to user to type in some piece of data.
print("hello"+input("what is your name ? "))

#use of variables help us to refer the function later on .(for eg-)
name= input('what is your name?')
length= len(name)
print(length)
#try to name your variables clearly (and it should be a single unit)so u can know there functionality easily
#data types-(string,integer,float,boolean)
#anything inside double quotes("") is treated as a string by the python.and instead of using (,)we use (_)I.E- instead of saying 4,748,3893 we type 4_748_3893 for a user to read them easily.
 #FLOAT- use of a decimal inside the integer i.e- 464.7565 or 3.14159
 #boolean- to check whether a condition is true/false for a computer and how he responds upon it.
 #TypeError is raised whenever an operation is performed on an incorrect/unsupported object type. For example, using the + (addition) operator on a string and an integer value will raise TypeError.


#MATHS-
#PEMDAS - stands for (Parenthesis,Exponents(**),Multiplication(*),Division,Addition & Subtraction)respectively.
#round is  used to round off a float no.
print(round(9/4,2))
score =0
# score +=1 (it means score + 1) than after writing print(score) . your output will be 1.
fstring{} #if u want to use integer+bool+float without changing each other into a single sting.
score= 0
grade= 8.9
is_swimming= True
# f-strings
print(f"your score is {score},your height is {grade},you are {is_swimming} genius")
#==,>=,<=,=!
#% = remainder
# Logical Operations- and, or & not.
# and(*), or(+), not(reverse)
if (score<10) or (score>90):
  print(f"Your score is {score}, you go together like coke and mentos.")
a=9
not a>10
true
.........................................................................
#The count() function will give you the number of times a letter occurs in a string.
"Angela".lower()
"angela"
'angela'. count('a')
2
#the lower() function reduces all the characters in lowercase.
#The escape codes are entered right into the print statement.
............................................................................
#to use art
print("\033[1;35;40m Bright Green  \n")
('''   /^^^^^^^\
       |  $  $ |
       |  ---- |
       |    O  |
        \______/     ''')
#The above ANSI escape code will set the text colour to bright green. The format is;
#\033[  Escape code, this is always the same
1 = Style, 1 for normal.
32 = Text colour, 32 for bright green.
40m = Background colour, 40 is for black.

  print("\033[1;34;40m Bright Green  \n")

This table shows some of the available formats;

TEXT COLOR	CODE	TEXT STYLE	CODE	BACKGROUND COLOR	CODE
Black	30	No effect	0	Black	40
Red	31	Bold	1	Red	41
Green	32	Underline	2	Green	42
Yellow	33	Negative1	3	Yellow	43
Blue	34	Negative2	5	Blue	44
Purple	35			Purple	45
Cyan	36			Cyan	46
White	37			White	47
..........................................................................
#RANDOM NUMBERS
import RANDOM
# randint function is used to generate a random no. b/w two numbers.
import RANDOM
random_integer= random.randit(1,10)
print(random_integer)
#each module is responsible for a particular section.

#we can make a seperate file and just import that file in python using import function and typing the file name.
import
random_float = random.random()
print(random_float)
........................................................................
#ASCII ART- for pics in program
.............................................................
# PYTHON LIST- LIST IS A DATA STRUCTURE IT IS A TYPE OF STORING TYPES OF DATA
LIST ALWAYS STAR AND END with A BRACKET[] SEPERATED BY COMMAS ,
LIST IS MADE SEQUENTIAL
LIST = SQUARE BRACKET
LIST SEQUENCE CAN BE REWRITED(ADD, CHANGESEQUENCE)
#APPEND- TO ADD SOMETHING IN THE END OF LIST
#APPEND, EXTEND, INSERT,REMOVE, POP, COUNT , SERVE('DON'T MEMORISE)
# choice it helps in returning a random item from either a list,tupleor string.
import random
list=['1', '2', '3', '4', '5']
print(list[1])
print(random.choice(list))
SPLIT COMMAND IS USED TO MAKE A STRING INTO SPLIT.
split- (",")
to make something like this ("arpit,is,a good boy")  into ['arpit', 'is', 'a good boy']
LIST1= ['a', 'b', 'c']
list2= ['d', 'e', 'f']
lister= ['LIST1', 'list2']
lister= [['a', 'b', 'c'], ['d', 'e', 'f']]
print(lister[0][2])
*********************************************************************************************************
ALWAYS CHECK HOW THE PYTHON is taking input - 2/'2'/"2"
*************************************************************************************************
#LOOPS-
#FOR LOOPS- DO SOMETHING FOR EACH INDIVIDIUAL ITEM
FRUITS=["Apple", "Peach", "Pear"],
for fruit in fruits:
    print(fruit)
    print(fruit+"pie"
for loops run as many as time the no. of items on the list
# to calculate length without using len( ) function :-
total_students= 0
for length in student_heights:
  total_students+=1
print(total_students)
 # to calculate the sum of an list without using the sum() function :-
total_height=0
 total_height= total_height + height
 or we can write it as- total_height += height
print(total_height)
*******************************************************************************
for n in range(0, len(student_heights)):
student_heights[n] = int(student_heights[n])
*******************************************************************************
#let suppose
total_height= total_height + height
or we can write it as- total_height += total_height
###########################################################################
using for loop with range functionality
for number in range(1,10)# NOTE:   here - 1 = start point and 10 is end point means it will not orint 10 and stop the command on 9
for number in range(1,100,3) here 3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#function- gives us A WAy to bundle all the instuctions in a one package.
TO make our own function-
1- start using "def" keyword
2- give function a name
3- give function paranthesis (diiferentiata a function from a variable)
4- give a colon at end so everything that comes after line indented/belongs to the function.

i.e- def my_app():                                       PROPER indentation IS MUST
      print("what")
      print("the hell!")
input- my_app()         -------- THIS IS CALLED "CALLING THE FUNCTION" (NAME AND SET OF PARENTHESIS WITH COLON)
output- what the hell!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TO MAKE A STRING INTO A LIST OF ITS characters.
animals=["cow","buffalow","giraffe","sheep","dog","lion","tiger","horse","rabbit"]
pc=random.choice(animals)
free_pc=list(pc)
INPUT- "RABBIT"
OUTPUT-["R","A","B","B","I","T"]
#############################################################################3
lowecase- keyword.lower()
############################################################################
#functions with INPUT
input-
def greet_with_name(name):
    print("how u doing{name}")
    print('what the hell is going on{name}')
greet_with_name(arpit)
output- how u doing arpit
        what the hell is going on arpit?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def how_u_doing(name,location):
    print(f"my name is {name}")
    print(f'i study in {location}')
#POSITIONAL ARGUMENT- IF U SWITCH THE ORDER OF VARIABLES FOR EX- LOCATION,name
you can also set the parameter=fixed input (i.e- name="Angelaf")
