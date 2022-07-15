files = []
with open('input.txt') as file:
    for i in file:
        lst = [x.strip() for x in i.split()]
        files.append(lst)

evenP, oddP, noP = 0, 0, 0
parity, palindrome = [], []
yesPal, noPal = 0, 0
words, digit = [], []

for i in range(len(files)):
    digit.append(files[i][0])
    words.append(files[i][1])

for i in digit:
    if float(i) % 1 != 0:
        parity.append("cannot have parity")
        noP = noP + 1
    else:
        if float(i) % 2 == 0:
            parity.append("has even parity")
            evenP = evenP + 1
        else:
            parity.append("has odd parity")
            oddP = oddP + 1

def check(str):
    global yesPal, noPal
    if str == str[::-1]:
        palindrome.append("is a palindrome")
        yesPal = yesPal + 1
    else:
        palindrome.append("is not a palindrome")
        noPal = noPal + 1

for i in range(len(words)):
    check(words[i])

outputTxt = open("output.txt", "w")
recordTxt = open("record.txt", "w")

for i in range(len(parity)):
    outputTxt.write(digit[i] + " " + parity[i] + " and " + words[i] + " " + palindrome[i])
    if i == len(parity):
        break
    outputTxt.write(str("\n"))

recordTxt.write("Percentage of odd parity: " + str(((int(oddP) / 5) * 100)) + "%\n")
recordTxt.write("Percentage of even parity: " + str(((int(evenP) / 5) * 100)) + "%\n")
recordTxt.write("Percentage of no parity: " + str(((int(noP) / 5) * 100)) + "%\n")
recordTxt.write("Percentage of palindrome: " + str(((int(yesPal) / 5) * 100)) + "%\n")
recordTxt.write("Percentage of non-palindrome: " + str(((int(noPal) / 5) * 100)) + "%\n")