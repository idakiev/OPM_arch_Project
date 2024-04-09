from django.shortcuts import render


# TODO: Implement the search bar!
def index(request):

    return render(request, 'web_app/index.html')
