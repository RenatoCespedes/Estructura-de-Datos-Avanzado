import cv2
import numpy as np
class Color(object):
    def __init__(self, red=0, green=0, blue=0,alpha=None):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def imprimir(self):
        print(self.red)
        print(self.green)
        print(self.blue)


def convertir(num):
    if(num[0] == '1'):
        if (num[1] == '1'):
            if (num[2]=='1'):
                return 7
            else:
                return 6
        else:
            if (num[2]=='1'):
                return 5
            else:
                return 4
    else:
        if (num[1] == '1'):
            if (num[2]=='1'):
                return 3
            else:
                return 2
        else:
            if (num[2]=='1'):
                return 1
            else:
                return 0

class OctreeNode(object):
    def __init__(self,level,parent):
        self.color = Color(0, 0, 0)
        self.contadorpixel = 0
        self.children = [None for _ in range(8)]
        
        if level < OctreeQuantizer.MAX_PROFUNDIDAD - 1:
            parent.add_level_node(level, self)
    def add_color(self,color,level,parent):
        print("nivel: ",level)
        if level >= OctreeQuantizer.MAX_PROFUNDIDAD:
            #print("R: ",self.color.red)
            self.color.red += color.red
            #print("G: ",self.color.green)
            self.color.green += color.green
            #print("B: ",self.color.blue)
            self.color.blue += color.blue
            #print("COUNT: ",self.pixel_count)
            self.contadorpixel += 1
            return
        indice = self.get_indiceColorByLevel(color,level)
        print(indice)
        if not self.children[indice]:
            self.children[indice] = OctreeNode(level, parent)
        self.children[indice].add_color(color, level + 1, parent)
    
    
    def get_indiceColorByLevel(self,color,level):
        r = color.red
        g = color.green
        b = color.blue
        r = bin(r)[2:].zfill(8)
        g = bin(g)[2:].zfill(8)
        b = bin(b)[2:].zfill(8)
        aux = ""
        aux = aux+r+g+b
        indice = convertir(aux)
        return indice


class OctreeQuantizer(object):
    MAX_PROFUNDIDAD = 8

    def __init__(self):
       
        self.levels = {i: [] for i in range(OctreeQuantizer.MAX_PROFUNDIDAD)}
        self.root = OctreeNode(0, self)
    def add_level_node(self, level, node):
        
        self.levels[level].append(node)
    
    def add_color(self, color):
        
        self.root.add_color(color, 0, self)


img = cv2.imread('hello2.jpg',1)
img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
width = img.shape[0]
height= img.shape[1]
#ret, bw_img = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
#print(*img[12,12])

oct = OctreeQuantizer()
'''
for i in range(height):
    for j in range (width):
        #print(bw_img[i,j])
        #print(bin(img[i,j][0])
        oct.add_color(Color(*img[i,j]))
        
 '''  
oct.add_color(Color(90,113,157))    
