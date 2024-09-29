from django.shortcuts import render
import requests

# Create your views here.
# Variable for API key
API = "cd543fbe65b94c6d9c3a6095b7b88f28"

def home(request):
    # Get the 'country' and 'category' parameters from the request
    country = request.GET.get('country', '')
    category = request.GET.get('category')
    
    # Initialize the URL variable
    url = ""
    
    # Check if the 'country' parameter is provided
    if country:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API}"
    elif category:  # Corrected: Use `elif` instead of `else` to ensure it checks if `category` is present
        url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={API}"
    
    # Fetch data only if URL is set, to avoid making requests with an empty URL
    if url:
        response = requests.get(url)
        data = response.json()
        # Extracting articles from the response data
        articles = data.get('articles', [])
    else:
        # If neither `country` nor `category` is provided, show an empty list or a default message
        articles = []

    context = {
        'articles': articles
    }

    return render(request, "newsapi/home.html", context)
