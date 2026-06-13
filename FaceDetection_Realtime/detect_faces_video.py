# USAGE
# python detect_faces_video.py

from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import os

# Default model files
DEFAULT_PROTOTXT = "deploy.prototxt"
DEFAULT_MODEL = "res10_300x300_ssd_iter_140000.caffemodel"

# Optional command-line arguments
ap = argparse.ArgumentParser()
ap.add_argument(
    "-p",
    "--prototxt",
    default=DEFAULT_PROTOTXT,
    help="path to Caffe deploy prototxt file"
)
ap.add_argument(
    "-m",
    "--model",
    default=DEFAULT_MODEL,
    help="path to Caffe pre-trained model"
)
ap.add_argument(
    "-c",
    "--confidence",
    type=float,
    default=0.5,
    help="minimum probability to filter weak detections"
)

args = vars(ap.parse_args())

# Check model files exist
if not os.path.exists(args["prototxt"]):
    print(f"[ERROR] Prototxt file not found: {args['prototxt']}")
    exit()

if not os.path.exists(args["model"]):
    print(f"[ERROR] Model file not found: {args['model']}")
    exit()

# Load model
print("[INFO] Loading model...")
net = cv2.dnn.readNetFromCaffe(
    args["prototxt"],
    args["model"]
)

# Start camera
print("[INFO] Starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# Main loop
while True:

    frame = vs.read()

    # Camera check
    if frame is None:
        print("[ERROR] Could not read frame from camera.")
        break

    frame = imutils.resize(frame, width=400)

    (h, w) = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(
        cv2.resize(frame, (300, 300)),
        1.0,
        (300, 300),
        (104.0, 177.0, 123.0)
    )

    net.setInput(blob)
    detections = net.forward()

    # Face counter
    face_count = 0

    # Loop through detections
    for i in range(0, detections.shape[2]):

        confidence = detections[0, 0, i, 2]

        if confidence < args["confidence"]:
            continue

        face_count += 1

        box = detections[0, 0, i, 3:7] * np.array(
            [w, h, w, h]
        )

        (startX, startY, endX, endY) = box.astype("int")

        text = f"Face: {confidence * 100:.2f}%"

        y = startY - 10 if startY - 10 > 10 else startY + 10

        cv2.rectangle(
            frame,
            (startX, startY),
            (endX, endY),
            (0, 0, 255),
            2
        )

        cv2.putText(
            frame,
            text,
            (startX, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (0, 0, 255),
            2
        )

    # Display face count
    cv2.putText(
        frame,
        f"Faces Detected: {face_count}",
        (10, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 0),
        2
    )

    # Exit instructions
    cv2.putText(
        frame,
        "ESC or Q = Exit",
        (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 255, 0),
        2
    )

    cv2.imshow("Face Detection", frame)

    key = cv2.waitKey(1) & 0xFF

    # Exit on Q
    if key == ord("q"):
        print("[INFO] Q pressed. Exiting...")
        break

    # Exit on ESC
    if key == 27:
        print("[INFO] ESC pressed. Exiting...")
        break

# Cleanup
print("[INFO] Cleaning up...")
cv2.destroyAllWindows()
vs.stop()
