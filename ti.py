import unittest
import time
import random
import itertools
from datetime import datetime

start = datetime.now()

def drawGame(game="",help=False):
    ''' Draw game. for testing
    :param :'''
    ref = '0123456789'
    board = ['' for x in range(1,11)]
    for i,move in enumerate(game,1):
        board[int(move)] = 'X' if (i%2) else 'O'

    print('--------', end='\n')
    for i in range(2,-1,-1):
        for j in range(1,4):

            print("|{:<1}".format(board[i*3+j]), end='')
            if help:
                print('|     |',end='')
                print("|{:<1}}".format(ref[i*3+j]), end=' ')
        print('|   *#*  ', end='\n')
    print('--------')

# passive bot; can play either player anywhere in game. No memory of any previous ( no need)
class dumbBot():
    ''''''
    def __init__(self,gameTree):
        self.gameTree = gameTree
        self.rules = self.makeRules()

    def makeRules(self):
        ary =[]
        # level 1
        ary += [{x: 1} for x in '51379']  #  + [{x: 0} for x in '2468']
        # level 2
        ary += [{'5' + x: 1} for x in '1379'] # +[{'5'+x:0} for x in '2468']
        ary +=[{x+'5':1} for x in '1379']
        ary +=[{x+'3' if x in '24' else '7':1} for x in '2468']
        #ary +=[{x+'5':0} for x in '2468'] + [{x+y:0} for x in '1379' for y in "13792468" if x != y]
        # level3 #5
        ary +=[{'5'+x+'7' if x in '24' else '3':1} for x in '2468'] # *special (away from O; next turn win auto from blocking)
        pick = lambda x: ('7' if x == '3' else '3') if x in '37' else ('1' if x == '9' else '1')
        ary += [{'5' + x + pick(x): 1} for x in '1379']  # *special  opposite, everything else draw
        # level3 # corner
        ary +=[{''.join(x):1} for x in itertools.permutations('1379', 3)]  # X wins, definite 2-threat
        ary +=[{x+y+'5':1} for x in '1379' for y in "2468"]  # X wins, definite 2-threat
        # level4 # corner -> center -> corner -> edge (auto draw after this)
        ary += [{pair[0]+'5'+pair[1]+y:1} for pair in itertools.permutations('1379', 2) for y in '2468']
        # level 4 # corner -> center -> edge -> corner (in between) *special case
        split= lambda x, y: ('9' if y in '68' else '1') if x in '37' else ('3' if y in '26' else '7')
        ary += [{x + '5' + y + split(x, y): 1} for x in "1379" for y in '2468']
        # level 4 # # center->corner -> opposite corner? ->  edge (force draw) ; another corner here loses
        pick = lambda x: ('7' if x == '3' else '3') if x in '37' else ('1' if x == '9' else '1')
        ary += [{'5' + x + pick(x)+y : 1} for x in '1379' for y in '2468']
        # level 4 # # pick center after 3 turns
        ary +=[{x+y+z+'5':1} for x in '2468' for y in "1379" for z in '13792468' if x+z not in self.gameTree.twins]
        dictionary = {}
        for a in ary:
            dictionary.update(a)
        return dictionary

    def bestMove(self):
      board = self.gameTree.board
      if 0<len(board) >=9:
          return 0
      if len(board) >2:
        a = next(iter("".join(trip) for m in self.gameTree.nextMoves for trip in
                      itertools.product(board[-2], board[len(board) - 2::-2][1:], m) if
                      "".join(trip) in self.gameTree.triples), "")
        if a:
            return a[-1]
        b = next(iter("".join(trip) for m in self.gameTree.nextMoves for trip in
                      itertools.product(board[-1], board[::-2][1:], m) if
                      "".join(trip) in self.gameTree.triples), "")
        if b:
          return b[-1]
      # find game ending threat
      threatList = [twin[1] for twin in itertools.product(board[len(board)-1::-2],self.gameTree.nextMoves) if "".join(twin) in self.gameTree.twins]
      if len(threatList)==2 and threatList[0]==threatList[1] :
          return threatList[0]
      # check rules
      plays = self.gameTree.nextMoves
      random.shuffle(plays)
      for p in plays:
          if board+p in self.rules and self.rules[board+p]==1 :
              return p
      # force opponent to block
      if len(threatList) > 0:
          return threatList[0]
      return random.choice(self.gameTree.nextMoves)

class gameTree():
    def __init__(self,board=""):
        self.board = board
        self.boardRef = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.win3ref  = {'123', '456', '789', '147', '258', '369', '159', '357'}
        self.triples = set(''.join(triplet) for win_triplet in self.win3ref for triplet in itertools.permutations(win_triplet,3))
        self.twins =  set(''.join(twin) for win_triplet in self.win3ref for twin in itertools.permutations(win_triplet,2))
        self.currentMove = len(board)
        self.nextMoves =list( set (list('123456789')) - set(board))
        random.shuffle(self.nextMoves )
        self.addBot()
        print()

    def addBot(self):
        self.Bot = dumbBot(self)

    def updateBoard (self,newMove):
        if len(self.nextMoves)==0:
            print("Game Over")
            return 0
        elif  newMove not in self.nextMoves:
            print("Invalid Move")
            return 0
        self.board = self.board+newMove
        self.nextMoves =list( set (list('123456789')) - set(self.board))
        return 1

    def checkGame(self, message=None):  #sanity check.
        if len(self.board)!=len(set(self.board)) or len(self.board)>=9 :
            return 0
        elif any(x for x in self.board if x not in '123456789'):
            return 0
        if len(self.board)<5:
            return 1  # no need to check in early game
        x_win = any(''.join(x) in self.triples for x in itertools.combinations(self.board[::2],3))
        o_win = any(''.join(x) in self.triples for x in itertools.combinations(self.board[1::2],3))
        if x_win or o_win:
            if message != None: message[0] = 'Player X Won!' if x_win else 'Player O Won!'
            return 2  # still evaluate to True but differs from can_continue:'1'
        # game can continue if checkGame return 1,
        return 1

class testTicTac(unittest.TestCase):
    def testTicTacToe(self):
        while input('Quit? :')!='y':
            newGame = gameTree('')
            newGame.addBot()
            userMove, message = '0', ['']
            if input('Let computer play first? ')=='y':
                newGame.updateBoard(newGame.Bot.bestMove())
            while True:
                while userMove not in newGame.nextMoves:  # make sure we are getting the right input
                    drawGame(newGame.board)
                    userMove = input("What is your Move? ([1-9] :")
                if (not newGame.updateBoard(userMove) or newGame.checkGame(message)!=1) or \
                   (not newGame.updateBoard(newGame.Bot.bestMove()) or newGame.checkGame(message)!=1)  :
                    drawGame(newGame.board)  # if any of these evalue to false, we will quit: 'break'
                    print(message)
                    break
        self.assertTrue(True)

    def setUp(self):
        self._started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self._started_at
        print('{} ({}s)'.format(self.id(), round(elapsed, 2)))

if __name__ == '__main__':
  unittest.main()
  print('Done')