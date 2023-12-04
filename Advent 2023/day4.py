from util import get_input

def a():
    lines = get_input()
    ans = 0
    for line in lines:
        left, right = line.split('|')
        left_nums = set(int(num) for num in left.split() if num.isdigit())
        right_nums = set(int(num) for num in right.split() if num.isdigit())
        points = len(left_nums.intersection(right_nums)) - 1
        if points >= 0:
            ans += 2 ** points

    return ans

def b():
    lines = get_input()
    ans = 0
    d = {}
    for idx, line in enumerate(lines):
        left, right = line.split('|')
        left_nums = set(int(num) for num in left.split() if num.isdigit())
        right_nums = set(int(num) for num in right.split() if num.isdigit())
        points = len(left_nums.intersection(right_nums))
        d[idx + 1] = [points, 1]
    
    for i in range(1, len(lines) + 1):
        points, nr = d[i]
        ans += nr
        for j in range(i + 1, i + 1 + points):
            d[j][1] += nr

    return ans


if __name__ == '__main__':
    print(a())
    print(b())