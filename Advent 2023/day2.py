import re
from util import get_input2
from functools import reduce

def a():
    ans = 0
    d = {'red': 12, 'green': 13, 'blue': 14}
    lines = get_input2()
    games = re.findall(r'Game (\d+):(.*)', lines)
    for game in games:
        flag = True
        balls = re.findall(r"(\d+) (\w+)", game[1])
        for ball in balls:
            if d[ball[1]] < int(ball[0]):
                flag = False
                break
        if flag:
           ans += int(game[0]) 
    
    return ans

def b():
    ans = 0
    lines = get_input2()
    games = re.findall(r'Game (\d+):(.*)', lines)
    for game in games:
        d = {'red': 0, 'green': 0, 'blue': 0}
        balls = re.findall(r"(\d+) (\w+)", game[1])
        for ball in balls:
            d[ball[1]] = max(d[ball[1]], int(ball[0]))
        ans += reduce(lambda x, y: x * y, d.values())
    
    return ans
                

if __name__ == '__main__':
    # print(a())
    print(b())