from django.shortcuts import render

# Create your views here.
def Home(request):
    context={}
    context['openpopup']=True
    return render(request,'index.html',context)

def textcompare(request):
    return render(request,'textcompare.html')