##################### Extra Hard Starting Project ######################

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas
import smtplib
import datetime as dt
import random

smtp_server = "smtp.gmail.com"
my_email = "adiamburhan@gmail.com"
password = "sgqifojkfppdoucv"
smtp_port = 587

today = dt.datetime.now()


# Read the CSV file into a DataFrame
df = pandas.read_csv("birthdays.csv")

# Method 1: Using iter rows
for index, row in df.iterrows():
    if row["day"] == today.day and row["month"] == today.month:
        selected_email = row["email"]
        name_to_append = row["name"]
        random_num = random.randint(1,3)
        template_file_path = f"./letter_templates/letter_{random_num}.txt"
        print(template_file_path)
        # Read the content of the letter template
        with open(template_file_path, 'r') as letter_file:
            letter_content = letter_file.read()
        # Replace [NAME] with the actual name
        letter_content = letter_content.replace("[NAME]", name_to_append)
        print(letter_content)
        with smtplib.SMTP(smtp_server, smtp_port) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs= selected_email,
                msg=f"Subject: Happy Birthday\n\n{letter_content}.")





















