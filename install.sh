#!/bin/bash

git submodule init
git submodule update

cd src/vendor/bootstrap/
git checkout v2.3.2
