import sys
import types

room01 = Room("A Prison Cell", "You are in a damp cell that is filled with the stench of unwashed human bodies. There are strange stains over the concrete floor. Your only light source is a flickering incandescent bulb screwed within a grate covered aluminum fixture.")
room02 = Room("A Hallway Lined with Cells", "You are in a long hallway lined with solid, windowless doors, each apparently leading to a cell. The hallway stretches to the east and west and the cell you emerged from is to the south.")
room03 = Room("East End of the Hallway", "You are at the eastern end of the cell lined hallway. The hallway leads to a dead end--it appears there is no way to exit the hallway from here.")
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
room01.add_item(item04)
room01.add_item(item03)
room01.add_item(item01)
room01.add_item(item02)
vals = {"spoon": item01, "rope": item02, "cot": item03, "door": item04, "key": item05, "shank": item07}

def start():
    print "Welcome to Prison Break Densetsu!"
    while True:
        sc = raw_input("Enter 'new' to begin a new game, enter 'load' to load an existing game: ")
        if sc == 'load':
            print "I'm sorry, the load game option is not implemented yet."
        elif sc == 'new':
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
        print "Type 'help' at any time for a list of commands!"
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
        print "It smells like someone died on this thing. You notice something under your pillow. It's a key!"
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
        print "You use the key to open the door. Why would a prison cell be unlockable from the inside?"
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
    if self.inroom == room03:
        print
        print "You tie the rope to a jutting piece of rebar and try to repel down the hole to the floor below. The rope snaps and you plummet!"
        print
        self.inv.remove(item02)
        self.inroom = room09
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

def action(player, input):
    if input == "":
        act = str((raw_input(str(player.hp) + "hp>"))).lower()
    pact = act.split()
    if pact == []:
        pass
    else:
        if pact[0] == 'help':
            print "Commands are NOT case sensitive."
            print "   Leave                  Exits the game."
            print "   Look <or> L            Looks at the room you are in."
            print "   Get <target>           Picks up an item."
            print "   Drop <target>          Drops an item in your inventory."
            print "   Inventory <or> I       Shows your inventory."
            print "   Go <direction>         Go either north, east, south or west."
            print "   Use <1 or 2 targets>   Use an item. May or may not destroy the item."
            print "   Talk <target>          Talk to an NPC. Takes no arguments."
            print ""
        if pact[0] == 'leave':
            print "Goodbye, " + player.name + "!"
            sys.exit()
        if pact[0] == 'look' or pact[0] == 'l':
            look(player, 'room')
        if pact[0] == 'get':
            try:
                player.get_item(vals[pact[1]])
                player.turn += 1
            except KeyError:
                print "You do not see that item here."
        if pact[0] == 'drop':
            try:
                player.drop_item(vals[pact[1]])
                player.turn += 1
            except KeyError:
                print "You do not have that item."
        if pact[0] == 'inventory' or pact[0] == 'i' or pact[0] == 'inv':
            player.print_inv()
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
            if len(pact) < 2:
                pass
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
            if pact[1] == "key" and len(pact) < 3:
                print "Use the key on what?"
            elif pact[1] == "key" and pact [2] == "door":
                if player.find_inv(item05) is True and player.find_rinv(item04) is True:
                    player.use_key()
                    player.turn += 1
                else:
                    print "You do not have a key for that door."
                        
    if player.pc == True:
        action(player, "")
# For some reason my add_exit methods didn't work when I included them in the
# Room class I realize that it'd be best to include the methods there.
# I will reassess how to add them.

add_exit_e(room02, room03)
add_exit_w(room03, room02)
add_exit_w(room02, room04)
add_exit_e(room04, room02)


    
start()

