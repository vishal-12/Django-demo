from django.db import models
from django.contrib import admin
from django.forms import TextInput, Textarea
from readme_service.template import template
from readme_service.models import (ReadMeModel)
from readme_service.sent_email import Email
from readme_service.send_html_report import file_operation
from django.conf import settings
import os
from os.path import join, dirname
from dotenv import load_dotenv
import datetime
#
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
template_name = os.getenv("template")


@admin.register(ReadMeModel)
class ReadMeAdmin(admin.ModelAdmin):
    list_display = ['id','FileType','ManagedCarePlan','PerformanceYear','QuarterOrAnnualIdentifier',
                   'KnownData','ChangestotheFileinthisDelivery','UpcomingChanges']
    #readonly_fields = ('created_at','updated_at')
    formfield_overrides = {
         models.CharField: {'widget': TextInput(attrs={'size': '60'})},
         models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols': 80})},
    }

    actions = ['send_email']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        if obj.user.is_authenticated:
            print ("current logged in user is {}".format(obj.user))
        super().save_model(request, obj, form, change)

    def send_email(self, request, queryset):
        requested_data = queryset.values()
        count=0
        length = len(requested_data)
        filename = list();email_body_data= None; attachments= list()
        while count < length:
            attachment,File_name,email_data = template(requested_data[count],request.user)
            filename.append(File_name)
            attachments.append(attachment)

            if email_body_data is None:
                email_body_data = email_data
            count+=1

        count1=0

        html_email_data = list()
        while count1 < length:
            email_data_bt_jinja=file_operation(template_name,requested_data,request.user)
            html_email_data.append(email_data_bt_jinja)
            count1+=1
        send_from ="YOUR EMAIL"
        send_to =["YOUR EMAIL"]
        subject ="Regarding : DXC Readme File Report"
        attachment = html_email_data #attachments
        email_body=   email_body_data
        password = "Password"
        filename = filename
        #print (send_from,send_to,subject,email_body,attachments,password,filename)
        email = Email(send_from=send_from, send_to=send_to, subject=subject, email_body=email_body, attachment=attachment,
                                  password=password, filename=filename)
        email.send_mail()
    send_email.short_description = "Send selected ReadMe Data to Sender"

admin.site.site_header = "DXC Admin"
admin.site.site_title = "DXC Admin Portal"
admin.site.index_title = "Welcome to DXC Portal"


