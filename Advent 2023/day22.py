import re
from collections import Counter
from copy import deepcopy

def check_intersection(b0, b1, b2, b3):
    x_intersect = (
        b0[0] <= b3[0] and b2[0] <= b1[0]
    )
    y_intersect = (
        b0[1] <= b3[1] and b2[1] <= b1[1]
    )
    z_intersect = (
        b0[2] <= b3[2] and b2[2] <= b1[2]
    )
    return x_intersect and y_intersect and z_intersect

def fall(ground, brick):
    moved = False
    (x1, y1, z1), (x2, y2, z2) = brick
    while z1 > 1 and not any(check_intersection((x1, y1, z1 - 1), (x2, y2, z2 - 1), b2, b3) == True for b2, b3 in ground):
        z1, z2 = z1 - 1, z2 - 1
        moved = True
    ground.append(((x1, y1, z1), (x2, y2, z2)))
    return moved

def a(bricks):
    ans1, ans2 = 0, 0
    ground = []
    for brick in bricks:
        _ = fall(ground, brick)
    bricks = ground
    ground = []
    for brick in bricks:
        test_bricks = [b for b in bricks if b != brick]
        ground = []
        fail = False
        for tb in test_bricks:
            moved = fall(ground, tb)
            if moved:
                ans2 += 1
                fail = True
        if not fail:
            ans1 += 1

    return ans1, ans2

if __name__ == '__main__':
    bricks = []
    
    with open('input.txt', 'r') as f:
        l = f.readline().strip()
        while l:
            l = [int(x) for x in re.split(r',|~', l.strip())]
            bricks.append((tuple(l[0:3]), tuple(l[3:])))
            l = f.readline().strip()
    bricks.sort(key=lambda l: l[0][2])
    print(a(bricks))