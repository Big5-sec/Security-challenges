# To be or not to be?

## Nuit du Hack's description

>  HAI 1.2
>    CAN HAS STDIO?
>      VISIBLE "I NEED TO GET THAT FLAG!!!!!"
>  KTHXBYE
>
>tips:  - no the prog is not a troll, and yes, you have to reverse it at least partly
>       - the flag you will find is the xxxx part of the complete flag ndh2k16_xxxxx

## Challenge description

This challenge is a whitespace crackme. As any crackme, you have to enter the correct password to be able to validate. To solve it, i think it's necessary to get a reinterpretation, in human understandable manner, of the program. One could think of it as a transpiling process.

## repository organisation
* ./
   * challenge.ws -> actual challenge file
* ./creation_files/
   * challenge_instrum.ws -> annotated whitespace challenge program
   * whitespace.c -> a whitespace interpreter
   * compile_ws.sh -> bash script to remove annotations in challenge_instrum and then test the program with the compiled version of the interpreter

## Write-up
No competitor has published any write-up for this challenge. I have so published a complete one on my blog [here](https://big5-security/blog/) that tries to explain everything from the ground up step by step. 
