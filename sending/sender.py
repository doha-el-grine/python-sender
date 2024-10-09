import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender_email, sender_password, recipient_emails, subject, body_template):
    try:
        # Setup the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  
        server.login(sender_email, sender_password)

        # Send email to each recipient
        for recipient in recipient_emails:
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = recipient
            message['Subject'] = subject

            # Customize the email body
            body = body_template.replace('${recepeint_emailname}', recipient.split('@')[0])
            message.attach(MIMEText(body, 'plain'))

            # Send the email
            server.sendmail(sender_email, recipient, message.as_string())
            print(f"Email sent to {recipient}!")

        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

# Email data
sender_email = 'dohaelgr1@gmail.com'
sender_password = 'wxyv rnzy dufh lseq'
recipient_emails = ['elgrinedouha@gmail.com',
                    'inesfaidi25@gmail.com' , 
                    'el-grinedouha@hotmail.com',
                    'Aderbazasi@gmail.com',
                    'Aderzoutdoors@gmail.com',
                    'Bugatti28@gmail.com',
                    'Ilyassmcclips@gmail.com',
                    'Ilyassaderbaz1@gmail.com',
                    'Cryptoaderbaz@gmail.com',
                    'ilyassaderbaz5@gmail.com',
                    'j89211274@gmail.com',
                    'Sam.laayouni@aui.ma'
]  

subject = 'Test Email'
body_template = 'Dear ${recepeint_emailname}, this is a test email sender using Python!(noteswap)'

# Send the email
send_email(sender_email, sender_password, recipient_emails, subject, body_template)
