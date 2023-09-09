import re
from google.cloud import vision


def detect_text_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations

    pattern = r'.*?L[vV]\. ?\d+ '

    if texts:
        results = [re.sub(pattern, '', item) for item in texts[0].description.split('\n')]
    else:
        return None

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    return results


print(detect_text_uri(
    'https://cdn.discordapp.com/attachments/1149992767049711636/1150037159504515153/Screenshot_20230909_023652_Pokmon_Sleep.jpg'))
