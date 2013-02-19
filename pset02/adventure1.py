import random
import weakref
import pickle

## Borrowed the color code from cards.py to make the game more readable.
COLORS = { 'ENDC':0,'DARK_RED':31,'RED':91,'RED_BG':41,'YELLOW':93,'YELLOW_BG':43,'BLUE':94,'BLUE_BG':44,'PURPLE':95,'MAGENTA_BG':45,'AUQA':96,'CYAN_BG':46,'GREEN':92,'GREEN_BG':42,'BLACK':30}
def termcode(num):
    return '\033[%sm'%num
color_on = None
while True:
    cc = raw_input("Enable terminal color codes? (YES or NO)")
    if cc.lower() == "yes":
        color_on = True
    if cc.lower() == "no":
        color_on = False
    if color_on is not None:
        break
def colorstr(astr, color):
    if color_on is True:
        return termcode(COLORS[color])+astr+termcode(COLORS['ENDC'])
    if color_on is False or color_on is None:
        return astr
def banner():
    print ""
    print colorstr("  /\  _|   _  _ _|_    _ _ /|    _    ", "RED_BG")
    print colorstr(" /--\(_|\/(-'| ) | |_|| (-' |.  |_)\/ ", "RED_BG")
    print colorstr("                                |  /  ", "RED_BG")

def start():
    ini.make_exits()
    ini.make_NPCs()
    banner()
    while True:
        sc = raw_input("Type NEW to begin a new game, type LOAD to load an existing game: ")       
        if sc.lower() == 'load':
            print "The load feature is not currently implemented."
        elif sc.lower() == 'new':
            game_begin()
            break
        elif sc.lower() == 'quit':
            break
        
def game_begin():
    name = ""
    while name == "":
        name = str(raw_input("Please enter your character's name: "))
        print "\nWelcome to your doom, " + name + "!"
        print "\nType 'HELP' at any time for a list of commands!\n"
        player = Player(name, "yourself", ini.room01, "pc", [], 10)
        look(player, 'room')
        prompt(player, "")

