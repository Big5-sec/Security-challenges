# Dimensional

## Nuit du Hack's description
> eh guys, i suspect my ML partner to extract sensitive data within his data sets. But i can't succeed in getting it. Could you help me?

## Challenge description
This challenge is a steganography challenge, where some data is hidden within the pcap. Actually, the pcap is a network capture where a csv file is sent. By retrieving this file, and then applying dimension reduction on it, one can be able to retrieve the flag by printing the remaining points of data. The hints necessary to understand what this challenge is about were the following : `Dimensional`, `ML partner` and the first part of `pca.pcap`, as pca is the acronym for the *principal component analysis* algorithm. 

## Author
waiting author agreement

## repository organisation
./
  * pca.pcap -> the challenge file
  * mlwriteup.py -> a write-up script to get the flag

## Write-up
To extract first the CSV, simply do the traditionnal shit with wireshark : `follow tcp stream` then `export file`. Then, the associated mlwriteup.py file will provide you with the complete solution to get theflag on the data.
