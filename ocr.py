import re
from google.cloud import vision


def detect_text_uri(uri):
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations

    pattern = r'Lv\. \d+ '
    
    if texts:
        positions = [4, 5, 7, 11, 15, 21, 24]
        results = [texts[0].description.split('\n')[i] for i in positions]
        results[0] = re.sub(pattern, '', results[0])
        pokemon = results[0]
        nature = results[4]
        skills = [results[1], results[2], results[3], results[5], results[6]]
    else:
        return None
       
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    print(pokemon, nature, skills)
    return pokemon, nature, skills

# detect_text_uri('https://cdn.discordapp.com/attachments/1056493099649597491/1149879618195685457/Screenshot_20230908_174928_Pokmon_Sleep.jpg')