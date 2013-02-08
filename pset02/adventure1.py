import sys

room01 = Room("A Prison Cell", "You are in a damp cell that is filled with the stench of unwashed human bodies. There are strange stains over the concrete floor. Your only light source is a flickering incandescent bulb screwed within a grate covered aluminum fixture.")
room02 = Room("A Hallway Lined with Cells", "You are in a long hallway lined with solid, windowless doors, each apparently leading to a cell. The hallway stretches to the east and west and the cell you emerged from is to the south.")
room03 = Room("East End of the Hallway", "You are at the eastern end of the cell lined hallway. The hallway leads to a dead end--it appears there is no way to exit the hallway from here.")
room04 = Room("West End of the Hallway", "You are at the western end of the hallway. Besides the numerous cell doors to the north and south, there is a strange symbol on the western wall.")
item01 = Item("a stainless steel spoon", "A dull metal spoon lies on the floor here.", True)
item02 = Item("a long, frayed rope", "A long length of frayed rope lies on the floor here.", True)
item03 = Item("a metal cot", "A metal framed cot with a stained mattress is here.", False)
item04 = Item("a concrete door", "A windowless concrete door opens to a hallway to the north.", False)
room01.add_item(item04)
room01.add_item(item03)
room01.add_item(item01)
room01.add_item(item02)
vals = {"spoon": item01, "rope": item02, "cot": item03, "door": item04}

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
        player1 = Player(name, room01)
        look(player1, 'room')
        action(player1)

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
    def __init__(self, name, inroom):
        self.inv = []
        self.name = name
        self.inroom = inroom
        
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

#class NPC(Player):
#    def __init__(self):
#    Player.__init__(self)
#    etc: see http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/

def action(player):
    act = str((raw_input(">"))).lower()
    pact = act.split()
    if pact == []:
        pass
    else:
        if pact[0] == 'help':
            print "Commands are NOT case sensitive."
            print "   Leave           Exits the game."
            print "   Look            Looks at the room you are in."
            print "   Get <target>    Picks up an item."
            print "   Drop <target>   Drops an item in your inventory."
            print "   Inventory       Shows your inventory."
            print "   go <direction>  Go either north, east, south or west."
            print ""
        if pact[0] == 'leave':
            print "Goodbye, " + player.name + "!"
            sys.exit()
        if pact[0] == 'look' or pact[0] == 'l':
            look(player, 'room')
        if pact[0] == 'get':
            try:
                player.get_item(vals[pact[1]])
            except KeyError:
                print "You do not see that item here."
        if pact[0] == 'drop':
            try:
                player.drop_item(vals[pact[1]])
            except KeyError:
                print "You do not have that item."
        if pact[0] == 'inventory' or pact[0] == 'i' or pact[0] == 'inv':
            player.print_inv()
        if pact[0] == 'go':
            if pact[1] == "north" or pact[1] == "n":
                player.go_n()
            if pact[1] == "east" or pact[1] == "e":
                player.go_e()
            if pact[1] == "south" or pact[1] == "s":
                player.go_s()
            if pact[1] == "west" or pact[1] == "w":
                player.go_w()

    action(player)

add_exit_n(room01, room02)
add_exit_s(room02, room01)
add_exit_e(room02, room03)
add_exit_w(room03, room02)
add_exit_w(room02, room04)
add_exit_e(room04, room02)

start()
