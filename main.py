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
#||====Health=========||3


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
       |=-=-=||STATS:    ||INVENTORY:             |        |WITCH||DMG:    25||fermented frog legs    |
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
  menu = input(main_menu).lower()
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
    print("\n1. Please only input lowercase letters.\nThis is due to the fact that\nim lazy and cant be bothered\nmaking it to react to every varient\nof whatever you need to input\n")
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
  if menu == '05':
    clear()
    print(
      """
╔═╗═╗ ╦╔═╗╦  ╔═╗╦╔╦╗╔═╗
║╣ ╔╩╦╝╠═╝║  ║ ║║ ║ ╚═╗
╚═╝╩ ╚═╩  ╩═╝╚═╝╩ ╩ ╚═╝
      """
      )
    time.sleep(0.5)
    print("Here lie all of the knowen exploits in my terrible code!")
    time.sleep(0.5)
    print("1. In the main menu you can actually press any key to leave.")
    menu = input("Press 'any key' to return:\n> ")
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
print("A pleasure to make your acquaintance, on this beautiful day!\n{} {}!".format(f_name, s_name))
time.sleep(3)
clear()
#Profession Selection loop.
loop = 0
while loop == 0:
  clear()
  print(char_create_menu)
  time.sleep(0.25)
  prof = input(
    """
What is your preferred profession?
==================================
1. Jack of All Trades
2. Elemental Mage
3. Reclusive Thief
4. Standard Warrior
>  """)
#Jack of All Trades
  if prof == '1':
    clear()
    print(char_create_menu)
    time.sleep(0.25)
    print(
      """
Brief Overview:
=====================================================
The Jack of All Trades is an interesting profession!
This is due to the fact that you dont specialize in
Just one thing! Although you are not exactly the best
at anything either. It would be a spoiler for me to
inform you on anything more! Although I can spare you
one last secret...
    """)
    time.sleep(0.5)
    print(
      """
Special ability:
=======================================================
During a battle, if your health drops below 2 points,
you can call upon a your ancestors to summon a horrifying
Wendigo to assist you in the battle.
      """)
    prof = input("To select input: '1' To return: 'b'\n> ")
    if prof == '1':
      break
    else:
      continue
#Elemental Mage
  if prof == '2':
    clear()
    print(char_create_menu)
    time.sleep(0.25)
    print(
      """
Brief Overview:
=======================================================
The Elemental Mage is the profession of Magic utilized
by only the most skilled Mages of any type! While a 
normal mage would only utilize and master one or two 
elements the Elemental Mage is able master all of the 5
elements and is also able to use them in a complemetary
manor. Sadly the secrets of magic where long ago
released so their special abilities are common knowlege.""")
    time.sleep(0.5)
    print(
      """
Special Ability:
=======================================================
As an Elemental Mage you are able to heal upto 50% of
your remaining health, this even works if you are healthy
but be warned the lower your health the less you are able
heal.""")
    prof = input("Input '1' to select, or Input 'b' to return:\n> ")
  if prof == '1':
    break
  else:
    continue
    
    






