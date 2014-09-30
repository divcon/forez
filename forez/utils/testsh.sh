#!/bin/sh
if [ -s result.html  ]
	then
		rm result.html
fi
python tests.py >> result.html
