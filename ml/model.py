import sys
import logging
import os
from .yolo.predictor import YOLODetector
from .detectron.predictor import DetectronDetector

logger = logging.getLogger("model_loader")


def load_yolo(args):
    if args.modelsize == "tiny":
        model_file = "clearbot-tiny.weights"
        cfg_file = "clearbot-tiny.cfg"
    elif args.modelsize == "full":
        model_file = "clearbot.weights"
        cfg_file = "clearbot.cfg"
    else:
        logger.info("Model type is not valid")
        sys.exit(1)

    detector = YOLODetector("model", use_gpu=True, weights_file=model_file,
                        config_file=cfg_file, confidence_thres=0.5)
    return detector

def load_detectron():
  detector = DetectronDetector()
  return detector