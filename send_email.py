import yagmail 

# Email credentials (Use environment variables for security!)
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

subject = "🎵 Your Weekly Spotify Stats"
body = summary  # This is from the previous script

yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
yag.send(to=RECEIVER_EMAIL, subject=subject, contents=body)

print("Email sent successfully!")
