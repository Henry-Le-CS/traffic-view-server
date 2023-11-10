import os
from app.model.condition_model import Model

def predict_condition(camera_id):
    """
    This function gets the condition from the camera id from BGT.
    Args:
        camera_id (string): The camera id.

    Returns:
        condition (string): The condition(LOS) from the camera.
    """
    try:
        model = Model()
        
        condition = model.predict(camera_id)
        return condition 
    
    except Exception as e:
        raise e