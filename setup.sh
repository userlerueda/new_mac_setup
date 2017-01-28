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
LOGGER="echo $(date +"%Y-%m-%d %H:%M") "
LOGGER_INFO="echo $(date +"%Y-%m-%d %H:%M") | INFO | "
${LOGGER_INFO} "Backing up files..."
${LOGGER_INFO} "A copy of your current files will be stored in ~/ with the extension .BAK.${TIMESTAMP}."
if [ -e ~/.bash_git ]
then
   mv ~/.bash_git ~/.bash_git.BAK.${TIMESTAMP}
fi

if [ -e ~/.bash_profile ]
then
   mv ~/.bash_profile ~/.bash_git.BAK.${TIMESTAMP}
fi

if [ -e ~/.bash_alias ]
then
   mv ~/.bash_alias ~/.bash_git.BAK.${TIMESTAMP}
fi

${LOGGER_INFO} "Done backing up files."
${LOGGER_INFO} "Copying new files..."
rsync .bash_git ~/
rsync .bash_profile ~/
rsync .bash_alias ~/
${LOGGER_INFO} "Done copying new files."
