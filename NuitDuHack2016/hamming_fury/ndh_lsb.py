#!/usr/bin/env python

import numpy as np
from PIL import Image
import sys

#le flag ici;  longueur de 21, donc 8*21=168=7*24, easy ici
str_flag='ndh2k16_ea5tc057dada2'
#hamming matrix
#H= np.matrix('0 0 0 1 1 1 1; 0 1 1 0 0 1 1; 1 0 1 0 1 0 1')
#H= np.matrix('1 0 1 0 1 0 1;0 1 1 0 0 1 1;0 0 0 1 1 1 1')
H= np.matrix('0 1 1 0 1 0 1;1 0 1 0 0 1 1;0 0 0 1 1 1 1')

#permet de normer un vecteur
def binarize(vecteur,taille):
    for j in xrange(0,taille):
        if vecteur[j][0]%2 == 0 :
            vecteur[j][0]=0
        if vecteur[j][0]%2 == 1 :
            vecteur[j][0]=1
    return vecteur

#recupere une matrice avec les bits du flag
def recup_matrice_flag(flag):
    str2=''
    #recup binaire flag
    for x in flag:
        xtemp= "{0:b}".format(ord(x))
        while (len(xtemp)<8) :
            xtemp='0'+ xtemp
        str2+=xtemp        

    #decoupage du flag binaire en fonction taille H    
    str3=''
    str4=''
    for i in xrange(0,len(str2)) :
        if (i%3) == 0 and i!=0 :
            str4+=str3+';'
            str3=''
        str3+=(str2[i]+' ')
    str4+=str3

    all_message=np.matrix(str4)
    all_message=all_message.T
    return all_message

#recupere la place de la modif si elle a lieu et change le vecteur si besoin
def get_modif(vecteur,matrice_flag,i):
    col=matrice_flag[:,[i]]
    temp_vect=H*vecteur
    binarize(temp_vect,3)

    #resultat du calcul de l'insertion: modif ou pas?
    u= col - temp_vect
    binarize(u,3)
    
    zero_array= np.matrix('0;0;0')
    #si pas de modif, on modifie pas
    if np.allclose(u,zero_array) :
        return vecteur
        
    #detect modif
    for i in xrange(0,7):
        if np.allclose(u,H[:,[i]]) :
            vecteur[i]+=1 
            binarize(vecteur,7)
            return vecteur

#recupere les bits de l'image
def get_str_image(path_img):
    buffer=''
    img = Image.open(path_img)
    l,h = img.size
    #pix = img.load()

    for x in xrange(0,h):
        p=img.getpixel((x,0))
        #r,g,b = pix[x, 0]
        #buffer += str(r&1)+str(g&1)+str(b&1)
        buffer += str(p[0]&1)+str(p[1]&1)+str(p[2]&1)
    return buffer

#cree un vecteur a partir des bits de l'image
def get_vecteur_str_img(str,i):
    buffer=''
    for j in str[i*7:(i+1)*7]:
        buffer+=j+';'
    buffer=buffer[:-1]
    return np.matrix(buffer)

#transforme un vecteur en string
def vecteur_to_string(vecteur,taille):
    buffer=''
    for j in xrange(0,taille):
        value=vecteur.item((j,0))
        buffer+=str(value)
    return buffer

#les operations pour ecrire l'image, en comment si on insere pas dans du blanc
def process(path_img,write_path_img):
    final_str_img=''
    matrice_flag=recup_matrice_flag(str_flag)
    str_img=get_str_image(path_img)
    for i in xrange(0,matrice_flag.shape[1]):
        vecteur=get_vecteur_str_img(str_img,i)
        new_vecteur=get_modif(vecteur,matrice_flag,i)
        final_str_img+=vecteur_to_string(new_vecteur,7)
    write_image(path_img,final_str_img,write_path_img)

#ecriture d'une image
def write_image(path_img,new_bits,new_path_img):
    img = Image.open(path_img)
    l,h = img.size
    for x in xrange(0,len(new_bits)/3):
        p=img.getpixel((x,0))
        #k1=255
        k1=p[0]
        k1= k1 & 254 | int(new_bits[x*3])
        #k2=255
        k2=p[1]
        k2= k2 & 254 | int(new_bits[x*3+1])
        #k3=255
        k3=p[2]
        k3= k3 & 254 | int(new_bits[x*3+2])
        img.putpixel((x,0),(k1,k2,k3))
    img.save(new_path_img)

#recup du flag a partir de l'image
def unprocess(img_path):
    final_str_img=''
    sol=''
    str_img=get_str_image(img_path)
    for i in xrange(0,60):
        vecteur=get_vecteur_str_img(str_img,i)
        vect_bits=H*vecteur
        binarize(vect_bits,3)
        final_str_img+=vecteur_to_string(vect_bits,3)       
    for i in xrange(0,21):
        sol += chr(int(final_str_img[i*8:i*8+8],2))
    print sol


#le main, pas tres original lol
def main():
    path_img=sys.argv[1]
    write_path_img=sys.argv[2]
    process(path_img,write_path_img)
    unprocess(write_path_img)
    
    
if __name__ == "__main__":
    main()

