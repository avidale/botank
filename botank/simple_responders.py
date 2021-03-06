from botank.copypaste_responder import copypaste
from botank.phrases import TOP_PHRASES

import random


class UserModel:
    def __init__(self, p_button=None, p_resample=None, texts_collections=None):
        if p_button is None and p_resample is None and texts_collections is None:
            p_button = 0.5
            p_resample = 0.5
            texts_collections = [TOP_PHRASES]
        else:
            if p_button is None:
                p_button = 0
            if p_resample is None:
                p_resample = 0
            if texts_collections is None:
                texts_collections = [TOP_PHRASES]

        self.p_button = p_button
        self.p_resample = p_resample
        self.texts_collections = texts_collections

    def make_next_phrase(self, resp, message_id=1):
        buttons = resp.get('response', {}).get('buttons', [])
        prev_text = resp.get('response', {}).get('text', '')
        if message_id == 0:
            return 'привет'
        if buttons and random.uniform(0, 1) < self.p_button:
            return random.choice(buttons)['title']
        if prev_text and random.uniform(0, 1) < self.p_resample:
            return copypaste(prev_text)
        collection_id = random.randrange(0, len(self.texts_collections))
        return random.choice(self.texts_collections[collection_id])
