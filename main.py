from random import randint
from time import sleep


print ("""

░█████╗░░██████╗██╗░░██╗░█████╗░░██████╗██╗░░██╗
██╔══██╗██╔════╝██║░░██║██╔══██╗██╔════╝██║░░██║
██║░░██║╚█████╗░███████║███████║╚█████╗░███████║
██║░░██║░╚═══██╗██╔══██║██╔══██║░╚═══██╗██╔══██║
╚█████╔╝██████╔╝██║░░██║██║░░██║██████╔╝██║░░██║
░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝
""")

base1 = "BTC"
timeset = "30"

while True:
  start1 = input ("""
  1 - Start block mining
  2 - About 
  3 - How to use
  4 - Kill Program 
  5 - [Experimental] Set block hash time
  6 - [Experimental] Set block base
  7 - Fun Hacker Number Rain
  8 - Speed Mine (Unprofitable)
  """)

  if start1 == "5":
    timeset = input ("Set a max time for mining a block: ")

  if start1 == "8":
    print ("Starting speed block mining...")

    while True:
      print ("BTC block found - Mining Now")

      print ("Finished mining crypto block. Finding data...")

      print ("ETH block - Base: " + base1 + " - Block ID:")
      print (randint(1,999999))
      sleep(0.3)
    

  if start1 == "7":
    print ("Starting...")
    while True:
      print ("$---------------" + str(randint(11111111111111111111,99999999999999999999)) + "---------------$")
      sleep(0.02)

  if start1 == "6":
    blok = input ("""Enter 1 for bitcoin base - Enter 2 for Etherium base - Enter 3 for Dogecoin base - Base is Bitcoin (BTC) at default
    """)
    if blok == "1":
      base1 = "BTC"
    if blok == "2":
      base1 = "ETH"
    if blok == "3":
      base1 = "DGC"
    

  if start1 == "4":
    print ("""  
    ┏━━━┳━┓┏━┳━━┳━━━━┓
    ┃┏━━┻┓┗┛┏┻┫┣┫┏┓┏┓┃
    ┃┗━━┓┗┓┏┛╋┃┃┗┛┃┃┗┛
    ┃┏━━┛┏┛┗┓╋┃┃╋╋┃┃
    ┃┗━━┳┛┏┓┗┳┫┣┓╋┃┃
    ┗━━━┻━┛┗━┻━━┛╋┗┛
      """)
    sleep(0.8)
    print ("""
    Exiting the program. Thank you for using OS Hash...
    """)
    sleep(1)
    exit()

  if start1 == "2":
    print ("""
    ╔═══╦══╗╔═══╦╗─╔╦════╗
    ║╔═╗║╔╗║║╔═╗║║─║║╔╗╔╗║
    ║║─║║╚╝╚╣║─║║║─║╠╝║║╚╝
    ║╚═╝║╔═╗║║─║║║─║║─║║
    ║╔═╗║╚═╝║╚═╝║╚═╝║─║║
    ╚╝─╚╩═══╩═══╩═══╝─╚╝
      """)
    sleep(0.8)
    print ("""
    OS Hash made by nomad.
    More about me at nomadtech.nomad5689.repl.co
    Our goal with OS Hash is to make a 
    simple to use crypto miner made in python. 
    If you have any problems or suggestions 
    put it on the project github repo.
    Thanks!
    """)

  if start1 == "3":
    print ("""
    ╔══╦═╗─╔╦═══╦═══╗
    ╚╣╠╣║╚╗║║╔══╣╔═╗║
    ─║║║╔╗╚╝║╚══╣║─║║
    ─║║║║╚╗║║╔══╣║─║║
    ╔╣╠╣║─║║║║──║╚═╝║
    ╚══╩╝─╚═╩╝──╚═══╝
    """)
    sleep(0.8)
    print ("""
    The OS Hash miner makes it 
    easy to mine for Cryptocurrencies such as 
    Bitcoin or Etherium easy,
    and without having to download lots of 
    sketchy software.
    The hash rate (profibility) of the miner 
    is currently: 5.37 hps

    To start mining all you need to do is type 1
    and the miner will start mining automatically.
    To stop mining just kill the task manually on
    whatever program you are using.
    
    If you have any problems with mining or suggestions
    just send me a message at nomad.#5679 on discord!
    """)

  if start1 == "1":
    sleep(1)
    print ("Starting block mining...")
    sleep(1)

    while True:
      sleep(randint(1,5))

      print ("BTC block found - Mining Now")

      sleep(randint(1,int(timeset)))

      print ("Finished mining crypto block. Finding data...")

      sleep(2.5)

      print ("ETH block - Base: " + base1 + " - Block ID:")
      print (randint(1,999999))
  sleep(1)
