from django import forms
from readme_service.models import ReadMeModel

class ReadMeForms(forms.ModelForm):
    class Meta:
        model = ReadMeModel
        fields =['FileType','PerformanceYear','QuarterOrAnualIswntifier',
                  'KnownData','expectedFieldChanges','UpcomingChanges','UserName']

    name = forms.CharField(label='File Type')
    PerformanceYear = forms.CharField(
        label='Performance year(s)'
    )
    QuarterOrAnualIswntifier = forms.CharField(
        label='Quarter or Annual Identifier(s)'
    )
    KnownData=forms.CharField(
        label='Known data quality issues'
    )
    expectedFieldChanges=forms.CharField(
        label='Expected Field changes'
    )
    UpcomingChanges=forms.CharField(
        label='Upcoming changes approved by ODM'
    )
    UserName = forms.CharField(
        label='User Name'
    )
