from PIL import Image
import io
import os

def get_color_codes(image_path):
    with open(image_path, "rb") as image_file:
        image = Image.open(io.BytesIO(image_file.read()))

    # Ensure image is in RGB mode
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Get the color of the first pixel
    pixel_color = image.getpixel((0, 0))

    # Convert RGB to HEX
    hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel_color)

    return pixel_color, hex_color

# update image name
image_name = "your_image_name.extention"

script_dir = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(script_dir, "img_location", image_name)
rgb_color, hex_color = get_color_codes(image_path)

print(f"RGB color code {rgb_color}") 
print(f"hex color code {hex_color}")
