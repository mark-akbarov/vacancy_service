import requests
from config.settings import ESKIZ_EMAIL, ESKIZ_PASSWORD, ESKIZ_URL


# ESKIZ_URL='https://notify.eskiz.uz/api/'
# ESKIZ_PASSWORD='MJ0G0uxFaDmVK0cfG3msXCfIyaVLI4IQPxQeAjmq'
# ESKIZ_EMAIL='markakbarov@gmail.com'

def get_token():
    url = ESKIZ_URL + 'auth/login/'
    body = {'email': ESKIZ_EMAIL, 'password': ESKIZ_PASSWORD}
    res = requests.post(url, json=body)
    print(res.content)
    if res.status_code == 200:
        return res.json().get('data').get('token')


def send_sms(jobs):
    body = {
    "mobile_phone": "998901515484",
    "message": f"{jobs}",
    "from": "4546"
    }
    url = ESKIZ_URL + "message/sms/send/"
    token = get_token()
    headers = {'Authorization': f'Bearer {token}'}
    res = requests.post(url, headers=headers, json=body)
    print(res.content)
    if res.status_code == 200:
        return 'success'