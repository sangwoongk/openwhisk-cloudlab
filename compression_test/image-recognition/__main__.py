from time import time
import random
import torch
from torchvision import transforms, models
from PIL import Image
import json

model = models.resnet50(pretrained=True)
model.eval()

class_idx = json.load(open("/imagenet_class_index.json", "r"))
idx2label = [class_idx[str(k)][1] for k in range(len(class_idx))]

images = None

def generate_image(size):
    image = Image.new('RGB', (size, size))
    pixels = image.load()
    for i in range(size):
        for j in range(size):
            pixels[i, j] = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
    return image


def generate_and_recognize_images(num_images):
    global images
    if images is None:
        images = [generate_image(224) for _ in range(num_images)]

    recognition_results = []

    for i in range(num_images):
        input_image = images[i]
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        input_tensor = preprocess(input_image)
        input_batch = input_tensor.unsqueeze(0)

        with torch.no_grad():
            output = model(input_batch)

        _, index = torch.max(output, 1)
        recognized_class = idx2label[index.item()]
        recognition_results.append(recognized_class)

    return recognition_results


def main(params):
    img_size = params['size']

    start = time()

    result = generate_and_recognize_images(img_size)
    latency = time() - start
    ret_val = {}
    ret_val["delay"] = latency

    return ret_val

if __name__ == '__main__':
    params = {'size': 1500000}
    main(params)