# from django.contrib import admin
# from django.forms import TextInput, Textarea
# from readme_service.models import ReadMeModel
# from readme_service.forms import ReadMeForms
# from django.db import models
#
# # Register your models here.
#
# class ReadMeAdmin(admin.ModelAdmin):
#     fields =['FileType','PerformanceYear','QuarterOrAnualIswntifier',
#                   'KnownData','expectedFieldChanges','UpcomingChanges','UserName']
#
#     readonly_fields = ('created_at','updated_at')
#     form = ReadMeForms
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size': '20'})},
#         models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
#     }
#
# admin.site.register(ReadMeModel,ReadMeAdmin)


from django.apps import apps
from django.contrib import admin


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)


models = apps.get_models()
for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass