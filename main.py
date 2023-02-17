import pandas
import smtplib
import random
import datetime as dt
import os

data = pandas.read_csv("birthdays.csv")
name = data["name"].tolist()
email = data["email"].tolist()
year = data["year"].tolist()
month = data["month"].tolist()
day = data["day"].tolist()

list_dir = os.listdir("letter_templates")

with open(f"letter_templates/{random.choice(list_dir)}") as file:
    files = file.read()

# You have to go to privacy in your mail settings and look for your password
my_email = "{Your mail}"
password = "{Your app password}"

now = dt.datetime.now()
date = now.day
months = now.month
time = now.time()
print(time)

if months in month and date in day:
    date_index = day.index(date)
    name_replaced_file = files.replace("[NAME]", name[date_index])
    print(name_replaced_file)

    with smtplib.SMTP("smtp.gmail.com", port=587) as content:
        content.starttls()
        content.login(user=my_email, password=password)
        content.sendmail(
            from_addr=my_email,
            to_addrs=email[date_index],
            msg=f"Subject:Birthday Wishes\n\n{name_replaced_file}"
        )
