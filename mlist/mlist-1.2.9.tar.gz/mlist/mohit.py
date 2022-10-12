import csv

class Mlist(list):

	def __sub__(self,other):
		return (each for each in self if each not in other)
		
	def dupr(self):
		new_list1 = self 
		d1 = dict(((each,"") for each in new_list1 ))
		self.clear()
		self.extend(d1.keys())

		
	def file(self, file1):
		fr = open(file1,"r")
		self.extend((line.strip() for line in fr))
		fr.close()
		#return self
		
	def removeall(self,item):
		for i in range(self.count(item)):
			self.remove(item)
		#return self
		
	def indexall(self,item):
		list1 = []
		len1 = len(self)
		a = -1
		for i in range(len1):
			if item in self[a+1:]:
				a = self.index(item, a+1)
				if a!=-1:
					list1.append(a)
			else:
				break
		return list1
		
	def diff(self,other, first=None, second=None):
		self1 = self 
		other1 = other
		if first is not None :
			self1=list(map(lambda x: x[first], self))

		if second is not None:
			other1 = list(map(lambda x: x[second],other ))
			
		list2= Mlist(self1.index(each) for each in self1 if each not in other1)
		#print (list2, first, second)
		list2.sort(reverse=1)
		for i in list2:
			del self[i]
		#return self
		
	def diffshow(self,other, first=None, second=None):
		self1 = self 
		other1 = other
		if first is not None :
			self1=list(map(lambda x: x[first], self))

		if second is not None:
			other1 = list(map(lambda x: x[second],other ))
			
		list2= Mlist(self1.index(each) for each in self1 if each not in other1)
		#print (list2, first, second)
		list2.sort()
		diff =Mlist([self[i] for i in list2])
		return diff
		
	def club(self,other, first=None, second=None):
		dict1 = {}
		if first is not None :
			self1=list(map(lambda x: x[first], self))

		if second is not None:
			other1 = list(map(lambda x: x[second],other ))
		
		list2= Mlist((self1.index(each),other1.index(each)) for each in other1 if each in self1)
		#print (list2, first, second)
		for k,v in list2:
			del other[v][second]
			self[k].extend(other[v])
		

	def lookup(self,other, first=None, second=None):
		self1 = self 
		other1 = other
		if first is not None :
			self1=list(map(lambda x: x[first], self))

		if second is not None:
			other1 = list(map(lambda x: x[second],other ))
			
		list2= Mlist(self1.index(each) for each in other1 if each in self1)
		#print (list2, first, second)
		list2.sort()
		diff =Mlist([self[i] for i in list2])
		return diff			

	
	def csv_read(self,file_name):
		with open(file_name) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			data = [each for each in csv_reader]
			#data =[[[each[0]].extend([eval(i) for i in each[1:]])] for each in csv_reader]
			#return (data)
			self.extend(data)
			#return self
			
			
	def csv_write(self,file_name):
		with open(file_name, 'w',newline='') as file:
			writer = csv.writer(file)
			writer.writerows(self)

	def file_write(self,file_name):
		fr = open(file_name, "w")
		fr.writelines(self)
		fr.close()
		
if __name__ == "__main__":
	list1  = Mlist([[1,7],[3,4],[9,8]])
	list2 = Mlist([5,7,8])
	#print (diff(list1 - list2) )
	list1.diff(list2,1)
	#print (list1)