"""
userinput = input("Write any sentence! ")
sentence = userinput.split()
wordcount = len(sentence)
print("There are " + str(wordcount) + " words in your sentence!")

number = int(input("Input a number! "))
if number % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")

bill = float(input("How much was the bill? (Don't put the $ sign) "))
service = input("How was the service? (bad, okay, good, or great) ")
if service == "bad":
    print("Your total will be $" + str(bill))
if service == "okay":
    print("Your total will be $" + str(bill * 1.15))
if service == "good":
    print("Your total will be $" + str(bill * 1.20))
else:
    print("Your total will be $" + str(bill * 1.25))

bill = float(input("How much was the bill? (No $ sign)"))
tip = int(input("How much did you tip? (Stil no $ sign)"))
total = bill + tip
print("Your total is $" + str(total))

number = int(input("Input any whole non-negative number: "))
for i in range(1, number + 1):
    if number % i == 0:
        print(i)
"""
listone = list1()
listtwo:  list2()
number1 = int(input("Type your first number: "))
number2 = int(input("Type your second number: "))
for i in range(1, number1 + 1):
    if number1 % i == 0:
        listone.append(i)
print(listone)
for i in range(1, number2 + 1):
    if number2 % i == 0:
        listtwo.append(i)