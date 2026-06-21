
age=int(input("Enter your age\n"))
country=input('Enter your country\n').upper()
def check(age:int,country:str):
    if age>18 and country =='USA':
        print('eligible')
    else:
        print('You are not eligible to vote!')

check(age,country)

