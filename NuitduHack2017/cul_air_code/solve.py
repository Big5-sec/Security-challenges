#!/usr/bin/env python

import Image
import pyexiv2
from sys import argv
from os import listdir
from os.path import isfile, join

def craft_image(p_dir):
    files = [f for f in listdir(p_dir) if isfile(join(p_dir, f))]
    images = [Image.open(p_dir + '/' + f) for f in files]
    exif = [pyexiv2.ImageMetadata(p_dir + '/' + f) for f in files]
    positions = []
    for e in exif:
        try:
            e.read()
            pos = e['Exif.Photo.UserComment'].value.split(' ')[-1]
            s_pos = pos.split(',')
            positions.append((int(s_pos[0]), int(s_pos[-1])))
        except:
            continue
    mode = images[0].mode
    final_image_width = (max(x[0] for x in positions) + 1) * max(x.size[0] for x in images)
    final_image_height = (max(x[1] for x in positions) + 1) * max(x.size[1] for x in images)
    print '* Number of pieces: %d' % len(files)
    print '* Image dimension : %dx%d' % (final_image_width, final_image_height)
    final_image = Image.new(mode, (final_image_width, final_image_height), 'white')
    for p, i in zip(positions, images):
        x = i.size[0] * int(p[0])
        y = i.size[1] * int(p[1])
        final_image.paste(i, (x, y, x + i.size[0], y + i.size[1]))
    final_image.save('final.png')

if __name__ == '__main__':
    if len(argv) != 2:
        print 'Usage: %s pieces_directory' % argv[0]
        exit(1)
    craft_image(argv[1])
