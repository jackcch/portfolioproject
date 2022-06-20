from django.shortcuts import render

def survey(requests):
    return render(requests, 'survey/surveyform.html')