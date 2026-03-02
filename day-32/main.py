import datetime as dt
import smtplib
import random

my_email = "24r05a6704@cmrithyderabad.edu.in"
password = "blru htfq nhxf nhjl"

now = dt.datetime.now()
weak_day = now.weekday()

if weak_day == 3:
    with open("quotes.txt")as file:
        all_quotes = file.readlines()
        quotes = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="nanabalu06@gmail.com",
            msg=f"Subject: Thursday Motivation\n\n{quotes}"
        )





# import smtplib
#
# my_email = "24r05a6704@cmrithyderabad.edu.in"
# password = "blru htfq nhxf nhjl"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as s:
#     s.starttls()
#     s.login(user=my_email, password=password)
#     s.sendmail(
#         from_addr=my_email,
#         to_addrs="matamshashank626@gmail.com",
#         msg="Subject: Hello I Am Karthikeya\n\nHi varun."
#     )

#
# import datetime as dt
# now = dt.datetime.now()
# print(now)

