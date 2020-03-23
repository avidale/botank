

def create_request(text, message_id=0, user_id=0, session_id=0):
    norm_text = text # todo: really normalize it
    raw_req = {
      "meta": {
        "locale": "ru-RU",
        "timezone": "Europe/Moscow",
        "client_id": "ru.yandex.searchplugin/5.80 (Samsung Galaxy; Android 4.4)",
        "interfaces": {
          "screen": {}
        }
      },
      "request": {
        "command": norm_text,
        "original_utterance": text,
        "type": "SimpleUtterance",
        "markup": {
          "dangerous_context": False,
        },
        "payload": {},
        "nlu": {
          "tokens": norm_text.split(),
          "entities": [],  # todo: imitate them
        }
      },
      "session": {
        "new": bool(message_id == 0),
        "message_id": message_id,
        "session_id": "botank-{}".format(session_id),  # todo: maybe create a new session
        "skill_id": "botank-f5rd-4079-a14b-788652932056",  # todo: maybe insert the provided skill id
        "user_id": "BOTANK{}".format(user_id),
      },
      "version": "1.0"
    }
    return raw_req
