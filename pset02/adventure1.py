import sys
import types



def start():
    print ""                                  
    print "  /\  _|   _  _ _|_    _ _ /|    _    "
    print " /--\(_|\/(-'| ) | |_|| (-' |.  |_)\/ "
    print "                                |  /  "
    while True:
        sc = raw_input("Type 'NEW' to begin a new game, enter 'LOAD' to load an existing game: ")
        if sc.lower() == 'load':
            print "I'm sorry, the load game option is not implemented yet."
        elif sc.lower() == 'new':
            game_begin()
            break
        else:
            print "Unknown input, please try again."

def game_begin():
        name = ""
        while name == "":
                name = str(raw_input("Please enter your character's name: "))
        print
        print "Welcome to your doom, " + name + "!"
        print
        print "Type 'HELP' at any time for a list of commands!"
        print
        player1 = Player(name, room01, True)
        look(player1, 'room')
        action(player1, "")

def look(player, target):
    if target == 'room':
        print "Room: " + player.inroom.title
        print player.inroom.rdesc
        player.inroom.invprint()
        print 
        print player.inroom.exits()
#    if target != "":
#        print target.idesc
    else:
        pass
    
def add_exit_n(room, exitroom):
        room.n = exitroom
def add_exit_s(room, exitroom):
        room.s = exitroom
def add_exit_e(room, exitroom):
        room.e = exitroom
def add_exit_w(room, exitroom):
        room.w = exitroom
        
class Player:
    def __init__(self, name, inroom, pc):
        self.inv = []
        self.name = name
        self.inroom = inroom
        self.turn = 0
        self.pc = pc
        self.hp = 10
        
    def get_item(self, item):
        if item.cantake == True:
            for n in self.inroom.rinv:
                if n == item:
                    self.inroom.rinv.remove(item)
                    self.inv.append(item)
        print "You take " + item.sdesc + "."
        if item.cantake == False:
            print item.sdesc.capitalize() + " is much too big for you to take it!"

    def drop_item(self, item):
        for n in self.inv:
            if n == item:
                self.inv.remove(item)
                self.inroom.rinv.append(item)
        print "You drop " + item.sdesc + "."

    def find_inv(self, item):
        for i in self.inv:
            if i == item:
                return True

    def find_rinv(self, item):
        for i in self.inroom.rinv:
            if i == item:
                return True

    def print_inv(self):
        print "Inventory:"
        for i in self.inv:
            print "   " + i.sdesc
    def go_n(self):
        if self.inroom.n != "":
            self.inroom = self.inroom.n
            look(self, 'room')
        else:
            print "There is no exit to the north."
    def go_e(self):
        if self.inroom.e != "":
            self.inroom = self.inroom.e
            look(self, 'room')
        else:
            print "There is no exit to the east."
    def go_s(self):
        if self.inroom.s != "":
            self.inroom = self.inroom.s
            look(self, 'room')
        else:
            print "There is no exit to the south."
    def go_w(self):
        if self.inroom.w != "":
            self.inroom = self.inroom.w
            look(self, 'room')
        else:
            print "There is no exit to the west."
        
            
        
class Room:
    def __init__(self, title, rdesc):
        self.title = title
        self.rdesc = rdesc
        self.rinv = []
        self.n = ""
        self.e = ""
        self.s = ""
        self.w = ""
        
    def add_item(self, item):
        self.rinv.append(item)

    def invprint(self):
        for i in self.rinv:
            print i.ldesc
            
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
    

class Item:
    def __init__(self, sdesc, ldesc, cantake):
        self.sdesc = sdesc
        self.ldesc = ldesc
        self.cantake = cantake
        self.used = 0
 

#Below are individual item methods. 

def use_cot(self):
    if item03.used == 0:
        print
        print "You notice something under your pillow. It's a key!"
        print
        room01.add_item(item05)
        self.get_item(item05)
        item03.used += 1
    if item03.used >= 1:
        print
        print "You rest on the dingy cot."
        print

Player.use_cot = types.MethodType(use_cot, None, Player)

def use_key(self):
    if self.inroom == room01:
        print
        print "You use the key to open the door."
        print
        add_exit_n(room01, room02)
        add_exit_s(room02, room01)
        room01.rinv.remove(item04)
        room01.add_item(item06)
        self.inv.remove(item05)
    else:
        pass

Player.use_key = types.MethodType(use_key, None, Player)

