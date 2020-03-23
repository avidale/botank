import requests
import random

from botank.shooter_result import ShooterResults
from botank.request_generator import create_request
from botank.simple_responders import resample_text


TOP_PHRASES = [
    'привет',
    'алиса',
    'яндекс',
    'а',
    'повтори',
    'что ты умеешь',
    'что ты можешь',
    'помощь',
    'выход',
    'выйти',
    'домой',
    'хватит',
]


def make_next_phrase(resp, message_id=1, p_skip_button=0.5, p_skip_resample=0.5):
    buttons = resp.get('response', {}).get('buttons', [])
    prev_text = resp.get('response', {}).get('text', '')
    if message_id == 0:
        return 'привет'
    if buttons and random.uniform(0, 1) > p_skip_button:
        return random.choice(buttons)['title']
    if prev_text and random.uniform(0, 1) > p_skip_resample:
        return resample_text(prev_text)
    return random.choice(TOP_PHRASES)


def run_simulation(url, verbose=True, n=10):

    reqs = []
    resps = []
    times = []
    codes = []
    resp = {}

    for i in range(n):
        text = make_next_phrase(resp, message_id=i)
        if verbose:
            print('u:', text)
        req = create_request(text, message_id=i)
        p = requests.post(url, json=req)
        reqs.append(req)
        codes.append(p.status_code)
        times.append(p.elapsed.total_seconds())
        if not p.status_code == 200:
            if verbose:
                print('b: error', p.status_code)
            resps.append(None)
            continue
        resp = p.json()
        resps.append(resp)
        if verbose:
            print('b:', resp['response']['text'])
    return ShooterResults(requests=reqs, responces=resps, times=times, codes=codes)
