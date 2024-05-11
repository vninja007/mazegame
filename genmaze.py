import random


def genMaze(w, h, dist=0.6, protection=False):

# seed = 0
    maze = [['X']*w for i in range(h)]
    def visit(r, c, hasvisit):
        maze[r][c] = ' '
        while True:
            nbrs = []
            if(r>1 and (r-2, c) not in hasvisit): nbrs.append(((r-2, c), (r-1, c)))
            if(r<h-2 and (r+2, c) not in hasvisit): nbrs.append(((r+2, c), (r+1, c)))
            if(c>1 and (r, c-2) not in hasvisit): nbrs.append(((r, c-2), (r, c-1)))
            if(c<w-2 and (r,c+2) not in hasvisit and (not protection or r*c != 1)): nbrs.append(((r, c+2), (r, c+1)))

            if not nbrs: return

            node, next = random.choice(nbrs)
            noder, nodec = node
            nextr, nextc = next
            maze[nextr][nextc] = ' '
            hasvisit.add((noder, nodec))
            visit(noder, nodec, hasvisit)

    while('@' not in ''.join(''.join(j for j in i) for i in maze)):
        maze = [['X']*w for i in range(h)]
        hasvisit = {(1, 1)}
        visit(1, 1, hasvisit)

        deadends = []

        for r in range(1, h, 2):
            for c in range(1, w, 2):
                if(r<=h*dist and c<=w*dist): continue
                if([maze[rr][cc] for rr in range(r-1,r+2) for cc in range(c-1,c+2)].count('X')==7):
                    deadends.append([r,c])
        if(len(deadends)==0): continue
        r, c = random.choice(deadends)
        maze[r][c] = '@'
        # print(maze)
        # input()

    return maze



if __name__=='__main__':
    print('\n'.join(''.join(j for j in i) for i in genMaze(41, 21)))