from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    usertext = request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    uppercase=request.GET.get('uppercase','off')
    lowercase=request.GET.get('lowercase','off')
    capitalize=request.GET.get('capitalize','off')
    countchar=request.GET.get('countchar','off')
    countword=request.GET.get('countword','off')
    linecount=request.GET.get('linecount','off')
    remnewline=request.GET.get('remnewline','off')
  
    if removepunc =="on":
        punctuations='''!()-[]{};:'"\,/.?@#$%^&*_~`'''
        analyzed =""
        for char in usertext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(uppercase=="on"):
        analyzed=""
        for char in usertext:
            analyzed= analyzed + char.upper()
        params={'purpose':'change to UPPERCASE','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(lowercase=="on"):
        analyzed=""
        for char in usertext:
            analyzed= analyzed + char.lower()
        params={'purpose':'change to lowercase','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(capitalize=="on"):
        analyzed=""
        for char in usertext:
            analyzed= usertext.title()
        params={'purpose':'change to capatalize','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(countchar=="on"):
        analyzed=""
        for char in usertext:
            analyzed= len(usertext)
        params={'purpose':'count characters','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(countword=="on"):
        analyzed=0
        for char in usertext:
            analyzed=len(usertext.split())
        params={'purpose':'count words','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(linecount=="on"):
        analyzed=0
        for char in usertext:
            analyzed=len(usertext.split(".") -1)
        params={'purpose':'count lines','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(remnewline=="on"):
        analyzed=0
        for char in usertext:
            analyzed=usertext.replace("\n\n","")
        params={'purpose':'remove new lines','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    
    else:
        return HttpResponse("error")

