#!/bin/bash

type casperjs > /dev/null 2>&1 || { echo >&2 "Casperjs is required, but not found. Aborting."; exit 1; }

casperjs test test/casperjs/api.js --url='http://localhost:8000/api/'
