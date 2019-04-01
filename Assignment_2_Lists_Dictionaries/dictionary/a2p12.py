 #python code to generate grade using dictionary. Dictionary should have student names as keys (assuming names are unique) 
 ##and subject_name and mark as value. There are 5 subjects for each student. Marks should be converted to grades (90 – 100 A+, 80-89 A etc).

def a2p12():

	dict1 = {}
	dict2 = {}
	marks ={}

	s = int(input("enter the no of students:"))
	for ch1 in range(s):
		name = input("Name of student:")
		
		for ch2 in range(5):
			sname = input("enter subject name:")
			smark = int(input("enter the marks:"))

			if 90<smark<=100:
				marks.update({sname:'A+'})
			elif 80<smark<=89:
				marks.update({sname:'A'})
			elif 70<smark<=79:
				marks.update({sname:'B+'})
			elif 60<smark<=69:
				marks.update({sname:'B'})
			elif 50<smark<=59:
				marks.update({sname:'C+'})
			elif 0<smark<=49:
				marks.update({sname:'F'})
			else:
				print("invalid marks")

		dict2.update({name:marks})

	print(dict2)

a2p12()












