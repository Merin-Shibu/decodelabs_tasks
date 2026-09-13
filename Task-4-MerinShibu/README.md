# Image Text Recognition using OCR

A basic Optical Character Recognition (OCR) system that extracts text from an input image using Python, OpenCV, and Tesseract OCR.

## Project Overview

This project demonstrates a basic image text recognition system using the Tesseract OCR engine.

The input image is preprocessed using grayscale conversion, Gaussian blur, and thresholding before the text is extracted using Tesseract.

## Objectives

- Load an input image
- Preprocess the image
- Extract text using OCR
- Calculate OCR confidence
- Display the recognized text clearly
- Verify that the recognition confidence is above 80%

## Technologies Used

- Python
- OpenCV
- Pytesseract
- Pillow
- Tesseract OCR

## How It Works

1. Load the input image.
2. Convert the image to grayscale.
3. Apply Gaussian blur.
4. Apply thresholding to improve text clarity.
5. Use Tesseract OCR to extract the text.
6. Calculate the average OCR confidence.
7. Display the recognized text and confidence result.

## Example Input

The test image contains:

```text
Artificial Intelligence
Project 4
DecodeLabs Internship