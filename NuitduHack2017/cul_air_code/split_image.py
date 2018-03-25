#!/usr/bin/env python

import os
import math
import Image
import string
import random
import pyexiv2
import argparse
import datetime
from sys import argv

def get_args(name):
    parser = argparse.ArgumentParser(prog=name)
    parser.add_argument(
        'image_file',
        help='path to an image file'
    )
    parser.add_argument(
        '-n',
        help='number of pieces after splitting \033[34m(default: 101)\033[0m',
        default=101,
        dest='npieces',
        metavar='NUM'
    )
    parser.add_argument(
        '-o',
        help='output directory for pieces \033[34m(default: ./pieces)\033[0m',
        default='./pieces',
        dest='out_dir',
        metavar='DIR'
    )
    args = parser.parse_args()
    return args

def get_random_name(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def write_position(image_file, pos):
    metadata = pyexiv2.ImageMetadata(image_file)
    metadata.read()
    key = 'Exif.Photo.UserComment'
    value = 'position: %d,%d' % (pos[0], pos[1])
    metadata[key] = pyexiv2.ExifTag(key, value)
    metadata.write()

def split_images(image_file, npieces):
    try:
        image = Image.open(image_file)
    except IOError:
        print '- %s is not a valid image file' % image_file
        exit(1)
    width, height = image.size
    num_split_width =  int(math.sqrt(npieces))
    num_split_height = int(math.sqrt(npieces))
    size_split_width = int(width / num_split_width)
    size_split_height = int(height / num_split_height)
    if size_split_width < 1 or size_split_height < 1:
        print '- Pieces size is lower than 1px, please choose a larger picture'
        exit(1)
    print '* number of images in width : %d' % num_split_width
    print '* number of images in height: %d' % num_split_height
    print '* size of images in width   : %d' % size_split_width
    print '* size of images in height  : %d' % size_split_height
    x = y = 0.0
    np = 0
    for i in xrange(0, num_split_height):
        y = int(i * size_split_height)
        for j in xrange(0, num_split_width):
            x = int(j * size_split_width)
            base = './pieces/piece'
            filename = base + '_' + get_random_name(6) + '.png'
            open(filename, 'a').close()
            piece = image.crop((int(x), int(y), int(x + size_split_width), int(y + size_split_height)))
            piece.save(filename)
            write_position(filename, (j, i))
            np += 1

if __name__ == '__main__':
    args = get_args(argv[0])
    print '* Splitting %s into %s pieces...' % (args.image_file, args.npieces)
    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)
    split_images(args.image_file, int(args.npieces))
    print '+ Done !'
