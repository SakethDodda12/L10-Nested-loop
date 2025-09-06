string = input("Please enter a string: ")
char = input("Enter a letter you want to count: ")
i = 0
count = 0

while(i < len(string)):
    if(string[i] == char):
        count = count + 1
    i = i + 1
print("The total number of times ", char, " has occured is ", count)