'''vowls ="a,e,i,o,u and rest of all are in alphabets are cosonats'''

char = input("enter the value of string:")
vowels = "aeiouAEIOU"

if char in vowels:
    print("the given charcater is vowel")
else:
    print("the given character is not a vowel")