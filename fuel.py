#The first thing that came to mind when I saw this problem was to use a BFS to solve it
#Unfortunatly, that ended up being too slow, as it was sort of a brute force solution

import time
def solution(num):
    try:
        num = int(num)
    except Exception:
        return -1
    if num <= 0:
        return -1
    #bfs???
    bfs_q = []
    bfs_q.append((num,0))
    
    while bfs_q:
        curr = bfs_q.pop(0)
        #bfs_q.sort()
        if curr[0] == 1:
            return curr[1]
        depth = curr[1]
        num = curr[0]
        if num & 1 == 0:
            bfs_q.append(((num >>1),depth+1))
        else:
            bfs_q.append(((num+1),depth+1))
            bfs_q.append(((num-1),depth+1))


gr = solution('4h') #2 
z = solution('-1') #2 
q = solution('0') #2    
a = solution('4') #2
b = solution('15') #5
c = solution('2') #1
d = solution('3') #2
t = time.time()
e = solution('1681') #14, 0.00000000s
print(time.time() - t)
t = time.time()
f = solution('16811') #19, 0.0010013s
print(time.time() - t)
t = time.time()
h = solution('16343442452') #44, 1.26s
print(time.time() - t)