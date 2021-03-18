import sys
import logging
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
