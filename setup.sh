#!/bin/bash -i

if [ ! -d dev_env/ ]; then
    python -m venv dev_env
    . dev_env/bin/activate
    python -m pip install -r requirements.txt
    pip install --upgrade pip
else
    . dev_env/bin/activate
fi
