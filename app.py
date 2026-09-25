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

numberone = int(input("Type your first number: "))
numbertwo = int(input("Type your second number: "))
def factors(n, f):
    factorlist = []
    for i in range(1, n + 1):
        if n % i == 0 and f % i == 0:
            factorlist.append(i)
    print(factorlist[-1])
factors(numberone, numbertwo)
"""