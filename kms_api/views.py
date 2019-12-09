from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json


# txt 파일 열어서 1더하기
def test():
    with open("../isitcomes.txt", 'r', encoding=('utf-8')) as count:
        countvalue = int(count.read()) + 1
    with open("../isitcomes.txt", 'w', encoding=('utf-8')) as count:
        count.write(str(countvalue))
    with open("../isitcomes.txt", 'r', encoding=('utf-8')) as count:
        print(int(count.read()) + 1)
    return 0


# 구버전 카카오톡 챗봇 키보드 리턴.
def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘', '내일']
    })


@csrf_exempt
def answer(request):
    print("여기까진 왔1")
    # ----여기까지 오는지  테스트

    # JSON 받아내기

    json_str = request.body
    print("여기까진 왔2")

    json_data = json.loads(json_str)
    print(json_data)
    print("여기까진 왔3")

    # 파라미터 값 걸러내기
    json_object = json_data["action"]
    print(json_object)
    print("여기까진 왔4")

    received_params = json_object["params"]
    print(received_params)
    print("여기까진 왔5")

    date = received_params['date']
    print(date)
    print("여기까진 왔6")
    meal_menu = received_params['meal_menu']
    print(meal_menu)
    print("여기까진 왔7")

    # 일단은 받은 meal_menu 를 다시 보내기
    result = {
        "version": "2.0",
        "data": {
            "menu": meal_menu,
            "date": date
        }
    }
    print(type(result))
    json.dumps(result)

    print(type(result))
    return JsonResponse(result)

'''

json_str = open('C://Django/test1.json', 'r', encoding=('utf-8'))
json_data = json.load(json_str)
print(type(json_data))

'''