from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'ai/index.html')

def squat(request):

    return render(request, 'ai/squat.html')