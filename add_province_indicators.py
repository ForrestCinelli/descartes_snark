from PIL import Image

snark = Image.open('des_snark.png')
white = (255, 255, 255)

# Cap is always listed first for each group of 15. 
# Next five are cap circle provinces. 
# Remaining nine are the outer nonagon. 

snark.putpixel((757, 5054), white)

''' Outer Ring '''

# Bottom Right 
7255, 5066

7509, 5146
7413, 4858
7107, 4853
7011, 5141
7257, 5313

5687, 5209
7880, 4611
7553, 4384
7235, 4144
7057, 4695
6881, 5235
6705, 5805
7096, 5805
7499, 5805

# Top Right
6015, 1239

6263, 1323
6166, 1036
5859, 1029
5763, 1319
6010, 1494

6790, 1247
6279, 873
5771, 498
5451, 741
5125, 978
5599, 1323
6059, 1650
6540, 2002
6669, 1616

# Top Left
1994, 1248

2247, 1326
2149, 1037
1843, 1034
1746, 1322
1994, 1492

2402, 1326
2876, 975
2556, 747
2225, 504
1718, 875
1215, 1251
1338, 1621
1465, 1997
1940, 1651

# Bottom Left
757, 5054

999, 5140
899, 4854
593, 4849
506, 5138
743, 5312

1136, 5255
951, 4702
766, 4140
448, 4372
132, 4607
316, 5208
508, 5796
907, 5800
1302, 5801

# Bottom
4002, 7430

4250, 7501
4150, 7216
3844, 7210
3747, 7501
3995, 7676

4753, 7511
4880, 7123
4289, 7121
3720, 7125
3125, 7124
3243, 7503
3369, 7885
4000, 7889
4633, 7887


''' Middle Ring '''
# Right
6306, 3193

6491, 3199
6361, 3021
6154, 3086
6157, 3303
6364, 3378

6664, 3147
6538, 2763
6374, 2839
6048, 2985
5880, 3059
5981, 3361
6076, 3668
6434, 3600
6793, 3524

# Top
3946, 1562

4125, 1564
3991, 1388
3788, 1454
3788, 1671
3995, 1747

4363, 1570
4405, 1210
4007, 1215
3602, 1212
3625, 1395
3663, 1749
3683, 1928
4000, 1928
4324, 1928

# Top Left
1662, 3306

1850, 3313
1719, 3137
1515, 3200
1513, 3413
1721, 3487

2015, 3367
2127, 3069
1791, 2918
1468, 2769
1339, 3150
1216, 3525
1400, 3567
1745, 3633
1928, 3661

# Bottom Left
2617, 6016

2802, 6013
2673, 5803
2465, 5898
2467, 6117
2673, 6185

2953, 6036
3039, 5881
2777, 5696
2511, 5512
2271, 5777
2032, 6038
2358, 6238
2680, 6516
2776, 6347

# Bottom Right
5488, 5948

5673, 5951
5543, 5774
5337, 5843
5338, 6057
5545, 6127

5857, 5911
5609, 5640
5480, 5513
5231, 5687
4966, 5891
5151, 6193
5321, 6522
5650, 6279
5975, 6052

''' Inner Ring '''
# Right
4949, 3700

5100, 3759
5041, 3587
4863, 3577
4807, 3760
4956, 3861

5242, 3773
5146, 3478
4709, 2117
4450, 2303
4187, 2492
4618, 3809
5041, 5132
5359, 5132
5672, 5126

# Top
4002, 3015

4147, 3063
4088, 2892
3911, 2882
3854, 3062
4003, 3163

5392, 3370
5482, 3065
5587, 2761
4161, 2761
3848, 2761
2409, 2763
2515, 3065
2615, 3370
4000, 3370

# Top Left
3054, 3706

3204, 3760
3142, 3588
2964, 3577
2908, 3760
3058, 3861

3385, 3816
3811, 2499
3554, 2306
3297, 2119
2862, 3472
2760, 3778
2326, 5131
2640, 5131
2960, 5131

# Bottom Left
3418, 4811

3563, 4867
3501, 4697
3324, 4689
3268, 4869
3417, 4975

4544, 5957
4649, 5648
4737, 5345
3623, 4535
2503, 3718
2241, 3904
1987, 4088
3136, 4925
3392, 5133

# Bottom Right
4586, 4812

4732, 4866
4673, 4691
4496, 4687
4437, 4866
4586, 4970

4609, 5119
4866, 4928
6017, 4096
5760, 3912
5504, 3721
4373, 4532
3255, 5340
3358, 5649
3454, 5961
snark.save('desk_snark_with_provinces.png', 'png')