# 5) მომხარებელს შემოატანინე input შეამოწმე, არის თუ არა რიცხვი 10-ზე მეტი ან ტოლი.

num1 = int(input("Enter the first number:"))

if num1 > 10:
    print("The number you entered is greater than 10.")
elif num1 < 10:
    print("The number you entered is NOT greater than 10.")
else:
    print("The number you entered is equal to 10.")