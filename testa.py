from graphviz import Digraph # pip install graphviz (Para crear el archivo dot por parte de python)
import os
os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz 2.44.1/bin/" #Instalar el compilador de graphviz y pasar el directorio del bin
import pandas as pd

def indexer(x):
    if x == 29:
        return 0
    else:
        return x+1

def d_euc(x,y):
    res = 0
    for i,j in zip(x,y):
        #print("j[",j,"] - i[",i,"] = ",j-i)
        res += ((j-i)**2)
        #print(res)
    return res**(0.5)

def add_queue(q,x):
    q.sort(key=lambda a:a[1])
    if(x[1]<q[len(q)-1][1]):
        q.remove(q[len(q)-1])
        q.append(x)
        q.sort(key=lambda a:a[1]) # 1 5 10

class point:
    # Almacenamiento de 11 ejes dimensionales representados por atributos del tumor
    def __init__(self,data):
        self.atr = data
        self.bng = True
        self.right = None
        self.left = None
    #def _set(data):
        
class kd_tree:
    def __init__(self):
        self.root = None
        self.points = []

    def pass_points(self,pointers):
        if(len(self.points)>1):
            self.points = []
        self.points = pointers
            
    #add_node : Función que crea el root incialemente y llama a la función que inicia la recursividad
    def build_kd(self):
        #print("Entra el punto : ",pointy)
        aux = self.points
        aux.sort(key=lambda x:x[0])
        #print(self.points)
        if(len(aux)%2==0):
            self.root = point(aux[int(len(aux)/2)])
        else:
            self.root = point(aux[int(len(aux)/2)])
        #print("Termino el punto : ",pointy)
        #self._build_kd(self.root.left,aux[0:int(len(aux)/2)],indexer(0))
        #self._build_kd(self.root.right,aux[int(len(aux)/2)+1:int(len(aux))],indexer(0))
        if(self.root.left is not None):
            self._build_kd(self.root.left,aux[0:int(len(aux)/2)],indexer(0))
        else:
            aux_l = aux[0:int(len(aux)/2)]
            aux_l.sort(key=lambda x:x[indexer(0)]) # Ordena por el segundo compente 
            if(len(aux_l)%2==0):
                self.root.left = point(aux_l[int(len(aux_l)/2)])
                #print(node.left.atr)
            else:
                self.root.left = point(aux_l[int(len(aux_l)/2)])
            self._build_kd(self.root.left,aux[0:int(len(aux)/2)],indexer(0))
        
        if(self.root.right is not None):
            self._build_kd(self.root.right,aux[int(len(aux)/2)+1:int(len(aux))],indexer(0))
        else:
            aux_r = aux[int(len(aux)/2)+1:int(len(aux))]
            aux_r.sort(key=lambda x:x[indexer(0)])
            if(len(aux_r)%2==0):
                self.root.right = point(aux_r[int(len(aux_r)/2)])
                #print(self.root.right..atr)
            else:
                self.root.right = point(aux_r[int(len(aux_r)/2)])
            self._build_kd(self.root.right,aux[int(len(aux)/2)+1:int(len(aux))],indexer(0))

    #_add_node : Función que insertará los puntos de manera recursiva similar a un binary tree
    def _build_kd(self,node,pointers,index):
        #print("Lista = ",node,", Puntos = ",pointers,'<',index,'>')
        if(len(pointers)>1):
            aux = pointers
            #print("My aux = ",aux)
            aux.sort(key=lambda x:x[index])
            """if(len(aux)%2==0):
                node = point(aux[len(aux)/2])
            else:
                node = point(aux[int(len(aux)/2)])
            """
            if(node.left is not None):
                self._build_kd(node.left,aux[0:int(len(aux)/2)],indexer(index))
            else:
                aux_l = aux[0:int(len(aux)/2)]
                aux_l.sort(key=lambda x:x[indexer(index)])
                if(len(aux_l)==0):
                    return
                if(len(aux_l)%2==0):
                    node.left = point(aux_l[int(len(aux_l)/2)])
                    print(node.left.atr)
                else:
                    node.left = point(aux_l[int(len(aux_l)/2)])
                self._build_kd(node.left,aux[0:int(len(aux)/2)],indexer(index))
            if(node.right is not None):
                self._build_kd(node.right,aux[int(len(aux)/2)+1:int(len(aux))],indexer(index))
            else:
                aux_r = aux[int(len(aux)/2)+1:int(len(aux))]
                aux_r.sort(key=lambda x:x[indexer(index)])
                if(len(aux_r)==0):
                    return
                if(len(aux_r)%2==0):
                    #print("Lista aux =",aux_r)
                    #print("El índice = ",int(len(aux_r)/2))
                    node.right = point(aux_r[int(len(aux_r)/2)])
                    #print(node.right.atr)
                else:
                    node.right = point(aux_r[int(len(aux_r)/2)])  
        else:
            node = point(pointers[0])
    
    def print_console(self):
        if(self.root != None):
            self._print_console(self.root)
        
    def _print_console(self,node):
       if(node != None):
            self._print_console(node.left)
            #print(node.atr,end='')
            if(node.left!=None):
                print("(",node.left.atr,") <--- ",end='')
            else:
                print("(NULL) <--- ",end='')
            print('[',node.atr,']',end='')
            if(node.right!=None):
                print(" --->(",node.right.atr,")")
            else:
                print(" --->(NULL)")
            self._print_console(node.right)
    def print_tree(self):
        dot = Digraph()
        self.printi(self.root,dot)
        dot.render('grafo',view=False)
    
    def printi(self,node,dot):
        if(node!=None):
            #print(node.atr)
            if(node.right != None):
                dot.node(str(node.right.atr),str(node.right.atr))
                dot.edge(str(node.atr),str(node.right.atr))
            self.printi(node.right,dot)
            dot.node(str(node.atr),str(node.atr))
            if(node.left != None):
                dot.node(str(node.left.atr),str(node.left.atr))
                dot.edge(str(node.atr),str(node.left.atr))
            self.printi(node.left,dot)
            
    def knn(self,pointr,k):
        queue = [([],float('inf'))]*k
        #print(queue)
        d = d_euc(pointr,self.root.atr)
        add_queue(queue,(self.root.atr,d))
        dr = d_euc(self.root.atr,self.root.right.atr)
        dl = d_euc(self.root.atr,self.root.left.atr)
        nodo = None
        if(dr<dl):
            nodo = (self.root.right.atr,dr)
            add_queue(queue,nodo)
            self._knn(pointr,self.root.right,queue)
        else:
            nodo = (self.root.left.atr,dl)
            add_queue(queue,nodo)
            self._knn(pointr,self.root.left,queue)
        return queue
    def _knn(self,pointr,node,queue):
        dr = None
        dl = None
        if(not(node.right!=None and node.left != None)):
            dr = d_euc(pointr,node.right.atr)
            dl = d_euc(pointr,node.left.atr)
            nodo = None
            if(dr<dl):
                nodo = (node.right.atr,dr)
                add_queue(queue,nodo)
                self._knn(pointr,node.right,queue)
            else:
                nodo = (node.left.atr,dl)
                add_queue(queue,nodo)
                self._knn(pointr,node.left,queue)
        elif(node.right!=None):
            dr = d_euc(pointr,node.right.atr)
            add_queue(queue,(node.right.atr,dr))
            #self._knn(pointr,node.right.atr)
            #self._knn()
        elif(node.left!=None):
            dr = d_euc(pointr,node.left.atr)
            add_queue((node.left.atr),dr)

