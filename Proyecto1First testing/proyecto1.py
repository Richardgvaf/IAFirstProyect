#imports
import networkx as nx
import tkinter as tk
import numpy as np
import view


posiciones={}
tablero=[]


class Nodo:
    def __init__(self, num):
        self.pos=num
        self.posXY=[0,0]
        self.padre=0
        self.matriz=np.zeros((6,6))
        self.G=0
        self.H=5
        self.F=self.G+self.H
        self.vecinos=[]
        self.bloq=[]
        

    def setPadre(self,num):
        self.padre=num
    
    def setG(self,num):
        self.G=num

    def setH(self,num):
        self.H=num

    def calcF(self):
        self.F=self.G+self.H
        if self.pos==1 or self.pos==6 or self.pos==31 or self.pos==36:
            self.F=self.F+10

    def calcposXY(self):
        self.posXY=posiciones[self.pos]

    def calcBloq(self):
        if (self.pos==0):
            self.bloq=[]
        else:
            for x in range (1,37):
                if (posiciones[x][0]==self.posXY[0] or posiciones[x][1]==self.posXY[1]):
                    self.bloq.append(x)
                else:
                    var=posiciones[x]
                    x1=abs(var[0]-self.posXY[0])
                    y1=abs(var[1]-self.posXY[1])
                    if (x1==y1):
                        self.bloq.append(x)

    def calcVecinos(self):
        if (self.pos==0):
            self.vecinos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        else:
            for x in range (1,37):
                if x not in self.bloq and x not in self.vecinos:
                    self.vecinos.append(x)

    
    def calcMatriz(self):
        self.matriz[self.posXY[0]][self.posXY[1]]=1





def main():
    cuadricula=np.zeros((6,6))
    genDicc()
    #Creación del grafo
    Grafo = nx.Graph()
    Grafo.add_node(Nodo(0))
    list(Grafo)[0].setG(0)
    list(Grafo)[0].calcBloq()
    list(Grafo)[0].calcVecinos()
    for x in range(1,37):
        Grafo.add_node(Nodo(x))

    for x in range(1,37):
        list(Grafo)[x].calcposXY()
        list(Grafo)[x].calcBloq()
        list(Grafo)[x].calcVecinos()
        list(Grafo)[x].setG(len(list(Grafo)[x].bloq))
        list(Grafo)[x].calcF()
        list(Grafo)[x].calcMatriz()
    AEstrella(Grafo)

def setEdges(grf):
    for x in range(37):
        var=list(Grafo)[x]

#Diccionario de posiciones
def genDicc():
    var=1
    x=0
    y=2
    for x in range(6):
        for y in range(6):
            posiciones.setdefault(var,[x,y])
            var+=1

def buscarpos(posXY):
    for pos in posiciones:
        if (posiciones[pos]==posXY):
            return pos

def menor(grafo,lista):#retorna el indice del nodo con menor F en el grafo
    var=lista[0]
    for ele in lista:
        if list(grafo)[ele].F<list(grafo)[var].F:
            var=ele
    return var

def calcNewG(nodo,vecino):
    newg=nodo.G
    if vecino.posXY[0]==(nodo.posXY[0]):
        newg=nodo.G
    if vecino.posXY[0]==(nodo.posXY[0]+1):
        newg=nodo.G+10
        if nodo.pos==0:
            newg=nodo.G+11
        else:
            if (vecino.posXY[1])<=(nodo.posXY[1]+2):
                newg=newg-1
    if vecino.posXY[0]==(nodo.posXY[0]+2):
        newg=nodo.G+21
    if vecino.posXY[0]==(nodo.posXY[0]+3):
        newg=nodo.G+31
    if vecino.posXY[0]==(nodo.posXY[0]+4):
        newg=nodo.G+41
    if vecino.posXY[0]==(nodo.posXY[0]+5):
        newg=nodo.G+51
    if vecino.posXY[0]==(nodo.posXY[0]+6):
        newg=nodo.G+61
    if nodo.pos==0:
        newg=newg+10
    return newg

def calcNewH(nodo,vecino):
    newh=0
    for bloque in vecino.bloq:
        if bloque not in nodo.bloq:
           newh=newh+1
    return newh

def defRuta(nodo,grafo):
    ruta=[nodo.pos]
    var1=nodo
    for x in range(6):
        var2=var1.padre
        ruta.append(var2)
        var1=list(grafo)[var2]
    return ruta

def crearTablero(ruta):
    global tablero
    num=5
    for x in range(6):
        lista=[]
        for y in range(6):
            var=[x,y]
            posi=ruta[num]
            if buscarpos(var)==posi:
                lista.append("Q")
                num=num-1
            else:
                lista.append("0")
        tablero.append(lista)
    print(tablero)
            



def AEstrella(grf):
    fin=False
    cerrado=[0]
    abierto=list(grf)[0].vecinos
    ruta=[]
    for veci in list(grf)[0].vecinos:
        G=calcNewG(list(grf)[0],list(grf)[veci])
        H=calcNewH(list(grf)[0],list(grf)[veci])
        list(grf)[veci].setG(G)
        list(grf)[veci].setH(H)
        list(grf)[veci].calcF()

    while not fin:
        if len(abierto)==0: #si ya no hay abiertos
            ruta=defRuta(list(grf)[men],grf)
            print(ruta)
            crearTablero(ruta)
            break
        men=menor(grf,abierto) #se toma el de menor F

        for vec in list(grf)[men].vecinos: #se analizan los vecinos
            newG=calcNewG(list(grf)[men],list(grf)[vec]) #se calcula el nuevo G
            if newG<list(grf)[vec].G: #si el nuevo G es menor se actualiza el G y H, y se coloca el nuevo padre
                list(grf)[vec].setG(newG)
                list(grf)[vec].setH(calcNewH(list(grf)[men],list(grf)[vec]))
                list(grf)[vec].setPadre(men)
                list(grf)[vec].calcF() #se recalcula F
                list(grf)[vec].bloq=[]
                list(grf)[vec].calcBloq()
                
                for bloque in list(grf)[men].bloq: #se agregan los nuevos bloqueados
                    """if bloque in abierto:
                            abierto.remove(bloque)"""
                    if bloque not in list(grf)[vec].bloq:
                        list(grf)[vec].bloq.append(bloque)
                        if bloque in list(grf)[vec].vecinos:
                            list(grf)[vec].vecinos.remove(bloque)
                    list(grf)[vec].calcVecinos() #se actualizan los vecinos
                    list(grf)[vec].bloq.sort()
                    list(grf)[vec].vecinos.sort()

        if men in abierto:
            abierto.remove(men)#se elimina de la lista de abiertos
            cerrado.append(men)#se incluye a la lista de cerrados
            if list(grf)[men].posXY[0]==5:
                ruta=defRuta(list(grf)[men],grf)
##                print(ruta)
                crearTablero(ruta)
                fin=True

    



main()
root = tk.Tk()
#Matrix1 = [[0,0,"Q",0,0,0],[0,0,0,0,0,"Q"],[0,"Q",0,0,0,0],[0,0,0,0,"Q",0],["Q",0,0,0,0,0],[0,0,0,"Q",0,0]]
app = view.Application(master=root,Matrix=tablero)

app.mainloop()



