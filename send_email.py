import yagmail

# Email credentials (Use environment variables for security!)
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_email_password"
RECEIVER_EMAIL = "your_email@gmail.com"

subject = "🎵 Your Weekly Spotify Stats"
body = summary  # This is from the previous script

yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
yag.send(to=RECEIVER_EMAIL, subject=subject, contents=body)

print("Email sent successfully!")
