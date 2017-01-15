#!/usr/bin/env bash
# Bash3 Boilerplate. Copyright (c) 2014, kvz.io

set -o errexit
set -o pipefail
set -o nounset
# Uncomment the next line if you want to debug
# set -o xtrace

# Set magic variables for current file & dir
__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
__file="${__dir}/$(basename "${BASH_SOURCE[0]}")"
__base="$(basename ${__file} .sh)"

# Validate README.md exists
if [ -e ${__dir}/../../README.md ]
then
   echo "README.md exists, everything Ok so far"
else
   echo "README.md does not exists, failing"
   exit 1
fi
#ls -1a ${__dir}/../../ | grep -v "^.$" | grep -v "^..$"
