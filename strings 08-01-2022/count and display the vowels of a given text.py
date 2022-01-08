#count and display the vowels of a given text
str1 = input("Please Enter String : ")
vowels = 0

for i in str1:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
            or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1

print("Total Number of Vowels in this String = ", vowels)