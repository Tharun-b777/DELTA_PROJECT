#!/bin/bash
if [ ! -e /home/data.db ]
then
	python -u pycsvdecode.py
fi

python -u prjc.py
