import cv2
import pytesseract

# Set the path to Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load the input image
image = cv2.imread("images/input.png")

# Check whether the image was loaded
if image is None:
    print("Error: Could not load the image.")
    print("Make sure input.png is inside the images folder.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply thresholding
_, threshold = cv2.threshold(
    blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Extract text using Tesseract OCR
# Extract text using Tesseract OCR
text = pytesseract.image_to_string(threshold)

# Get OCR confidence scores
data = pytesseract.image_to_data(
    threshold,
    output_type=pytesseract.Output.DICT
)

confidences = []

for confidence in data["conf"]:
    if float(confidence) > 0:
        confidences.append(float(confidence))

average_confidence = (
    sum(confidences) / len(confidences)
    if confidences
    else 0
)

# Display the extracted text and confidence
print("\n===== OCR RESULT =====")
print(text)
print("======================")
print(f"Average OCR Confidence: {average_confidence:.2f}%")

if average_confidence >= 80:
    print("Recognition confidence: PASS")
else:
    print("Recognition confidence: BELOW 80%")