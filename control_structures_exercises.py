#----------------------------------------------
# 1. Conditional Basics
# a.

day = input('Enter a day of the week: ')
if day.lower() == "monday":
    print('The day is Monday')
else:
    print('The day is not Monday')


#----------------------------------------------
# b. 

day = input('Enter a day of the week: ')
if day.lower() == 'saturday' or day.lower() == 'sunday':
    print('The day is a weekend')
else:
    print('The day is a weekday')


#----------------------------------------------
# c. 

hour_worked_per_week = 50
rate_hourly = 20
rate_hourly_overtime = rate_hourly + rate_hourly/2
overtime_work_per_week = hour_worked_per_week - 40
if hour_worked_per_week <= 40:
    paycheck_weekly = rate_hourly * hour_worked_per_week
    print(paycheck_weekly)
else:
    paycheck_weekly = (rate_hourly * hour_worked_per_week) + (overtime_work_per_week * rate_hourly_overtime)
    print(paycheck_weekly)


#----------------------------------------------
# 2. Loop Basics
# a. While

i = 5
while i <= 15:
    print(i)
    i += 1


#----------------------------------------------
i = 0
count = 0
while i < 101:
    count += 2
    print(count)
    if count == 100:
        i = 101


#----------------------------------------------
i = 0
count = 100
while i < 101:
    count -= 5
    print(count)
    if count == -10:
        i = 101


#----------------------------------------------
i = 2
while i < 1_000_000:
    print(i)
    i = i ** 2


#----------------------------------------------
i = 0
count = 105
while i < 101:
    count -= 5
    print(count)
    if count == 5:
        i = 101


#----------------------------------------------
# b. For Loops
i. 
number = int(input('Enter a number: '))
print()

for i in range(1,11):
    
    print(f'{number} X {i} {number*i}')


#----------------------------------------------
# ii.

for i in range (1,10):
    print(str(i)* i)


#----------------------------------------------
# c.break and continue
# i. 
number = int(input('Enter a positive integer: '))
while number > 0:
    print(number)
    number -= 1


#----------------------------------------------
# ii.

number = int(input('Enter a positive integer: '))
count = 0
for i in range(number +1):
    print(i)
    

#----------------------------------------------
#. iii.

number = int(input('Enter an odd number between 1 and 50: '))

while number % 2 == 0 or  number < 1 or number > 50:
    number = int(input('Enter an odd number between 1 and 50: '))
    if number %2 == 1 and number > 1 and number < 50:
        #print(number)
        break

print(f'\nNumber to skip is: {number}')
print()
for i in range(50):
    if i % 2 == 1:
        if i == number:
            print(f'Yikes!, Skipping number: {i}')
            continue
        print(f'Here is an odd number: {i}')
        

#----------------------------------------------
# 3. Fizzbuzz

for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, 'Fizzbuzz')
    elif i % 3 == 0:
        print(i, 'Fizz')
    elif i % 5 == 0:
        print(i, 'Buzz')
    else:
        pass


#----------------------------------------------
# 4. 
number = int(input('What number would you like to go up to? '))
print(f'\nHere is your table')
print(f'\n number          |  squared      |  cubed')
print(f' _ _ _ _ _ _ _ _ | _ _ _ _ _ _ _ | _ _ _ _ _')
for i in range(1, (number + 1)):
    print(f'{i:5}            |{i **2:5}          |{i **3:5}')


#----------------------------------------------
# 5. 
number = int(input('Enter a numerical grade from 0 to 100: '))
flag = True
while True:
    if number >= 97:
        print('A+')
    elif number >= 93:
        print('A')
    elif number >= 90: 
        print('A-')
    elif number >= 87:
        print('B+')
    elif number >= 83:
        print('B')
    elif number >= 80 :
        print('B-')
    elif number >= 77:
        print('C+')
    elif number >= 73:
        print('C')
    elif number >= 70 :
        print('C-')
    elif number >= 67:
        print('D+')
    elif number >= 63:
        print('D')
    elif number >= 60 :
        print('D-')
    else:
        print('F')
        
    user_prompt = input("""To continue, enter Y:
To exit, Enter N    :""")
    if user_prompt.upper() == 'Y':
        number = int(input('\nEnter a numerical grade from 0 to 100: '))
    elif user_prompt.upper() == 'N':
            break
    else:
        print('Wrong input, exiting....')
        print('Exit complete')
        break
            

      
#----------------------------------------------
# 6. 
book_dict = {'book1':{'title':'I am Malala', 'author':'alala Yousafzai,Chrisina Lamb', 'genre':'autobiography'},
        'book2':{'title': 'Ulysses', 'author': 'James Joyce', 'genre': 'fiction'},
        'book3':{'title': 'Killing England','author': 'Bill O’Reilly and Martin Dugard', 'genre':'history'},
        'book4':{'title':'Hiroshima', 'author': 'John Hresey', 'genre': 'history'},
        'book5': {'title': 'Dune', 'author':'Frank Herbert', 'genre':'fiction'}
        }

for books in book_dict:
    print(books)
    print(book_dict[books])
    
    
user_prompt = input('''\nFrom genre list: autobiography, fiction, history
Enter one:\n''')
print()
for i in book_dict:
    if book_dict[i]['genre'] == user_prompt:
        print(book_dict[i]['title'])


        
    