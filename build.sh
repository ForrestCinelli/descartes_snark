#! /bin/bash

set -e # Error = stop executing script
set -x # Echo each command before running. 

python add_province_indicators.py

[ -d 'DescartesSnark' ] && mv DescartesSnark DescartesSnarkBackup
mkdir DescartesSnark
mv *.tga DescartesSnark
cp DescartesSnark.map DescartesSnark
cp Steam/Banner.png DescartesSnark
cp Steam/dom6ws.txt DescartesSnark
rm -rf DescartesSnarkBackup
