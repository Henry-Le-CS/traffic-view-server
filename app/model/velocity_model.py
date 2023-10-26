import torch
import torch.nn as nn
from torchvision import transforms
import torchvision.models as models
from app.helper.image_helper import get_image_from_camera

class Model:
    def __init__(
        self,
        model_name="resnet_velocity_v3.pth",
        model=None
    ):  
        if model is None:
            self.model = models.resnet18()
        else:
            self.model = model

        num_features = self.model.fc.in_features
        self.model.fc = nn.Linear(num_features, 1)
        model_image_path = "app/pretrained/velocity/" + model_name
        self.model = self.model.to("cpu")
        self.model.load_state_dict(torch.load(model_image_path, map_location="cpu"))
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])
        self.model.eval()


    def predict(self, camera_id):
        try:
            image = get_image_from_camera(camera_id)
            image = self.transform(image)
            image = image.unsqueeze(0)  # Add batch dimension
            with torch.no_grad():
                output = self.model(image)
                prediction = output[0].numpy()
                return prediction[0]
        except Exception as e:
            return str(e)
