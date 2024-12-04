import numpy as np

data_type = [('name' , 'S15') , ('class' , int) , ('height' , float)]

student_details = [('Ayaan' , 5 , 48.5) , ('Devansh' , 6 , 52.5) , ('Kavya' , 5 , 40.10) , ('Pakhi' , 6 , 50.11)]

students = np.array(student_details , dtype = data_type)

print("Original array : ")
print(students)

print()

print("Sort by height : ")
print(np.sort(students , order = 'height'))