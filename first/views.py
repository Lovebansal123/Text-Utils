import imp
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello")
    # param = {'name':'Harry','place':'Mars'}
    # return render(request,'index.html', param)


def analyze(request):
    djtext = request.POST.get('text','default')
    djremovepunc = request.POST.get('removepunc','off')
    djfullcapti = request.POST.get('fullcapti','off')
    djnewline = request.POST.get('newline','off')
    djextraspace = request.POST.get('extraspace','off')


# ************ Remove Punctuations *********************
    if djremovepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        djtext = analyzed

# ************* Captialize************************
    if djfullcapti=='on':
        analyzed = ""
        for char in djtext:
                analyzed = analyzed+char.upper()
        djtext = analyzed
# *****************newline remover*******************
    if djnewline=='on':
        analyzed = ""
        for char in djtext:
            # for transporting new line character in network \n and \r both are used 
            if char != '\n' and char!='\r':
                analyzed = analyzed+char
        djtext = analyzed
# *****************extraspace remover*******************
    if(djextraspace=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        djtext = analyzed
        
    if(djextraspace=='off' and djfullcapti=='off' and djnewline=='off' and djremovepunc=='off'):
        return HttpResponse('Error')

    params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    # Analyze the text
    return render(request, 'analyze.html', params)