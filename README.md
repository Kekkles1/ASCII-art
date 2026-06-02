# Image to ASCII Art Converter

This is my first time using Python. This is a small project that reads images and converts them into ASCII art.

The program takes the RGB values of each pixel, calculates the brightness, and then uses those brightness values to create an ASCII character matrix.

## How to Run

Create a virtual environment and install OpenCV:

```bash
pip install opencv-python
```

The folder already contains images of the Mona Lisa and a Whale Shark.

By default, the program generates ASCII art for the Mona Lisa image. To generate ASCII art for the Whale Shark image, simply change the image path in the Python file.

## Preview

Below is an example of how the result should look:\
Mona Lisa \ 
<img width="547" height="770" alt="image" src="https://github.com/user-attachments/assets/e1beb94d-8ae3-4267-bb7c-53466a4847e1" />

Whale Shark \
<img width="603" height="740" alt="image" src="https://github.com/user-attachments/assets/d9846d26-d165-40d6-a751-bb8db7b9efa7" />
