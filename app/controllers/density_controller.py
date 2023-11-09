import os
from app.model.density_model import Model

def predict_density(camera_id):
    """
    This function gets the density from the camera id from BGT.
    Args:
        camera_id (string): The camera id.

    Returns:
        density (string): The density from the camera.
    """
    try:
        model = Model()
        
        density = model.predict(camera_id)
        return density 
    
    except Exception as e:
        raise e