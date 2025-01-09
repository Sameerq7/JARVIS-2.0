import os
import socket
import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv
import keyboard
from features.speak_and_play import speak_and_play

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

socket.setdefaulttimeout(10)

# def read_recent_emails():
#     if not EMAIL or not PASSWORD:
#         print("Email or Password not set properly in environment variables.")
#         return

#     try:
#         mail = imaplib.IMAP4_SSL("imap.gmail.com")
#         mail.login(EMAIL, PASSWORD)
#         mail.select("inbox")

#         status, messages = mail.search(None, "ALL")
#         email_ids = messages[0].split()

#         if not email_ids:
#             print("Boss, there is nothing to display.")
#             speak_and_play("Boss, there is nothing to display.")
#             mail.logout()
#             return

#         recent_email_ids = email_ids[:5]

#         for index, i in enumerate(recent_email_ids):
#             status, msg_data = mail.fetch(i, "(RFC822)")
#             msg = email.message_from_bytes(msg_data[0][1])

#             sender = msg.get("From")
#             sender_name, sender_email = email.utils.parseaddr(sender)

#             subject, encoding = decode_header(msg["Subject"])[0]
#             if isinstance(subject, bytes):
#                 subject = subject.decode(encoding if encoding else 'utf-8')

#             body = ""
#             if msg.is_multipart():
#                 for part in msg.walk():
#                     if part.get_content_type() == "text/plain":
#                         body = part.get_payload(decode=True).decode()
#                         break
#             else:
#                 body = msg.get_payload(decode=True).decode()

#             message = f"Boss, this email is from sender name {sender_name} with the subject {subject}. Body of the email: {body}"
#             print(message)
#             speak_and_play(message)

#             if index < len(recent_email_ids) - 1:
#                 print("Press Enter to continue reading or Esc to exit reading.")
#                 while True:
#                     if keyboard.is_pressed('esc'):
#                         print("Exiting reading.")
#                         mail.logout()
#                         return
#                     elif keyboard.is_pressed('enter'):
#                         break

#         print("Boss, there is nothing more to display.")
#         speak_and_play("Boss, there is nothing more to display.")
#         mail.logout()
    
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         speak_and_play(f"An error occurred: {e}")

def read_recent_emails():
    if not EMAIL or not PASSWORD:
        print("Email or Password not set properly in environment variables.")
        return

    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        # Get all email IDs (latest first)
        status, messages = mail.search(None, "ALL")
        email_ids = messages[0].split()[::-1]  # Reverse order for latest emails

        if not email_ids:
            print("Boss, there is nothing to display.")
            speak_and_play("Boss, there is nothing to display.")
            mail.logout()
            return

        for email_index, email_id in enumerate(email_ids[:2]):  # Limit to 2 emails per execution
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])

            sender = msg.get("From")
            sender_name, sender_email = email.utils.parseaddr(sender)

            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")

            # Extract and clean email body
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain" and not part.get("Content-Disposition"):
                        body = part.get_payload(decode=True).decode()
                        break
            else:
                body = msg.get_payload(decode=True).decode()

            # Remove links and limit to 3 sentences for speaking
            sentences = [line for line in body.split("\n") if not line.startswith("http") and line.strip()]
            body_preview = " ".join(sentences).split(".")[:3]  # First 3 sentences
            body_preview = ". ".join(body_preview).strip() + "."

            # Print the full body and speak the first three lines
            print(f"\nEmail {email_index + 1}:")
            print(f"From: {sender_name} <{sender_email}>")
            print(f"Subject: {subject}")
            print("Body:")
            print(body.strip())
            speak_and_play(
                f"Boss, this email is from {sender_name} with the subject {subject}. "
                f"And Here is the message in the email body: {body_preview}"
            )

        print("\nBoss, no more emails will be spoken for now.")
        speak_and_play("Boss, no more emails will be spoken for now.")
        mail.logout()

    except Exception as e:
        print(f"An error occurred: {e}")
        speak_and_play(f"An error occurred: {e}")
