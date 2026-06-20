print(10+2)

print(10/3)#3.3333333333333335
print(int(10/3))#3
# shorthand assignment operators: =, +=, -=, *=, /=, %=

a = 100

a = 200

print(a)


a += 100

print(a)

a -= 50

print(a)

a /= 2

print(a) #125.0
print(round(10/4,1))

# logical operators: and, or, not
s = 'Hello World'

print('H' and 'W' in s) #true

print(True and True)
print(True or False)#true

s = 'Java Python C# C++'

print( 'Java' or 'Ruby' in s)

age = 29
citizen_ship = 'USA'
is_eligible = age >= 18 and citizen_ship == 'USA'

print(is_eligible)

has_java = 'Java' in s
print(has_java)

# !contains()
print('Python' not in s)

print(not False)
print(not True)  # !

print('----------------------------------')

s = 'Java'
s2 = 'Java'

print( s is s2) # to heck if two variables are referencing to the same objects ( == operator of java)
