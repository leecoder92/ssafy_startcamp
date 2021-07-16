import requests

# 챗봇 api정보
token = '1814396870:AAF4Zkv-uboYXUv2GdYy5saF-NETb_PFYDQ'

app_url = f'https://api.telegram.org/bot{token}/'

response = requests.get(app_url + 'getUpdates').json()

#미세먼지 api정보
key = 'tbs6UQbrFmdbBFgOrvIGo9euNZV0ZZCnaT8wtnOpYKF3XyTQ1Nf25h6MoKCZHmOCpDa3nreGmZhnUVbSUKzvtw%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&returnType=json&numOfRows=5&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
data = requests.get(url).json()

#미세먼지 텍스트 설정
sido_name = data['response']['body']['items'][0]['sidoName']
dust = int(data['response']['body']['items'][0]['pm10Value'])

#챗봇 ID설정
chat_id = response.get('result')[0].get('message').get('chat').get('id')
# data['result'][0]['message']['chat']['id']

#보낼 메시지 설정
text = f'{sido_name}의 미세먼지 농도는 {dust}입니다.'

#메시지 보내기
message_url = f'{app_url}sendMessage?chat_id={chat_id}&text={text}'

print(requests.get(message_url))