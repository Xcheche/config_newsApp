from django.shortcuts import render
import requests

# Create your views here.
# Variable for api key
API = "cd543fbe65b94c6d9c3a6095b7b88f28"


def home(request):
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API}"
    response = requests.get(url)
    data = response.json()
    print(data)

    return render(request, "newsapi/home.html", {"data": data})
