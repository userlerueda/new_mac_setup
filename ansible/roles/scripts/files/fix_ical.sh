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
LOGGER_EMERGENCY="echo $(date +"%Y-%m-%d %H:%M") | EMERG | "
LOGGER_ALERT="echo $(date +"%Y-%m-%d %H:%M") | ALERT | "
LOGGER_CRITICAL="echo $(date +"%Y-%m-%d %H:%M") | CRIT | "
LOGGER_ERROR="echo $(date +"%Y-%m-%d %H:%M") | ERROR | "
LOGGER_WARNING="echo $(date +"%Y-%m-%d %H:%M") | WARN | "
LOGGER_NOTICE="echo $(date +"%Y-%m-%d %H:%M") | NOTICE | "
LOGGER_INFO="echo $(date +"%Y-%m-%d %H:%M") | INFO | "
LOGGER_DEBUG="echo $(date +"%Y-%m-%d %H:%M") | DEBUG | "

arg1="${1:-}"

${LOGGER_INFO} "Fixing iCal..."
${LOGGER_INFO} "Closing iCal.."
for pid in $(ps -fe | grep Calendar | grep -v "grep Calendar" | awk '{ print $2 }')
do
  kill -9 ${pid}
done
${LOGGER_INFO} "iCal closed"
${LOGGER_INFO} "Removing cache files"
rm -rf '~/Library/Calendars/Calendar\ Cache*'
${LOGGER_INFO} "Cache files removed"
${LOGGER_INFO} "Reopening calendar app..."
open /Applications/Calendar.app
${LOGGER_INFO} "Calendar app reopened"
