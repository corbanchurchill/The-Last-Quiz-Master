#||===================||#
#||------MODULES------||#
#||===================||#

#external 
from os import system, name
import time
import pyfiglet
import colorama
from pyfiglet import Figlet
from time import sleep
import random
#||-------------------||#
#internal

#||-------------------||#

#||===================||#
#||----DEFINITIONS----||#
#||===================||#

#||--Clear Function---||#
def clear():

  #WINDOWS
  if name == 'nt':
    system('cls')

  #UNIX
  else:
    system('clear')
#||-------------------||#


#||===================||#
#||===MENU=CONTEXT====||#
#||===================||#
def about_text():
  print("The Last Quiz Master is a text based quiz rpg game written\nin python. It is based off the story of an unlucky adventurer,\nwho is lost in the land of Uulgurm'ath.This ancient land is\nriddled with many hostile creatures. To survive you must have\nwitt, intelligence and bravery. You decide how you go about in\nthis adventure.")
  time.sleep(9)
  print("\nTo fulfil your burning curiosity, here is my github link: \nhttps://github.com/corbanchurchill/The-Last-Quiz-Master\n\naGVyZSBpcyB0aGUgc291cmNlIG9mIG1vc3Qgb2YgbXkgcXVlc3Rpb25zOg0KaHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvTGlzdF9vZl9jb21tb25fbWlzY29uY2VwdGlvbnM=")



#||===================||#
#||====ASCII=TEXT=====||#
#||===================||#


#||====TITLE=SCREEN===||#
def title_ascii():
  print(
    """
 ==========================================================   
  ╔╦╗╦ ╦╔═╗  ╦  ╔═╗╔═╗╔╦╗  ╔═╗ ╦ ╦╦╔═╗  ╔╦╗╔═╗╔═╗╔╦╗╔═╗╦═╗
   ║ ╠═╣║╣   ║  ╠═╣╚═╗ ║   ║═╬╗║ ║║╔═╝  ║║║╠═╣╚═╗ ║ ║╣ ╠╦╝
   ╩ ╩ ╩╚═╝  ╩═╝╩ ╩╚═╝ ╩   ╚═╝╚╚═╝╩╚═╝  ╩ ╩╩ ╩╚═╝ ╩ ╚═╝╩╚═
 ==========================================================
    """
  )

#||TITLE=SCREEN=WELCOME||#
def title_welcome():
  print(
    """
                 =----------------------= 
                   ┬ ┬┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐
                   │││├┤ │  │  │ ││││├┤ 
                   └┴┘└─┘┴─┘└─┘└─┘┴ ┴└─┘
                 =----------------------= 
    """
    )

#||==TITLE=SCREEN=TO==||#
def title_screen_to():
  print(
    """
                         =------=
                          ┌┬┐┌─┐
                           │ │ │
                           ┴ └─┘
                         =------=
    """
  )

#||=====MAIN=MENU======||#
main_menu ="""
============================
  ╔╦╗╔═╗╦╔╗╔  ╔╦╗╔═╗╔╗╔╦ ╦
  ║║║╠═╣║║║║  ║║║║╣ ║║║║ ║
  ╩ ╩╩ ╩╩╝╚╝  ╩ ╩╚═╝╝╚╝╚═╝
============================

 Welcome to a new adventure!

1. Begin
2. Info
3. About

"""

#||CHARACTER=CREATION||#
char_create_menu ="""
   ============================= 
    ╔═╗╦ ╦╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
    ║  ╠═╣╠═╣╠╦╝╠═╣║   ║ ║╣ ╠╦╝
    ╚═╝╩ ╩╩ ╩╩╚═╩ ╩╚═╝ ╩ ╚═╝╩╚═
      ┌─┐┬─┐┌─┐┌─┐┌┬┐┬┌─┐┌┐┌   
      │  ├┬┘├┤ ├─┤ │ ││ ││││   
      └─┘┴└─└─┘┴ ┴ ┴ ┴└─┘┘└┘ooo
   =============================
    """

#||====GAME=OVER====||#
def game_over_screen():
  print(
    """
▀▄    ▄ ████▄   ▄       ██▄   ▄█ ▄███▄   ██▄   
  █  █  █   █    █      █  █  ██ █▀   ▀  █  █  
   ▀█   █   █ █   █     █   █ ██ ██▄▄    █   █ 
   █    ▀████ █   █     █  █  ▐█ █▄   ▄▀ █  █  
 ▄▀           █▄ ▄█     ███▀   ▐ ▀███▀   ███▀  
               ▀▀▀                             
                                               
    """
  )

#||==INSTRUCTIONS==||#
instruction_screen ="""
==================================
 ╦╔╗╔╔═╗╔╦╗╦═╗╦ ╦╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
 ║║║║╚═╗ ║ ╠╦╝║ ║║   ║ ║║ ║║║║╚═╗
 ╩╝╚╝╚═╝ ╩ ╩╚═╚═╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝
================================== 
    """

