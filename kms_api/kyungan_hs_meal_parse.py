import requests
from bs4 import BeautifulSoup
import re


def get_menu(ymd):
    try:
        date = ymd
        url = "http://kyungan.hs.kr/lunch.view?date=%d" % date

        html_code = get_html(url)
        btsoup = BeautifulSoup(html_code, "html.parser")
        span_tags = btsoup.find_all("span")

        span_tags = str(span_tags)
        span_tags = re.sub('<a.*?>.*?</a>', '', span_tags, 0, re.I | re.S)
        span_tags = re.sub('<span class=.*?>.*?</span>', '', span_tags, 0, re.I | re.S)
        span_tags = span_tags.replace('[', '')
        span_tags = span_tags.replace(']', '')
        span_tags = span_tags.replace(' ', '')
        span_tags = span_tags.replace('<span>', '')
        span_tags = span_tags.replace('</span>', '')
        element = span_tags.split(',')
        while '' in element:
            element.remove('')
        element.remove('FONTSIZE')
        element.remove('NITROEYEHIGHSCHOOL')
        element.remove('식단상세보기')

        while len(element) < 3:
            element.append('식단 정보가 없습니다.')

        for i in range(len(element)):
            element[i] = element[i].replace('&amp;', '/')
            element[i] = element[i].replace('.', '\n')
            element[i] = element[i] + '\n'
        meal_menu = "〓〓〓〓[급식표]〓〓〓〓\n──(해)조식(해)──\n" + element[0] + "──(밥)중식(밥)──\n" + element[1] + "──(치킨)석식(치킨)──\n" + \
                    element[2] + "〓〓〓〓〓〓〓〓〓〓〓〓"

    except:
        meal_menu = '학교 사이트에서 식단을 불러올 수 없었습니다,,,!(헉)'

    return meal_menu


def get_html(url):
    received_data = requests.get(url)

    if received_data.status_code == 200:
        html_code = received_data.text

    return html_code

