# Hamming Fury

## Nuit du Hack's Description

> After people have discover that F5 algorithm tool used to put "F5" in the header of steganographied images; we wanted to have a better tool here at hackerzvoice. We so want to know if you can decrypt this image, in order to know the efficiency of our tool.
> 
> ps: no wet paper, just simple lsb hamming here!

## Challenge description

This challenge is a steganography challenges, where the flag is stored within an image. It uses the principles of correction code theory, here hamming codes, to encode information using last significant bits, but with less bits needed (the ratio is here 7/4). As describing the whole process can be a bit tedious, here is a wikipedia [article](https://fr.wikipedia.org/wiki/Code_de_Hamming_(7,4)) where one can find how information can be encoded using hamming codes.

To solve it, the challenger has to get the LSB bits within the image, then gets the output by iterating over every possible correction matrixes. The good output can be retrieved as we know flag has a `ndh2k16_<flag>` pattern. A hint on the size of the matix is given within the image, just strings it.

## Repository organization
* ./
   * hamming_fury.png -> the image used for the challenge
   * test_crack.py -> a python program to solve the challenge (was used to determine how much time was needed to get the good matrix)
   * ndh_lsb.py -> a python program to embed our flag within an image using hamming codes.
   
## Write-up
a write-up has been published by 0x90root team's member Alkanor [here](https://0x90r00t.com/2016/07/05/ndh2k16-2016-stegano-150-hamming-fury-write-up/)
