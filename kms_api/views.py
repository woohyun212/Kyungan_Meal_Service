from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json


def test():
    with open("../isitcomes.txt", 'r', encoding=('utf-8')) as count:
        countvalue = int(count.read()) + 1
    with open("../isitcomes.txt", 'w', encoding=('utf-8')) as count:
        count.write(str(countvalue))
    with open("../isitcomes.txt", 'r', encoding=('utf-8')) as count:
        print(int(count.read()) + 1)
    return 0


def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘', '내일']
    })


@csrf_exempt
def answer(request, message):
    print(message)  # 여기까지 오는데 500에러라;;ㅎ
    print(request)
    '''test()
    # JSON 받아내기
    json_str = ((request.body).decode('utf-8'))
    json_data = json.loads(json_str)

    # 파라미터 값 걸러내기
    json_object = json_data["action"]
    received_params = json_object["params"]
    date = received_params['date']
    meal_menu = received_params['meal_menu']

    result = {
        "version": "2.0",
        "data": {
            "menu": meal_menu
        }
    }'''
    # 그러게요 왤까요.
    return render(request, 'test.html')




