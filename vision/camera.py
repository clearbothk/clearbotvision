import sys
import cv2
import logging

logger = logging.getLogger("camera_loader")


def load_camera(source):
    cap = cv2.VideoCapture(source)
    if cap is None or not cap.isOpened():
        logger.error(f"Could not load source camera: {source}")
        sys.exit(1)
    return cap
