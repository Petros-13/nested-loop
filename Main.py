string = input("Enter your own word:")
char = input("Enter your own character:")
i=0
count = 0
while(i < len(string)):
    if string[i] == char:
        count += 1
    i += 1
print("The number of times",char,"the character apppears",count)
