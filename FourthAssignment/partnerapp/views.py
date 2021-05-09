from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'partnerapp/home.html')

def result(request):
    name = random.sample(range(1, 16), 2)

    list = ('강연우', '김서영', '김소은', '김유진', '김정운', '노은성', '문다연', 
    '박경나', '박혜준', '안현주', '오예림', '이민정', '이연수', '장한빛', '조원아', '황서경')

    partner = random.sample(list, 2)
    return render(request, 'partnerapp/result.html', {'name':name, 'partner': partner})
