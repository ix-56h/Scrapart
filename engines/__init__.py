import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ScrapEngine():
    def __init__(self, config):
        self.config = config

    # Just check if the current url is present in "appartements.txt"
    def check_if_data_exist(self, url):
        f = open("datas.txt", 'r')
        datas = f.readlines()
        f.close()
        for line in datas:
            if url in line:
                return True
        return False

    # Writes datas functions into "appartements.txt"
    def write_data(self, url):
        f = open("datas.txt", 'a')
        f.write(url+'\n')
        f.close()
        return
    
    def scrap_data() -> str:
        # Return mail content to append
        pass
    
class MailingEngine():
    def __init__(self, config):
        self.receiver = config['GMAIL']['receiver']
        self.receiver2 = config['GMAIL']['receiver2']
        self.sender_address = config['GMAIL']['email']
        self.sender_pass = config['GMAIL']['pass']
        self.mail_content = ""
    
    # Notify me by EMAIL 
    def notify_mail(self):
        for receiver in [self.receiver, self.receiver2]:
            if receiver:
                #Setup the MIME
                message = MIMEMultipart()
                message['From'] = self.sender_address
                message['To'] = receiver
                message['Subject'] = '[Python][Appartement] Nouveaux appartements disponibles !'   #The subject line
                #The body and the attachments for the mail
                message.attach(MIMEText(self.mail_content, 'plain'))
                #Create SMTP session for sending the mail
                session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                session.starttls() #enable security
                session.login(self.sender_address, self.sender_pass) #login with mail_id and password
                text = message.as_string()
                session.sendmail(self.sender_address, receiver, text)
                session.quit()