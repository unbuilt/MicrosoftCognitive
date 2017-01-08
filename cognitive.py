"""Python module for Microsoft Cognitive Services"""

#!/usr/bin/env python
# coding: utf-8

import time
import requests

class ComputerVision():
    """Computer Vision API"""

    def __init__(self, key):
        # Variables
        self._url = 'https://api.projectoxford.ai/vision/v1.0/analyze'
        self._key = key

    def analyze_image(self, image_data, language='en', max_retries=3):
        """Analyze the impage"""

        # Computer Vision parameters
        params = {'visualFeatures' : 'Tags,Description', 'language': language}

        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = self._key
        headers['Content-Type'] = 'application/octet-stream'

        retries = 0
        result = None

        while True:
            response = requests.request('post', self._url, \
            data=image_data, headers=headers, params=params)

            if response.status_code == 429:
                print("Message: %s" % (response.json()['error']['message']))

                if retries <= max_retries:
                    time.sleep(1)
                    retries += 1
                    continue
                else:
                    print('Error: failed after retrying!')
                    break
            elif response.status_code == 200 or response.status_code == 201:
                if 'content-length' in response.headers \
                and int(response.headers['content-length']) == 0:
                    result = None
                elif 'content-type' in response.headers \
                and isinstance(response.headers['content-type'], str):
                    if 'application/json' in response.headers['content-type'].lower():
                        result = response.json() if response.content else None
                    elif 'image' in response.headers['content-type'].lower():
                        result = response.content
            else:
                print("Error code: %d" % (response.status_code))
                print("Message: %s" % (response.json()))

            break

        return result


class Translator():
    """Microsoft Translator Text API"""

    def __init__(self, key):
        self._key = key

    def _get_translator_token(self):
        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = self._key
        token_url = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
        response = requests.request('post', token_url, headers=headers)
        return response.text

    def translate(self, text, from_language='en', to_language='zh-CHS'):
        """Translate the text into another language"""

        url = 'http://api.microsofttranslator.com/v2/Http.svc/Translate'
        params = {'text': text, 'from': from_language, 'to': to_language}
        token = self._get_translator_token()
        headers = {'Authorization': 'Bearer ' + str(token)}
        response = requests.request('get', url, headers=headers, params=params)
        text = response.text
        start = text.find('>')
        end = text.find('</')
        if start > 0 and end > 0:
            text = text[start+1:end]
        text = text[:]
        return text


if __name__ == "__main__":
    pass
