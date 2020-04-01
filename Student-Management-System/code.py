# --------------
# Suraj Code starts here
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

#Concatenate classes and creation of new class 
new_class = class_1 + class_2
print(new_class)

#adding a new name
new_class.append('Peter Warden')
print(new_class)

#removing a wrong name
new_class.remove('Carla Gentry')
print(new_class)

# Code ends here


# --------------
#Suraj Code starts here
#Creating Dictionary of Geoffrey Hinton 
#c = {"course_1": "Maths", "course_2": "English", "course_3": "History", "course_4": "French", "course_5": "Science"}
courses = {'Math':65,
'English':70,
'History':80,
'French':70,
'Science':60}

#Adding all the marks scored out of 100
total = sum(courses.values())
print(total)

#calculating the percentage
percentage = float(total)*(100/500)
# percentage = total * (100/500)
print(percentage)

# Code ends here


# --------------
# Code starts here
mathematics = {'Geoffrey Hinton' : 78,
'Andrew Ng':95,
'Sebastian Raschka':65,
'Yoshua Benjio':50,
'Hilary Mason':70,
'Corinna Cortes':66,
'Peter Warden':75}
max_marks_scored = max(mathematics,key = mathematics.get)
topper = max_marks_scored
print (topper)



# Code ends here  


# --------------
# Given string
topper = 'andrew ng'

# Code starts here
first_name = "andrew"
last_name = "ng"
full_name = (last_name + " " + first_name)
print(full_name)

certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


