from PIL import Image

def resize_image(input_path, output_path, size=(224, 224)):
    
    img = Image.open(input_path)
    
    resized = img.resize(size)
    
    resized.save(output_path)
    
    print("Image resized and saved")


if __name__ == "__main__":
    resize_image("input.jpg", "resized.jpg")