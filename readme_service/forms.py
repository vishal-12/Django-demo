from django import forms
from readme_service.models import ReadMeModel


class ReadMeForms(forms.ModelForm):
    class Meta:
        model = ReadMeModel
        fields =['FileType','Managed_care_plan','PerformanceYear','QuarterOrAnnualIdentifier',
                  'KnownData','ChangestotheFileinthisDelivery','UpcomingChanges']

    FileType = forms.CharField(label='File Type')
    
    Managedcareplan = forms.CharField(
        label ='Managed Care Plan')
    
    PerformanceYear = forms.CharField(
        label='Performance year'
    )
    QuarterOrAnnualIdentifier = forms.CharField(
        label='Quarter or Annual Identifier'
    )
   
    KnownData=forms.CharField(
        label='Known data quality issues'
    )
    ChangestotheFileinthisDelivery=forms.CharField(
        label='Changes to the File in this Delivery' 
    )
    UpcomingChanges=forms.CharField(
        label='Upcoming Changes approved by ODM and Tentative Date'
    )
    