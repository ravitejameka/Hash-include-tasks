# HELLO WORLD PROGRAM 
print("Hello, World!")

# DATA TYPE IDENTIFICATION #
a = 5
print(type(a))
b = "hii"
print(type(b))
c = 10.5
print(type(c))

# STRING MANIPULATION#

a = "hello"
r = a.upper()
print(r)
print(len(r))
l = a.replace("h","c")
print(l)

# TYPE CASTING#

a = 10.567584
print(int(a))
s = "10.765"
print(float(s))


# STRING METHOD EEXPLORATION #
n = "hello"
c = 0
for i in n:
    if i =='a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        c+=1
print(c)
i = n[::-1]
print(i)
if n == n[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

# EVEN OR ODD#
    
n = int(input())
if n % 2 == 0:
    print("is even number")
else:
    print(" is odd number")

    
# STRING CONCATENATION #

x = "Hello"
y = "Hi"
z = "Bye"
print(x + y + z)

# BASIC LIST OPERATION #

a = [4,2,1,3,5]
a.append(6)
print(a)
a.pop(2)
print(a)
r = sorted(a)
print(r)

# PALINDROME CHECKER #

s = "ror"
i = s[::-1]
print(i)
if s == s[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
    
# SIMPLE CALCULATOR #    
    
a = 2
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)