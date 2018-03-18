# A balanced RSA a day keeps the security analyst away

## Nuit du Hack's description
> hey guys, i have intercepted a communication between freeman and majinboo about challs for tonight, and i wanted to troll them by divulgating flags… Unfortunately, i was not able to do so however i got some infos about the tool they use in their encrypted communication. here is what i have so far : rsa public key of freeman, used to encode an aes 256 key with no salt, which is then used to encode the flag.

## challenge description
"A balanced RSA a day keeps the security analyst away" (see the apple's reference?) is a challenge in which you need to decrypt the message that has been sent between two parties. As in real applications, the asymmetric cryptography is used to send ciphered a symmetric key, which is the key used to cipher the real message.

The flaw resides in the fact, as the title may indicate, the two factors used to create the RSA key are unbalanced, that means that N = p *q where p << q (<< meaning that p is inferior to q with lots of magnitude orders) and N is the ciphering module. As such, the p factor can be brute-forced. 

Here is a little java code snippet to do the trick:
```java
public Casse_rsa(BigInteger tocasse) {
    this.trouve=false;
    this.p= BigInteger.valueOf(0);
    this.n=tocasse;
    while(this.p.compareTo(this.n)==-1){
        this.p=this.p.nextProbablePrime();
        if(tocasse.remainder(this.p)==BigInteger.valueOf(0)){
            System.out.println("trouve");
            this.q=this.n.divide(p);
            System.out.println("n: "+ this.n + "p: "+ this.p +"q:" + this.q);
            this.trouve=true;
            break;
        }  
    }
}
```
To solve it, one has to discover the p factor first, then calculates all the RSA primitives to be able to decipher the AES key, and finally use the AES key to decipher the message (no salt used).

## repository organisation
the files are the following :

* ./
   * aes_key_cipher -> the ciphered AES symmetric key
   * ciphermessage  -> the ciphered message
   * pub_key        -> the public RSA key
* ./creation_files/
   * aes_key        -> unciphered AES key
   * message        -> the original and unciphered message
   * newkey.der     -> the certificate for the RSA key
   * asn            -> the ASN description of the RSA key as used with openssl
   
## write-up
A write-up has been published by Yann Cam on his [blog](https://www.asafety.fr/cryptologie/wargame-ndh-2016-write-up-crypto-a-balanced-rsa-a-day-keeps-the-security-analyst-away/)
