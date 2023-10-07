from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.

# 1 without REST and no model query FBV


def no_rest_no_model(request):
    guests = [{
        'id': 1,
        'Name': 'Omar',
        'Mobile': '01111111111',
    },
        {
        'id': 2,
        'Name': 'Yassin',
        'Mobile': '0110000000',
    },
    ]
    return JsonResponse(guests, safe=False)
