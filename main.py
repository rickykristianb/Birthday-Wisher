import random
import smtplib
import datetime as dt
from dotenv import load_dotenv
import os

import pandas

# CONSTANT
load_dotenv()
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')


# TODO: Open the csv file and read it
def read_birthday_file():
    data = pandas.read_csv("birthdays.csv", index_col=False)
    return data


# TODO: Select the random letter and replace the name to the name birthday person
def select_letter():
    letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    selected_letter = random.choice(letter_list)
    with open(f"./letter_templates/{selected_letter}") as letter:
        letter_container = letter.read()
    return letter_container


# TODO: Check is today is one of the person on the list birthday
def check_birthday():
    now = dt.datetime.now()
    now_month = now.month
    now_day = now.day

    file = read_birthday_file()
    for (index, row) in file.iterrows():
        if row.month == now_month and row.day == now_day:
            send_email(to_email=row['email'], recipient_name=row['name'])


# TODO: Send email to birthday person
def send_email(to_email: str, recipient_name: str):
    letter = select_letter()
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=["ricky.kristianb@gmail.com", "learnpythn@yahoo.com"],
            msg=f"Subject:Happy Birthday\n\n{letter.replace('[NAME]', str(recipient_name))}",
            rcpt_options="ricky.kristianb@gmail.com",
        )


# MAIN
def main():
    check_birthday()


if __name__ == "__main__":
    main()

