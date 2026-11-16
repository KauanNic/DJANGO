import os
from django.http import HttpResponse


def home(request):
    file_path = os.path.join(os.path.dirname(__file__), 'index.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        return HttpResponse(f.read())
