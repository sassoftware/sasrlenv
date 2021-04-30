# Copyright © 2020, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import logging
import os
from pathlib import Path
home = str(Path.home())

def get_logger(log_dir=home+'/.SASGym',log_level='debug'):
    # set logger
    logger = logging.getLogger()
    logFormatter = logging.Formatter("%(asctime)s %(levelname)s %(process)s [%(funcName)s:%(lineno)d] %(message)s")
    # logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")

    # create cache folder if it does not exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # create file handler for logger
    fileHandler = logging.FileHandler("{0}/{1}.log".format(log_dir, 'hist'))
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)

    # create stream handler for logger
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)

    if log_level == 'info':
        logger.setLevel(logging.INFO)
    elif log_level == 'debug':
        logger.setLevel(logging.DEBUG)
    elif log_level == 'warning':
        logger.setLevel(logging.WARNING)
    elif log_level == 'error':
        logger.setLevel(logging.ERROR)

    return logger