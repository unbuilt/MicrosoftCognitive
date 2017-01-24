# MicrosoftCognitive
Python module for Microsoft Cognitive Services

* Only for Python 3

## Supported API

### Computer Vision API
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
* Only support detect faces from image data

```python
face_key = 'YOUR_API_KEY' # Please set the correct key here before running the test
filename = r'YOUR_IMAGE_FILENAME' # Please set a valid filename here before running the test
with open(filename, 'rb') as image_file:
    data = image_file.read()
face = Face(face_key)
result = face.detect_image(data, 'age,gender,headPose,smile,facialHair,glasses')
```

### Translator Text API
* Only support translate method

```python
translator_key = 'YOUR_API_KEY' # Please set the correct key here before running the test
translator = Translator(translator_key)
text = 'a blurry photo of a train at night'
translated_text = translator.translate(text)
```

## TODO
* Support image url for Computer Vision

