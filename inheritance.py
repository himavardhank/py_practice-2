class A(object):
	def m1(self):
		print("from A m1 method")
class B(A):
	def m1(self):
		print("from B m1 method")

class C(A,B):
	def m1(self):
	    print("from c m1 method")
	    
c=C()
c.m1()