class initialize_game(object):
    def __init__(self):
        self.spoon01 = Spoon()
        self.rope01 = Rope()
        self.cot01 = Cot()
        self.door01 = LockedDoor()
        self.door02 = UnlockedDoor()
        self.key01 = Key()
        #item06 was a second door. Deleted, created by Door.use method.
        #item07 was a shank, now created by the Spoon.use method.
        self.ball01 = Ball("red")
        self.ball02 = Ball("yellow")
        self.ball03 = Ball("blue")
        self.ball04 = Ball("green")
        self.pizza01 = Pizza()
        self.item13 = Sock() 
        self.room01 = Room("A Cramped Domicile", "You are in a damp cell that is filled with the stench of unwashed human \nbodies. There are strange stains over the concrete floor. Your only light \nsource is a flickering incandescent bulb screwed within a grate covered \naluminum fixture.", [], [], "", "", "", "")
        self.room02 = Room("A Hallway Lined with Cells", "You are in a long hallway lined with solid, windowless doors, each \napparently leading to a cell. The hallway stretches to the east and \nwest and the cell you emerged from is to the south.", [], [], "", "", "", "")
        self.room03 = Room("East End of the Hallway", "You are at the eastern end of the cell lined hallway. The hallway leads \nto a dead end--however, it appears a large hole has been blasted in the \nmiddle of the floor here. The pit is shadowy and you cannot tell what \nlies beyond.", [], [], "", "", "", "")
        self.room04 = Room("West End of the Hallway", "You are at the western end of the hallway. Besides the numerous cell doors \nto the north and south, there is a strange symbol on the western wall.", [], [], "", "", "", "")
        self.room05 = Room("Northwestern corner of a Ballpit", "You are at the northwest corner of the ballpit.", [], [], "", "", "", "")              
        self.room06 = Room("Northern side of a Ballpit", "You are at the northern side of the ballpit.", [], [], "", "", "", "")              
        self.room07 = Room("Northeastern corner of a Ballpit", "You are at the northeast corner of the ballpit.", [], [], "", "", "", "")
        self.room08 = Room("Western side of a Ballpit", "You are at the Western side of the ballpit.", [], [], "", "", "", "")
        self.room09 = Room("Center of a Ballpit", "You are in the center of the google HQ's ballpit.", [], [], "", "", "", "")
        self.room10 = Room("Eastern side of a Ballpit", "You are at the Eastern side of the ballpit.", [], [], "", "", "", "")
        self.room11 = Room("Southwestern corner of a Ballpit", "You are at the southwestern corner of the ballpit.", [], [], "", "", "", "")
        self.room12 = Room("Southern side of a Ballpit", "You are at the southern side of the ballpit.", [], [], "", "", "", "")
        self.room13 = Room("Southeastern corner of a Ballpit", "You are in the southeastern corner of a ballpit.", [], [], "", "", "", "") 
    def make_exits(self):
        self.room02.add_exit_e(self.room03)
        self.room03.add_exit_w(self.room02)
        self.room02.add_exit_w(self.room04)
        self.room04.add_exit_e(self.room02)
        self.room09.add_exit_n(self.room06)
        self.room06.add_exit_s(self.room09)
        self.room09.add_exit_e(self.room10)
        self.room10.add_exit_w(self.room09)
        self.room09.add_exit_s(self.room12)
        self.room12.add_exit_n(self.room09)
        self.room09.add_exit_w(self.room08)
        self.room08.add_exit_e(self.room09)
        self.room05.add_exit_e(self.room06)
        self.room06.add_exit_w(self.room05)
        self.room06.add_exit_e(self.room07)
        self.room07.add_exit_w(self.room06)
        self.room05.add_exit_s(self.room08)
        self.room08.add_exit_n(self.room05)
        self.room07.add_exit_s(self.room10)
        self.room10.add_exit_n(self.room07)
        self.room11.add_exit_e(self.room12)
        self.room12.add_exit_w(self.room11)
        self.room12.add_exit_e(self.room13)
        self.room13.add_exit_w(self.room12)
        self.room11.add_exit_n(self.room08)
        self.room08.add_exit_s(self.room11)
        self.room13.add_exit_n(self.room10)
        self.room10.add_exit_s(self.room13)
        self.ballz = [self.ball01, self.ball02, self.ball03, self.ball04]
        #Work on the dictionary below to have better command implementation....  
        self.room01.n = ""
        self.room02.s = ""
        self.cot01.used = 0
        self.room01.add_item(self.door01)
        self.room01.add_item(self.cot01)
        self.room01.add_item(self.spoon01)
        self.room01.add_item(self.rope01)
        self.rooms = {'room01': self.room01, 'room02': self.room02, 'room03': self.room03, 'room04': self.room04, 'room05': self.room05, 'room06': self.room06, 'room07': self.room07, 'room08': self.room08, 'room09': self.room09, 'room10': self.room10, 'room11': self.room11, 'room12': self.room12, 'room13': self.room13}
        self.ballpit = {'room05': self.room05, 'room06': self.room06, 'room07': self.room07, 'room08': self.room08, 'room09': self.room09, 'room10': self.room10, 'room11': self.room11, 'room12': self.room12, 'room13': self.room13}
        for room in self.ballpit:
            for ball in self.ballz:
                self.ballpit[room].add_item(ball)
    def make_NPCs(self):
        self.demon = NPC("Ballpit Demon", "A tiny demon bounces around the ballpit here.", self.room09, "npc", [], 10)
        
