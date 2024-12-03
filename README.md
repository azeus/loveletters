Daily Love Letter Email Scheduler 💌

A Python script to send daily emails with heartfelt messages. This project uses Python’s smtplib and schedule libraries to automate the sending of emails, ensuring that your loved ones feel appreciated every day.

Features

	•	Sends automated emails daily at a specified time.
	•	Simple and lightweight, built with Python.
	•	Uses Gmail’s SMTP server for secure email delivery.
	•	Fully customizable message content, recipient, and schedule.

Prerequisites

	1.	Python: Make sure Python 3.6+ is installed on your system.
	2.	Email Account: A Gmail account to send the emails.
	3.	Environment Variables: For security, store your email credentials securely.

Installation

	1.	Clone the Repository

git clone https://github.com/azeus/loveletters.git
cd loveletters


	2.	Set Up Environment Variables
Add the following variables to your environment:
	•	GMAIL_ID: Your Gmail address.
	•	GMAIL_PWD: Your Gmail password or app-specific password.
For Mac/Linux:

export GMAIL_ID="your-email@gmail.com"
export GMAIL_PWD="your-email-password"

For Windows:

set GMAIL_ID=your-email@gmail.com
set GMAIL_PWD=your-email-password


	3.	Install Required Libraries
Ensure schedule is installed. If not, install it using pip:

pip install schedule

Usage

	1.	Customize the Script
	•	Modify the recipient, subject, and msg variables in the schedule_email function to personalize your emails.
	2.	Run the Script

python loveletter.py


	3.	Sit Back and Relax
The script will send emails daily at the scheduled time. The default time is set to 09:00 AM, but you can modify it by editing:

schedule.every().day.at("09:00").do(schedule_email)

Example Output

Email scheduler started. Waiting to send emails...
Email sent to <recipient_email_id> with Subject: 'Love Letter' and Message: 'I am thinking about you'

Notes

	•	Security: Avoid hardcoding email credentials in the script. Use environment variables to store sensitive information securely.
	•	Gmail Settings: If you’re using Gmail, enable “Allow less secure apps” or set up an app-specific password.
	•	Customization: Update the message or schedule easily in the script.


License

This project is open-source and licensed under the MIT License.

Acknowledgments

Inspired by the joy of making loved ones feel special every day. 💖
