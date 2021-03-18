import sys
import cv2
from vision.camera import load_camera
from vision.video import load_video_writer
from ml.model import load_detector
import logging
import argparse

logger = logging.getLogger("root")


def main(args):
    detector = load_detector(args)
    video_writer_original = load_video_writer("recording_original.mp4", (1280 , 720))
    video_writer_labelled = load_video_writer("recording_labelled.mp4", (1280 , 720))
    cap = load_camera(0)

    while True:
        (success, frame) = cap.read()
        video_writer_original.write(frame)
        if not success:
            logger.error("Fatal error: Frame not received.")
            sys.exit(1)
        detector_result = detector.detect(frame)

        for box in detector_result:
            bbox = box["bbox"]
            label = box["label"]
            x = bbox["x"]
            y = bbox["y"]
            w = bbox["width"]
            h = bbox["height"]
            cv2.rectangle(img=frame,
                          pt1=(x, y),
                          pt2=(x + w, y + h),
                          color=(36, 255, 12),
                          thickness=2)
            cv2.putText(img=frame,
                        text=label,
                        org=(x, y - 30),
                        fontFace=cv2.FONT_HERSHEY_COMPLEX,
                        fontScale=0.7,
                        color=(36, 255, 12),
                        thickness=2)

        video_writer_labelled.write(frame)

        if args.video_out:
            cv2.imshow("clearbotvision", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    video_writer_labelled.release()
    video_writer_original.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clearbot AI and PController")
    parser.add_argument('-v', '--video_out', type=bool, default=False, help="Show the camera video output")
    parser.add_argument('--debug', type=bool, default=False, help="Switch to debug mode")
    parser.add_argument('-m', '--model', type=str, default="full", help="Either 'tiny' or 'full' model")
    _args = parser.parse_args()
    if _args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    main(_args)
