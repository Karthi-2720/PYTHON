import datetime as dt
import random
import pandas as pd
import smtplib

my_email = "24r05a6704@cmrithyderabad.edu.in"
password = "blru htfq nhxf nhjl"
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)
bd_data = pd.read_csv("birthdays.csv")
birthday_data = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in bd_data.iterrows()}
if today in birthday_data:
     file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
     with open(file_path, "r") as letter_file:
          birthday_person = birthday_data[today]
          content = letter_file.read()
          replaced_msg = content.replace("[NAME]", birthday_person["name"])

     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
          connection.starttls()
          connection.login(user=my_email, password=password)
          connection.sendmail(
               from_addr=my_email,
               to_addrs=birthday_person["email"],
               msg=f"Subject: Advance Happy Birthday {birthday_person['name']}\n\n{replaced_msg}"
          )


# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter.
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



