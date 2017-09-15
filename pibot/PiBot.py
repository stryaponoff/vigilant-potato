import requests


class PiBot:
    MARKDOWN = "Markdown"
    HTML = "HTML"

    def __init__(self, token):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{token}/"

    def get_updates(self, offset=None, timeout=30):
        method = "getUpdates"
        params = {"timeout": timeout, "offset": offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()["result"]
        return result_json

    def send_message(self, chat_id, text, parse_mode=None):
        method = "sendMessage"
        params = {"chat_id": chat_id, "text": text}

        if parse_mode in (self.MARKDOWN, self.HTML):
            params.update({"parse_mode": parse_mode})

        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update
