name = input("Enter your name: ")

Maths = float(input("Enter maths marks: "))
Science = float(input("Enter science marks: "))
English = float(input("Enter english marks: "))

total = Maths + Science + English
average = total/3
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail


print("\n______ Result ______")
print("Name:", name)
print("Total Marks:", total)
print("Average Marks:", round(average,2))
print("Grade:", grade)



