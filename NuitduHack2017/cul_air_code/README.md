# Cul_air_code

## Author
waiting for his agreement

## Nuit du Hack's description

no description was provided to challengers

## Challenge description
This challenge was provided as a steganography challenge during Nuit du Hack, however it was first presented like a programmation challenge. The idea was indeed for challengers to reconstruct especially the QRcode contained within the image given the metainformation inscribed in it. 

## Repository organization

./
 cul_air_code.png	-> the challenge file

more to come depending on author agreement

## write-up

Several write-ups have been published : [here](https://quentin.dufour.io/blog/2017-06-25/write-up-wargame-ndh-xv) or [here](http://techoverflow.fr/2017/06/26/ndh2k17-wargame-write-up-cul-air-code/).

Actually none of them give the intended way to solve the end of the challenge, as expected by the author. Indeed, if you run exiftool on the final image (the one containing the key), you get the following message : 

    :::console
    Warning : [minor] Trailer data after PNG IEND chunk
    
So if you extends the height of the image directly, then you could see the complete image, containing the whole key for the xor.
