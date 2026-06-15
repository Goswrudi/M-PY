#  1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class twoDvector():
    def __init__(self, i, j):
        self.i = i 
        self.j = j 

    def output(self):
        print(f"The i vector is {self.i} and j vector is {self.j}")


    def addition(self):
        solution = (self.i+self.j) 
        print(f"The Adittion of 2D-Vector Spaces {self.i}î & {self.j}ĵ is = {solution} îĵ  : ")


# Making the 3-D Vector 

class threeDvector(twoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k 

    def output(self):
        print(f"The vector i is {self.i}, The vector j is {self.j}, The vector k is {self.k}") 

    def addition(self):
        solution = (self.i+self.j+self.k)
        print(f"The Addition of 3D-vector Spaces {self.i}î + {self.j}ĵ  + {self.k}k̂ = {solution} îĵk̂ : ") 


# Calling The 2D Vector Space 

x = twoDvector(1, 2)
x.output()
x.addition()

# Calling The 3D Vector Space

y =threeDvector(5, 6, 7) 
y.output()
y.addition() 

# Now Make a Sum for A 2D Vector,  which add  them .

# def addition(self):
        # solution = (self.i+self.j) 
        # print(f"The Solution of twoDvector {self.i} & {self.j} is {solution})

# addition()

# NOTE : Make sure the output will represent withh
#                      î  ĵ  k̂ 

# Now for A 3D Vector

# def addition(self):
#        solution = (self.i+self.j+self.k)
        #print(f"The Addition of 3D-vector Spaces {self.i}î + {self.j}ĵ  + {self.k}k̂ {solution} : ")
 