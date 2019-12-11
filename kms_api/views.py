from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
import json
from kms_api import kyungan_hs_meal_parse


@csrf_exempt
def answer(request):
    # JSON 받아내기
    json_str = request.body
    json_data = json.loads(json_str)
    # action-prams 파라미터 추출
    received_params = json_data["action"]["params"]
    # params 에서 내부 파라미터들 추출
    # sys_date 가 문자열로 인식됨;
    # 이유는 모르겠음 str to dict 처리
    received_sys_date = received_params['sys_date']
    received_sys_date = json.loads(received_sys_date)
    received_date = received_sys_date["date"]
    date = str(received_date).replace('-', '')
    school_name = '경안고등학교'
    # 수집한 정보들을 다시 전송
    result = {
        "version": "2.0",
        "data": {
            "meal_menu": kyungan_hs_meal_parse.get_menu(int(date)),
            "date": date,
            "school_name": school_name
        }
    }
    json.dumps(result)

    return JsonResponse(result)
