num = int(input("Enter the number: "))
t = num
numLen = 0
while t > 0:
    numLen += 1
    t //= 10

if numLen >= 4:
    mid_index = numLen // 2
    chk = 0
    temp = num
    
    while temp > 0:
        rem = temp % 10
        if chk == mid_index:
            midOne = rem
        elif chk == (mid_index - 1):
            midTwo = rem
        temp //= 10
        chk += 1
    prod = midOne * midTwo
    print(f"\nProduct of Mid digits ({midOne} * {midTwo}) = {prod}")
else:
    print("\nIt's not a 4 or more than 4-digit number!")
