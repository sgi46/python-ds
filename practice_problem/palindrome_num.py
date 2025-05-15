# def palindrome(num):
#     org = num
#     rev = 0

#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num = num // 10

#     print("Reversed:", rev)
#     print("Original:", org)

#     if rev == org:
#         print("palindrome")
#     else:
#         print("no")

def palindrome(num):
    
    org = num
    rev = 0

    while num>0:
        digit = num%10
        rev = rev*10 + digit
        num = num//10
    
    print(rev)
    print(org)

    if rev == org:
        print("palindrome")
    else: 
        print("no")

print(palindrome(121))