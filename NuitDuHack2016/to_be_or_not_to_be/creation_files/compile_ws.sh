#!/bin/bash
cp challenge_instrum.ws sed.ws
sed 's/[a-z0-9A-Z_\(\):,]*//g' sed.ws > challenge.ws
./a.out challenge.ws


