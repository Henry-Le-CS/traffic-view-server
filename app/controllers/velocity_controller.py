import os
from app.model.velocity_model import Model

def predict_velocity(camera_id):
    """
    This function gets the velocity from the camera id from BGT.
    Args:
        camera_id (string): The camera id.

    Returns:
        velocity (float): The velocity from the camera.
    """
    try:
        # model_name = os.getenv('VELOCITY_MODEL_IMAGE')
        model = Model(
            # model_name=model_name
            )
        
        velocity = model.predict(camera_id)
        return str(velocity) # float32 cannot be used for jsonify
    
    except Exception as e:
        raise e