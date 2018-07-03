from utils.AppRunner import AppRunner
from utils.HandlersFactor import HandlersFactory
from utils.logger import get_logger

from utils.runtime import set_sigint


def main():
    logger = get_logger("ICUMister")

    camera_handler, face_identification, face_verification, notifier = HandlersFactory.create_dummies(logger)

    set_sigint(logger, camera_handler)

    AppRunner().run(logger, camera_handler, face_identification, face_verification, notifier)
    logger.info("Bye bye")


if __name__ == "__main__":
    main()
