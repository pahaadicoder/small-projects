#Write your code below this row 👇
for n in range(1,101):
  if n%3==0:
   print("Fizz")
   if n%5==0:
     print("Fizz Buzz")
  elif n%5==0:
    print("Buzz")
  else:
    print(n)
    