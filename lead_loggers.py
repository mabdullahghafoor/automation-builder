
# For current date and time
from datetime import datetime

# For leads inputs
name = input ("Enter Your Name: ")

# Email Validation
while True:
    email = input ("Enter Your Email: ")
    if "@" in email:
        break
    else:
        print("Invalid Email. Please Try Again!")


business = input ("Enter your business: ")

# For printing time and date
current_time = datetime.now()
date_string = current_time.strftime("%Y-%m-%d %H-%M-%S")

# For format of the data
lead_data = f"{date_string}, {name}, {email}, {business}\n"

# For appending data to csv file
with open("leads.csv", "a") as file:
    file.write(lead_data)

# For acknowledgment
print("Leads saved Successfully!")