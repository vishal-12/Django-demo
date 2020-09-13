from django.db import models
from django import forms
import os
import sys
from jinja2 import Template
from django.forms.widgets import Textarea

File_Type = [
        ('File_R MCP_Quarterly_Enrollment_File','File_R MCP_Quarterly_Enrollment_File'),
        ('File_R Revised MCP_Quarterly_Enrollment_File for Add/Del','File_R Revised MCP_Quarterly_Enrollment_File for Add/Del'),
        ('File_D  MCP_payment_and_attribution_validation File for CPC','File_D  MCP_payment_and_attribution_validation File for CPC'),
        ('File_J  CPC Practice Summary Report/ CPC Partnership Summary Report File',
        'File_J  CPC Practice Summary Report/ CPC Partnership Summary Report File'),
        ('File_O CPC Member-level provider report CSV data file for MCPs',
        'File_O CPC Member-level provider report CSV data file for MCPs'),
        ('File_G5 CPC Shared savings payment file for MCPs','File_G5 CPC Shared savings payment file for MCPs')
         
         ]
Managed_Care_Plan_OPTIONS = [
        ('BUCKEYE','BUCKEYE'),('CARESOURCE','CARESOURCE'),('MOLINA','MOLINA'),('PARAMOUNT','PARAMOUNT'),('UNITED','UNITED')
    ]
PerformaceYear_OPTIONS =[
        ('2018','2018'),('2019','2019'),('2020','2020'),('2021','2021'),('2022','2022'),('2023','2023'),('2024','2024'),('2025','2025'),('2026','2026'),
        ('2027','2027'),('2028','2028'),('2029','2029'),('2030','2030')
        ]

QuarterOrAnnualIdentifier_OPTIONS =[('Q1','Q1'),('Q2','Q2'),('Q3','Q3'),('Q4','Q4'),('Annual','Annual')]

class ReadMeModel(models.Model):

    class Meta:
        db_table = 'tbl_readme_file'
        verbose_name = "ReadMe data"
        verbose_name_plural = "ReadMe"
        ordering = ("created_at",)

    id = models.AutoField(primary_key=True)
    FileType = models.CharField(max_length=256, verbose_name='File Type', default='none', choices=File_Type)
    ManagedCarePlan= models.CharField(max_length=256, verbose_name='Managed Care Plan',default ='none',choices=Managed_Care_Plan_OPTIONS)
    PerformanceYear = models.CharField(max_length=256, verbose_name='Performance Year',default='none',choices=PerformaceYear_OPTIONS)
    QuarterOrAnnualIdentifier = models.CharField(max_length=256,verbose_name='Quarter or Annual Identifier',default='none',choices=QuarterOrAnnualIdentifier_OPTIONS)
    KnownData =  models.TextField(max_length=2000,verbose_name='Known Data Quality Issues')
    ChangestotheFileinthisDelivery = models.TextField(max_length=2000,verbose_name='Changes to the File in this Delivery')
    UpcomingChanges = models.TextField(max_length=2000,verbose_name='Upcoming Changes approved by ODM and Tentative Date')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Updated At')
   
    def save(self,*args, **kwargs):
        super(ReadMeModel, self).save(*args,**kwargs)
        return True

    def __str__(self):
        string_format = "id is {} and File Type is {}. ".format(self.id,self.FileType)
        return string_format

    def __unicode__(self):
        string_format = "id is {} and File Type is {}. ".format(self.id,self.FileType)
        return unicode(string_format) or u''
