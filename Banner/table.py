#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue
def force_to_unicode(text): 
  "If text is unicode, it is returned as is. If it's str, convert it to Unicode using UTF-8 encoding" 
  return text if isinstance(text, unicode) else text.decode('utf8')

print
print (""+B+"          ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print (""+R+"          ┃"+B+"00."+G+"             Antivirus"+R+"        ┃")
print (""+R+"          ┃"+B+"01."+G+"        Android Freezen"+B+"        ┃")
print (""+R+"          ┃"+B+"02."+G+"         Android Ransn"+B+"         ┃")
print (""+R+"          ┃"+B+"03."+G+"        Android Malware"+B+"        ┃")
print (""+R+"          ┃"+B+"04."+G+"       Android Decryptor"+B+"       ┃")
print (""+R+"          ┃"+B+"05."+G+"       Android Decryptor2"+B+"      ┃")
print (""+R+"          ┃"+B+"06."+G+"        Android SMS Tief"+B+"       ┃")
print (""+R+"          ┃"+B+"07."+G+"   Android Dangerous Malware"+B+"   ┃")
print (""+R+"          ┃"+B+"08."+G+"      Android ENC Malware"+B+"      ┃")
print (""+R+"          ┃"+B+"09."+G+"      Android Door Trojan"+R+"      ┃")
print (""+R+"          ┃"+B+"10."+R+"             EXIT              ┃")
print (""+B+"          ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[0m")
print
