from django.db import models
from readme_service.sent_email import *

class ReadMeModel(models.Model):

    class Meta:
        db_table = 'tbl_readme_file'
        verbose_name = "ReadMe data"
        verbose_name_plural = "ReadMe"
        ordering = ("created_at",)

    FileType = models.CharField(max_length=256, verbose_name='File Type')
    PerformanceYear = models.CharField(max_length=256, verbose_name='Performance year(s)')
    QuarterOrAnualIswntifier = models.CharField(max_length=256,verbose_name='Quarter or Annual Identifier(s)')
    KnownData = models.CharField(max_length=256,verbose_name='Known data quality issues')
    expectedFieldChanges = models.CharField(max_length=256,verbose_name='Expected Field changes')
    UpcomingChanges = models.CharField(max_length=256,verbose_name='Upcoming changes approved by ODM')
    UserName = models.CharField(max_length=256,verbose_name='User Name')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Updated At')

    def save(self,*args,**kwargs):

        if self.FileType:
            pass

        print (self.FileType)
        send_from = "vibhu0891@gmail.com"  # os.getenv('sender')
        send_to = ["vibhu0891@gmail.com"]  # os.getenv('reciever')
        print(send_from)
        print(send_to)

        # attachment = '''Hi,
        #
        # Please find attached readme file.
        #
        #
        # Regards,
        # Vishal Sharma'''
        attachment = "Hi,\n\n" \
                     "Please find attached readme file.\n\n" \
                     "Regards,\n" \
                     "Vishal Sharma"
        print (attachment)

        email_data = "               ReadMe File Report\n\n" \
                     "File Type = {}\n\n" \
                     "Performance year(s) = {}\n\n" \
                     "Quarter or Annual Identifier(s) = {}\n\n" \
                     "Known data quality issues = {}\n\n"\
                     "Expected Field changes = {}\n\n" \
                     "Upcoming changes approved by ODM = {}\n\n" \
                     "User Name = {}".format(
            self.FileType,
            self.PerformanceYear,
            self.QuarterOrAnualIswntifier,
            self.KnownData,
            self.expectedFieldChanges,
            self.UpcomingChanges,
            self.UserName)

        print (email_data)

        send_mail(send_from, send_to, "DXC : ReadMe file", email_data, attachment)
        super(ReadMeModel, self).save(*args,**kwargs)
        return True

    def __str__(self):
        return self.FileType

    def __unicode__(self):
        return unicode(self.FileType) or u''
#
# class ReadMeUserManager(BaseUserManager):
#     class Meta:
#         db_table = 'tb1_readme_manager'
#         verbose_name = "Manager Tables"
#         #ordering = (created_at,)
#
#     def create_user(self, email, first_name, last_name, password=None,commit=True):
#         """
#             Creates and saves a User with the given email, first name, last name
#             and password.
#         """
#
#         if not first_name:
#             raise ValueError('User must have an First Name')
#         if not last_name:
#             raise ValueError('User must have an Last Name')
#         if not email:
#             raise ValueError('User must have an valid email address')
#
#         user = self.model(email=self.normalize_email(email),
#                      first_name=first_name,
#                     last_name=last_name
#                           )
#         user.set_password(password)
#         if commit:
#             user.save(using=self._db)
#         return user
#
#     def create_superuser(self,email, first_name, last_name, password):
#         """
#             Creates and saves a superuser with the given email, first name,
#             last name and password
#         """
#         user = self.create_user(email,
#                                 first_name=first_name,
#                                 last_name=last_name,
#                                 password=password,
#                                 commit=False
#                                 )
#         user.is_staff= True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
