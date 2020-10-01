# created file by Keval

# importing necessary modules
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

# def aboutus(request):
    # return render(request, "hello")


def analyze(request):


    # Get the text
    djtext = request.POST.get('text', 'default')

    # Retrieve checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')


    # Analyze the text
    # Check which checkbox is on(Clicked)
    if removepunc == "on":
        punctuations = '''!()-{}[];:'"/<>.\,?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        dic1 = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        dic1 = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        dic1 = {'purpose':'Removed NewLine', 'analyzed_text':analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        dic1 = {'purpose':'Extra Space Remover', 'analyzed_text':analyzed}
        djtext = analyzed

    if charcounter == "on":
        analyzed = len(djtext)
        dic1 = {'purpose':'Char Counter', 'analyzed_text':analyzed}
        # return HttpResponse(f"{djtext} - {len(djtext)}")

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcounter != "on"):
        return HttpResponse("Error")


    return render(request, 'analyze.html', dic1)
