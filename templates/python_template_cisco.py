#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Usage:
  {program} [options] something (somethingelse|nothing|all)
  {program} (-h | --help)
  {program} (-v | --version)

Options:
  -h --help      Show this screen.
  -v --version   Show version.
  -d --debug     Enable debug.

"""

__author__        = "Luis Rueda"
__email__         = "lurueda@cisco.com"
__copyright__     = "Cisco Systems, Inc."
__status__        = "Development"   # Prototype, Development or Production
__version__       = "0.0.0"

import sys
import logging
import sys
import os
from docopt import docopt
from datetime import datetime

SCREEN_LOGGING_LEVEL = logging.INFO

def main(args):
    """
    main program

    executes main program

    Parameters
    ----------
    args : list
        list of args parsed by the script when executed
    """
    pass

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
