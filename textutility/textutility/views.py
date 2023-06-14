#i have made this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')


def analyze(request):
    djtext =request.GET.get('text', 'default')


    analyzed=djtext
    params={'purpose':'Remove Punctuations',' analyzed_text':analyzed}
    return render(request, 'anlayze.html', params)

def analyze(request):

    # Get the text
    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
    return render(request,'analyze.html',params)
# # def newlineremove(request):
#     return HttpResponse('''<h1>NEWLINE REMOVE</h1> <a href= "http://127.0.0.1:8000/"> HOME </a> ''')

# def capitalize(request):
#     return HttpResponse('''<h1>CAPITALIZE</h1> <a href= '/'> HOME </a> ''')

# def spaceremove(request):
#     return HttpResponse('''<h1>SPACE REMOVE</h1> <a href= "http://127.0.0.1:8000/"> HOME </a> ''')

# def charcount(request):
#     return HttpResponse('''<h1>CHAR COUNT</h1> <a href= "http://127.0.0.1:8000/"> HOME </a> ''')

