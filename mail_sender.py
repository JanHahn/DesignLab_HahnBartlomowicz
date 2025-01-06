import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random


# Funkcja do wysyłania maila
def send_email(sender_email, receiver_email, subject, body, smtp_server, port, login, password):
    # Utworzenie obiektu wiadomości
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Dodanie treści wiadomości
    message.attach(MIMEText(body, 'plain'))

    try:
        # Połączenie z serwerem SMTP i wysłanie wiadomości
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Użycie TLS do bezpiecznej komunikacji
            server.login(login, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("E-mail sent.")
    except Exception as e:
        print(f"error: {e}")

# Przykład użycia funkcji
send_email(
    sender_email='designlab.locker@gmail.com',
    receiver_email='tomasz.bartlomowicz18@gmail.com',
    subject='Design Lab Locker',
    body=f'Hello, your unlock code is {random.randint(1000, 9999)} ',
    smtp_server='smtp.gmail.com',  # Adres serwera SMTP (np. dla Gmail: 'smtp.gmail.com')
    port=587,  # Port SMTP (np. dla Gmail: 587)
    login='designlab.locker@gmail.com',
    password='ddfg hdzm ombs faof'
)