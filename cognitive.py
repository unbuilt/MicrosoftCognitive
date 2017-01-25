"""Python module for Microsoft Cognitive Services"""

#!/usr/bin/env python
# coding: utf-8

import time
import requests

class ComputerVision():
    """Computer Vision API"""

    def __init__(self, key):
        """Initialize the ComputerVision

        Keyword arguments:
        key -- the API key for Computer Vision API
        """

        self._url = 'https://api.projectoxford.ai/vision/v1.0/analyze'
        self._key = key

    def analyze_image(self, image_data, features, language='en', max_retries=3):
        """Analyze the impage

        Keyword arguments:
        image_data -- the binary data of the image
        features -- the features what to analyze, sepatated by ',',
                    e.g. 'Categories,Tags,Description,Faces,ImageType,Color,Adult'
        language -- the language for response, only support 'en' and 'zh' (default 'en')
        max_tetries -- the number of retries when the request failed (default 3)
        """

        params = {'visualFeatures' : features, 'language': language}

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


class Face():
    """Face API"""

    def __init__(self, key):
        """Initialize Face

        Keyword arguments:
        key -- the API key for Face API
        """

        self._url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect'
        self._key = key

    def detect_image(self, image_data, face_attributes):
        """Analyze the impage

        Keyword arguments:
        image_data -- the binary data of the image
        face_attributes -- the face attributes what to be returned, sepatated by ',',
                    e.g. 'age,gender,headPose,smile,facialHair,glasses'
        returnFaceAttributes
        """

        params = {'returnFaceAttributes' : face_attributes}

        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = self._key
        headers['Content-Type'] = 'application/octet-stream'
        response = requests.request('post', self._url, \
            data=image_data, headers=headers, params=params)

        return response.json()


class Emotion():
    """Emotion API"""

    def __init__(self, key):
        """Initialize Emotion

        Keyword arguments:
        key -- the API key for Emotion API
        """

        self._url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
        self._key = key

    def recognize_image(self, image_data):
        """Analyze the impage

        Keyword arguments:
        image_data -- the binary data of the image
        """

        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = self._key
        headers['Content-Type'] = 'application/octet-stream'
        response = requests.request('post', self._url, data=image_data, headers=headers)

        return response.json()


class LUIS():
    """Language Understanding Intelligent Service"""

    def __init__(self, key):
        """Initialize LUIS

        Keyword arguments:
        key -- the API key for Language Understanding Intelligent Service
        """

        self._url = 'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/'
        self._prebuilt_cortana_chinese = 'c27c4af7-d44a-436f-a081-841bb834fa29'
        self._key = key

    def predict(self, query, appid=None):
        """Predict the intent and entities

        Keyword arguments:
        query -- the query
        appid -- the app id, when it's None, will use the prebuilt Cortana application for Chinese
        """

        params = {'subscription-key' : self._key, 'q': query}

        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = self._key
        headers['Content-Type'] = 'application/octet-stream'

        if not appid:
            appid = self._prebuilt_cortana_chinese
        url = self._url + appid

        response = requests.request('get', url, params=params, headers=headers)

        return response.json()

class Autosuggest():
    """Autosuggest API"""

    def __init__(self, key):
        """Initialize Autosuggest

        Keyword arguments:
        key -- the API key for Autosuggest API
        """

        self._url = 'https://api.cognitive.microsoft.com/bing/v5.0/suggestions/'
        self._key = key

    def suggestions(self, query):
        """Get suggestions for query

        Keyword arguments:
        query -- the query
        """

        params = {'subscription-key' : self._key, 'q': query}

        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = self._key
        headers['Content-Type'] = 'application/octet-stream'

        response = requests.request('get', self._url, params=params, headers=headers)

        return response.json()

class WebSearch():
    """Web Search API"""

    def __init__(self, key):
        """Initialize WebSearch

        Keyword arguments:
        key -- the API key for Web Search API
        """

        self._url = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
        self._key = key

    def search(self, query, count=10, offset=0, safesearch='moderate', mkt='zh-cn'):
        """Get web search result for query

        Keyword arguments:
        query -- the query
        """

        params = {'q': query, 'count': count, 'offset': offset, 'mkt': mkt, 'sefesearch': safesearch}

        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = self._key
        headers['Content-Type'] = 'application/octet-stream'

        response = requests.request('get', self._url, params=params, headers=headers)

        return response.json()

class Translator():
    """Microsoft Translator Text API"""

    def __init__(self, key):
        """Initialize Translator

        Keyword arguments:
        key -- the API key for Microsoft Translator Text API
        """

        self._key = key

    def _get_translator_token(self):
        headers = dict()
        headers['Ocp-Apim-Subscription-Key'] = self._key
        token_url = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
        response = requests.request('post', token_url, headers=headers)
        return response.text

    def translate(self, text, from_language='en', to_language='zh-CHS'):
        """Translate the text into another language

        Keyword arguments:
        text -- the text to translate
        from_language -- the language of the text to translate (default 'en'')
        to_language -- the language want to translate to (default 'zh-CHS')
        """

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
