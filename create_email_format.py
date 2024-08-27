# John Smith -> Dairy Farm
# johnsmith@dairyfarm.com.au

# Snake Case -> first_name -> Python preferred for variables and functions
# Pascal Case -> FirstName -> preferred for class names
# Camel Case -> firstName -> Javascript preferred for variables and functions
# Kebab Case -> first-name -> CSS preferred for variables

# Get First name from the user
first_name = input("Enter your first name:")

# Get Last name from the user
last_name = input("Enter your last name:")

# Get the name of the company without space
company_name = input("Enter the name of the company without spaces:")

# Create the email format
email_format = (first_name + "." + last_name + "@" + company_name + ".com.au").lower()

email_format_fstring = f"{first_name}.{last_name}@{company_name}.com.au".lower()


# Print that email
print(email_format)
print(email_format_fstring)