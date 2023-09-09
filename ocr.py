import crop
from google.cloud import vision


def detect_text_uri(uri):
    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=crop.crop_image(uri))
    # image.source.image_uri = crop.crop_image(uri)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        positions = [0, 1, 2, 3, 4, 5, 6]
        results = [texts[0].description.split('\n')[i] for i in positions]
        pokemon = results[0]
        nature = results[1]
        skills = [results[2], results[3], results[4], results[5], results[6]]
    else:
        return None

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    print(pokemon, nature, skills)
    return pokemon, nature, skills

detect_text_uri('https://cdn.discordapp.com/attachments/1056493099649597491/1149879618195685457/Screenshot_20230908_174928_Pokmon_Sleep.jpg')

