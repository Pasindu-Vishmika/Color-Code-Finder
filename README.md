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
    git clone https://github.com/your-username/image-color-extractor.git
    ```

2. Install the necessary dependencies, such as PIL (Python Imaging Library). You can install dependencies using pip:

    ```bash
    pip install pillow
    ```
3. Add your image to `img_location` directory 

4. Run the Python script, providing the path to the image you want to analyze. Replace `your_image_name.extention` with the actual path to your image:

    ```bash
    python color_code_extractor.py your_image_name.extention
    ```

5. The script will process the image and output the RGB and HEX color codes of the first pixel.

## Usage Example

```bash
python color_code_extractor.py 111.png
