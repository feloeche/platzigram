#platzi gram views
from django.http import HttpResponse
#Utilities
from datetime import datetime
import json


def hello_world(request):

    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return  HttpResponse(f'Oh, hi Current server time is {now}')

def sort_integers(request):
    numbers = request.GET['numbers']
    
    numbers = [int(i) for i in numbers.split(',')]
    neat_list = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': neat_list,
        'message': 'integers sorted successfuly'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        massage = f'sorry{name}, you are not allowed here'   
    else:
        massage = f'Hello {name}!!, Welcome to platzigram'
    
    return HttpResponse(massage)

    