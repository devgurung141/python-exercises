rent_days_for_mermaid = 3
rent_days_for_brother_bear = 5
rent_days_for_hercules = 1
rent_price_per_day = 3

total_rent_price = rent_price_per_day* (rent_days_for_mermaid + rent_days_for_brother_bear + rent_days_for_hercules)
# print(total_rent_price)

# ---------------------------------------
google_pay_per_hour = 400
amazon_pay_per_hour = 380
facebook_pay_per_hour = 350

google_hours = 6
amazon_hours = 4
facebook_hours = 10

payment = (google_pay_per_hour * google_hours) + (amazon_pay_per_hour * amazon_hours) + (facebook_pay_per_hour * facebook_hours)
#print(payment)

# ---------------------------------------
class_not_full  = True
class_schedule_not_conflict_current_schedule = True
class_enorll = class_not_full and class_schedule_not_conflict_current_schedule

# ---------------------------------------
item_more_than_2_items = True
offer_not_expire = True
premimum_member = True
product_offer = (item_more_than_2_items or premimum_member)and offer_not_expire


# ---------------------------------------
username = 'codeup'
password = 'notastrongpassword'

# the password must be at least 5 characters
len(password) >= 5
# solution:
check1 = len(password) >= 5

# the username must be no more than 20 characters
len(username) <= 20
#solution
check2 = len(username) <= 20


# the password must not be the same as the username
username != password
#solution
check3 = username != password


# neither the username or password can start or end with whitespace
not((username or password).startswith(' ')) or ((username or password).endswith(' '))
#solution
no_whitespace_username = not(username.startswith(' ') or username[-1] == ' ')
no_whitespace_password = not(password.startswith(' ') or password[-1] == ' ')
user_and_pass_valid = no_whitespace_password and no_whitespace_username
