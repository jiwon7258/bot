#-*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from django.core.files import File
import test
import sys
import os.path

def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['학식이 궁금', '일정이 궁금']
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    cafeteria_name = received_json_data['content']
    today_date = datetime.date.today().strftime("%m월 %d일")

    return JsonResponse({
        'message': {
            'text': getResult()
        },
        'keyboard': {
            'type': 'buttons',
            'buttons': ['학식이 궁금', '일정이 궁금']
        }

    })

def getResult() :
    try :
        contents = open('/home/jiwon/Django/bot/meal/meal.txt', 'r', encoding='utf-8')
        cont = contents.readlines()
        filecon = ''
        for list in cont:
            filecon = filecon + list
        print(filecon)
        return(filecon)
    except :
        return 'b'

print(getResult())
