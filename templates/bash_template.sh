#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
# set -o xtrace

# Set magic variables for current file & dir
__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
__file="${__dir}/$(basename "${BASH_SOURCE[0]}")"
__base="$(basename ${__file} .sh)"
__root="$(cd "$(dirname "${__dir}")" && pwd)" # <-- change this as it depends on your app
LOGGER=echo
LOGGER_DEBUG="${LOGGER} | DEBUG | "
LOGGER_INFO="${LOGGER} | INFO | "
LOGGER_WARNING="${LOGGER} | WARN | "
LOGGER_ERROR="${LOGGER} | ERROR | "

arg1="${1:-}"
