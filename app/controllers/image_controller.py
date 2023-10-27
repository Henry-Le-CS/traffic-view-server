import base64
import requests
from PIL import Image
from io import BytesIO
from app.constants.crawler import CRAWLER_AUTH_ENDPOINT_GT, CRAWLER_AUTH_HEADER_GT, CRAWLER_IMAGE_ENDPOINT_GT, CRAWLER_IMAGE_HEADER_GT
import matplotlib.pyplot as plt

def get_image_url(camera_id):
    response = requests.get(url=CRAWLER_AUTH_ENDPOINT_GT, headers=CRAWLER_AUTH_HEADER_GT)
    cookies = response.cookies

    image_endpoint = CRAWLER_IMAGE_ENDPOINT_GT + camera_id
    image_response = requests.get(
        url=image_endpoint,
        headers=CRAWLER_IMAGE_HEADER_GT,
        cookies=cookies
    )

    image_bytes = BytesIO(image_response.content)
    image = Image.open(image_bytes).convert("RGB")

    img_byte_array = BytesIO()
    
    image.save(img_byte_array, format="JPEG")
    plt.savefig(img_byte_array, format='png')
    plt.clf()
    
    img_byte_array.seek(0)
    img_bye_array_png = base64.b64encode(img_byte_array.getvalue())
    
    data_url = "data:image/jpeg;base64," + img_bye_array_png.decode('utf-8')
    return data_url
