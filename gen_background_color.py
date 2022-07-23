from matplotlib import image as mpimg
import matplotlib.pyplot as plt
from numpy import floor
import os

def main():
    # convert array of three values into a hex string
    def rgb2hex(rgb):
        return 'complement_%02X%02X%02X' % rgb
    # compute complemetary color function
    def complementary_color(img):
        return floor(255 - img.mean(axis=(0,1))).astype(int)
    
    # compute complementary color for all image in the flder img/flowers
    # and save them in the folder img/background_color_image_name
    for filename in os.listdir('img/flowers'):
        if filename.endswith('.jpg'):
            img = mpimg.imread('img/flowers/' + filename)
            rgb_complement = tuple(complementary_color(img))
            hex_complement = rgb2hex(rgb_complement)
            mpimg.imsave('img/background_color/' + hex_complement + '.png', img)
            print('Complementary color for ' + filename + ' saved.')

    # plt.show()

if __name__ == '__main__':
    main()
    exit(0)