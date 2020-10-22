#!/usr/bin/bash


function create(){
    cd /home/coolnoname2/Programming/5Projects/AutomationPython
    python create.py $1
    sleep 5
    source .env
    cd $FILEPATH$1
    #cd /home/coolnoname2/Programming/5Projects/AutomationPython/$1
    git init
    git remote add origin https://github.com/botParrot/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master 
    #rm -r $1
}   