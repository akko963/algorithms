import unittest
import time
from random import randint
import math
# I find merge_sort implementation in loops as clunky. The recursion version is so much better
def makeList(count = 41, lbound=0,ubound=99):
    l = [randint(lbound,ubound) for _ in range(0, count)]
    return l
def board(std=64):
    ls = [ 0 for _ in range(std)]
    return ls

def findSpot(ref,i):
    if not ref or ref[i]!=0:
        return []
    board = ref.copy()
    mult= i%8
    div = i//8
    for j in range(8):
        board[div*8+j]=1
        board[j*8+mult]= 1
        k = j*8
        if j< 8-mult:
            x = i+k+j
            a = x- (j*16)
            if x < 64: board[x]= 1
            if a >= 0 : board[a] = 1
        if j <= mult :
            y = i+k-j
            b = y - (j*16)
            if y < 64: board[y]= 1
            if b >= 0 : board[b]= 1
    board[i] = 9
    return board
def drawBoard(board,x=8):
    if not(board):
        return
    print('\n---------------------')
    for i in range(x-1,-1,-1):
        print('\n[{}'.format(i), end='] : ')
        for j in range(x):
            print("{:<2}".format(board[i*x+j]),end=' ')
    print('\n---------------------')

def eightQueens(board=[], n=8):
#
    if n==0:
        print('****  Hit  ** ',board.count(9),board.count(0),n)
        drawBoard(board)
        return board
    if n>0 and  board.count(0)>0:

        branch = board.copy()
        empty = [index for index,element in enumerate(board) if element == 0]
        for i in empty:
            #print ('for n=',n,i)
            branch = findSpot(board,i)
            if branch:
                #return  eightQueens(branch, n - 1)
                branch = eightQueens(branch, n - 1)
                if branch:
                     return branch
    return []
def findMoves(ref,lastmove, x=6,y=6):
    rem = lastmove%x
    moves = []

    if lastmove +y+2 < x*y and x-rem-1 >=2 and ref[lastmove +y+2]==0:
        moves.append(lastmove +y+2)
    if lastmove +2*y+1 < x*y and x-rem-1 >=1 and ref[lastmove +2*y+1]==0:
        moves.append(lastmove +2*y+1)
    if lastmove -y+2 >=0 and x-rem-1 >=2 and ref[lastmove -y+2]==0:
        moves.append(lastmove -y+2)
    if lastmove -2*y+1 >=0 and x-rem-1 >=1 and ref[lastmove -2*y+1]==0:
        moves.append(lastmove -2*y+1)

    if lastmove +y-2 < x*y and rem >=2 and ref[lastmove +y-2]==0:
        moves.append(lastmove +y-2)
    if lastmove +2*y-1 < x*y and rem >=1 and ref[lastmove +2*y-1]==0:
        moves.append(lastmove +2*y-1)
    if lastmove -y -2>=0 and rem >=2 and ref[lastmove -y-2]==0:
        moves.append(lastmove -y-2)
    if lastmove -2*y -1>=0 and rem >=1 and ref[lastmove -2*y-1]==0:
        moves.append(lastmove -2*y-1)

    return moves

def travelKnight(ref ,lastmove=14):
    if ref.count(0)==0:
        return ref

    empty = findMoves(ref,lastmove)
    for i in empty:
        if i>=36 or ref[i] != 0:
            print('exception',i)
            drawBoard(ref,6)
            raise Exception('Unexpected error. Quitting')
        #branch = ref.copy()
        ref[i]=ref[lastmove]+1
        branch = travelKnight(ref,i)
        if branch:
            if ref.count(0)>3:
                 drawBoard(ref,6)
            return branch
        ref[i]=0
    return []

for i in range(10):
    ref = board(36)
    start = randint(0, 35)
    ref[start]=1
#    print(len(ref),ref.count(0))
#    drawBoard(ref,6)
    ans = travelKnight(ref,start)
    if ans:
        print('Answer found: @',i)
        drawBoard(ans,6)

class recursions(unittest.TestCase):
    @unittest.skip('')
    def test8Queens(self):
        starter = board()
        test = eightQueens(starter, 8)
        self.assertTrue(test.count(9)==8)
    def setUp(self):
        self._started_at = time.time()
    def tearDown(self):
        elapsed = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed, 2)))

