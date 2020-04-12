import requests

from botank.request_generator import create_request
from botank.shooter_result import ShooterResults
from botank.simple_responders import UserModel


def run_simulation(url, user_model=None, verbose=True, n=10):
    if user_model is None:
        user_model = UserModel()

    reqs = []
    resps = []
    times = []
    codes = []
    resp = {}

    session_id = 0
    for i in range(n):
        new_session = (i == 0) or resp.get('response', {}).get('end_session', False)
        if new_session:
            session_id += 1
        text = user_model.make_next_phrase(resp, message_id=i)
        if verbose:
            print('u:', text)
        req = create_request(text, message_id=i, new_session=new_session, session_id=session_id)
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
