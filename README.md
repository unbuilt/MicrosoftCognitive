# MicrosoftCognitive

Python module for Microsoft Cognitive Services

https://www.microsoft.com/cognitive-services

* Only for Python 3

## Supported API

### Computer Vision API

https://www.microsoft.com/cognitive-services/en-us/computer-vision-api

* Only support analyze image data

```python
computer_vision_key = 'YOUR_API_KEY' # Please set the correct key here before running the test
filename = r'./data/img_8274469980498163810.jpg'
with open(filename, 'rb') as image_file:
    data = image_file.read()
computer_vision = ComputerVision(computer_vision_key)
result = computer_vision.analyze_image(data, 'Tags,Description')
```

### Face API

https://www.microsoft.com/cognitive-services/en-us/face-api

* Only support detect faces from image data

```python
face_key = 'YOUR_API_KEY' # Please set the correct key here before running the test
filename = r'YOUR_IMAGE_FILENAME' # Please set a valid filename here before running the test
with open(filename, 'rb') as image_file:
    data = image_file.read()
face = Face(face_key)
result = face.detect_image(data, 'age,gender,headPose,smile,facialHair,glasses')
```

### Emotion API

https://www.microsoft.com/cognitive-services/en-us/emotion-api

* Only support recognize emotions from image data

```python
emotion_key = 'YOUR_API_KEY' # Please set the correct key here before running the test
filename = r'YOUR_IMAGE_FILENAME' # Please set a valid filename here before running the test
with open(filename, 'rb') as image_file:
    data = image_file.read()
emotion = Emotion(emotion_key)
result = emotion.recognize_image(data)
```

### LUIS - Language Understanding Intelligent Service

https://www.microsoft.com/cognitive-services/en-us/language-understanding-intelligent-service-luis

There is a Python SDK for LUIS: https://github.com/Microsoft/Cognitive-LUIS-Python/

* Only support predict

```python
luis_key = 'YOUR_API_KEY' # Please set the correct key here before running the test
luis = LUIS(luis_key)
result = luis.predict('北京天气')
```

```json
{
  "query": "北京天气",
  "intents": [
    {
      "intent": "builtin.intent.weather.check_weather"
    }
  ],
  "entities": [
    {
      "entity": "北京",
      "type": "builtin.weather.absolute_location"
    }
  ]
}
```

### Translator Text API

https://www.microsoft.com/cognitive-services/en-us/translator-api

* Only support translate method

```python
translator_key = 'YOUR_API_KEY' # Please set the correct key here before running the test
translator = Translator(translator_key)
text = 'a blurry photo of a train at night'
translated_text = translator.translate(text)
```

## TODO
* Support image url for Computer Vision

