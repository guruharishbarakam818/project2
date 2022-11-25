from django.shortcuts import render

# Create your views here.
def jinjacondition(request):
    d={'name':'harish'}
    return render(request,'jinjacondition.html',d)