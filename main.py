import json
import logging

from utils.AppRunner import AppRunner
from utils.HandlersFactory import HandlersFactory
from utils.logger import get_logger

from utils.runtime import set_sigint


def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)


def main():
    get_logger('msrestazure', logging.WARNING)
    logger = get_logger("ICUMister")
    config = load_config()

    app_runner = AppRunner(config, HandlersFactory.create_camera_dummy, HandlersFactory.create_pipeline_rest)
    set_sigint(logger, app_runner)
    app_runner.run()

    logger.info("Bye bye")


if __name__ == "__main__":
    main()
