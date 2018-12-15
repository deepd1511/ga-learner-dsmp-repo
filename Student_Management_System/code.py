# --------------
# Code starts here

class_1 = ['Geoffrey Hinton',"Andrew Ng","Sebastian Raschka","Yoshua Bengio"]
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

new_class = class_1+class_2

print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
# Code ends here


# --------------
# Code starts here

courses = {}
courses['Math']=65
courses['English']=70
courses['History']=80
courses['French']= 70
courses['Science'] = 60

total = sum(courses.values())
print(total)
percentage = (total/500)*100
print(percentage)
# Code ends here


# --------------
# Code starts here
mathematics = {}
mathematics['Geoffrey Hinton']=78
mathematics['Andrew Ng'] = 95
mathematics['Sebastian Raschka'] = 65
mathematics['Yoshua Benjio'] = 50
mathematics['Hilary Mason'] =70
mathematics['Corinna Cortes']=66
mathematics['Peter Warden']=75

topper = max(mathematics,key = mathematics.get)
print(topper)


# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


# Code starts here
first_name =topper.split(" ")[0]
last_name = topper.split(" ")[1]

full_name = last_name+ " "+first_name
print(full_name)
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


