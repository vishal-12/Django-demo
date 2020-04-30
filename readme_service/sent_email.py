#!bin/bash/env python

import smtplib
import os, sys, re, ast
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from datetime import date, timedelta
import argparse
import json
import ssl


# from dotenv import load_dotenv


def send_mail(send_from, send_to, subject, text, email_data, files=None):
    read = "{}\n{}\n{}\n".format('', '', '')
    text = read + text
    print(text)

    assert isinstance(send_to, list)
    # assert isinstance(files, list)

    msg = MIMEMultipart();
    msg['From'] = send_from;
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True);
    msg['Subject'] = subject
    filename = "readme.doc"
    # msg.attach(MIMEText(text,"plain"))
    part = MIMEBase("application", "octet-stream")
    part.set_payload(text)
    encoders.encode_base64(part)
    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    msg.attach(part)
    # context = ssl.create_default_context()
    part = MIMEText(email_data, 'plain');
    msg.attach(part);
    msg.as_string()
    # smtp = smtplib.SMTP("smtp.outlook.office365.com",587, timeout=20);smtp.starttls()

    smtp = smtplib.SMTP("smtp.gmail.com:587");
    smtp.starttls()
    smtp.ehlo();
    smtp.login('vibhu0891@gmail.com', 'Kaushik93!!')
    smtp.sendmail(send_from, send_to, msg.as_string());
    smtp.close()


# base_path=re.search(r'/[a-z]+/[a-z]+/',os.path.realpath(sys.argv[0]))
# load_dotenv(os.path.join(base_path.group(),'.env'))
