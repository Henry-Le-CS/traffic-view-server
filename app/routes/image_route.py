from flask import Blueprint
from app.controllers.image_controller import get_image_url
image_blueprint = Blueprint('image', __name__, url_prefix='/api')

@image_blueprint.route('/get_image/<camera_id>', methods=['GET'])
def get_image(camera_id):
    url = get_image_url(camera_id)
    return url