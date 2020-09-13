#!bin/bash/env python

import smtplib
import os, sys
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import argparse
import logging
import ast
from email import encoders


class Email(object):
    def __init__(self, send_from=None, send_to=None, subject=None, email_body=None, attachment=None, password=None,
                 filename=None):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d')
        self.logger = logging.getLogger(__name__)
        self.send_from = send_from
        self.send_to = send_to
        self.subject = subject
        self.email_body = email_body
        self.password = str(password)
        self.attachment = attachment
        self.filename = filename

    def send_mail(self, files=None):
        self.logger.info("going to send email to {} from {}".format(self.send_to, self.send_from))
        assert isinstance(self.send_to, list), "should be list"

        # adding sendders and recievers
        msg = MIMEMultipart();
        msg['From'] = self.send_from;
        msg['To'] = COMMASPACE.join(self.send_to)
        msg['Date'] = formatdate(localtime=True);
        msg['Subject'] = self.subject

        print ("-----------------------")

        if self.attachment and self.filename:
            for count, filename in enumerate(self.filename):
                print(count, filename, self.attachment[count])
                part = MIMEBase("application", "octet-stream")
                part.set_payload(self.attachment[count])
                encoders.encode_base64(part)

                # Add header as key/value pair to attachment part
                # filename= self.filename

                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {filename}",
                )
                msg.attach(part);
        else:
            self.logger.info("attachment can't be None")
            raise

        if self.email_body:
            part = MIMEText(self.email_body, 'plain');
            msg.attach(part)
            msg.as_string()
        else:
            self.logger.info("email_body can't be None")
            raise

        # for outlook
        # smtp = smtplib.SMTP("smtp.outlook.office365.com",587, timeout=20);smtp.starttls()

        # for gmail
        smtp = smtplib.SMTP("smtp.gmail.com", 587, timeout=20);
        smtp.starttls()
        smtp.ehlo();

        # going to login
        try:
            smtp.login(self.send_from, self.password)
            smtp.sendmail(self.send_from, self.send_to, msg.as_string());
            smtp.close()
        except Exception as error:
            self.logger.info("task.status failed due to {}".format(error))
            raise

        self.logger.info("task.status success")

#
# if __name__ == "__main__":
#     send_from = "vibhu0891@gmail.com"  # "put hour email id here"  #example "abc@gmail.com"
#     send_to = [
#         "vibhu0891@gmail.com"]  # ["put the email id whom you want to add into to"]   #example ["emailid1@gmail.com","email-id-2@gmail.com"]
#     subject = "This is the test email"  # example "this is the test email"
#     password = "Kaushik93!!"  # example "Kaushik93!!"  #"your gmail password"
#     email_body = '''
#
#
#         this is the email body email
#
#         '''  # "this is the test email "
#     attachment = ["attachment", "new", "start", "fuck"]
#     filename = ["vishal.txt", "aman.txt", "raman.txt"]
#     aa = Email(send_from=send_from, send_to=send_to, subject=subject, email_body=email_body, attachment=attachment,
#                password=password, filename=filename)
#     aa.send_mail()























##if __name__=="__main__":
##
##    parser = argparse.ArgumentParser(description='Input information about job logs.')
##
##    parser.add_argument('--send_from', dest='send_from' , required=True, help='Please enter send_from of sender')
##    #parser.add_argument('--send_to', dest='send_to' , required=True, help='Please enter email address at which you want to send to')
##    parser.add_argument('--send_to','--list', nargs='+', help='it will append the string to list', required=True)
##    parser.add_argument('--subject', dest='subject' , required=True, help='Please enter URL of Vcenter')
##    parser.add_argument('--password', dest='password' , required=True, help='Please enter password of email')
##    parser.add_argument('--email_body', dest='email_body' , required=True, help='Please enter email_body of sender')
##    args = parser.parse_args()
##    a=Email(args.send_from,args.send_to,args.subject,args.email_body,args.password)
##    a.send_mail()




