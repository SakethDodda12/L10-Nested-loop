num = input("Enter the number: ")
length = len(num)

if length >= 4:
    if length % 2 == 0:
        mid1 = int(num[length//2 - 1])
        mid2 = int(num[length//2])
        product = mid1 * mid2
        print(f"The product of mid digits({mid1}*{mid2}) = {product}")
    else:
        mid = int(num[length//2])
        product = mid * mid
        print(f"Middle digit is {mid}, so product = {product}")
else:
    print("Its not a 4 digit or more number!")