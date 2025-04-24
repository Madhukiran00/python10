
# num = 2
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# num = 2
# if num & 1 == 0:
#     print("Even")
# else:
#     print("Odd")




# def is_even(n):
#     return "Even" if n % 2 == 0 else "Odd"

# print(is_even(13))



# check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(check_even(10))







#Ternary Operator

# num = 21
# _, rem = divmod(num, 2)
# print("Even" if rem == 0 else "Odd")
# # 









# By Using divmod
# num = 21
# rem = divmod(num, 2)
# print("Even" if rem == 0 else "Odd")





def even_or_odd(n): #6 4 2 n=0
    if n==0 :
        return "Even"
    elif n==1:
        return "Odd"
    return even_or_odd(n-2) #6-2=4  4-2=2 2-2=0

res=even_or_odd(6)
print(res)




