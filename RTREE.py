import math
B=3
def take_first(point):
    return point.x
def take_second(point):
    return point.y
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return "point(x={}, y={})".format(self.x, self.y)

class mbr:
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def constains(self,point):
        return (point.x >= self.x - self.w and point.x <= self.x + self.w 
		       and point.y >= self.y - self.h and point.y <= self.y + self.h)
    
class Node:
    def __init__(self):
        self.children=[]
        self.data_points=[]
        self.padre= None
        self.min_bound=[-1,-1,-1,-1] #x1,y1,x2,y2
    
    def is_leaf(self):
        return(self.children.__len__()==0)
    
    def is_overflow(self):
        if self.is_leaf():
            return(self.data_points.__len__()>B)
        else:
            return(self.children.__len__()>B)
    def is_root(self): 
        return(self.padre is None)
    
    def add_point(self,p):
        self.data_points.append(p)
        
    def num_points(self):
        return len(self.data_points)
    def sort_points_x(self):
        return sorted(self.data_points,key=take_first)
    def sort_points_y(self):
        return sorted(self.data_points,key=take_second)
    def get_perimetro(self):
        #distancia de los lados
        return((self.min_bound[2]-self.min_bound[0])+(self.min_bound[3]-self.min_bound[1]))
    
class rtree:
    def __init__(self):
        self.root=Node()
    def split(self,n):
        min_perimetro=99999999
        m=n.num_points()
        Spx=n.sort_points_x()
        node1=Node()
        node2=Node()
        for i in range(math.ceil(0.4 * B), m - math.ceil(0.4 * B)):
            node1.children=Spx[0:i]
            node2.children=Spx[i:m]
            perimetro=node1.get_perimetro()+node2.get_perimetro()
            if min_perimetro>perimetro:
                min_perimetro=perimetro
        Spy=n.sort_points_y()
        for i in range(math.ceil(0.4 * B), m - math.ceil(0.4 * B)):
            node1.children=Spy[0:i]
            node2.children=Spy[i:m]
            perimetro=node1.get_perimetro()+node2.get_perimetro()
            if min_perimetro>perimetro:
                min_perimetro=perimetro
        return node1,node2
    def update_mbr(self,n):
        x_c,y_c=[],[]
        if len(n.children)==0:
            for i in n.data_points:
                x_c=i.x
            for j in n.data_points:
                y_c=j.y
        else:
            x_c =[i.min_bound[0] for i in n.children] + [j.min_bound[2] for j in n.children]
            y_c =[i.min_bound[1] for i in n.children] + [j.min_bound[3] for j in n.children]
        n.min_bound[0]=min(x_c)
        n.min_bound[1]=min(x_c)
        n.min_bound[2]=min(y_c)
        n.min_bound[3]=min(y_c)
    def handle_overflow(self,n): #n es el nodo
        node1,node2=self.split(n)
        if n.is_root():
            root=Node()
            self.insert_child(root,node1)
            self.insert_child(root,node2)
            self.root=root
        else:
            w=n.padre
            self.update_mbr(w)
            self.insert_child(w,node2)
            if w.is_overflow():
                self.handle_overflow(w)
        print("estamos en handle")
    def calcula_incremento_perimetro(self,n,p): # cadad vez que se inserta un punto se actualiza el perimetro
        x1=min([n.min_bound[0],n.min_bound[2],p.x])
        x2=max([n.min_bound[0],n.min_bound[2],p.x])
        y1=min([n.min_bound[1],n.min_bound[3],p.y])
        y2=max([n.min_bound[1],n.min_bound[3],p.y])
        incremento=(x2-x1)+(y2-y1)-n.get_perimetro()
        return incremento

    def choose_subtree(u,p):
        min_perimetro= 99999999
        best_node=None
        if u.is_leaf():
            return u
        else:
            for i in u.children:
                if min_perimetro>self.calcula_incremento_perimetro(i,p):
                    min_perimetro=self.calcula_incremento_perimetro(i,p)
                    best_node=i
        print("este es el mejor",best_node.data_points)
        return best_node

    def insert(self,u,p): #u es el nodo o raiz y p es el point
        
        if u.is_leaf():
            u.add_point(p)
            if u.is_overflow():
                self.handle_overflow(u)#manejo el desbordamiento
        else:
            v=choose_subtree(u,p)
            insert(v,p)
        
        print("insertado")

    def insert_child(self,node_parent,node_child):
        node_parent.children.append(node_child)
        node_child.padre=node_parent
    
    def intersect(self,node,q):
        c1_x,c1_y=(node.min_bound[2]+node.min_bound[0])*0.5,(node.min_bound[3]+node.min_bound[1])*0.5
        len1,b_1=node.min_bound[2]-node.min_bound[0],node.min_bound[3]-node.min_bound[1]
        len2,b_2=q[2]-q[0],q[3]-q[1]
        c2_x,c2_y=0.5*(q[2]+q[0]),0.5*(q[3]+q[1])
        return (abs(c1_x-c2_x)<=(len1+len2)/2 and abs(c1_y-c2_y)<=(b_1+b_2)/2)
    def range_query(self,u,r):
        points_in_r=[]
        if u.is_leaf():
            for p in u.data_points:
                if r[0]<=p.x<=r[2] and r[1]<=p.y<=r[3]:
                    points_in_r.append(p)
            return points_in_r
        else:
            for i in u.children:
                if self.intersect(u,r):
                    points_in_r += self.range_query(u,r)
            return points_in_r
        print("Estan en r",points_in_r)

            

r=[2,8,6,7]
p1=point(8,3)
p2=point(4,5)
p3=point(2,1)
p4=point(0,1)
p5=point(1,6)
p6=point(4,3)
p7=point(3,7)
p8=point(2,9)
p9=point(6,8)
p10=point(2,4)
no=Node()
n1=Node()
rt= rtree()
rt.insert(no,p1)
rt.insert(no,p2)
rt.insert(no,p3)
rt.insert(no,p4)
rt.insert(no,p5)
print("segundo ********************* ")
rt.insert(n1,p6)
rt.insert(n1,p7)
rt.insert(n1,p8)
rt.insert(n1,p9)
rt.insert(n1,p10)
rt.range_query(no,r)
