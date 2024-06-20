from datetime import datetime

from django.shortcuts import render
def index(request):
    return render(request, 'catalog/index.html', {'date': datetime.now(), 'pseudo': 'Olive & Tom'})
