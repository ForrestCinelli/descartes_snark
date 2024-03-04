#! /bin/bash

python add_province_indicators.py

rm -rf DescartesSnark
mkdir DescartesSnark
mv *.tga DescartesSnark
cp DescartesSnark.map DescartesSnark
cp Steam/* DescartesSnark