#from ast import operator
#from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.
#def calculator(request):
   # return HttpResponse('계산기 기능 구현 시작입니다. 이게 맞나요?')
#    print(f'request = {request}')
#    print(f'request type = {type(request)}')

   # 1. 데이터 확인
#    num1 = request.GET.get('num1')
#    num2 = request.GET.get('num2')
#    operators = request.GET.get('operators')

   # 2. 계산
#    if operators == '+':
#        result = int(num1) + int(num2)
#    elif operators == '-':
#        result = int(num1) - int(num2)
#    elif operators == '*':
#        result = int(num1) * int(num2)
#    elif operators == '/':
#        result = int(num1) / int(num2)
#    else:
#        result = 0

    # 3. 응답
#    return render(request, 'calculator.html', {'result': result})

from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.

lotto_num = []

def getRandomNumber():
    number = random.randint(1,45)
    return number

    print(f'request = {request}')
    print(f'request type = {type(request)}')

def lotto(request):
    import random
    result = random.sample(range(1,46), 6)
    context = {
        'result':result
    }
    return render(request, 'lotto.html', context)



