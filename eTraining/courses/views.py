from django.shortcuts import render # type: ignore
from courses.models import Course, Module,Lesson, Ressource, Stripe
import requests
import json

# Create your views here.

#fetch api
def get_country_data():
    api_key = "oc05ECOYzofAPPdequkF60EZU6rLlsVyk0X5ExHA"
    api_url = f"https://countryapi.io/api/all?apikey={api_key}"
    response = requests.get(api_url)
    data = response.json()
    return data

#load data's api in json
def load_json(param):
    j_son = get_country_data()
    d_json = json.dumps(j_son)
    js_loads = json.loads(d_json)
    return js_loads

#views for courses, modules and lessons
def allcourse(request):
    #querys of Module
    alldata = Module.objects.all()

    return render(request, 'courses/allModule.html',{'data':alldata})

def lesson_introduction(request):
    data = Lesson.objects.filter(title='INTRODUCTION OF PYTHON')
    return render(request, 'courses/BasicsIntrodrouction.html', {'data':data})

def index(request):
    return render(request, 'courses/landingPage.html')

def home_stripe(request):
    
    return render(request, "courses/homeStripe.html")

def confirm_stripe(request):
    return render(request, "confirmStripe.html")