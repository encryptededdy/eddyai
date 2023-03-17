
import requests
import base64

ENDPOINT = 'https://tiktok-tts.weilnet.workers.dev/api/generation'


class TikTokVoice:
    def saveData(self, data):
        decodedData = base64.b64decode(data)
        webmFile = ("./tiktok.webm")
        with open(webmFile, 'wb') as file:
            file.write(decodedData)

    def generate(self, text):
        payload = {
            "text": text,
            "voice": "en_us_001"
        }

        res = requests.post(ENDPOINT, json=payload, headers={
                            "Content-Type": "application/json"})
        jsonResponse = res.json()
        if jsonResponse["success"] == False:
            raise Exception(jsonResponse["error"])

        self.saveData(jsonResponse["data"])
