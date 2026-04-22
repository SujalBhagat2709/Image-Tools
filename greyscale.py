from PIL import Image

def convert_to_grayscale(input_path, output_path):
    
    img = Image.open(input_path)
    
    gray = img.convert("L")
    
    gray.save(output_path)
    
    print("Grayscale image saved")


if __name__ == "__main__":
    convert_to_grayscale("input.jpg", "gray.jpg")