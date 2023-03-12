
first_char = input("enter starting letter: ")
second_char = input("enter last letter: ")
alpha ={}
for i in range(ord(first_char), ord(second_char)+1) :
    alpha[chr(i)]=i
print(alpha)