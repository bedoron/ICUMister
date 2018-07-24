#!/bin/bash
cd /home/pi/ICUMister
export GIT_SSH_COMMAND='ssh -i /home/pi/.ssh/id_rsa'
git pull
dos2unix environment.env
export $(cat environment.env | xargs) && \
/home/pi/.virtualenvs/cv/bin/python main.py