#  1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise

#  is_two  defines a single paramter, my_input is either a string or a number, and will return  boolean value
def is_two(my_input):
    #  convert the passed argument to string and check if it is equal to string 2. If True then, return True else False
    if str(my_input) == '2': 
        return True 
    return False
    

#  2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

#  is_vowel define a single parameter, alphabet that is a string, and will return a boolean value
def is_vowel(alphabet):
    """convert the passed argument to lowercase in order to check both uppercase and lowecase arguments.
    If passed arguments are in string of 'aeiou', return True. If not return False."""
    if alphabet.lower() in ('aeiou'):
        return True
    return False


#  def contain_vowel(user_input):
    
#     for char in user_input:
#         if char.lower() in ('aeiou'):
#             return True
#     return False
          

#     if any(char.lower() in ('aeiou') for char in user_input):
#         return True
#     return False


#  3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

#  is_constant define a single parameter, alphabet that is a string, and will return a boolean value
def is_constant(alphabet):
    #  convert the passed argument to lowercase in order to check both uppercase and lowecase arguments.
    #  If passed arguments are in not in string of 'aeiou', return True. If not return False.
    if alphabet.lower() not in ('aeiou'):
        return True
    return False


#  4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

#  caitalize_consant defines a single parameter, word that is string, and will return a string value
def capitalize_constant(word):
    # check if first leter of passed argument is a vowel. If yes, capitalize it.
    if word[0] not in ('aeiou'):
        return word.capitalize()
    

#  5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

#  cacluate_tip defines two parameters: tip_percent and bill and will return the amount to tip
def calculate_tip(tip_percent,bill):
    #  Divide tip_percent by 100 to convert percentage into decimal and multiply by bill to get a result.
    return (tip_percent/100)* bill 
    

#  6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

#  apply_discount defines two parameters: original_price, discount_percent and will return the price after the discount
def apply_discount(original_price, discount_percent):
    #  Divide discount percentage by 100 to convert to decimal, multiply discount decimal by original price to get
    #  discount amount, then subtract discount amount from original price to the price after discount
    price = original_price - (discount_percent/100)* original_price
    return price


#  7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

#  handle_commas defines a single parameter, number that is a string, and will return a string without a comma
def handle_commas(number):
    #  check if passed argument has a comma, if True, then replace the comma with empty string.
    if ',' in number:
        return number.replace(',', '')


#  8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

#  get_letter_grade defines a single parameter, number is int, and will return a string.
def get_letter_grade(number):
    #  check if passed argument is valid that it is between 0 and 100
    if 0 <= number <= 100: 
        #  check if passed argument is greater than or equal to 88. If True, return 'A'. If False, check further down
        if number >= 88:    
            return 'A'
        #  check if passed argument is greater than or equal to 80. If True, return 'B'. If False, check further down
        elif number >= 80: 
            return 'B'
        #  check if passed argument is greater than or equal to 67. If True, return 'C'. If False, check further down
        elif number >= 67:  
            return 'C'
        #  check if passed argument is greater than or equal to 60. If True, return 'D'. If False, check further down
        elif number >=60:  
            return 'D'
        #  If passed argument is False on all above conditions, then return 'F'
        else:             
            return 'F'
        
        
#  9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

#  remove_vowels defines a single parameter, text that is a string, and will return a string value without vowels
def remove_vowels(text):
    #  maketrans method's last parameter remove all vowesl if present in a text string and store modified text
    text_with_constant = text.maketrans('', '', 'aeiou')  
    #  translate method returns modified text
    return text.translate(text_with_constant)  


''' 
10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
        - anything that is not a valid python identifier should be removed
        - leading and trailing whitespace should be removed
        - everything should be lowercase
        - spaces should be replaced with underscores
        -  for example:
            - Name will become name
            - First Name will become first_name
            - % Completed will become completed
'''

#  import string module
import string
#  normalize name defines a single parameter, name that is a string, and return a string value
def normalize_name(name):
    #  convert passed argument to lower case using lower method and remove spaces at the begining and at the end of the string
    name = name.lower().strip()
    #  string.punctuation give all sets of the punctuation
    #  place string. punctutation in maketrans method's last parameter to remove all sets of the punctuation
    translated_name = name.maketrans('', '', string.punctuation)
    #  tranlsate method store modified string 
    name1 = name.translate(translated_name)
    #  replace method replace empty space with underscore
    name1 = name1.replace(' ', '_')
    #  check if first letter of modified passed argument is digit. If True, remove it.
    if name1[0].isdigit():
        #  get substring after first letter
        name1 = name1[1:]
    return name1


''' 
11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
    - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    -cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
'''

#  cumulative_sum defines a single parameter, my_list that is a list, and returnd a list value
def cumulative_sum(my_list):
    #  iterate over lenght of passed argumnet
    for i in range(len(my_list)):
        #  check if i+ 1 is less than lenght of  the passed argument so that i +1 is not out of index.
        if i+1 < len(my_list):
            #  If i + 1 is within index of length of the passed argument, add first index item and consecutive index 
            #  item and replace consecutive index with result, then repeat the process of adding and replacing
            my_list[i+1] = my_list[i] + my_list[i+1]
    return my_list


'''
Bonus
1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation
 of the time in a 24-hour format. Bonus write a function that does the opposite.
'''

#  twelveto24 defines a single paramete, time_12 is a string and return a single string value
def twelveto24(time_12):
    #  get first two letter of passed argument and convert those to int
    hour = int(time_12[:2])
    #  get last two letter of passed argument and compare with 'am'
    if time_12[-2:] == 'am':
        #  compare if hour is lesser than 12
        if hour < 12:
            #  return first six letter of passed argument to get a time before miday
            return time_12[0:5]
        else:
            #  if hour is greater than 12, add string '00' infront of letters from 2 to 4 of passed argument to get a time after midnight
            return '00'+time_12[2:5]
    #  if last two letters of passed argument does not match with 'am', then they match with 'pm'
    else:
        #  compare if hour is lesser than 12
        if hour < 12:
            #  add 12 to hour to time after miday
            hour = hour + 12
            #  add hour infront of letters from 2 to 4 of passed argument to get time after miday
            return str(hour) + time_12[2:5]
        else:
            #  return first five letters of passed argument to get time after between miday and one'o clock of day
            return time_12[0:5]


#  twentyfourto12 defines a single parameter, time_24 is a string, and returns a string value      
def twentyfourto12(time_24):
    #  get first two letter of passed argument and convert those to int
    hour = int(time_24[:2])
    #  compare if an hour is leeser than 21
    if  hour > 21:
        #  subtract 12 from hours greater than 21 to get a time after 10 at nighttime
        hour = hour - 12
        #  return time after 10 at nightime
        return ( str(hour) + time_24[2:] + 'pm')
    #  compare if an hour is greater than 12
    elif hour > 12:
       #  subtract 12 from hours greater than 12 to get a time after midday
        hour = hour -12
        #  add '0' string infront of letters from 2 to last of passed argument to get time after miday but 10 at nightime
        return ( '0' + str(hour) + time_24[2:] + 'pm')
    #  compare if an hour is equal to 12
    elif hour == 12:
            #  return time between midday and one at daytime
            return (str(hour) + time_24[2:] + 'pm')
    #  compare if an hour is leeser than 9 at daytime
    elif hour > 9: 
        #  return time after 10 at daytime
        return (str(hour) + time_24[2:] + 'am')
    elif hour > 1:
        #  return time between 1 and 9 at daytime
        return ('0' + str(hour) + time_24[2:] + 'am')
    else:
        #  return time between midnight and 1 at nightime
        return ('12' + time_24[2:] + 'am')

