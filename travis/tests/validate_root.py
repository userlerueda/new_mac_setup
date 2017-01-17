#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Usage:
  {program} [options] validate (root|travis|all)
  {program} [options] display top-level-dir
  {program} (-h | --help)
  {program} (-v | --version)

Options:
  -h --help      Show this screen.
  -v --version   Show version.
  -d --debug     Enable debug.

"""

__author__        = "Luis Rueda (userlerueda@gmail.com)"
__email__         = "userlerueda@gmail.com"
__copyright__     = "Luis Rueda (userlerueda@gmail.com)"
__status__        = "Development"   # Prototype, Development or Production
__version__       = "0.0.1"

import sys
import logging
import sys
import os
from docopt import docopt
from datetime import datetime

SCREEN_LOGGING_LEVEL = logging.INFO

def file_exists(dir, filename):
    top_level_dir = dir
    files = [f for f in os.listdir(top_level_dir) if os.path.isfile(os.path.join(top_level_dir, f))]
    files = [element.lower() for element in files]
    logger.debug(files)
    if filename.lower() in files:
        return True
    else:
        return False

def main(args):
    if args["validate"]:
        if args["root"] or args["all"]:
            if not file_exists("./", "README.md"):
                logger.error("README.md does not exist!")
                sys.exit(1)
            if not file_exists("./", "setup.sh"):
                logger.error("setup.sh does not exist!")
                sys.exit(1)
            logger.info("root tests OK")
        if args["travis"] or args["all"]:
            if not file_exists("./", ".travis.yml"):
                logger.error(".travis.yml does not exist!")
                sys.exit(1)
            logger.info("travis tests OK")

    if args["display"] and args["top-level-dir"]:
        print(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]) + " - STDOUT - " + os.getcwd())

if __name__ == "__main__":
    # Setup the Logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(SCREEN_LOGGING_LEVEL)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    #logger.critical('This is a critical message.')
    #logger.error('This is an error message.')
    #logger.warning('This is a warning message.')
    #logger.info('This is an informative message.')
    #logger.debug('This is a low-level debug message.')
    #print(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]) + " - STDOUT - This is a stdout printed message.")

    program_name = sys.argv[0]
    args = docopt(__doc__.replace('{program}', program_name), version=__version__)

    if args['--debug']:
        SCREEN_LOGGING_LEVEL = logging.DEBUG
        stream_handler.setLevel(SCREEN_LOGGING_LEVEL)
        logger.debug(args)
    main(args)
