#! /bin/bash

python add_province_indicators.py

mv DescartesSnark DescartesSnarkBackup
mkdir DescartesSnark
mv *.png DescartesSnark
cp DescartesSnark.map DescartesSnark
cp Steam/* DescartesSnark
rm -rf DescartesSnarkBackup
