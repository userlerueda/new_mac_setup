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
#__root="$(cd "$(dirname "${__dir}")" && pwd)" # <-- change this as it depends on your app

arg1="${1:-}"

# Installer starts here
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOGGER=echo
${LOGGER} " | INFO | Backing up files"
${LOGGER} " | INFO | A copy of your current files will be stored in ~/ with the extension .BAK.${TIMESTAMP}"
mv ~/.bash_git ~/.bash_git.BAK.${TIMESTAMP}
mv ~/.bash_profile ~/.bash_git.BAK.${TIMESTAMP}
mv ~/.bash_alias ~/.bash_git.BAK.${TIMESTAMP}
${LOGGER} " | INFO | Copying new files"
rsync -v .bash_git ~/
rsync -v .bash_profile ~/
rsync -v .bash_alias ~/
