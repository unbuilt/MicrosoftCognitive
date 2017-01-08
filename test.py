"""Test cognitive services"""

#!/usr/bin/env python
# coding: utf-8

from cognitive import ComputerVision, Translator

def test_computer_vision():
    """Test Computer Vision API"""

    # Load raw image file into memory
    computer_vision_key = 'YOUR_API_KEY' # Please set the correct key here before running the test
    filename = r'./data/img_8274469980498163810.jpg'
    with open(filename, 'rb') as image_file:
        data = image_file.read()
    computer_vision = ComputerVision(computer_vision_key)
    result = computer_vision.analyze_image(data)
    print(result)
    print(result['description']['captions'])


def test_translator():
    """Text Translator Text API"""

    translator_key = 'YOUR_API_KEY' # Please set the correct key here before running the test
    translator = Translator(translator_key)
    text = 'a blurry photo of a train at night'
    translated_text = translator.translate(text)
    print(translated_text)


if __name__ == "__main__":
    test_computer_vision()
    test_translator()
