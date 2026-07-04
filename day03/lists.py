groceries_list=['Eggs','Milk','Rice']
groceries_list.append('Chicken')
print(len(groceries_list))
groceries_list.extend(('Beef','Oranges','Onion'))

print(len(groceries_list)) #7
print(groceries_list) #['Eggs', 'Milk', 'Rice', 'Chicken', 'Beef', 'Oranges', 'Onion']
#groceries_list[-2:]='Cheery' #assign tople or list if you are slicing
#print(groceries_list) #['Eggs', 'Milk', 'Rice', 'Chicken', 'Beef', 'C', 'h', 'e', 'e', 'r', 'y']

groceries_list[-2]='Cheery' #no slice just assigned
print(groceries_list)##['Eggs', 'Milk', 'Rice', 'Chicken', 'Beef', 'Cheery', 'Onion']

print('------------------------------------')

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers_list)

numbers_list[2:-2] = [300, 4000, 5, 60000]

print(numbers_list)

print('------------------------------------')

characters=['a','b','c','d','e','f','g','h','i']
list1=characters[2:len(characters)-3]
print(list1)#['c', 'd', 'e', 'f']
list2=characters[:4]
print(list2)
list3=characters[2:]#['a', 'b', 'c', 'd']
print(list3)#['c', 'd', 'e', 'f', 'g', 'h', 'i']
characters[2:5]=['C',"D",'E',"F",'X','Y','Z']
print(characters) # ['a', 'b', 'C', 'D', 'E', 'F', 'X', 'Y', 'Z', 'f', 'g', 'h', 'i'] shifted
names=['Conor','Steve','Hazel','Breanne']
for x in names:
    print(x)
nums=[10,20,30,40,50]

for i in range(2,len(nums)):

   # nums[i]/=5 # [10, 20, 6.0, 8.0, 10.0]
    nums[i]=int(nums[i]/5)

print(nums)#[10, 20, 6, 8, 10]

for i in reversed(range(len(nums))):
    print(nums[i])
for x in nums[::-1]:
    print(x)

for x in reversed(nums):
    print(x)

i=0
while i<len(nums):
    print(nums[i])
    i+=1


print('------------------------------------')

for i in range(1, 6):
    i += 2
    print(i)#3 4 5 6 7

print('------------------------------------')

nums = [60, 500, 10, 20, 15, 5, 0]

# nums.sort()  # ascending order

nums.sort(reverse=True)

print(nums)

print('------------------------------------')

list1 = [10, 20, 30, 40]

# list1 = list( reversed(list1) )

list1.reverse()

print(list1)

print('------------------------------------')

tuple_elements = ('Java', 'Python', 'C#', 'Ruby')

list_elements = list(tuple_elements)
list_elements[-2] = 'C++'
list_elements.append('SWIFT')

print(list_elements)

tuple_elements = tuple(list_elements)

print(tuple_elements)

print('------------------------------------')

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

print(list1 is list2)#false

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3, 4, 5)

print(tuple1 is tuple2)#true


print('------------------------------------')


groceries_list = ['Eggs', 'Milk', 'Rice']

groceries_list.append('Chicken')
groceries_list.extend(('Beef', 'Oranges', 'Onion'))

print(groceries_list)

groceries_list.remove('Beef')

print(groceries_list)

groceries_list.pop()

print(groceries_list)

groceries_list.pop(1)

print(groceries_list)

groceries_list.insert(2, 'Apple')

print(groceries_list)


print( groceries_list.index('Eggs'))

nums = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]

print(nums.count(1))


print('--------------- Comprehensions -------------------------')

nums = []

for x in range(1, 51):
    nums.append(x)

print(nums)

print('------------------------------------')

"""
divisible_by_5 = []

for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)

print(divisible_by_5)
"""

divisible_by_5 = tuple( [ x  for x in nums if x % 5 == 0 ] )

print(divisible_by_5)

print('------------------------------------')

even_nums = [ x for x in nums if x % 2 == 0]
odd_numbers = [x for x in nums if x % 2 != 0]

print(even_nums)
print(odd_numbers)

print('------------------------------------')

names = ['Python', 'Java', 'Java', 'JavaScript', 'java', 'JaVA', 'Ruby']

names = [x for x in names if x.lower() != 'java']

print(names)#['Python', 'JavaScript', 'Ruby']
