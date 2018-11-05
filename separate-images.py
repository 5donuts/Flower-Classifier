#!/usr/bin/env python3

import os, sys
from random import shuffle, randint

# directory names
TESTDIR = "testing"
VALIDIR = "validation"
TRAINDIR = "training"

def make_dirs(rootdir):
    dirs = [TESTDIR, VALIDIR, TRAINDIR]
    for item in dirs:
        dir = os.path.join(rootdir, item)
        if not os.path.exists(dir):
            os.makedirs(dir)
            print("Created directory %s" % dir)

if __name__ == "__main__":
    # usage: ./separate-images.py flowers-scaled/<flower-type>/
    # ex: ./separate-images.py flowers-scaled/dandelion/
    rootdir = sys.argv[1]

    # randomize image list, then separate into training, validation, and
    # testing groups
    images = os.listdir(rootdir)
    shuffle(images)
    len = len(images)

    # make the output directories
    make_dirs(rootdir)

    for i in range(0, len):
        print("Processing item %d of %d -> " % (i + 1, len), end='')

        # skip directories
        if os.path.isdir(os.path.join(rootdir, images[i])):
            print("skipping directory")
            continue

        # add ~20% of images to 'testing'
        if randint(1, 5) == 1:
            src = os.path.join(rootdir, images[i])
            dest = os.path.join(rootdir, TESTDIR, images[i])
            # print("%s -> %s" % (src, dest))
            print(TESTDIR)
            os.rename(src, dest)
        # add ~16% of images to 'validation'
        elif randint(1, 25) <= 4:
            src = os.path.join(rootdir, images[i])
            dest = os.path.join(rootdir, VALIDIR, images[i])
            # print("%s -> %s" % (src, dest))
            print(VALIDIR)
            os.rename(src, dest)
        # add the remaining ~64% of images to 'training'
        else:
            src = os.path.join(rootdir, images[i])
            dest = os.path.join(rootdir, TRAINDIR, images[i])
            # print("%s -> %s" % (src, dest))
            print(TRAINDIR)
            os.rename(src, dest)
