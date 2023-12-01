from util import get_input

def a():
    lines = get_input()
    ans = 0
    for line in lines:
        start, end = 0, len(line) - 1
        f1, f2 = True, True
        while f1 or f2:
            if line[start].isdigit() and f1:
                ans += 10 * int(line[start])
                f1 = False
            if line[end].isdigit() and f2:
                ans += int(line[end])
                f2 = False
            start += 1
            end -= 1
    return ans

def b():
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
         '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    lines = get_input()
    ans = 0
    for line in lines:
        left, right = len(line) - 1, 0
        for number, val in d.items():
            idx = line.find(number)
            if idx != -1 and idx <= left:
                left_val = val
                left = idx
            idx = line.rfind(number)
            if idx != -1 and idx >= right:
                right_val = val
                right = idx
        ans += 10 * left_val + right_val
    
    return ans
        
if __name__ == '__main__':
    print(a())
    print(b())