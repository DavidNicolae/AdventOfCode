class Merger(object):
   def merge(self, intervals):
      """
      :type intervals: List[Interval]
      :rtype: List[Interval]
      """
      if len(intervals) == 0:
         return []
      self.quicksort(intervals,0,len(intervals)-1)
      stack = []
      stack.append(intervals[0])
      for i in range(1,len(intervals)):
         last_element= stack[len(stack)-1]
         if last_element[1] >= intervals[i][0]:
            last_element[1] = max(intervals[i][1],last_element[1])
            stack.pop(len(stack)-1)
            stack.append(last_element)
         else:
            stack.append(intervals[i])
      return stack
   def partition(self,array,start,end):
      pivot_index = start
      for i in range(start,end):
         if array[i][0]<=array[end][0]:
            array[i],array[pivot_index] =array[pivot_index],array[i]
            pivot_index+=1
      array[end],array[pivot_index] =array[pivot_index],array[end]
      return pivot_index
   def quicksort(self,array,start,end):
      if start<end:
         partition_index = self.partition(array,start,end)
         self.quicksort(array,start,partition_index-1)
         self.quicksort(array, partition_index + 1, end)

def get_input():
    dict = {}
    f = open('input.txt', 'r')
    for line in f.readlines():
        line = line.strip()
        sensor_x = int(line[line.index('=') + 1:line.index(',')])
        line = line[line.index(',') + 4:]
        sensor_y = int(line[:line.index(':')])
        line = line[line.index('=') + 1:]
        beacon_x = int(line[:line.index(',')])
        line = line[line.index('=') + 1:]
        beacon_y = int(line)
        dict[(sensor_x, sensor_y)] = (beacon_x, beacon_y)
    return dict

def a():
    blocked = set()
    y = 2000000
    dict = get_input()
    sensors = dict.keys()
    beacons = dict.values()
    for sensor, beacon in dict.items():
        max_dist = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
        max_dist -= abs(sensor[1] - y)
        for i in range(max_dist + 1):
            pos = (sensor[0] + i, y)
            if pos not in sensors and pos not in beacons:
                blocked.add(pos)
            pos = (sensor[0] - i, y)
            if pos not in sensors and pos not in beacons:
                blocked.add(pos)
    return len(blocked)

# def b():
#     max_val = 20
#     coef = 4000000
#     dict = get_input()
#     for i in range(max_val + 1):
#         for j in range(max_val + 1):
#             ok = 0
#             for sensor, beacon in dict.items():
#                 max_dist = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])    
#                 if abs(i - sensor[0]) + abs(j - sensor[1]) <= max_dist:
#                     ok = 1
#                     break
#             if ok == 0:
#                 print(i, j)
#                 return i * coef + j
#     return 0

def b():
    max_val = 4000000
    coef = 4000000
    dict = get_input()
    for y in range(max_val + 1):
        print(y)
        intervals = []
        for sensor, beacon in dict.items():
            max_dist = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
            max_dist -= abs(sensor[1] - y)
            if max_dist >= 0:
                intervals.append([max(sensor[0] - max_dist, 0), min(sensor[0] + max_dist, max_val)])
        merger = Merger()
        interval = merger.merge(intervals)
        if len(interval) > 1:
            return (interval[1][0] - 1) * coef + y
    return 0

print(a())
print(b())
