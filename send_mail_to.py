import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
from logger_config import logging

subject = "Email Subject"
sender = "<sender mail>"
password = "<sender password i.e. App password of gmail>"


def send_email_to_user(recipients, body):
    logging.mail_send_logger.info("[Started : ] send mail to %s"%(','.join(recipients),))
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        try:
            smtp_server.login(sender, password)
        except smtplib.SMTPAuthenticationError as e:
            logging.mail_send_logger.info("[Failed : ] Authentication failed . receiver: %s sender:%s"%( ','.join(recipients),sender))
            return 
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent! ----------------------->")

def get_html(sent_to, sender):
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Animeta Brandstar Inquiry</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }
                
                .container {
                    max-width: 600px;
                    margin: 20px auto;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                
                h1 {
                    color: #333;
                }
                
                p {
                    color: #666;
                    line-height: 1.6;
                }
                
                .contact-details {
                    margin-top: 20px;
                }
                
                .thank-you {
                    margin-top: 30px;
                    font-weight: bold;
                    color: #4CAF50;
                }
            </style>
        </head>
        <body>

        <div class="container">
            <h1>Hi %s,</h1>
            
            <p>
                I am writing to you on behalf of ‘Animeta Brandstar’, a first-of-its-kind tech-data enabled influencer marketing platform.
                We work with various brands, across categories and markets, on their influencer marketing/branded content briefs.
                And, would love to recommend you for the same, for all relevant opportunities.
            </p>
            
            <p>
                At present, we only have your email ID in our database. Given the time-sensitive nature of these briefs, we would appreciate if you can provide us with your phone/WhatsApp number, where we can reach you or your manager directly, for a faster turn-around.
            </p>
            
            <div class="contact-details">
                <p>Kindly reply to this mail, with the below details:</p>
                <ul>
                    <li>Contact Phone number: </li>
                    <li>Name of Point of contact (POC), if other than you: </li>
                    <li>Alternate email/phone number: </li>
                </ul>
            </div>
            
            <p class="thank-you">Thank you for providing the same!</p>
            
            <p>Warm regards,<br>%s</p>
        </div>

        </body>
        </html>
    '''%(sent_to, sender)

def send_html_mail(recipients, receiver_name):
    logging.mail_send_logger.info("[Started : ] send mail to %s"%(','.join(recipients),))
    sender_name = 'Prabin Pandey'
    msg = EmailMessage()
    msg['Subject'] = 'Email Subject'
    msg['From'] = sender
    msg['To'] = ','.join(recipients)
    msg.set_content(get_html(receiver_name, sender_name), subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        try:
            smtp_server.login(sender, password)
            smtp_server.send_message(msg)
        except smtplib.SMTPAuthenticationError:
            logging.mail_send_logger.info("[Failed : ] Authentication failed . receiver: %s sender:%s"%( ','.join(recipients),sender))
            return
        except BaseException as e:
            logging.mail_send_logger.info("[Failed : ] Failed to send . receiver: %s sender:%s"%( ','.join(recipients),sender))
            return
    logging.mail_send_logger.info("[Success: ] Mail successfully sent!")

# send_email(recipients, body).
