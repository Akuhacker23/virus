GNU nano 5.8                   trojan.py
#!/bin/python

#module
import os
import sys
import time

# mengetik otomatis
def auto(z):
        for e in z + "/n":
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.05)

#pertanyaan (y/t)
def nanya():
    nanya =raw_input("Apakah Anda Ingin Attack Lagi? [Y/T] ~> ")
    if nanya =="Y" or nanya =="y":
        menu()
    elif nanya =="T" or nanya =="t":
        auto("Makasih sobat:)")
        time.sleep(1)
        sys.exit()
    elif nanya =="" or nanya ==' ':
        auto("jangan sampe kosong ya sobat")
        time.sleep(1)
        nanya()
    else:
        auto("Salah, masukan input pilihan dengan benar!")
        time.sleep(1)
        nanya()


# menu
def menu():
    os.system("clear")
    logo = """
+---------------------------------------------+
[+] Pembuat script by :Raihan
[+] github     :https://github.com/Akuhacker23
[+] tiktok     :ffhann.06
[+] youtube    :TERMUX TUTORIAL SIMPLE
+---------------------------------------------+"""
    print logo
    nomor = raw_input("Masukan nomor Target ~> ") # input untuk si user memasukan nomor nya  
    jumlah = int(input("Masukan Jumlah Kiriman ~> ")) # untuk menyuruh si user masukan jumlah nya 
    time.sleep(1)

    try:
        for i in  range(jumlah):
         print "Mencoba mengirim virus ke nomor ~>",nomor
         time.sleep(0.1)
    except KeyboardInterrupt:
        print "#### selesai ####"

    nanya()
menu()
