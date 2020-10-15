import vtk 
import random
from vtk.util.colors import tomato

class Point:
	def __init__ (self, x, y, z, userData=None): #Creacion del punto con eje x y z
		self.x = x
		self.y = y
		self.z = z
		self.flag = False       #
		self.userData = userData #Dato

class Rectangle:
	def __init__ (self ,x,y,z,w,h,f):
		self.x = x  #center
		self.y = y
		self.z = z
		self.w = w  #half width
		self.h = h  #half height
		self.f = f  #frente
        
# verifica si este objeto contiene un objeto Punto
	def contains (self,point):
		if (point.x <= self.x+self.w and point.x >= self.x-self.w and point.y <= self.y+self.h  and 
            point.y >= self.y-self.h and point.z <= self.z + self.f and point.z >= self.z-self.f):
            #point.flag=True
			print(point.x)
			print(point.y)
			print(point.z)
			return True
		return False
	
# verifica si este objeto se intersecta con otro objeto Rectangle
	def intersects (self,range):
		if(range.x - range.w >self.x + self.w  or range.x +range.w < self.x -self.w   or
			range.y - range.h >self.y + self.h or range.y +range.h < self.y -self.h or 
          range.z -range.f >self.z + self.f or range.z + range.f < self.z - self.f):
			return False
		return True
    
    
class OcTree:
	def __init__(self,boundary , n ):
		self.boundary = boundary #Rectangle
		self.capacity = n #capacidad máxima de cada cuadrante
		self.points = [] #vector, almacena los puntos a almacenar
		self.divided = False
		self.hijos = []
#divide nuestro quadtree en 4 quadtrees
	def subdivide (self):
		x = self.boundary.x
		y = self.boundary.y
		z = self.boundary.z
		w = self.boundary.w/2
		h = self.boundary.h/2
		f = self.boundary.f/2
        
		no = Rectangle(x-w,y-h,z-f,w,h,f)
		ne = Rectangle(x+w,y-h,z-f,w,h,f)
		so = Rectangle(x-w,y+h,z-f,w,h,f)
		se = Rectangle(x+w,y+h,z-f,w,h,f)
        
		fno = Rectangle(x-w,y-h,z+f,w,h,f)
		fne = Rectangle(x+w,y-h,z+f,w,h,f)
		fso = Rectangle(x-w,y+h,z+f,w,h,f)
		fse = Rectangle(x+w,y+h,z+f,w,h,f)  

		sonNO = OcTree(no, self.capacity)
		sonNE = OcTree(ne, self.capacity)
		sonSO = OcTree(so, self.capacity)
		sonSE = OcTree(se, self.capacity)
		fsonNO = OcTree(fno, self.capacity)
		fsonNE = OcTree(fne, self.capacity)
		fsonSO = OcTree(fso, self.capacity)
		fsonSE = OcTree(fse, self.capacity)
		self.hijos.append(sonNO)
		self.hijos.append(sonNE)
		self.hijos.append(sonSO)
		self.hijos.append(sonSE)
		self.hijos.append(fsonNO)
		self.hijos.append(fsonNE)
		self.hijos.append(fsonSO)
		self.hijos.append(fsonSE)
		self.divided = True
#algoritmo
#1.- Se crean cuatro QuadTrees, uno por cada cuadrante (qt_northeast, qt_northwest,
	#	qt_southeast, qt_southwest() tener cuidado con el tamaño (boundary) de cada Quadtree.
#2.- Asignar los QuadTree creados a cada hijo (this.northeast, this.northwest,
	#	this.southeast, this.southwest(), ejemplo:
# this.northeast = qt_northeast;
#3.- Cambiar el flag this.divided a true
	def insert(self,p):
		if(self.boundary.contains(p)==False):
			return
		if (len(self.points) < self.capacity):
			self.points.append(p)
		else:
			if(self.divided==False):
				self.subdivide()
			for i in range(0,8):
				self.hijos[i].insert(p)

            
	def query(self,ranges, found):
		if(self.boundary.intersects(ranges)==False):
			return
		for i in self.points:
			if(ranges.contains(i)):
				found.append(i)
		if(self.divided):
			for i in range(0,8):
				self.hijos[i].query(ranges,found)
            
	def rect(self,ren,x,y,z,xx,yy,zz,flag=0):
		colors = vtk.vtkNamedColors() 
		
		
		cube = vtk.vtkCubeSource()
		cube.SetBounds(x-xx,x+xx,y-yy,y+yy,z-zz,z+zz)
		cube.Update()
		cubeMapper = vtk.vtkPolyDataMapper()
		cubeMapper.SetInputData(cube.GetOutput())
		cubeActor = vtk.vtkActor()
		cubeActor.SetMapper(cubeMapper)
		if(flag==1):
			cubeActor.GetProperty().SetColor(colors.GetColor3d("red"))
			cubeActor.GetProperty().SetOpacity(0.5)
		else:
			cubeActor.GetProperty().SetColor(colors.GetColor3d("green"))
			cubeActor.GetProperty().SetOpacity(0.3)
		ren.AddActor(cubeActor)
		ren.ResetCamera()
		ren.GetActiveCamera().Azimuth(30)
		ren.GetActiveCamera().Elevation(30)
		ren.ResetCameraClippingRange()
		ren.SetBackground(colors.GetColor3d("white"))


		
        
	def point(self,ren,x,y,z,flag=0):
		colors = vtk.vtkNamedColors() 
        
		
        
		sphereSource = vtk.vtkSphereSource()
		sphereSource.SetCenter(x, y, z)
		sphereSource.SetRadius(10)
        
		mapper = vtk.vtkPolyDataMapper()
		mapper.SetInputConnection(sphereSource.GetOutputPort())
		actor = vtk.vtkActor()
    
		actor.SetMapper(mapper)
		if(flag==1):
			actor.GetProperty().SetColor(colors.GetColor3d("red"))
		else:
			actor.GetProperty().SetColor(colors.GetColor3d("yellow"))
		ren.ResetCamera()
		ren.GetActiveCamera().Azimuth(30)
		ren.GetActiveCamera().Elevation(30)
		ren.ResetCameraClippingRange()
		ren.SetBackground(colors.GetColor3d("white"))
        
		ren.AddActor(actor)

	def show(self,ren):

		self.rect (ren,self.boundary.x , self.boundary.y , self.boundary.z , self.boundary.w, self.boundary.h,self.boundary.f)
		if(self.divided):
			for i in range(0,8):
				self.hijos[i].show(ren)

		for i in self.points:
			self.point(ren,i.x,i.y,i.z)
		#print("no entre")
		'''dato=random.random()*400
		dato1=random.random()*400
		dato2=random.random()*400
		ranges = Rectangle(dato,dato1,dato2,10,10,10)
		self.rect(ren,ranges.x,ranges.y,ranges.z,ranges.w,ranges.h,ranges.f,1)
		pointss = []
		self.query(ranges,pointss)
		for p in pointss:
			self.point(p.x,p.y,p.z,1)'''
        
def setup():
	ren = vtk.vtkRenderer()
	renWin = vtk.vtkRenderWindow()
	renWin.SetWindowName("OcTree")
	renWin.AddRenderer(ren)
	iren = vtk.vtkRenderWindowInteractor()
	iren.SetRenderWindow(renWin)
	renWin.SetSize(600, 600)
   
	iren.Initialize()
	cubo = Rectangle(200,200,200,200,200,200)
	octcubo = OcTree(cubo,4)
	for i in range(100):
		p= Point(random.random()*400,random.random()*400,random.random()*400)
		octcubo.insert(p)
	octcubo.show(ren)
	iren.Start() 
    
setup()
