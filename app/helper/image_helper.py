import requests
from PIL import Image
from io import BytesIO
from app.constants.crawler import CRAWLER_AUTH_ENDPOINT_GT, CRAWLER_AUTH_HEADER_GT, CRAWLER_IMAGE_ENDPOINT_GT, CRAWLER_IMAGE_HEADER_GT

def get_image_from_camera(camera_id):
    """
    This function gets the image from the camera id from BGT.
    Args:
        camera_id (string): The camera id.

    Returns:
        image (PIL.Image): The image from the camera.
    """
    try:
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
        
        return image
    except Exception as e:
        raise e
