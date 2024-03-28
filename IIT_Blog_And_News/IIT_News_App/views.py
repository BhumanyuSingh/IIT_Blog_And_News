# # from django.shortcuts import render
# from django.shortcuts import render
# import requests
# import json

# Api_key = "ff3c83b79be548d09da3bd2743b64a62"

# def home(request):
#     country = request.GET.get("counrty")
#     cetegory = request.GET.get("cetegory")
#     if country :
#         url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={Api_key}"
#     else:
#         url = f"https://newsapi.org/v2/top-headlines?cetegory={cetegory}&apiKey={Api_key}"



#     # url = "https://newsapi.org/v2/everything?q=tesla&from=2024-02-28&sortBy=publishedAt&apiKey=ff3c83b79be548d09da3bd2743b64a62"
#     response = requests.get(url)
#     data = response.json()
#     # data = json.loads(data)
#     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#     # print(data)
#     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#     # Check if "articles" key exists before using it

#     if "articles" in data.keys():
#         articles = data.get("articles")
#     else:
#         # Handle the case where "articles" is missing (optional)
#         articles = []  # Empty list
#         print("API response might not contain articles")

#     context = {
#         "articles": articles,
#     }

#     return render(request, "news_api/home.html", context)


from django.shortcuts import render
import requests
API_KEY = 'ff3c83b79be548d09da3bd2743b64a62'


# Create your views here.


def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']



    context = {
        'articles' : articles
    }

    return render(request, 'news_api/home.html', context)



