def use_rope(self):
    if self.inroom == room01:
        print
        print "You tie the rope to the light fixture and try to hang yourself. The rope snaps into two worthless pieces. What a waste!"
        print
        self.inv.remove(item02)
        room03.add_item(item02)
    if self.inroom == room03:
        print
        print "You tie the rope to a jutting piece of rebar and try to repel down the hole to the floor below. The rope snaps and you plummet!"
        print
        self.inv.remove(item02)
        self.inroom = room09
        look(self, 'room')
    else:
        pass

Player.use_rope = types.MethodType(use_rope, None, Player)
    
def use_spoon(self):
    if self.inroom == room01 or self.inroom == room02:
        print
        print "You sharpen the spoon into a crude shank by running it over the concrete floor for a few hours."
        print
        self.inv.remove(item01)
        self.inroom.add_item(item07)
        self.get_item(item07)
    else:
        pass
    
Player.use_spoon = types.MethodType(use_spoon, None, Player)

class NPC(Player):
    def __init__(self, name, inroom, pc):
        Player.__init__(self, name, inroom, False)

def action(player, act):
    if act == "" or act is None:
        act = str((raw_input(str(player.hp) + "hp>"))).lower()
    pact = act.split()
    if pact == []:
        pass
    if len(pact) > 3:
        print "Bad Syntax. Type 'help' for commands."
    if len(pact) == 1:
        if pact[0] == 'help':
            print "Commands are NOT case sensitive."
            print "   Drop <target>           Drops an item in your inventory."
            print "   Get <target>            Picks up an item."
            print "   Inventory <or> I        Shows your inventory." 
            print "   Leave                   Exits the game."
            print "   Look <or> L             Looks at the room you are in."
            print "   Look <target>           Look at an item or non-player character(NPC)."
            print "   Go [n|e|s|w]   Go either north, east, south or west."
            print "   Talk <target>           Start a conversation with an NPC."
            print "   Say [1|2|3]             Pick a dialog option when talking to an NPC."
            print "   Use <target>          Use an item. May or may not destroy the item."
        if pact[0] == 'leave':
            print "Goodbye, " + player.name + "!"
            sys.end()
        if pact[0] == 'inventory' or pact[0] == 'i' or pact[0] == 'inv':
            player.print_inv()
        if pact[0] == 'look' or pact[0] == "l":
            look(player, 'room')
        if pact[0] == 'get':
            print "Get what?"
        if pact[0] == 'use':
            print "Use what?"
        if pact[0] == 'throw':
            print "Throw what in which direction [n|e|s|w]?"
        if pact[0] == 'go':
            print "Go in what direction [n|e|s|w]?"
        if pact[0] == 'talk':
            print "Talk to who?"
        if pact[0] == 'say':
            print "Say what?"
        if pact[0] == 'drop':
            print "Drop what?"
        if pact[0] == 'use':
            print "Use what?"
            
        
        else:
            pass
    if len(pact) == 2:
        if pact[0] == 'get' and pact[1] == "ball":
            ret = 0
            for ball in ballz:
                if player.find_rinv(ball):
                    player.get_item(ball)
                    ret = 1
                    player.turn += 1
                    break
            if ret == 0:
                print "There are no balls suitable for throwing here."
        if pact[0] == 'get':
            try:
                if player.find_rinv(kwords[pact[1]]):
                    player.get_item(kwords[pact[1]])     
                    player.turn += 1
            except KeyError:
                print "Get which item?"
                             
        if pact[0] == 'drop':
            try:
                player.drop_item(kwords[pact[1]])
                player.turn += 1
            except KeyError:
                print "Drop which item?"
        if pact[0] == 'go':
            if pact[1] == "north" or pact[1] == "n":
                player.go_n()
                player.turn += 1
            if pact[1] == "east" or pact[1] == "e":
                player.go_e()
                player.turn += 1
            if pact[1] == "south" or pact[1] == "s":
                player.go_s()
                player.turn += 1
            if pact[1] == "west" or pact[1] == "w":
                player.go_w()
                player.turn += 1
        if pact[0] == 'use':
            if pact[1] == "rope":
                if player.find_inv(item02):
                    player.use_rope()
                    player.turn += 1
                else:
                    print "You don't have any rope."
            if pact[1] == "spoon":
                if player.find_inv(item01):
                    player.use_spoon()
                    player.turn += 1
                else:
                    print "You don't have a spoon."
            if pact[1] == "cot":
                if player.find_rinv(item03):
                    player.use_cot()
                    player.turn += 1
                else:
                    print "You do not see a cot here."
            if pact[1] == "key":
                if player.find_inv(item05):
                    player.use_key()
                    player.turn += 1
                else:
                    print "You don't have a key."
        if pact[0] == 'throw':
            print "Throw what in which direction?"
    if len(pact) == 3:
        if pact[0] == 'use' and pact[1] == 'key' and pact[2] == 'door':
                print "Try just <use key>."
                
                # I'll have an if statement the throw command here.
                    
    if player.pc == True:
        action(player, "")


