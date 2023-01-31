
class CamelCase(object):
	# create and configure log
	
	def __init__(self, intake = "C;M;   The lordOfThe Rings   ", newString = "", part1 = "", part2 = ""):
		""" camelCase __init__ """

		self.intake = intake
		self.newString = newString
		self.part1 = part1
		self.part2 = part2 

		self.part1 = intake[0]
		self.part2 = intake[2]
		self.newString = intake[4:]

	# remove all ()
	def removePar(self):
		string = self.newString
		temp = ""
		# build temp string by looping
		for i in string:
			if i == "(" or i == ")":
				temp = temp
			else:
				temp = "{}{}".format(temp, i)
		self.newString = temp
	

	# add a space before capitalized letters
	def preCap(self):
		string = self.newString
		temp = ""
		# build temp string by looping
		for i in string:
			if i.isupper() == True:
				temp = "{} {}".format(temp, i)
			else:
				temp = "{}{}".format(temp, i)
		# update self.newString and strip
		self.newString = temp.strip()
	# varify all alphas following spaces are cap
	def postSpace(self):
		string = self.newString
		string = string.strip()
		temp = ""
		# build temp string by looping
		for i in range(len(string)):
			if string[i - 1] == " " and string[i].isalpha() == True:
				temp = "{}{}".format(temp, string[i].upper())
			else:
				temp = "{}{}".format(temp, string[i])
		# update self.newString		
		self.newString = temp
	
	# remove repeated spaces
	def singleSpace(self):
		string = self.newString
		string = string.strip()
		temp = ""
		n = len(string)
		
		# build temp string by looping
		for i in range(n):
			if string[i] == " " and string[i + 1] == " ":
				continue
			else:
				temp = "{}{}".format(temp, string[i])
		# update self.newString
		self.newString = temp
	# remove all spaces
	def noSpace(self):
		string = self.newString
		string = string.strip()
		temp = ""
		
		# build temp string by looping
		for i in string:
			if i == " ":
				temp = temp
			else:
				temp = "{}{}".format(temp, i)
		self.newString = temp.strip()


	# if part1 is S
	def isS(self):
		string = self.newString
		
		self.removePar()
		self.preCap()
		self.postSpace()
		self.singleSpace()
		self.newString = self.newString.lower()
	
	# if part2 is C
	def isC(self):
		string = self.newString
		
		self.removePar()
		self.preCap()
		self.postSpace()
		self.noSpace()
		
		string = self.newString
		string = string[0].upper() + string[1:]
		self.newString = string
	
	# if part2 is V
	def isV(self):
		string = self.newString
		
		self.removePar()
		self.preCap()
		self.postSpace()
		self.noSpace()
		string = self.newString
		string = string[0].lower() + string[1:]
		self.newString = string

	# if part2 is M
	def isM(self):
		string = self.newString
		
		self.removePar()
		self.preCap()
		self.postSpace()
		self.noSpace()
		
		string = self.newString
		string = string[0].lower() + string[1:] + "()"
		self.newString = string

	# choose is S C V M functions by part2
	def choose(self):
		part1 = self.part1
		part2 = self.part2
		if part1 == "S":
			self.isS()
		elif part2 == "C":
			self.isC()
		elif part2 == "V":
			self.isV()
		elif part2 == "M":
			self.isM()
		else:
			print("make sure your string is in the correct format; _;_;fjdkljfdkl")


def main():
	try:
		while True: 
			g = CamelCase(intake = input())
			g.choose()
			print(g.newString)
	except:
		exit()	


#	while True: 
#		g = CamelCase(intake = input())
#		g.choose()
#		print(g.newString)
		
if __name__ == "__main__":
	main()


