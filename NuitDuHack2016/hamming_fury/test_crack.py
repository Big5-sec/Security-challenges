#!/usr/bin/env python                                                                  

import numpy as np
from PIL import Image
import sys
import itertools

col0=np.matrix('0;0;1')
col1=np.matrix('0;1;0')
col2=np.matrix('1;0;0')
col3=np.matrix('0;1;1')
col4=np.matrix('1;1;0')
col5=np.matrix('1;0;1')
col6=np.matrix('1;1;1')




dict={0:col0,1:col1,2:col2,3:col3,4:col4,5:col5,6:col6}

d = range(0,7)
e = len(d)

#permet de normer un vecteur                                                           
def binarize(vecteur,taille):
    for j in xrange(0,taille):
        if vecteur[j][0]%2 == 0 :
            vecteur[j][0]=0
        if vecteur[j][0]%2 == 1 :
            vecteur[j][0]=1
    return vecteur

#transforme un vecteur en string                                                      
def vecteur_to_string(vecteur,taille):
    buffer=''
    for j in xrange(0,taille):
        value=vecteur.item((j,0))
        buffer+=str(value)
    return buffer

#cree un vecteur a partir des bits de l'image                                          
def get_vecteur_str_img(str,i):
    buffer=''
    for j in str[i*7:(i+1)*7]:
        buffer+=j+';'
    buffer=buffer[:-1]
    return np.matrix(buffer)

#recupere les bits de l'image                                                         
def get_str_image(path_img):
    buffer=''
    img = Image.open(path_img)
    l,h = img.size
    #pix = img.load()

    for x in xrange(0,h):
        p=img.getpixel((x,0))
        #r,g,b = pix[x, 0]
        buffer += str(p[0]&1)+str(p[1]&1)+str(p[2]&1)
    return buffer


#recup du flag a partir de l'image                                                     
def unprocess(img_path):
    final_str_img=''
    sol=''
    str_img=get_str_image(img_path)
    #K=np.matrix('0 1 1 0 1 0 1;1 0 1 0 0 1 1;0 0 0 1 1 1 1')
    for p in itertools.permutations(d, e):
        H=np.concatenate((dict[p[0]],dict[p[1]],dict[p[2]],dict[p[3]],dict[p[4]],dict[p[5]],dict[p[6]]),axis=1)
        print "******************************"
        print H
        """
        if np.allclose(H,K):
            print 'found'
        """

        for i in xrange(0,60):
            vecteur=get_vecteur_str_img(str_img,i)
            vect_bits=H*vecteur
            binarize(vect_bits,3)
            final_str_img+=vecteur_to_string(vect_bits,3)
            
        for i in xrange(0,21):
            sol += chr(int(final_str_img[i*8:i*8+8],2))
                #sol+='a'
        if sol.startswith('ndh'):
            print 'flag : ',sol
            return
        print sol
        sol=''
        final_str_img=''

def main():
    write_path_img=sys.argv[1]
    unprocess(write_path_img)

if __name__ == "__main__":
    main()
