#!/usr/bin/python
# -*- coding: utf-8 -*

import os
import sys
import time
from xml.etree import ElementTree
from xml.dom import minidom 

# Inventory code for the lab


while 1: 

        tuna = raw_input('<--∆--> ')

        def cls():
            
                action = "\n"
                return action * 40

        def darkmatter():
                space = "\n"
                return space * 25

        def logo():
                get = os.system("cat /Users/billylundh/Desktop/labbet/mahlabs.txt")
                return get

        def readfile():
                get = os.system("cat /Users/billylundh/Desktop/labbet/inventory.xml")
                return get
#new fix
        def searchcatagory():
                root = ElementTree.parse('/Users/billylundh/Desktop/labbet/inventory.xml').getroot();

                print "\n"
                search = raw_input("Search catagory: ");
                print "\n"

                find = [component for component in root.findall('component') if component.findtext('catagory') == search]
                for component in find:
                        print "\n","name: ", component.findtext('name'),"\n","description: ", component.findtext('description'), "\n","Nbr: ", component.findtext('nbr'), "\n","catagory: ", component.findtext('catagory'), "\n"


        def rm_endtag():
                # Read how many lines the file contains,
                f = open("/Users/billylundh/Desktop/labbet/inventory.xml","r")
                lines = f.readlines()
                f.close()

                # Open the file in write mode.
                # remove the last line, ie </root>
                
                f = open("/Users/billylundh/Desktop/labbet/inventory.xml","w")
                for line in lines:
                    if line!="</components>":
                            f.write(line)
                f.close()

        def rm_endtag_users():
                # Read how many lines the file contains,
                f = open("/Users/billylundh/Desktop/labbet/users.xml","r")
                lines = f.readlines()
                f.close()

                # Open the file in write mode.
                # remove the last line, ie </root>
                
                f = open("/Users/billylundh/Desktop/labbet/users.xml","w")
                for line in lines:
                    if line!="</system>":
                            f.write(line)
                f.close()

        def addobjekt():
                x = raw_input("name: ")
                y = raw_input("description: ")
                z = raw_input("nbr: ")
                a = raw_input("catagory: ")

                appendfile = open("/Users/billylundh/Desktop/labbet/inventory.xml", 'a')
                appendfile.write("\n<component>" + "\n<name>" + x + "</name>" + "\n<description>" + y + "</description>" + "\n<nbr>" + z + "</nbr>" + "\n<description>" + a + "</description>" + "\n</component>\n</components>")
                appendfile.close()

            
        def newuser():
                x = raw_input("Ange använadre namn: ")
                y = raw_input("Scanna ditt kort och tryck enter: ")
                z = raw_input("Ange email: ")

                appendfile = open("/Users/billylundh/Desktop/labbet/users.xml", 'a')
                appendfile.write("<user>" + x + "</user>" + "\n<id>"+ y + "</id>" + "\n<email>" + z + "\n<email>" + z + "</email>")
                appendfile.close()

       # def finduser():




        if tuna == 'quit': break

        elif tuna == 'clear':
                print cls();
                print "\t\t\t\t\t\t\t\t", logo();
                print darkmatter();

        elif tuna == 'read':
                print cls();
                readfile();
                print darkmatter();

        elif tuna == 'search':
                print cls();
                searchcatagory();
                print darkmatter();

        elif tuna == '1':
                print cls();
                searchcatagory();
                print darkmatter();

        elif tuna == '2':
            # return item
                print cls();
                searchcatagory();
                print darkmatter();

        elif tuna == '3':
            #new user
                print cls();
                rm_endtag_users();
                newuser();
                print darkmatter();

        elif tuna == '4':
            #read xml
                print cls();
                readfile();
                print darkmatter();

        elif tuna == '5':
            # add component
                print cls();
                rm_endtag();
                addobjekt();
                print darkmatter();

        elif tuna == '6':
            # see lent items.
                print cls();
                rm_endtag();
                addobjekt();
                print darkmatter();



