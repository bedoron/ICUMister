import logging
import sys


def get_logger(namespace):
    """
    :type namespace: str
    :rtype: logging.Logger
    """
    root = logging.getLogger(namespace)

    if not logging._handlers:
        root.propagate = 0
        root.setLevel(logging.INFO)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        root.addHandler(ch)

    return root
