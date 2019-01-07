import networkx as nt
import math
import numpy as np
import random
p=20
size=10
n1=10
n2=10
group_size=n1*n2

def zdobadz_wiedze(G,i,field):
    x=random.randrange(size);
    y=random.randrange(size);
    if(field[x,y]>0):
        nt.get_node_attributes(G,'agent')[i].knowledge[x,y]=field[x,y]-1
        nt.get_node_attributes(G,'agent')[i].hypothesis[x,y]=field[x,y]-1
        nt.get_node_attributes(G,'agent')[i].przypisanie=(x,y)
    

class agent:
    def __init__(self,G):
        self.przypisanie=None
        self.knowledge=np.zeros((size,size),dtype=int)
        self.hypothesis=np.zeros((size,size),dtype=int)

def powieksz_wiedze(G,group_size,size):
    for i in range(group_size):
        if(nt.get_node_attributes(G,'agent')[i].przypisanie!=None):
            indeks_sasiada=0
            for j in range(size):
                for k in range(size):
                    while(nt.get_node_attributes(G,'agent')[i].knowledge[j,k]>0 and indeks_sasiada<len(list(nt.neighbors(G,i)))):
                        if(nt.get_node_attributes(G,'agent')[list(nt.neighbors(G,i))[indeks_sasiada]].przypisanie==None):
                            nt.get_node_attributes(G,'agent')[i].knowledge[j,k] = nt.get_node_attributes(G,'agent')[i].knowledge[j,k]-1
                            nt.get_node_attributes(G,'agent')[list(nt.neighbors(G,i))[indeks_sasiada]].przypisanie=(i,k)
                        indeks_sasiada=indeks_sasiada+1
            for j in range(len(list(nt.neighbors(G,i)))):
                nt.get_node_attributes(G,'agent')[list(nt.neighbors(G,i))[j]].knowledge
                nt.get_node_attributes(G,'agent')[i].hypothesis=np.logical_or(nt.get_node_attributes(G,'agent')[i].knowledge,nt.get_node_attributes(G,'agent')[list(nt.neighbors(G,i))[j]].knowledge)
    for i in range(group_size):
        nt.get_node_attributes(G,'agent')[i].knowledge=nt.get_node_attributes(G,'agent')[i].hypothesis.copy()
    sum=0
    for i in range(group_size):
        if(nt.get_node_attributes(G,'agent')[i].przypisanie!=None):
            sum=sum+1
    print(sum)
    

G=nt.caveman_graph(n1,n2)
field=np.zeros((size,size),dtype=int)
for i in range(p):
    x=random.randrange(size)
    y=random.randrange(size)
    field[x,y]=4
valu={}
for i in range(group_size):
    valu[i]=agent(G)
nt.set_node_attributes(G,valu,'agent')
#print(type(G))
#print(nt.neighbors(G,5))
print(field)
for j in range(7):
    for i in range(group_size):
        if (nt.get_node_attributes(G,'agent')[i].przypisanie==None):
            zdobadz_wiedze(G,i,field)
    #powiększanie wiedzy
    sum=0
    for i in range(group_size):
        if(nt.get_node_attributes(G,'agent')[i].przypisanie!=None):
            sum=sum+1
    print(sum)
    powieksz_wiedze(G,group_size,size)