class Player:
    def __init__(self, name, ldesc, inroom, pc, inventory, hp):
        self.name = name #String
        self.ldesc = ldesc #String
        self.inroom = inroom #Id of object created with Room (ex room01)
        self.inv = inventory #list containing item IDs (ex rope01)
        self.pc = pc # "active", "stored", or "npc" (string) 
        self.hp = hp #Health points of the character (int)

    def get_item(self, itemstr):
        item = self.find_rinv(itemstr)
        if self.find_rinv(itemstr) is None:
            print "You do not see a %s here." % itemstr
        if self.find_rinv(itemstr):
            if item.cantake == True: #checks if the item is takeable.
                if len(self.inv) < 10: #checks for room in inventory
                    self.inroom.rinv.remove(item)
                    self.inv.append(item)
                    if self.pc == "pc":
                        print "You take %s." % item.sdesc
                if len(self.inv) >= 10 and self.pc == "pc":
                    print "You have too many items in your inventory."
            if item.cantake == False and self.pc == "pc":
                print item.sdesc.capitalize() + " is much too big for you to take it!"

    def drop_item(self, itemstr):
        item = self.find_inv(itemstr)
        if self.find_inv(itemstr) is None:
            print "You do not have a %s." % itemstr
        if self.find_inv(itemstr):
            self.inv.remove(item)
            self.inroom.rinv.append(item)
            if self.pc == "pc":
                print "You drop %s." % item.sdesc

    def use_item(self, itemstr):
        if self.find_inv(itemstr):
            self.find_inv(itemstr).use(self)
        elif self.find_rinv(itemstr):
            self.find_rinv(itemstr).use(self)
        elif self.find_inv(itemstr) is False and self.find_rinv(itemstr) is False:
            print "You do not a %s that you can use." % itemstr

    def find_inv(self, itemstr):
        for i in self.inv:
            if i.kword == itemstr:
                return i

    def find_rinv(self, itemstr):
        for i in self.inroom.rinv:
            if i.kword == itemstr:
                return i
            
    def print_inv(self):
        print "Inventory:"
        for i in self.inv:
            print "   " + i.sdesc

    def go(self, direction):
        if direction == 'n' or direction == 'north':
            if self.inroom.n != "":
                self.inroom = self.inroom.n
                if self.pc == "pc":
                    look(self, 'room')
            elif self.inroom.n == "":
                if self.pc == "pc":
                    print "There is no exit to the north."
        elif direction == 'e' or direction == 'east':
            if self.inroom.e != "":
                self.inroom = self.inroom.e
                if self.pc == "pc":
                    look(self, 'room')
            elif self.inroom.e == "":
                if self.pc == "pc":
                    print "There is no exit to the east."
        elif direction == 's' or direction == 'south':
            if self.inroom.s != "":
                self.inroom = self.inroom.s
                if self.pc == "pc":
                    look(self, 'room')
            elif self.inroom.s == "":
                if self.pc == "pc":
                    print "There is no exit to the south."
        elif direction == 'w' or direction == 'west':
            if self.inroom.w != "":
                self.inroom = self.inroom.w
                if self.pc == "pc":
                    look(self, 'room')
            elif self.inroom.w == "":
                if self.pc == "pc":
                    print "There is no exit to the west."
        elif direction != 'n' and direction != 'north' and direction != 'e' and direction != 'east' and direction != 's' and direction != 'south' and direction != 'w' and direction != 'west':
            print "Go in which direction?"
        else:
            pass

#This will throw items in inventory and deal damage to players.
    def throw(self, weapon, direction):
        if self.inroom.direction != "":
            pass

#This prompts NPCs to act, called after the player acts.
    def turn(self, reference):
        if reference is None:
            pass
        else:
            reference.demon_ai(self)
        

class NPC(Player):
    def __init__(self, name, ldesc, inroom, pc, inventory, hp):
        self.name = name #String
        self.ldesc = ldesc #String
        self.inroom = inroom #Id of object created with Room (ex room01)
        self.inv = inventory #list containing item IDs (ex rope01)
        self.pc = pc # "active", "stored", or "npc" (string) 
        self.hp = hp #Health points of the character (int)
        self.inroom.pinv.append(self.ldesc)

