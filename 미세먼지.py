import requests

key = 'tbs6UQbrFmdbBFgOrvIGo9euNZV0ZZCnaT8wtnOpYKF3XyTQ1Nf25h6MoKCZHmOCpDa3nreGmZhnUVbSUKzvtw%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=5&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
data = requests.get(url).json()


"""
실습
'sidoName의 미세먼지 농도는 pm10value입니다.'라는 메시지를 출력하시오.
"""
sido_name = data['response']['body']['items'][4]['sidoName']
# print(sido_name)
dust = int(data['response']['body']['items'][4]['pm10Value'])
# print(dust)
print(f'{sido_name}의 미세먼지 농도는 {dust}입니다.')