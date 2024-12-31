from django.shortcuts import render # type: ignore
import requests
import json

# Create your views here.


def get_country_data(city):
    api_key = "oc05ECOYzofAPPdequkF60EZU6rLlsVyk0X5ExHA"
    api_url = f"https://countryapi.io/api/all?apikey={api_key}"
    response = requests.get(api_url)
    data = response.json()
    return data

def index(request):
    return render(request, 'courses/landingPage.html')

def home_stripe(request):
    return render(request, "courses/homeStripe.html")

def confirm_stripe(request):
    return render(request, "confirmStripe.html")