data_points = []
file = pd.read_csv("KNNAlgorithmDataset.csv")
nfile = file[["diagnosis","radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]]
data = pd.DataFrame(nfile,columns=["diagnosis","radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"])
for i in range(len(data)):
    temp = []
    temp.append(data.loc[i,'radius_mean'])
    temp.append(data.loc[i,'texture_mean'])
    temp.append(data.loc[i,'perimeter_mean'])
    temp.append(data.loc[i,"area_mean"])
    temp.append(data.loc[i,"smoothness_mean"])
    temp.append(data.loc[i,"compactness_mean"]),
    temp.append(data.loc[i,"concavity_mean"])
    temp.append(data.loc[i,"concave points_mean"])
    temp.append(data.loc[i,"symmetry_mean"])
    temp.append(data.loc[i,"fractal_dimension_mean"])
    temp.append(data.loc[i,"radius_se"])
    temp.append(data.loc[i,"texture_se"])
    temp.append(data.loc[i,"perimeter_se"])
    temp.append(data.loc[i,"area_se"])
    temp.append(data.loc[i,"smoothness_se"])
    temp.append(data.loc[i,"compactness_se"])
    temp.append(data.loc[i,"concavity_se"])
    temp.append(data.loc[i,"concave points_se"])
    temp.append(data.loc[i,"symmetry_se"])
    temp.append(data.loc[i,"fractal_dimension_se"])
    temp.append(data.loc[i,"radius_worst"])
    temp.append(data.loc[i,"texture_worst"])
    temp.append(data.loc[i,"perimeter_worst"])
    temp.append(data.loc[i,"area_worst"])
    temp.append(data.loc[i,"smoothness_worst"])
    temp.append(data.loc[i,"compactness_worst"])
    temp.append(data.loc[i,"concavity_worst"])
    temp.append(data.loc[i,"concave points_worst"])
    temp.append(data.loc[i,"symmetry_worst"])
    temp.append(data.loc[i,"fractal_dimension_worst"])
    if(data.loc[i,"diagnosis"] == 'M'):
        temp.append(0)
    else:
        temp.append(1)
    data_points.append(tuple(temp))

kd = kd_tree()
#popopoints = [(3,6,12,1),(17,15,3,2),(13,14,5,3),(6,12,6,4),(9,1,9,5),(2,7,0,6),(10,19,14,7),(17,1,17,8),(1,19,2,9),(11,9,20,10)]
kd.pass_points(data_points)
kd.build_kd()
#kd.print_console()
data_diag = kd.knn((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,0),5)
#print(type(data_diag[0][0][31]))
counter = 0
for j in data_diag:
    if(j[0][30][0] == 0):
        counter += 1
if((counter / len(data_diag))>0.5):
    print("Maligno")
else:
    print("Benigno")
