def romanToInt(s: str) -> int:
    # Dictionary of roman numerals
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Length of the given string
    n = len(s)
    # This variable will store result
    num = roman_map[s[n - 1]]
    print(num)
    # Loop for each character from right to left
    for i in range(n - 2, -1, -1):
        # Check if the character at right of current character is bigger or smaller
        if roman_map[s[i]] >= roman_map[s[i + 1]]:
            num += roman_map[s[i]]
        else:
            num -= roman_map[s[i]]
    return num
s1=romanToInt(s='III')
print(s1)

#another method:







print("Roman to Integer")

num={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
n=0
l=[]
prev=0
value=input("enter the number")
#creating list
for i in value:
    l.append(i)


#counting
for k in l:
    for i ,j in num.items():

        if k==j:
           if prev<i :
              prev = i
              n =i-n
           elif prev >= i :
                prev = i
                n +=i
print(f"from Roman {value} into Integer {n}")