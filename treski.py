
# List of global variables
COLORS = ['RED','blue','cyan','black','dark violet','purple', 'brown','dark red','dark blue']
board = lambda x,y : ('A',chr(ord('A')+x),'A',chr(ord('A')+y))

N,S,W,E = board(21,19)
list0_inc=[chr(x) for x in range(ord(N),ord(S)+1)]
list0_dec=list(reversed([chr(x) for x in range(ord(N),ord(S)+1)]))
list1_inc=[chr(x) for x in range(ord(W),ord(E)+1)]
list1_dec=list(reversed([chr(x) for x in range(ord(W),ord(E)+1)]))


import itertools

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
            print(x)
            newTs = [[x[0], x[1], all_dots[findIndex(x[0])].hop('E', i + 1)]]
            Ts += newTs
    return all_dots,Ts

import tkinter
from random import randint
from time import sleep
def tk():
    '''
    draw the grid and triangles generated from generate()
    @return:
    '''
    indent_x=indent_y = 50
    gap_x = 20
    gap_y = 25
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
    for x in Ts:
        sleep(.05)
        c.delete('triangles')
        c.create_polygon(translate(x),fill= COLORS[randint(0,len(COLORS)-1)],tags = 'triangles')
        c.update()
    c.winfo_geometry()
    tkinter.mainloop()

if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 :
        tk()
