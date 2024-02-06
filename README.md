# Image Color Extractor

This Python script extracts both RGB and HEX color codes from images. It supports popular image formats like PNG, JPEG, and more, providing flexibility to specify image paths for analysis. The script outputs color codes in both RGB and HEX formats, making it easy to integrate into other applications or workflows.

## Key Features

- Extracts RGB and HEX color codes from images.
- Supports popular image formats like PNG, JPEG, and more.
- Provides flexibility to specify image paths for analysis.
- Outputs color codes in both RGB and HEX formats for easy integration into other applications or workflows.

## How to Use

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Pasindu-Vishmika/image-color-extractor.git
    ```

2. Install the necessary dependencies, such as PIL (Python Imaging Library). You can install dependencies using pip:

    ```bash
    pip install pillow
    ```
3. Add your image to `img_location` directory

4. Update code line number 22 with `your_image_name.extention` .

   ## Usage Example
   `image_name = "your_image_name.extention"` -> `image_name = "111.png"`
   
6. The script will process the image and output the RGB and HEX color codes of the first pixel.

## Usage Example

```bash
python color_code_extractor.py 
