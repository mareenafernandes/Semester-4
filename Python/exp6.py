import numpy as np

class myMatrix:

	def __init__(self, rows=1, cols=1):
		self.rows = rows
		self.cols = cols
		self.matrix = np.random.random((rows, cols))

	def add(self, add_matr):
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				self.matrix[i][j] = self.matrix[i][j] + add_matr.matrix[i][j]
	
	def subtr(self, subtr_matr):
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				self.matrix[i][j] = self.matrix[i][j] - subtr_matr.matrix[i][j]

	def mult(self, multi_matr):
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				for k in range(0, self.cols):
					self.matrix[i][j] = self.matrix[i][k] * multi_matr.matrix[k][j]	
	
	def display_matr(self):
		print(self.matrix)
		print("\n")

	def gen_inverse(self):
		inv_obj = myMatrix()
		inv_obj.matrix = np.linalg.inv(self.matrix)
		return inv_obj

class sqMatrix(myMatrix):

	def __init__(self, rows=1, cols=1):
		super().__init__(rows, cols)
		if self.rows != self.cols:
			print("Not a Square Matrix!!")

	def gen_inverse(self):
		inv_obj = sqMatrix()
		inv_obj.matrix = np.linalg.inv(self.matrix)
		return inv_obj

	def eigenvals(self):
		print(np.linalg.eig(self.matrix))
		
matr1 = myMatrix(3,3)
matr2 = myMatrix(3,3)

print("Matrix 1: ")
matr1.display_matr()
print("Matrix 2: ")
matr2.display_matr()

print("Matrix 1 after adding to Matrix 2: ")
matr1.add(matr2)
matr1.display_matr()

print("Matrix 2 after subtracting matrix 1 from it: ")
matr2.subtr(matr1)
matr2.display_matr()

print("Matrix 1 X Matrix 2")
matr1.mult(matr2)
matr1.display_matr()

print("Matrix 2 inverse: ")
inv_obj = matr2.gen_inverse()
inv_obj.display_matr()

print("Square Matrix 1: ")
sqmatr1 = sqMatrix(3,3)
sqmatr1.display_matr()

print("Square Matrix 1 Inverse: ")
sqmatr12inv = sqmatr1.gen_inverse()
sqmatr12inv.display_matr()

print("Square Matrix 1 Eigen Values: ")
sqmatr1.eigenvals()
