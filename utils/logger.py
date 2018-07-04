import logging
import sys


def get_logger(namespace, log_level=logging.INFO):
    """
    :type namespace: str
    :rtype: logging.Logger
    """
    root = logging.getLogger(namespace)

    if not logging._handlers:
        root.propagate = 0
        root.setLevel(log_level)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        root.addHandler(ch)

    return root
