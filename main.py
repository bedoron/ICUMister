import json

from utils.AppRunner import AppRunner
from utils.HandlersFactor import HandlersFactory
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

    app_runner = AppRunner(config)
    app_runner.initialize()
    app_runner.run(logger, camera_handler, face_identification, face_verification, notifier)

    logger.info("Bye bye")


if __name__ == "__main__":
    main()