#I tried to put the following room and object creations within a method,
#but I found that the other methods would have trouble referencing rooms
#when they were created with a method.

room01 = Room("A Prison Cell", "You are in a damp cell that is filled with the stench of unwashed human bodies. There are strange stains over the concrete floor. Your only light source is a flickering incandescent bulb screwed within a grate covered aluminum fixture.")
room02 = Room("A Hallway Lined with Cells", "You are in a long hallway lined with solid, windowless doors, each apparently leading to a cell. The hallway stretches to the east and west and the cell you emerged from is to the south.")
room03 = Room("East End of the Hallway", "You are at the eastern end of the cell lined hallway. The hallway leads to a dead end--however, it appears a large hole has been blasted in the middle of the floor here. The pit is shadowy and you cannot tell what lies beyond.")
room04 = Room("West End of the Hallway", "You are at the western end of the hallway. Besides the numerous cell doors to the north and south, there is a strange symbol on the western wall.")
room05 = Room("Northwestern corner of a Ballpit", "You are at the northwest corner of the ballpit.")              
room06 = Room("Northern side of a Ballpit", "You are at the northern side of the ballpit.")              
room07 = Room("Northeastern corner of a Ballpit", "You are at the northeast corner of the ballpit.")
room08 = Room("Western side of a Ballpit", "You are at the Western side of the ballpit.")
room09 = Room("Center of a Ballpit", "You are in the center of the Google HQ's ballpit.")
room10 = Room("Eastern side of a Ballpit", "You are at the Eastern side of the ballpit.")
room11 = Room("Southwestern corner of a Ballpit", "You are at the southwestern corner of the ballpit.")
room12 = Room("Southern side of a Ballpit", "You are at the southern side of the ballpit.")
room13 = Room("Southeastern corner of a Ballpit", "You are in the southeastern corner of a ballpit.")
item01 = Item("a stainless steel spoon", "A dull metal spoon lies on the floor here.", True)
item02 = Item("a long, frayed rope", "A long length of frayed rope lies on the floor here.", True)
item03 = Item("a metal cot", "A metal framed cot with a stained mattress is here.", False)
item04 = Item("a concrete door", "A windowless concrete door is locked and bars the way to the north.", False)
item05 = Item("a worn metal key", "A worn metal key glimmers faintly on the floor.", True)
item06 = Item("a concrete door", "A windowless concrete door opens to a hallway to the north.", False)
item07 = Item("a crude metal shank", "A spoon that has been sharpened into a crude knife is here.", True)
item08 = Item("a red plastic ball", "A red plastic ball is in the ballpit.", True)
item09 = Item("a yellow plastic ball", "A yellow plastic ball is in the ballpit.", True)
item10 = Item("a blue plastic ball", "A blue plastic ball is in the ballpit.", True)
item11 = Item("a green plastic ball", "A green plastic ball is in the ballpit.", True)
item12 = Item("a piece of pizza", "A piece of pizza has been abandoned in the ballpit.", True)
item13 = Item("a smelly sock", "A smelly sock has been left in the ballpit.", True)
ballz = [item08, item09, item10, item11]
room01.add_item(item04)
room01.add_item(item03)
room01.add_item(item01)
room01.add_item(item02)
room09.add_item(item08)
room09.add_item(item09)
room09.add_item(item10)
room09.add_item(item11)
kwords = {"spoon": item01, "rope": item02, "cot": item03, "door": item04, "key": item05, "shank": item07, "red": item08, "yellow": item09, "blue": item10, "green": item11}
add_exit_e(room02, room03)
add_exit_w(room03, room02)
add_exit_w(room02, room04)
add_exit_e(room04, room02)
add_exit_n(room09, room06)
add_exit_s(room06, room09)
add_exit_e(room09, room10)
add_exit_w(room10, room09)
add_exit_s(room09, room12)
add_exit_n(room12, room09)
add_exit_w(room09, room08)
add_exit_e(room08, room09)
add_exit_e(room05, room06)
add_exit_w(room06, room05)
add_exit_e(room06, room07)
add_exit_w(room07, room06)
add_exit_s(room05, room08)
add_exit_n(room08, room05)
add_exit_s(room07, room10)
add_exit_n(room10, room07)
add_exit_e(room11, room12)
add_exit_w(room12, room11)
add_exit_e(room12, room13)
add_exit_w(room13, room12)
add_exit_n(room11, room08)
add_exit_s(room08, room11)
add_exit_n(room13, room10)
add_exit_s(room10, room13)

start()

