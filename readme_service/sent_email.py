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
                part = MIMEBase("application", "octet-stream")
                part.set_payload(self.attachment[count])
                encoders.encode_base64(part)
                # Add header as key/value pair to attachment part;cl/.
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

