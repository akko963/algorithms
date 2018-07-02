'''
Copyright (c) 2018 Aung Ko Ko Oo
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# Required global vars
COLORS = ['RED','blue','cyan','black','dark violet','purple', 'brown','dark red','dark blue']
board = lambda x,y : ('A',chr(ord('A')+x),'A',chr(ord('A')+y))

N,S,W,E = board(20,18)
list0_inc=[chr(x) for x in range(ord(N),ord(S)+1)]
list0_dec=list(reversed([chr(x) for x in range(ord(N),ord(S)+1)]))
list1_inc=[chr(x) for x in range(ord(W),ord(E)+1)]
list1_dec=list(reversed([chr(x) for x in range(ord(W),ord(E)+1)]))

import itertools
import unittest

class Treski(object):

    def __init__(self, id,index):
        self.id = id
        self.index = index
        if {'N','E','W','S'}.issubset(vars()) or {'N','E','W','S'}.issubset(globals()):
            self.N,self.W ,self.S ,self.E  = N,W,S,E
        self.directions = {}
        self.directions['N'] = [''.join([chr(x),id[1]]) for x in range(ord(id[0])-1,ord(self.N)-1,-1)]
        self.directions['S'] = [''.join([chr(x),id[1]]) for x in range(ord(id[0])+1,ord(self.S)+1)]
        self.directions['E'] = [''.join([id[0],chr(x)]) for x in range(ord(id[1])+1,ord(self.E)+1)]
        self.directions['W'] = [''.join([id[0],chr(x)]) for x in range(ord(id[1])-1,ord(self.W)-1,-1)]
        if ord(id[0])+ord(id[1]) %2 : # 0 evaluate to false
            for dest in ['NW','NE','SW','SE']:
                list0 = list(itertools.dropwhile(lambda x: x != id[0], list0_dec if dest[0]=='N' else list0_inc))
                list1 = list(itertools.dropwhile(lambda x: x != id[1], list1_dec if dest[1]=='W' else list1_inc))
                list0[:] =list0[1:]
                list1[:] = list1[1:]
                self.directions[dest] = [''.join(x) for x in zip(list0,list1)]
        else:
            for dest in ['NW', 'NE', 'SW', 'SE']: self.directions[dest] = list()

    def hop(self, dest, steps):
        return self.directions[dest][steps-1]

def generate():
    '''
    generate grid-locations of each square and id-locations of triangles, creates and uses an array of Treski
    @return:
    '''
    all_dots = []
    Ts = []
    for y in list0_inc:
        for x in list1_inc:
            all_dots.append(Treski(''.join([y,x]),len(all_dots)))

    for idx,dot in enumerate(all_dots):
        def findIndex (item):  # find the array-index of the square from id (ex: 'AA') , returns the array_index
            found =next(x.index for x in all_dots if x.id == item)
            return found
        listN = dot.directions['N']
        listS = dot.directions['S']
        listW = dot.directions['W']
        listE = dot.directions['E']
        newTw = [[x[0], x[1],x[2]] for x in zip(listN,listS, listW)]
        newTe = [[x[0], x[1], x[2]] for x in zip(listN, listS, listE)]
        newT1 =  [[x[0],x[1],dot.id ]for x in zip(listS,listW)]
        newT2 = [[x[0], x[1], dot.id] for x in zip(listS, listE)]
        if ord(dot.id[0]) + ord(dot.id[1]) % 2:
            listNW = dot.directions['NW']
            listSW = dot.directions['SW']
            listNE = dot.directions['NE']
            listSE = dot.directions['SE']
            newTup = [[x[0], x[1], dot.id] for x in zip(listNW, listNE)]
            newTdown= [[x[0], x[1], dot.id] for x in zip(listSW, listSE)]
            Ts += newTup + newTdown
        Ts += newTw+newTe+newT1+newT2
        for i, x in enumerate(zip(listS,listW)):
            newTs = [[x[0], x[1], all_dots[findIndex(x[0])].hop('W', i + 1)]]
            Ts += newTs
        for i, x in enumerate(zip(listS, listE)):
            newTs = [[x[0], x[1], all_dots[findIndex(x[0])].hop('E', i + 1)]]
            Ts += newTs
    return all_dots,Ts

import tkinter
from random import randint
from time import sleep
def tk():
    '''
    Use tkinter to draw the graphics. Uses built-in python tkinter for python 3.6. Tested on windows.
    draw the grid and triangles generated from generate()
    @return:
    '''
    indent_x=indent_y = 20
    gap_x = 34
    gap_y = 24
    tl = lambda letter : ord(letter) - ord('A')  # translate from letter to a number (id)
    def translate (tri):
        '''
        translate the triangle in id_locations to grid locations
        @param tri: list of 3 items: each represents a point on the grid
        @return: 3 pairs of x,y grid locations of the triangle
        '''
        return    [y for x in tri for y in  [indent_x+tl(x[1])*gap_x,indent_y+tl(x[0])*gap_y] ]
    all,Ts = generate()
    frame =  [((indent_x+tl(x.id[1])*gap_x,indent_y+tl(x.id[0])*gap_y, indent_x+tl(x.id[1])*gap_x+1,indent_y+tl(x.id[0])*gap_y+1),'.')  for x in all]

    c = tkinter.Canvas(tkinter.Tk(),width=900,height=600); c.pack()
    c.pack()
    for x,id in frame:
        c.create_text((x[0],x[1]),text=id, fill = 'Gray')
    print('Total Number of Triangles',len(Ts))
    c.update()
    sleep(25)
    for x in Ts:
        sleep(.01)
        c.delete('triangles')
        c.create_polygon(translate(x),fill= COLORS[randint(0,len(COLORS)-1)],tags = 'triangles')
        c.update()
    c.update()
    c.winfo_geometry()
    tkinter.mainloop()

class TTreski(unittest.TestCase):
    def test_A(self):
        print('a')
    def testT(self):
        all,Ts = generate()
        print('Total Number of Triangles from generated list:',len(Ts))
        Ts = [*map(lambda x: tuple(x), Ts)]

        print(Ts[:20])
        original = {*map(lambda x: tuple(x), Ts)}
        print("original total, unique", len(original))
        modified= {*map(lambda x: tuple(sorted(x)), Ts)}
        modified = list(modified)
        print('modified total, unique',len(modified))
        self.assertEqual(len(original),len(modified))

        #look for dupes
        from collections import Counter
        dupes = [k for k, v in Counter(Ts).items() if v > 1]
        self.assertEqual(len(dupes),0)
        # IF there ARE any dupes, lets see what they are
        print('dupes', len(dupes), dupes)
        print('dupes',[ (x,"@ index",i) for x in dupes  for i,T in enumerate(Ts)if T== x])


    def setUp(self):
        pass

if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 :
        #tk()
        unittest.main()
        pass
