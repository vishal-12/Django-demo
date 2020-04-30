from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
# Create your views here.



def create_loan_view(request):

    customers = ReadMeModel.objects.all()
    print (customers)
    form = ApplyLoanForm()
    if request.method == 'POST':
        print (request.data)
        form = ReadMeForms(request.POST)
        if form.is_valid():
            client = form.save()
            client.save()
        return True


def index(request):
    return HttpResponse("DXC ReadME file Automation")
