number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

marks = float(input("Enter your marks: "))

if marks > 90:
    print("Grade: A")
elif marks > 80 and marks <= 90:
    print("Grade: B")
elif marks > 70 and marks <= 80:
    print("Grade: C")
else:
    print("Grade: D")