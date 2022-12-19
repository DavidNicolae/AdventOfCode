def get_input():
    valve_map = {}
    flow_map = {}
    f = open('input.txt', 'r')
    for line in f.readlines():
        line = line.strip()
        valve = line[6:8]
        flow = int(line[line.index('=') + 1:line.index(';')])
        if 'valves' in line:
            line = line[line.index('valves') + 7:]
        else:
            line = line[line.index('valve') + 6:]
        line = line.split(', ')        
        valve_map[valve] = line
        if flow != 0:
            flow_map[valve] = flow
    return valve_map, flow_map

def find_solution(valve, time, score, adj_map, flow_map, visited, scores):
    hash = ''
    visited_h = list(visited)
    if valve not in visited_h:
        visited_h.append(valve)
    visited_h = sorted(visited_h)
    for e in visited_h:
        hash += ' ' + e
    scores[hash] = max(scores.get(hash, 0), score)
    for v in flow_map:
        remaining_time = time - adj_map[valve][v] - 1
        if v not in visited and remaining_time >= 0:
            next_score = score + remaining_time * flow_map[v]
            visited.add(v)
            find_solution(v, remaining_time, next_score, adj_map, flow_map, visited, scores)
            visited.remove(v)
    # return scores
    

def ab():
    start = 'AA'
    time = 30
    score = 0
    scores = {}
    visited = set()
    valve_map, flow_map = get_input()
    adj_map = {}
    for valve in valve_map:
        adj_map[valve] = {v: 1 if v in valve_map[valve] else float('+inf') for v in valve_map}
    
    for k in adj_map:
        for i in adj_map:
            for j in adj_map:
                adj_map[i][j] = min(adj_map[i][j], adj_map[i][k] + adj_map[k][j])
    
    find_solution(start, time, score, adj_map, flow_map, visited, scores)
    answer1 = max(scores.values())

    scores = {}
    find_solution(start, 26, 0, adj_map, flow_map, visited, scores)
    answer2 = -1

    for key1 in scores:
        for key2 in scores:
            if key1 == key2:
                continue
            key_s = key1.split(' ')
            ok = True
            for s in key_s: 
                if s in flow_map and key2.find(s) != -1:
                    ok = False
                    break
            if ok:
                answer2 = max(answer2, scores[key1] + scores[key2])
    
    return answer1, answer2

print(ab())