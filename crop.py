import requests
import io
from PIL import Image
from io import BytesIO


def crop_image(url):
    response = requests.get(url)
    image_data = BytesIO(response.content)

    img = Image.open(image_data)
    standard_size = (1080, 2400)
    img_resized = img.resize(standard_size)

    # Crop Pokemon name.
    crop_name = (311, 226, 596, 297)
    name_img = img_resized.crop(crop_name)

    # Crop Pokemon nature.
    crop_nature = (135, 1559, 449, 1622)
    nature_img = img_resized.crop(crop_nature)

    # Crop Pokemon subskills.
    crop_skill_1 = (92, 820, 500, 888)
    skill_1_img = img_resized.crop(crop_skill_1)

    crop_skill_2 = (585, 819, 989, 882)
    skill_2_img = img_resized.crop(crop_skill_2)

    crop_skill_3 = (93, 990, 497, 1053)
    skill_3_img = img_resized.crop(crop_skill_3)

    crop_skill_4 = (582, 989, 984, 1054)
    skill_4_img = img_resized.crop(crop_skill_4)

    crop_skill_5 = (99, 1158, 501, 1223)
    skill_5_img = img_resized.crop(crop_skill_5)

    # cropped_img.show()
    images = [name_img, nature_img, skill_1_img, skill_2_img, skill_3_img, skill_4_img, skill_5_img]
    cropped = combine_images(images)
    with BytesIO() as f:
        cropped.save(f, format='JPEG')
        return f.getvalue()



def combine_images(images):
    # Get individual image dimensions
    widths, heights = zip(*(i.size for i in images))

    # Determine the size of the merged image
    total_width = sum(widths)
    max_height = max(heights)

    # Create an empty image with the determined size
    new_img = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for img in images:
        new_img.paste(img, (x_offset, 0))
        x_offset += img.width

    return new_img
