import torch
import torch.nn as nn
from torchvision import transforms
import torchvision.models as models
from app.helper.image_helper import get_image_from_camera

class Model:
    def __init__(
        self,
        model_name="efficientnet_b1_density_model.pth",
    ):  
        model_image_path = "app/pretrained/density/" + model_name
        self.model = torch.load(model_image_path, map_location='cpu')
        
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(torch.tensor([0.48604893, 0.47804295, 0.47611874]), torch.tensor([0.20945826, 0.19714504, 0.2004261]))
        ])
        self.model.eval()

    def predict(self, camera_id):
        try:
            image = get_image_from_camera(camera_id)
            image = self.transform(image)
            image = image.unsqueeze(0)
            
            with torch.no_grad():
                outputs = self.model(image)
                
                _, predicted = torch.max(outputs, 1)
                                 
                return str(predicted.item())
            
        except Exception as e:
            return str(e)
