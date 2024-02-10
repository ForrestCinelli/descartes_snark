from PIL import Image

snark = Image.open('des_snark.png')
white = (255, 255, 255)

''' Outer Ring '''
# Bottom Left
snark.putpixel((757, 5054), white)

snark.save('desk_snark_with_provinces.png', 'png')