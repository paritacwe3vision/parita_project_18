import cv2

filename = input("Image file: ")

img = cv2.imread("qr2.png")

detector = cv2.QRCodeDetector()

data, points, _ = detector.detectAndDecode(img)

if data:
    print("QR Content:", data)
    print("Location:", points)
else:
    print("No QR code found")
