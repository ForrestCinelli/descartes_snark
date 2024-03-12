from PIL import Image
import os

white = (255, 255, 255)

def add_province_indicators(snark: Image) -> None:
    """ Cap is always listed first for each group of 15. 
    Next five are cap circle provinces. 
    Remaining nine are the outer nonagon.
    """
    ''' Outer Ring '''

    # Bottom Right 
    snark.putpixel((7255, 5066), white)

    snark.putpixel((7509, 5146), white)
    snark.putpixel((7413, 4858), white)
    snark.putpixel((7107, 4853), white)
    snark.putpixel((7011, 5141), white)
    snark.putpixel((7257, 5313), white)

    snark.putpixel((7684, 5209), white)
    snark.putpixel((7880, 4611), white)
    snark.putpixel((7553, 4384), white)
    snark.putpixel((7235, 4144), white)
    snark.putpixel((7057, 4695), white)
    snark.putpixel((6881, 5235), white)
    snark.putpixel((6705, 5805), white)
    snark.putpixel((7096, 5805), white)
    snark.putpixel((7499, 5805), white)

    # Top Right
    snark.putpixel((6015, 1239), white)

    snark.putpixel((6263, 1323), white)
    snark.putpixel((6166, 1036), white)
    snark.putpixel((5859, 1029), white)
    snark.putpixel((5763, 1319), white)
    snark.putpixel((6010, 1494), white)

    snark.putpixel((6790, 1247), white)
    snark.putpixel((6279, 873), white)
    snark.putpixel((5771, 498), white)
    snark.putpixel((5451, 741), white)
    snark.putpixel((5125, 978), white)
    snark.putpixel((5599, 1323), white)
    snark.putpixel((6059, 1650), white)
    snark.putpixel((6540, 2002), white)
    snark.putpixel((6669, 1616), white)

    # Top Left
    snark.putpixel((1994, 1248), white)

    snark.putpixel((2247, 1326), white)
    snark.putpixel((2149, 1037), white)
    snark.putpixel((1843, 1034), white)
    snark.putpixel((1746, 1322), white)
    snark.putpixel((1994, 1492), white)

    snark.putpixel((2402, 1326), white)
    snark.putpixel((2876, 975), white)
    snark.putpixel((2556, 747), white)
    snark.putpixel((2225, 504), white)
    snark.putpixel((1718, 875), white)
    snark.putpixel((1215, 1251), white)
    snark.putpixel((1338, 1621), white)
    snark.putpixel((1465, 1997), white)
    snark.putpixel((1940, 1651), white)

    # Bottom Left
    snark.putpixel((757, 5054), white)

    snark.putpixel((999, 5140), white)
    snark.putpixel((899, 4854), white)
    snark.putpixel((593, 4849), white)
    snark.putpixel((506, 5138), white)
    snark.putpixel((743, 5312), white)

    snark.putpixel((1136, 5255), white)
    snark.putpixel((951, 4702), white)
    snark.putpixel((766, 4140), white)
    snark.putpixel((448, 4372), white)
    snark.putpixel((132, 4607), white)
    snark.putpixel((316, 5208), white)
    snark.putpixel((508, 5796), white)
    snark.putpixel((907, 5800), white)
    snark.putpixel((1302, 5801), white)

    # Bottom
    snark.putpixel((4002, 7430), white)

    snark.putpixel((4250, 7501), white)
    snark.putpixel((4150, 7216), white)
    snark.putpixel((3844, 7210), white)
    snark.putpixel((3747, 7501), white)
    snark.putpixel((3995, 7676), white)

    snark.putpixel((4753, 7511), white)
    snark.putpixel((4880, 7123), white)
    snark.putpixel((4289, 7121), white)
    snark.putpixel((3720, 7125), white)
    snark.putpixel((3125, 7124), white)
    snark.putpixel((3243, 7503), white)
    snark.putpixel((3369, 7885), white)
    snark.putpixel((4000, 7889), white)
    snark.putpixel((4633, 7887), white)


    ''' Middle Ring '''
    # Right
    snark.putpixel((6306, 3193), white)

    snark.putpixel((6491, 3199), white)
    snark.putpixel((6361, 3021), white)
    snark.putpixel((6154, 3086), white)
    snark.putpixel((6157, 3303), white)
    snark.putpixel((6364, 3378), white)

    snark.putpixel((6664, 3147), white)
    snark.putpixel((6538, 2763), white)
    snark.putpixel((6374, 2839), white)
    snark.putpixel((6048, 2985), white)
    snark.putpixel((5880, 3059), white)
    snark.putpixel((5981, 3361), white)
    snark.putpixel((6076, 3668), white)
    snark.putpixel((6434, 3600), white)
    snark.putpixel((6793, 3524), white)

    # Top
    snark.putpixel((3946, 1562), white)

    snark.putpixel((4125, 1564), white)
    snark.putpixel((3991, 1388), white)
    snark.putpixel((3788, 1454), white)
    snark.putpixel((3788, 1671), white)
    snark.putpixel((3995, 1747), white)

    snark.putpixel((4363, 1570), white)
    snark.putpixel((4405, 1210), white)
    snark.putpixel((4007, 1215), white)
    snark.putpixel((3602, 1212), white)
    snark.putpixel((3625, 1395), white)
    snark.putpixel((3663, 1749), white)
    snark.putpixel((3683, 1928), white)
    snark.putpixel((4000, 1928), white)
    snark.putpixel((4324, 1928), white)

    # Top Left
    snark.putpixel((1662, 3306), white)

    snark.putpixel((1850, 3313), white)
    snark.putpixel((1719, 3137), white)
    snark.putpixel((1515, 3200), white)
    snark.putpixel((1513, 3413), white)
    snark.putpixel((1721, 3487), white)

    snark.putpixel((2015, 3367), white)
    snark.putpixel((2127, 3069), white)
    snark.putpixel((1791, 2918), white)
    snark.putpixel((1468, 2769), white)
    snark.putpixel((1339, 3150), white)
    snark.putpixel((1216, 3525), white)
    snark.putpixel((1400, 3567), white)
    snark.putpixel((1745, 3633), white)
    snark.putpixel((1928, 3661), white)

    # Bottom Left
    snark.putpixel((2617, 6016), white)

    snark.putpixel((2802, 6013), white)
    snark.putpixel((2673, 5833), white)
    snark.putpixel((2465, 5898), white)
    snark.putpixel((2467, 6117), white)
    snark.putpixel((2673, 6185), white)

    snark.putpixel((2953, 6036), white)
    snark.putpixel((3039, 5881), white)
    snark.putpixel((2777, 5696), white)
    snark.putpixel((2511, 5512), white)
    snark.putpixel((2271, 5777), white)
    snark.putpixel((2032, 6038), white)
    snark.putpixel((2358, 6283), white)
    snark.putpixel((2680, 6516), white)
    snark.putpixel((2776, 6347), white)

    # Bottom Right
    snark.putpixel((5488, 5948), white)

    snark.putpixel((5673, 5951), white)
    snark.putpixel((5543, 5774), white)
    snark.putpixel((5337, 5843), white)
    snark.putpixel((5338, 6057), white)
    snark.putpixel((5545, 6127), white)

    snark.putpixel((5857, 5911), white)
    snark.putpixel((5609, 5640), white)
    snark.putpixel((5480, 5513), white)
    snark.putpixel((5231, 5687), white)
    snark.putpixel((4966, 5891), white)
    snark.putpixel((5151, 6193), white)
    snark.putpixel((5321, 6522), white)
    snark.putpixel((5650, 6279), white)
    snark.putpixel((5975, 6052), white)

    ''' Inner Ring '''
    # Right
    snark.putpixel((4949, 3700), white)

    snark.putpixel((5100, 3759), white)
    snark.putpixel((5041, 3587), white)
    snark.putpixel((4863, 3577), white)
    snark.putpixel((4807, 3760), white)
    snark.putpixel((4956, 3861), white)

    snark.putpixel((5242, 3773), white)
    snark.putpixel((5146, 3478), white)
    snark.putpixel((4709, 2117), white)
    snark.putpixel((4450, 2303), white)
    snark.putpixel((4187, 2492), white)
    snark.putpixel((4618, 3809), white)
    snark.putpixel((5041, 5132), white)
    snark.putpixel((5359, 5132), white)
    snark.putpixel((5672, 5126), white)

    # Top
    snark.putpixel((4002, 3015), white)

    snark.putpixel((4147, 3063), white)
    snark.putpixel((4088, 2892), white)
    snark.putpixel((3911, 2882), white)
    snark.putpixel((3854, 3062), white)
    snark.putpixel((4003, 3163), white)

    snark.putpixel((5392, 3370), white)
    snark.putpixel((5482, 3065), white)
    snark.putpixel((5587, 2761), white)
    snark.putpixel((4161, 2761), white)
    snark.putpixel((3848, 2761), white)
    snark.putpixel((2409, 2763), white)
    snark.putpixel((2515, 3065), white)
    snark.putpixel((2615, 3370), white)
    snark.putpixel((4000, 3370), white)

    # Top Left
    snark.putpixel((3054, 3706), white)

    snark.putpixel((3204, 3760), white)
    snark.putpixel((3142, 3588), white)
    snark.putpixel((2964, 3577), white)
    snark.putpixel((2908, 3760), white)
    snark.putpixel((3058, 3861), white)

    snark.putpixel((3385, 3816), white)
    snark.putpixel((3811, 2499), white)
    snark.putpixel((3554, 2306), white)
    snark.putpixel((3297, 2119), white)
    snark.putpixel((2862, 3472), white)
    snark.putpixel((2760, 3778), white)
    snark.putpixel((2326, 5131), white)
    snark.putpixel((2640, 5131), white)
    snark.putpixel((2960, 5131), white)

    # Bottom Left
    snark.putpixel((3418, 4811), white)

    snark.putpixel((3563, 4867), white)
    snark.putpixel((3501, 4697), white)
    snark.putpixel((3324, 4689), white)
    snark.putpixel((3268, 4869), white)
    snark.putpixel((3417, 4975), white)

    snark.putpixel((4544, 5957), white)
    snark.putpixel((4649, 5648), white)
    snark.putpixel((4737, 5345), white)
    snark.putpixel((3623, 4535), white)
    snark.putpixel((2503, 3718), white)
    snark.putpixel((2241, 3904), white)
    snark.putpixel((1987, 4088), white)
    snark.putpixel((3136, 4925), white)
    snark.putpixel((3392, 5133), white)

    # Bottom Right
    snark.putpixel((4586, 4812), white)

    snark.putpixel((4732, 4866), white)
    snark.putpixel((4673, 4691), white)
    snark.putpixel((4496, 4687), white)
    snark.putpixel((4437, 4866), white)
    snark.putpixel((4586, 4970), white)

    snark.putpixel((4609, 5119), white)
    snark.putpixel((4866, 4928), white)
    snark.putpixel((6017, 4096), white)
    snark.putpixel((5760, 3912), white)
    snark.putpixel((5504, 3721), white)
    snark.putpixel((4373, 4532), white)
    snark.putpixel((3255, 5340), white)
    snark.putpixel((3358, 5649), white)
    snark.putpixel((3454, 5961), white)


for img_file in os.listdir('base_images'):
    if img_file.endswith('.png') and img_file != 'Descartes_snark.png':
        image = Image.open('base_images/' + img_file)
        add_province_indicators(image)
        image.save(img_file) # move it to root dir
