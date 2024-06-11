import smtplib

email="henryremax70@outlook.com"
receiver_email="pascalremax900@protonmail.com"
 
subject="subject the aksajjskdsdjn"
message="message sdjsdjsdksjd 1234556789"

text=f"Subject:{subject}\n\n{message}"

server=smtplib.SMTP("smtp-mail.outlook.com",587)
server.starttls()

server.login(email,"Pjdsjdskjsdskewj9")

server.sendmail(email,receiver_email,text)

print("Email has been sent to "+receiver_email)