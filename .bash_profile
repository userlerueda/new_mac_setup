export PATH=/opt/local/bin:/opt/local/sbin:$PATH

if [ -f /opt/local/etc/profile.d/bash_completion.sh ]; then
    . /opt/local/etc/profile.d/bash_completion.sh
fi

source ~/.bash_git
