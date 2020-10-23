import sys
import resource
from copy import copy, deepcopy

sys.setrecursionlimit(10 ** 7)

class Pentomino: 
    num = 12
    F = [[[0], [0, 1, 2], [1]], 
        [[0], [0, 1], [-1, 0]], 
        [[0], [-1, 0, 1], [1]], 
        [[0, 1], [-1, 0], [0]],
        [[0], [-1, 0, 1], [-1]],
        [[0, 1], [1, 2], [1]],
        [[0], [-2, -1, 0], [-1]],
        [[0], [-1, 0], [0, 1]]]#0 F 8パターン*

    I = [[[0], [0], [0], [0], [0]],  
        [[0, 1, 2, 3, 4]]] #1  I 2パターン

    L = [[[0, 1, 2, 3], [3]], 
        [[0, 1], [0], [0], [0]], 
        [[0], [0, 1, 2, 3]], 
        [[0], [0], [0], [-1, 0]], 
        [[0], [-3, -2, -1, 0]],
        [[0], [0], [0], [0, 1]],
        [[0, 1, 2, 3], [0]],
        [[0, 1], [1], [1], [1]]] #2  L 8パターン*

    N = [[[0, 1, 2], [-1, 0]], 
        [[0], [0], [0, 1], [1]], 
        [[0, 1], [-2, -1, 0]], 
        [[0], [0, 1], [1], [1]],
        [[0, 1], [1, 2, 3]],
        [[0], [-1, 0], [-1], [-1]],
        [[0, 1, 2], [2, 3]],
        [[0], [0], [-1, 0], [-1]]] #3 N 8パターン*

    P = [[[0, 1, 2], [0, 1]],
        [[0], [0, 1], [0, 1]],
        [[0, 1], [-1, 0, 1]], 
        [[0, 1], [0, 1], [1]],
        [[0, 1], [0, 1, 2]],
        [[0, 1], [0, 1], [0]],
        [[0, 1, 2], [1, 2]],
        [[0], [-1, 0], [-1, 0]]] #4 P 8パターン*

    T = [[[0], [0, 1, 2], [0]], 
        [[0], [0], [-1, 0, 1]], 
        [[0], [-2, -1, 0], [0]], 
        [[0, 1, 2], [1], [1]]] #5 T 4パターン

    U = [[[0, 1], [1], [0, 1]], 
        [[0, 1, 2], [0, 2]], 
        [[0, 1], [0], [0, 1]], 
        [[0, 2], [0, 1, 2]]] #6 U 4パターン

    V = [[[0, 1, 2], [2], [2]], 
        [[0, 1, 2], [0], [0]], 
        [[0], [0], [0, 1, 2]], 
        [[0], [0], [-2, -1, 0]]] #7 V 4パターン
    
    W = [[[0, 1], [1, 2], [2]], 
        [[0, 1], [-1, 0], [-1]],
        [[0], [0, 1], [1, 2]],
        [[0], [-1, 0], [-2, -1]]] #8 W 4パターン

    X = [[[0], [-1, 0, 1], [0]]] #9 X 1パターン

    Y = [[[0], [-1, 0, 1, 2]],
        [[0], [0], [-1, 0], [0]], 
        [[0, 1, 2, 3], [2]], 
        [[0], [0, 1], [0], [0]],
        [[0, 1, 2, 3], [1]],
        [[0], [-1, 0], [0], [0]],
        [[0], [-2, -1, 0, 1]],
        [[0], [0], [0, 1], [0]]] #10 Y 8パターン*

    Z = [[[0], [0, 1, 2], [2]],
        [[0, 1], [0], [-1, 0]],
        [[0], [-2, -1, 0], [-2]],
        [[0, 1], [1], [1, 2]]] #11 Z 4パターン*

    mino = [F, I, L, N, P, T, U, V, W, X, Y, Z]
    name = ['F', 'I', 'L', 'N', 'P', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    __idx = [0, 2, 3, 4, 11]

    #反転が必要なもの: F, L, N, P, Y, Z

    def __reverse(self, m): 
        m[0], m[-1] = m[-1], m[0]
        return m

    def __print(self): 
        id = 0
        for i in self.mino: 
            print(self.name[id] + ": ")
            for j in i:
                print(j)
            print()
            id += 1

##############################
w = 10
h = 6
pm = Pentomino()


visit = [[False for i in range(w)] for j in range(h)]

def print_mino():
    for idx, i in enumerate(pm.mino):
        print(idx, ":")
        for j in i:
            b2 = [[-1 for i in range(11)] for j in range(11)]
            x2, y2 = 5, 5
            for k in j:
                for l in k:
                    b2[x2 + l][y2] = idx
                y2 += 1
            for k in range(11):
                for l in range(11):
                    if b2[k][l] != -1:
                        if b2[k][l] < 10:
                            print('0' + str(b2[k][l]) + ' ', end='')
                        else:
                            print(str(b2[k][l]) + ' ', end='')
                    else:
                        print("** ", end='')
                print()
            print()


def print_board():
    for i in range(h): 
        for j in range(w): 
            if board[i][j] != -1:
                print(pm.name[board[i][j]] + ' ', end='')
            else:
                print("* ", end='')
        print()

def complete(): 
    for i in range(h): 
        for j in range(w):
            if board[i][j] == -1:
                return False
    print_board()
    return True

def restore(idx, i, x, y, board):
    yt = copy(y)
    for j in i:
        for k in j:
            board[x+k][yt] = -1
        yt += 1


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(x, y, visit, d):

    if not(0 <= x < h and 0 <= y < w) or visit[x][y]:
        return d
        
    visit[x][y] = True
    d += 1


    for i in range(len(dx)):
        d = dfs(x + dx[i], y + dy[i], visit, d)

    return d

def check_board(b):
    for x in range(h):
        for y in range(w):
            if b[x][y] == -1:
                visit[x][y] = False
            else:
                visit[x][y] = True

    for x in range(h):
        for y in range(w):
            if b[x][y] == -1 and not visit[x][y]:
                #print("start", x, y)
                d = dfs(x, y, visit, 0)
                #print("depth", d)
                if d % 5 != 0:
                    return False
    return True

xs, ys = 0, 0
comp_cnt = 0
used = [False for i in range(pm.num)]
def solve(x, y, b):
    global used
    #print(x, y)
    #print_board()

    cnt = 0
    for i in used:
        if not i:
            cnt += 1
    if cnt <= 0:
        global comp_cnt
        comp_cnt += 1
        print(used)
        print_board()
        print("#" + str(comp_cnt) + ":")
        print_board()
        print("Completed!!")

    if not check_board(b):
        #print("Less than 4 boxes")
        return False
     
    for i in range(pm.num):
        if used[i]: 
            continue
        for j in pm.mino[i]:
            #print(i, x, y)
            yt = copy(y)
            flag = False
            for k in j:
                for l in k:
                    if not(0 <= x+l < h and 0 <= yt < w) or b[x+l][yt] != -1:
                        flag = True
                        break
                yt += 1
                if flag:
                    break
            if flag:
                continue
            #print("Place:", i)
            yt = copy(y)

            xs = x
            ys = y

            for k in j:
                for l in k:
                    board[x+l][yt] = i
                yt += 1
            used[i] = True
            idx = i

#            if all(used):
#                return True
#                #sys.exit()

            minx, miny = 0, 0
            flag = False
            for y in range(w):
                for x in range(h):
                    if b[x][y] == -1:
                        minx = x
                        miny = y
                        flag = True
                        break
                if flag:
                    break

            solve(minx, miny, b)
            restore(i, j, xs, ys, b)
            x = xs
            y = ys
            used[i] = False
            #print("Restore")
                        
    return False     

#print_mino()
board = [[-1 for i in range(w)] for j in range(h)]
solve(0, 0, board)
