export PATH=/opt/local/bin:/opt/local/sbin:~/bin:/usr/local/sbin:$PATH

if [ -f /opt/local/etc/profile.d/bash_completion.sh ]; then
    . /opt/local/etc/profile.d/bash_completion.sh
fi

if [ -e .bash_alias ]
then
  source .bash_alias
fi

source ~/.bash_git
