class User:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		print("создался новый экземпляр User")

	def sayName(self):
		print("мое имя :", self.first_name)

	def sayFam(self):
		print("моя фамилия :", self.last_name)

	def sayName_Fam(self):
		print("меня зовут :", self.first_name, " ", self.last_name)
		
