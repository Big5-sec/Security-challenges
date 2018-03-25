# Unlucky

## Nuit du Hack description

no description was made for this challenge, as everything is included within the challenge file.

## Challenge description
This challenge is a crypto one, based on CVE-2015-8618 : `Go, from its 1.5 version to 1.5.2, had a bug in its CRT, occuring very rarely, and allowing one to leak p or q when signing messages.`. The whole idea was so to exploit this vulnerability to recover the private key and then decipher the message.

## Repository organization
./
  challenge.txt -> the challenge file

./writeup/
  writeup.go -> a complete write-up in go
  enc.pem -> the ciphered message
  flag.txt -> the final flag
  pub.pem -> the public RSA key of the challenge

## Author
Lesterpig [@lesterpig](https://twitter.com/lesterpig) 

## Write-ups
Several write-ups were made available on blogs : [here](https://github.com/YoloSw4g/writeups/tree/master/2017/NdH2k17/Unlucky) or [here](https://ndiab.github.io/ctf-writeup/2017/06/26/ndhXV_unlucky.html) 