#||===INFORMATION===||#
about_screen ="""
=======================    
╔═╗  ╔╗   ╔═╗  ╦ ╦  ╔╦╗
╠═╣  ╠╩╗  ║ ║  ║ ║   ║ 
╩ ╩  ╚═╝  ╚═╝  ╚═╝   ╩ 
┌┬┐┬ ┬┌─┐  ┌─┐┌─┐┌┬┐┌─┐
 │ ├─┤├┤   │ ┬├─┤│││├┤ 
 ┴ ┴ ┴└─┘  └─┘┴ ┴┴ ┴└─┘
======================= 


"""

#||================||#


#||================||#
#||=ASCII=ENTITIES=||#
#||================||#

#||=====OLD=HAG====||#
def ent_old_hag():
  print(
    """
                                       __,,,
                                 _.--'    /
                              .-'        /
                            .'          |
                          .'           /
                         /_____________|
                       /`~~~~~~~~~~~~~~/
                     /`               /
      ____,....----'/_________________|---....,___
,--""`             `~~~~~~~~~~~~~~~~~~`           `""--,
`'----------------.----,------------------------,-------'`
               _,'.--. \                         \

            c   , '--'  |                        /
           /    )'-.    \                       /
          |  .-;        \                       |
          \_/  |___,'    |                    .-'
         .---.___|_      |                   /
        (          `     |               .--'
         '.         __,-'\             .'
           `'-----'`      \        __.'
                           `-..--'`
      ==============================================
       |=-=-=||STATS:    ||INVENTORY:             |               
       |WITCH||DMG:    25||fermented frog legs    |
       |=-=-=||HEALTH: 15||ancient enchanted stick|
      ==============================================
"""
)

#||======Orc======||#
def ent_orc():
  print(
    """
            ,      ,   
           /(.-""-.)\

        | \/ =.  .= \/ |
        \( \  ö  0  / )/
         \_, '/  \' ,_/
          /   \__/   \

        ___\ \|UU|/ /___
      /`    \ .--. /    `\

=================================        
 |=-=||STATS:    ||INVENTORY:  |
 |ORC||DMG:    10||ragged cloth|
 |=-=||HEALTH: 35||small club  |
=================================
    """
  )

#||=====KNIGHT=====||#
def ent_dark_knight():
  print(
    """
      _,.
    ,` -.)
   ( _/-\\-._
  /,|`--._,-^|            ,
  \_| |`-._/||          ,'|
    |  `-, / |         /  /
    |     || |        /  /
     `r-._||/   __   /  /
 __,-<_     )`-/  `./  /
'  \   `---'   \   /  /
    |           |./  /
    /           //  /
\_/' \         |/  /
 |    |   _,^-'/  /
 |    , ``  (\/  /_
  \,.->._    \X-=/^
  (  /   `-._//^`     
   `Y-.____(__}          
    |     {__)           
          ()             
=========================================
 |=-=-=||STATS:    |INVENTORY:         |
 |KNGHT||DMG:    35|steel-plated armour|
 |=-=-=||HEALTH: 40|iron broadsword    |
=========================================
    """
    )

#||=ENEMY=VALUES=||#


#||START=SEQUENCE||#
clear()
title_welcome()
time.sleep(.25)
title_screen_to()
time.sleep(.75)
title_ascii()
time.sleep(2.5)
clear()
#||-----------------||#


#||MAIN=MENU=OPTIONS||#
loop = 0
while loop == 0:
  clear()
  menu = input(main_menu)
#||=====ABOUT======||#
  if menu == '3':
    clear()
    print(about_screen)
    menu = input(
      """
Welcome to the last Quiz Master! This game is a text based 
quiz rpg, that is set in the trecherous land of Uulgerm'ath
filled with enimies of everykind from, Dark Posessed knights
to disguting old hags. An adventure through this land 
requires knowlege and intellect on an unprecidented scale.

Input 'b' to return: """)
  if menu == 'b':
    continue
#||====INFO====||#
  if menu == '2':
    clear()
    print(instruction_screen)
    time.sleep(0.5)
    print("\n1. Please only input lowercase letters.\n\n")
    menu = input("Input 'b' to return: ")
  if menu == 'b':
    continue
#||====CHAR=CREATE===||#
  if menu == '1':
    clear()
    print(char_create_menu)
    menu = input("Press '1' to start, or b to return: ")
    if menu == '1':
      break
    else:
      continue
  if menu == 'four':
    clear()
    print("Source:\nhttps://en.wikipedia.org/wiki/List_of_common_misconceptions")
    menu = input("Input 'b' to return: ")
  if menu == 'b':
    continue
#||------------------||#
  
clear()
print(char_create_menu)
time.sleep(0.5)
print("Welcome to Uulgerm'ath adventurer!")
f_name = input("What is your First Name?\n> ")
time.sleep(0.5)
print("Greetings and Salutations {}!".format(f_name))
time.sleep(0.25)
print("Oh, Yes!")
s_name = input("So {}, What is your Surname?\n> ".format(f_name))
time.sleep(0.5)
clear()
print(char_create_menu)
print("A pleasure to make your acquaintance, on this beautiful day! {} {}!".format(f_name, s_name))
clear()
print(char_create_menu)