class Room(object):
    def __init__(self, title, rdesc, rinv, pinv, n, e, s, w):
        self.title = title #String
        self.rdesc = rdesc #String
        self.rinv = rinv # Default is [], list of items in room
        self.pinv = pinv # Default is [], list of people in room
        self.n = "" # Default is "", which indicates no exit.
        self.e = ""
        self.s = ""
        self.w = ""
    def add_item(self, item):
        self.rinv.append(item)
    def add_exit_n(self, exitroom):
        self.n = exitroom
    def add_exit_s(self, exitroom):
        self.s = exitroom
    def add_exit_e(self, exitroom):
        self.e = exitroom
    def add_exit_w(self, exitroom):
        self.w = exitroom

    def inv_print(self):
        for i in self.rinv:
            print i.ldesc
        for y in self.pinv:
            print y
            
    def exits(self):
        exits = []
        if self.n != "":
            exits.append("N")
        if self.e != "":
            exits.append("E")
        if self.s != "":
            exits.append("S")
        if self.w != "":
            exits.append("W")
        return "Exits: " + str(exits)
    
kwords = {}

class Item(object):
    def __init__(self, kword, sdesc, ldesc, cantake, used):
        self.kword = kword
        self.cword = colorstr(self.kword, "CYAN_BG")
        self.sdesc = sdesc #string
        self.ldesc = ldesc #string
        self.cantake = cantake #True or False
        self.used = used #Starts at 0, int
        self.store_kword()

    def store_kword(self):
        kwords[self.kword] = self

class Rope(Item):
    def __init__(self):
        self.kword = "rope"
        self.cword = colorstr(self.kword, "CYAN_BG")
        self.sdesc = "a long, frayed %s" % self.cword
        self.ldesc = "A long length of frayed %s lies on the floor here." % self.cword
        self.cantake = True
        self.used = 0
        self.store_kword()
    def use(self, player):
        if player.inroom == ini.room01:
            print "\nYou tie the rope to the light fixture and try to hang yourself. The rope snaps into two worthless pieces. What a waste!\n"
            player.inv.remove(ini.rope01)
            ini.room03.add_item(ini.rope01)
        if player.inroom == ini.room03:
            print "\nYou tie the rope to a jutting piece of rebar and try to repel down the hole to the floor below. The rope \nsnaps and you plummet!\n"
            player.inv.remove(ini.rope01)
            player.inroom = ini.room09
            look(player, 'room')
        else:
            pass

class Key(Item):
    def __init__(self):
        self.kword = "key"
        self.cword = colorstr(self.kword, "CYAN_BG")
        self.sdesc = "a worn metal %s" % self.cword
        self.ldesc = "A worn metal %s glimmers faintly on the floor." % self.cword
        self.cantake = True
        self.used = 0
        self.store_kword()
    def use(self, player):
        if player.inroom == ini.room01:
            print "\nYou use the key to open the door.\n"
            ini.room01.add_exit_n(ini.room02)
            ini.room02.add_exit_s(ini.room01)
            ini.room01.rinv.remove(ini.door01)
            ini.room01.rinv.append(ini.door02)
            player.inv.remove(self)
        else:
            pass

class Spoon(Item):
    def __init__(self):
        self.kword = "spoon"
        self.cword = colorstr(self.kword, "CYAN_BG")
        self.sdesc = "a stainless steel %s" % self.cword
        self.ldesc = "A dull metal %s lies on the floor here." % self.cword
        self.cantake = True
        self.used = 0
        self.store_kword()
    def use(self, player):
        if player.inroom == ini.room01:
            print '\nYou sharpen the spoon into a crude shank by running it over the concrete floor for a few hours.\n'
            player.inv.remove(self)
            shank01 = Shank()
            player.inroom.add_item(shank01)
            player.get_item("shank")
            print "\nThat was a lot of work! You're getting tired.\n"
        else:
            pass

