from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'index.html')

def textcompare(request):
    return render(request,'textcompare.html')