import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "freidora@fritas.patatas"
receiver_email = "vokefam765@luravell.com"
password = "L4Fr31d0r4Fr13P47474$"
subject = "Hello"
body = "Body"

# MW_SMTP_ID=fritas.patatas
# MW_SMTP_HOST=ssl://smtp.firtas.patatas
# MW_SMTP_PORT=465
# MW_SMTP_USER=freidora@fritas.patatas
# MW_SMTP_PASS=
# MW_SENDER=freidora@fritas.patatas

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to email
message.attach(MIMEText(body, "plain"))

try:
    # Connect to the SMTP server
    server = smtplib.SMTP(
        "ssl://smtp.firtas.patatas", 465
    )  # Replace with your SMTP server and port
    server.starttls()  # Secure the connection
    server.login(sender_email, password)

    # Send email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email. Error: {str(e)}")

finally:
    # server.quit()
    pass