class Shank(Item):
    def __init__(self):
        self.kword = "shank"
        self.cword = colorstr(self.kword, "CYAN_BG")
        self.sdesc = "a crude metal %s" % self.cword
        self.ldesc = "A spoon that has been sharpened into a crude %s is here." %self.cword
        self.cantake = True
        self.used = 0
        self.store_kword()
    def use(self, player):
        pass

class Cot(Item):
    def __init__(self):
        self.kword = "cot"
        self.cword = colorstr(self.kword, "CYAN_BG")
        self.sdesc = "a metal %s" % self.cword
        self.ldesc = "A metal framed %s with a stained mattress is here." % self.cword
        self.cantake = False
        self.used = 0
        self.store_kword()
    def use(self, player):
        if self.used == 0:
            print "\nYou notice something under your pillow. It's a key!\n"
            key01 = Key()
            player.inroom.add_item(key01)
            player.get_item("key")
            self.used += 1
        if self.used >= 1:
            print "\nYou rest on the dingy cot.\n"

class LockedDoor(Item):
    def __init__(self):
        self.kword = "door"
        self.cword = colorstr(self.kword, "CYAN_BG")
        self.sdesc = "a concrete %s" % self.cword
        self.used = 0
        self.ldesc = "A %s made of iron bars is locked and bars the way to the north." % self.cword
        self.cantake = False
        self.store_kword()
    def use(self,player):
        print "The door is locked."

class UnlockedDoor(Item):
    def __init__(self):
        self.kword = "door"
        self.cword = colorstr(self.kword, "CYAN_BG")
        self.sdesc = "a concrete %s" % self.cword
        self.used = 0
        self.ldesc = "A %s made of iron bars is unlocked and reveals the way to the north." % self.cword
        self.cantake = False
        self.store_kword()
    def use(self):
        print "The door is unlocked and open."

class Ball(Item):
    def __init__(self, color):
        self.kword = "ball"
        self.cword = colorstr(self.kword, "CYAN_BG")
        self.color = color #string
        self.sdesc = "a " + self.color + " plastic " + self.cword
        self.ldesc = self.sdesc + " is in the ballpit here."
        self.cantake = True
        self.used = 0
        self.store_kword()
    def use(self, player):
        pass

class Pizza(Item):
    def __init__(self):
        self.kword = "pizza"
        self.cword = colorstr(self.kword, "CYAN_BG")
        self.sdesc = "a piece of %s" % self.cword
        self.ldesc = "A piece of  %s has been abandoned in the ballpit." % self.cword
        self.cantake = True
        self.used = 0
        self.store_kword()
    def use(self, player):
        player.inv.remove(self)
        print "\nYou eat a slice of pizza, restoring a small amount of health.\n"
        player.hp += 2
        if player.hp > 10:
            player.hp = 10
            
class Sock(Item):
    def __init__(self):
        self.kword = "sock"
        self.cword = colorstr(self.kword, "CYAN_BG")
        self.sdesc = "a smelly %s" % self.cword
        self.ldesc = "A smelly %s has been left in the ballpit." % self.cword
        self.cantake = True
        self.used = 0
        self.store_kword()
    def use(self, player):
        player.inv.remove(self)
        print "\nYou play around with a smelly sock for some reason. Gross! (Health lost.)\n"
    

    
