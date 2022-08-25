# Hurdle 2 - Working with While Loops
def turn_right():
  turn_left()
  turn_left()
  turn_left()  
def jump():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()
# while at_goal != True:
#  jump()
while not at_goal():
  jump()
  
'''
for loops are really great when you want to iterate over something and you need to do something with each thing that you are iterating over. 
while loops are better when you don't really care what number in a sequence you're in, which item you're iterating through in a list and you just simply want to carry out some sort of functionality many, many, many times until some sort of condition that you set is met. 
# alert: While loops are more dangerous than for loops, because in for loops, you're setting ahead of time how many times something is going to run. It's going to stop once it reaches the end of the list of items in that particular case or once it reaches the upper bound of the range it's in. However, while loops will continue to run until a particular condition switches to false. So, if you have some sort of condition that never becomes false, well then the while loops becomes something known as an infinite loop. 
'''