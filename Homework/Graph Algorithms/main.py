import queue
rc = input().split()
R = int(rc[0])
C = int(rc[1])
m = []

for i in range(R):
    k = [str(i) for i in input().split()][:C]
    if ('s' in k):
        sr = i
        sc = k.index('s')
    m.append(k)

rq = []
cq = []

move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

reached_end = False
visited = []
for i in range(R):
    k = []
    for j in range(C):
        k.append(False)
    visited.append(k)

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def explore_neighbours(r, c, nodes_in_next_layer):
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if (rr < 0) or (cc < 0):
            continue
        if (rr >= R) or (cc >= C):
            continue
        if (visited[rr][cc] == True):
            continue
        if (m[rr][cc] == '#'):
            continue
        rq.insert(0, rr)
        cq.insert(0, cc)
        visited[rr][cc] = True
        nodes_in_next_layer = nodes_in_next_layer + 1

def BFS_queue(nodes_in_next_layer, nodes_left_in_layer, reached_end, move_count):
    rq.insert(0, sr)
    cq.insert(0, sc)
    visited[sr][sc] = True
    while (len(rq) > 0):
        r = rq.pop(-1)
        c = cq.pop(-1)
        if (m[r][c] == 'e'):
            reached_end = True
            break

        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]

            if (rr < 0) or (cc < 0):
                continue
            if (rr >= R) or (cc >= C):
                continue
            if (visited[rr][cc] == True):
                continue
            if (m[rr][cc] == '#'):
                continue
            rq.insert(0, rr)
            cq.insert(0, cc)
            visited[rr][cc] = True
            nodes_in_next_layer = nodes_in_next_layer + 1

        nodes_left_in_layer = nodes_left_in_layer - 1
        if (nodes_left_in_layer == 0):
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count = move_count + 1
    if (reached_end == True):
        return move_count
    return -1

print(BFS_queue(nodes_in_next_layer, nodes_left_in_layer, reached_end, move_count))