#This accepts AI input or player input (str), returns a word list to
#command functions.
def prompt(player, act):
    act = str(act)
    if act == "" or act is None:
        act = str((raw_input(str(player.hp) + "hp>"))).lower()
    pact = act.split()
    if pact == []:
        pass
    if len(pact) > 3:
        print "Too many command words. Type 'help' for command syntax."                
    if pact[0] == "look" or pact[0] == "l":
        if len(pact) >= 3:
            print "Try 'look <target>' or just 'look.'"
        if len(pact) == 2:
            look(player, pact[1])
        if len(pact) == 1:
            look(player, 'room')
    if pact[0] == 'throw':
        if len(pact) == 3:
            player.throw(pact[1], pact[2])
        if len(pact) != 3:
            print "Try 'throw <weapon> <direction>'"
    if pact[0] == 'use':
        if len(pact) == 2:
            player.use_item(pact[1])
        if len(pact) != 2:
            print "Try 'use <object>'"
    if pact[0] == 'go':
        if len(pact) >= 3:
            print "Try 'go <direction>' or '<direction>'"
        if len(pact) == 2:
            player.go(pact[1])
    if pact[0] == "n" or pact[0] == "north" or pact[0] == "e" or pact[0] == "east" or pact[0] == "s" or pact[0] == "south" or pact[0] == "w" or pact[0] == "west":
        player.go(pact[0])
    if pact[0] == 'help':
        help()
    if pact[0] == 'get':
        if len(pact) == 2:
            player.get_item(pact[1])
        if len(pact) != 2:
            print "Try 'get <item>'"
    if pact[0] == 'drop':
        if len(pact) == 2:
            player.drop_item(pact[1])
        if len(pact) != 2:
            print "Try 'drop <item>'"
    if pact[0] == 'inventory' or pact[0] == 'i':
        player.print_inv()
    if pact[0] == "leave" or pact[0] == "quit":
        quit_game(player)

    if player.pc == "pc":
        prompt(player, "")
    
# Catching commonly attempted commands that are not linked to functions.
    if pact[0] == 'open':
        print "There is no 'open' command. Type 'help' for commands."
    if pact[0] == 'unlock':
        print "There is no 'unlock' command. Try the 'use' command instead."
        
            
def help():
    print "Commands are NOT case sensitive."
    print "   Drop <target>           Drops an item in your inventory."
    print "   Get <target>            Picks up an item."
    print "   Inventory <or> I        Shows your inventory." 
    print "   Leave <or> Quit         Exits the game."
    print "   Save                    Saves game data."
    print "   Look <or> L             Looks at the room you are in."
    print "   Look <target>           Look at exits, an item or non-player character(NPC)."
    print "   Go [n|e|s|w]            Go either north, east, south or west."
    print "   Talk <target>           Start a conversation with an NPC."
    print "   Say [1|2|3]             Pick a dialog option when talking to an NPC."
    print "   Use <target>            Use an item. May or may not destroy the item."

def quit_game(player):
    while True:
        quitprompt = raw_input("Would you like to SAVE or just LEAVE the game?")
        if quitprompt.lower() == 'save':
            print "The save game feature is not currently implemented."
            print "\nSee you later, %s!\n" % player.name
            player.pc = "stored"
            break
        elif quitprompt.lower() == 'quit' or quitprompt.lower() == 'leave':
            print "\nSee you later, %s!\n" % player.name
            player.pc = "stored"
            break
        else:
            pass

def look(player, target):
    if player.pc != "pc":
        pass
    if target == 'room':
        print "You look at the room and see..."
        print "   [" + player.inroom.title + "]"
        print player.inroom.rdesc
        player.inroom.inv_print()
        print 
        print player.inroom.exits()
    if target == "exit" or target == "exits":
        nesw = {'north': player.inroom.n, 'east':player.inroom.e, 'south':player.inroom.s, 'west':player.inroom.w}
        ret = 0
        for direc in nesw:
            if nesw[direc] == "":
                ret += 1
            if nesw[direc] != "":
                print "To the " + direc + " you see..."
                print "   " + nesw[direc].title + "."
                for person in nesw[direc].pinv:
                    print person
                print
        if ret == 4:
            print "There are no obvious exits."
        if ret < 3:
            pass
    if target != "exit" or target != "room" or target != "exits":
        pass


    
ini = initialize_game()
start()


