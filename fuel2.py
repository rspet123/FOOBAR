
#While I was working on the BFS solution, I noticed a few "rules" in the problem
#Such as:
# if the number is even, ALWAYS divide
# if the number is 3 or 

import time
def solution(num):
  try:
      num = int(num) #Make our string an int, easy
  except Exception:
      return -1
  if num <= 0:
      return -1
  depth=0
  while num != 1:
      num = int(num)
      if num & 1 ==0:
          # We can check if our number is currently even, 
          # if so, the best solution is always to divide by 2
          # we can accomplish this quickly by bitshifting left
          num >>= 1
      elif((num == 3) or (num % 4 ==1 )): 
          # if we can easily make this into an even number, we do so
          # by subtracting 1
          num -= 1
      else:
          # if all else fails, we'll add one, since this is the only move that 
          # numerically moves us "away" from 1
          num += 1
      depth+=1
  return depth
    
    

gr = solution('4h') #2 
z = solution('-1') #2 
q = solution('0') #2    
a = solution('4') #2
b = solution('15') #5
c = solution('2') #1
d = solution('3') #2
t = time.time()
e = solution('1681') #14
print(time.time() - t)
t = time.time()
f = solution('16811') #19
print(time.time() - t)
t = time.time()
h = solution('16343442452') #44
print(time.time() - t)
t = time.time()
k = solution('16343443244441322555555555443243243234234444444444424777777756752') #284, 1.26s
print(time.time() - t)