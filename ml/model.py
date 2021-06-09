import sys
import logging
import os
from .detector import Detector
logger = logging.getLogger("model_loader")


def load_detector(args):
    if args.model == "tiny":
        model_file = "clearbot-tiny.weights"
        cfg_file = "clearbot-tiny.cfg"
    elif args.model == "full":
        model_file = "clearbot.weights"
        cfg_file = "clearbot.cfg"
    else:
        logger.info("Model type is not valid")
        sys.exit(1)

    detector = Detector("model", use_gpu=True, weights_file=model_file,
                        config_file=cfg_file, confidence_thres=0.5)
    return detector

def load_detectron():
  from detectron2.config import get_cfg
  from detectron2.data.detection_utils import read_image
  from .detectron.predictor import VisualizationDemo
  cfg = get_cfg()
  cfg.merge_from_file(os.path.sep.join(
            [os.path.dirname(os.path.realpath(__file__)), "detectron", "config.yml"]))
  cfg.MODEL.RETINANET.SCORE_THRESH_TEST = 0.5
  cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
  cfg.MODEL.PANOPTIC_FPN.COMBINE.INSTANCES_CONFIDENCE_THRESH = 0.5
  cfg.MODEL.WEIGHTS = os.path.sep.join(
            [os.path.dirname(os.path.realpath(__file__)), "model", "detectron.pth"])
  cfg.MODEL.DEVICE = "cpu"
  cfg.freeze()
  demo = VisualizationDemo(cfg)
  return demo