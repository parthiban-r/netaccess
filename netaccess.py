#!/usr/local/bin/python2
# Author: Parthiban R
# Last Updated: 20 June 2018
# License: MIT License
 
# edit to fill your login details

un="UserName"   
pw="Passwrod"

#

if (un=="UserName"):
    print('change your login details at /usr/local/bin/netaccess.py')

import getpass

try:
    try:
        import mechanize
    except:
        import sys
        if sys.version_info[0] >= 3:
            print("ERROR: Use Python version 2.7 to run code")
        else:
            print("ERROR: mechanize library not found")
            print("Follow the commands to install mechanize")
            print("1. /usr/bin/ruby -e \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\"")
            print("2. brew install python2")
            print("3. pip2 install mechanize")

    br=mechanize.Browser()

    try:
        response=br.open("https://netaccess.iitm.ac.in/account/login") 
        print('Login Page Loded')
    except:
        print("ERROR: Webpage unavailable - check connection")
        exit(1)
    try:
        br.select_form(nr=0)
    except:
        print("ERROR: Webpage unavailable - check connection")
        exit(1)

    if (un=="UserName"):
        print("Enter LDAP login details in /usr/local/bin/netaccess.py")
        un=raw_input('un: ')
    if (pw=="Yourpw"):
        print("Enter LDAP login details in /usr/local/bin/netaccess.py")
        pw=getpass.getpass()

    br.form["userLogin"]=un
    br.form["userPassword"]=pw
    url1=br.geturl()
    result=br.submit()
    url2=br.geturl()
    if (url1==url2):
        print("ERROR: Wrong Credentials\n Enter LDAP login details in /usr/local/bin/netaccess.py")
        exit(1)
    print('Login Succesful')
    br.visit_response(result)
    print('Approval Page\n Approving for 1 day...')
    br.follow_link(br.find_link(url_regex="approve"))
    br.select_form(nr=0)
    br.form["duration"] = ["2"]
    result=br.submit()

    print("Aproval Succesful")
except:
    print("Aproval Unsuccesful")
