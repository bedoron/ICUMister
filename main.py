import json

from utils.AppRunner import AppRunner
from utils.HandlersFactory import HandlersFactory
from utils.JPEGHandler import JPEGHandler
from utils.logger import get_logger

from utils.runtime import set_sigint


def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)


def main():
    logger = get_logger("ICUMister")

    camera_handler, face_identification, face_verification, notifier = HandlersFactory.create_dummies(logger)
    set_sigint(logger, camera_handler)
    config = load_config()

    jpeg_handler = JPEGHandler(logger, face_identification, face_verification, notifier)

    app_runner = AppRunner(config)
    app_runner.initialize()
    app_runner.run(camera_handler, jpeg_handler)

    logger.info("Bye bye")


if __name__ == "__main__":
    main()
