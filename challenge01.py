#!/usr/bin/env python3

icecream = ["indentation", "spaces"]

tlgstudents= ["Bryan", "Colin", "Erik", "Gregory", "John", "Kishor", "Leia", "Maria", "Monte", "Jarrad", "Pemba", "Don", "Tim", "Travis", "Trung"]

icecream.append(str(4))

studentid= int(input("Enter a number from 0 - 14: "))

#randomly grab an element from a list
#randomstudent= random.choice(tlgstudents)

selection= tlgstudents[int(studentid)]

print(type(icecream[2]))

# <student_name> always uses <4> <spaces> to indent.

print(selection +" " + "always uses" + " " +  icecream[2] + " " + icecream[1] +" " + "to indent.")

# F-STRING
print(f"{selection} always uses {icecream[2]} {icecream[1]} to indent.")
#print(f"RANDOM STUDENT {randomstudent} always uses {icecream[2]} {icecream[1]}to indent.")

#print("The following awesome students are in this class:", ", ".join(tlgstudents))
