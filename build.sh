#! /bin/bash

set -e # Error = stop executing script
set -x # Echo each command before running. 

python add_province_indicators.py

[ -d 'DescartesSnark' ] && mv DescartesSnark DescartesSnarkBackup
mkdir DescartesSnark
mv *.png DescartesSnark
cp DescartesSnark.map DescartesSnark
cp Steam/* DescartesSnark
rm -rf DescartesSnarkBackup
