# bounce.py
#
# Exercise 1.5
height = 100
number = 0
while(number < 10):
    height = height * (3/5)
    print(f" {number+1} {round(height,4)}")
    number += 1