import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from torch.nn.utils.rnn import pack_padded_sequence

# Load pre-trained image recognition model
image_model = models.resnet50(pretrained=True)
image_model = nn.Sequential(*list(image_model.children())[:-1])
image_model.eval()

# Load pre-trained caption generator model
caption_model = ...
# Define the caption model architecture and load pre-trained weights

# Define the image preprocessing transform
image_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

# Function to generate captions for images
def generate_caption(image):
    # Preprocess the image
    image = image_transform(image).unsqueeze(0)
    
    # Extract features from the image using the pre-trained image model
    with torch.no_grad():
        features = image_model(image).squeeze()
    
    # Pass the features through the caption generator model
    caption = caption_model.generate_caption(features)
    
    return caption

# Example usage
image = Image.open('image.jpg')
caption = generate_caption(image)
print('And the image')