n = int(input("Enter an integer number: "))
adjacent = False
last = n % 10

while n > 0 and adjacent == False:
        new_n = n//10
        next = new_n%10
        if last != next:
            n = new_n
            last = new_n%10
            next = (new_n//10)%10
        else:
            adjacent = True           
if adjacent == True:
    print("Yes")
else:
    print("No")
