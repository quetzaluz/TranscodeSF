import types
import random
import weakref
import pickle

def start():
    print ""                                  
    print "  /\  _|   _  _ _|_    _ _ /|    _    "
    print " /--\(_|\/(-'| ) | |_|| (-' |.  |_)\/ "
    print "                                |  /  "
    while True:
        sc = raw_input("Type 'NEW' to begin a new game, enter 'LOAD' to load an existing game: ")
        if sc.lower() == 'load':
            game_load()
        elif sc.lower() == 'new':
            game_begin()
            break
        elif sc.lower() == 'quit':
            break
        
def game_begin():
    room01.n = ""
    room02.s = ""
    item03.used = 0
    room01.add_item(item04)
    room01.add_item(item03)
    room01.add_item(item01)
    room01.add_item(item02)
    for room in ballpit:
        for ball in ballz:
            room.add_item(ball)
    name = ""
    while name == "":
        name = str(raw_input("Please enter your character's name: "))
        print "\nWelcome to your doom, " + name + "!"
        print "\nType 'HELP' at any time for a list of commands!\n"
        player1 = Player(name, "yourself", room01, "pc", [], 10)
        look(player1, 'room')
        action(player1, "")

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
        try:
            if player.find_rinv(kwords[target]) or player.find_inv(kwords[target]):
                look(player, kwords[target])
        except KeyError:
            "You do not see a " + target + " here."
        
class Player:
    def __init__(self, name, ldesc, inroom, pc, inventory, hp):
        self.name = name #String
        self.ldesc = ldesc #String
        self.inroom = inroom #Id of object created with Room (ex room01)
        self.inv = inventory #list containing item IDs (ex item02)
        self.pc = pc # "active", "stored", or "npc" (string) 
        self.hp = hp #Health points of the character (int)

    def get_item(self, item):
        if item.cantake == True:
            for n in self.inroom.rinv:
                if n == item:
                    if len(self.inv) <= 10:
                        self.inroom.rinv.remove(item)
                        self.inv.append(item)
                    if self.inv == 10 and self.pc == "pc":
                         "You have too many items in your inventory."
            if self.pc == "pc":
                print "You take " + item.sdesc + "."
        if item.cantake == False and self.pc == "pc":
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

#these commands move the player between rooms. Originally I tried to have
#a single go(self, direction) command, but kept encountering various errors.
    def go_n(self):
        if self.inroom.n != "":
            self.inroom = self.inroom.n
            if self.pc == "pc":
                look(self, 'room')
        else:
            if self.pc == "pc":
                print "There is no exit to the north."
            
    def go_e(self):
        if self.inroom.e != "":
            self.inroom = self.inroom.e
            if self.pc == "pc":
                look(self, 'room')
        else:
            if self.pc == "pc":
                print "There is no exit to the east."
            
    def go_s(self):
        if self.inroom.s != "":
            self.inroom = self.inroom.s
            if self.pc == "pc":
                look(self, 'room')
        else:
            if self.pc == "pc":
                print "There is no exit to the south."
            
    def go_w(self):
        if self.inroom.w != "":
            self.inroom = self.inroom.w
            if self.pc == "pc":
                look(self, 'room')
        else:
            if self.pc == "pc":
                print "There is no exit to the west."

#This will throw items in inventory and deal damage to players.
    def throw(self, weapon, target, direction):
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
        self.inv = inventory #list containing item IDs (ex item02)
        self.pc = pc # "active", "stored", or "npc" (string) 
        self.hp = hp #Health points of the character (int)
        self.inroom.pinv.append(self.ldesc)
    
    def random_move(self, player):
        exit_list = self.inroom.exits()
        ran_room = random.choice(exit_list)
        if ran_room == "N":
            if self.inroom == player.inroom:
                print "A " + self.name.lower() + " bounces off to the north."
            for person in self.inroom.pinv:
                if person == self.ldesc:
                    self.inroom.pinv.remove(self.ldesc)
            self.go_n()
            self.inroom.pinv.append(self.ldesc)
        if ran_room == "E":
            if self.inroom == player.inroom:
                print "A " + self.name.lower() + " bounces off to the east."
            for person in self.inroom.pinv:
                if person == self.ldesc:
                    self.inroom.pinv.remove(self.ldesc)
            self.go_e()
            self.inroom.pinv.append(self.ldesc)
        if ran_room == "S":
            if self.inroom == player.inroom:
                print "A " + self.name.lower() + " bounces off to the south."
            for person in self.inroom.pinv:
                if person == self.ldesc:
                    self.inroom.pinv.remove(self.ldesc)
            self.go_s()
            self.inroom.pinv.append(self.ldesc)
        if ran_room == "W":
            if self.inroom == player.inroom:
                print "A " + self.name.lower() + " bounces off to the west."
            for person in self.inroom.pinv:
                if person == self.ldesc:
                    self.inroom.pinv.remove(self.ldesc)
            self.go_w()
            self.inroom.pinv.append(self.ldesc)

    def demon_ai(self, player):
        start_ai = False
        for room in ballpit:
            if player.inroom == room:
                start_ai = True
        if start_ai is True:
            if self.inroom == player.inroom:
                self.random_move(player)
#                if self.inroom.n == player.inroom:
#                   self.throw(ball, player, n)
#                if self.inroom.e == player.inroom:
#                   self.throw(ball, player, e)
#                if self.inroom.s == player.inroom:
#                   self.throw(ball, player, s)
#                if self.inroom.w == player.inroom:
#                   self.throw(ball, player, w)
            if self.inv <= 6:
                for item in self.inroom.rinv:
                    for ball in ballz:
                        if item == ball:
                             self.get_item(item)
            else:
                    self.random_move(player)
                            

#saves data in dictionaries that are used to construct rooms and the player.
# THESE FUNCTIONS ARE CURRENTLY VERY BUGGY

def game_save(player):
    pdata = {'name': player.name, 'ldesc': player.ldesc, 'inroom': player.inroom, 'pc': player.pc, 'inventory': [], 'hp': player.hp }
    for item in player.inv:
        player.get_item(item)
    player_data = pdata
    items_data = {'item01': {}, 'item02': {}, 'item03': {}, 'item04': {}, 'item05': {}, 'item06': {}, 'item07': {}, 'item08': {}, 'item09': {}, 'item10': {}, 'item11': {}, 'item12': {}, 'item13': {}}
    rooms_data = {'room01': {}, 'room02': {}, 'room03': {}, 'room04': {}, 'room05': {}, 'room06': {}, 'room07': {}, 'room08': {}, 'room09': {}, 'room10': {}, 'room11': {}, 'room12': {}, 'room13': {}}
    for i in items:
        data = items[i].data()
        items_data[i] = data
    for r in rooms:
        data = rooms[r].data()
        rooms_data[r] = data
    f = open('save_data.pkl', 'wb')
    pickle.dump([player_data, items_data, rooms_data], f)
    f.close()
    
    print "Character '" + player.name + "' saved."
    
def game_load():
    try:
        f = open('save_data.pkl', 'rb')
        player_data, items_data, rooms_data = pickle.load(f)
        f.close()
        player1 = Player(player_data['name'], player_data['ldesc'], player_data['inroom'], player_data['pc'], player_data['inventory'], player_data['hp'])
        for i in items:
            data = items_data[i]
            items[i] = Item(data['sdesc'], data['ldesc'], data['cantake'], data['used'])
        for r in rooms:
            data = rooms_data[r]
            rooms[r] = Room(data['title'], data['rdesc'], data['rinv'], data['n'], data['e'], data['s'], data['w'])
        print "\nWelcome back, " + player1.name + "!\n"
        look(player1, 'room')
        action(player1, "")
    except IOError:
        print "No valid data present."

class Room(object):
    def __init__(self, title, rdesc, rinv, pinv, n, e, s, w):
        self.title = title #String
        self.rdesc = rdesc #String
        self.rinv = rinv # Default is [], list of items in room
        self.pinv = pinv # Default is [], list of people in room
        self.n = "" # Default is "" \/
        self.e = ""
        self.s = ""
        self.w = ""

    def data(self):
        self.data = {'title': self.title, 'rdesc': self.rdesc, 'rinv': [], 'n': self.n, 'e': self.e, 's': self.s, 'w': self.w}
        for item in self.rinv:
            self.data['rinv'].append(item)
        return self.data
            
    def add_item(self, item):
        self.rinv.append(item)

    def add_exit_n(room, exitroom):
        room.n = exitroom
    def add_exit_s(room, exitroom):
        room.s = exitroom
    def add_exit_e(room, exitroom):
        room.e = exitroom
    def add_exit_w(room, exitroom):
        room.w = exitroom

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
    

class Item(object):
    def __init__(self, sdesc, ldesc, cantake, used):
        self.sdesc = sdesc #string
        self.ldesc = ldesc #string
        self.cantake = cantake #True or False
        self.used = used #Starts at 0, int

    def data(self):
        return {'sdesc': self.sdesc, 'ldesc': self.ldesc, 'cantake': self.cantake, 'used': self.used}
 

####Below are individual item methods. 

def use_cot(self):
    if item03.used == 0:
        print "\nYou notice something under your pillow. It's a key!\n"
        room01.add_item(item05)
        self.get_item(item05)
        item03.used += 1
    if item03.used >= 1:
        print "\nYou rest on the dingy cot.\n"

Player.use_cot = types.MethodType(use_cot, None, Player)

def use_key(self):
    if self.inroom == room01:
        print "\nYou use the key to open the door.\n"
        room01.add_exit_n(room02)
        room02.add_exit_s(room01)
        room01.rinv.remove(item04)
        room01.add_item(item06)
        self.inv.remove(item05)
    else:
        pass

Player.use_key = types.MethodType(use_key, None, Player)

def use_rope(self):
    if self.inroom == room01:
        print "\nYou tie the rope to the light fixture and try to hang yourself. The rope snaps into two worthless pieces. What a waste!\n"
        self.inv.remove(item02)
        room03.add_item(item02)
    if self.inroom == room03:
        print "\nYou tie the rope to a jutting piece of rebar and try to repel down the hole to the floor below. The rope snaps and you plummet!\n"
        self.inv.remove(item02)
        self.inroom = room09
        look(self, 'room')
    else:
        pass

Player.use_rope = types.MethodType(use_rope, None, Player)
    
def use_spoon(self):
    if self.inroom == room01:
        print '\nYou sharpen the spoon into a crude shank by running it over the concrete floor for a few hours.\n'
        self.inv.remove(item01)
        self.inroom.add_item(item07)
        self.get_item(item07)
        print "\nThat was a lot of work! You're getting tired.\n"
    else:
        pass
    
Player.use_spoon = types.MethodType(use_spoon, None, Player)

def action(player, act):
    if act == "" or act is None:
        act = str((raw_input(str(player.hp) + "hp>"))).lower()
    pact = act.split()
    if pact == []:
        pass
    if len(pact) > 3:
        print "Too many command words. Type 'help' for commands."
    if len(pact) == 1:
        if pact[0] == 'help':
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
        if pact[0] == 'leave' or pact[0] == 'quit':
            while True:
                quitprompt = raw_input("Would you like to 'SAVE' your game or just 'QUIT?'")
                if quitprompt.lower() == 'save':
                    game_save(player)
                    print "See you later, " + player.name + "! Type 'start()' to play again."
                    player.pc = "stored"
                    break
                elif quitprompt.lower() == 'quit' or quitprompt.lower() == 'leave':
                    print "See you later, " + player.name + "!"
                    print "Type 'start()' to play again."
                    player.pc = "stored"
                    break
            else:
                pass
        if pact[0] == 'save':
            game_save(player)
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
        if pact[0] == "north" or pact[0] == "n":
            player.go_n()
            player.turn(demon)
        if pact[0] == "east" or pact[0] == "e":
            player.go_e()
            player.turn(demon)
        if pact[0] == "south" or pact[0] == "s":
            player.go_s()
            player.turn(demon)
        if pact[0] == "west" or pact[0] == "w":
            player.go_w()
            player.turn(demon)
        else:
            pass
        
    if len(pact) == 2:
        if pact[0] == 'open' and pact[1] == 'door':
            print "You'll need a key to open the door."
        if pact[0] == 'get' and pact[1] == "ball":
            ret = 0
            for ball in ballz:
                if player.find_rinv(ball):
                    player.get_item(ball)
                    ret = 1
                    player.turn(demon)
                    break
            if ret == 0:
                print "There are no balls suitable for throwing here."
        if pact[0] == 'get':
            try:
                if player.find_rinv(kwords[pact[1]]):
                    player.get_item(kwords[pact[1]])
                    player.turn(demon)
            except KeyError:
                if pact[1] == 'ball':
                    pass
                else:
                    print "Get which item?"
        if pact[0] == 'drop':
            try:
                player.drop_item(kwords[pact[1]])
                player.turn(demon)
            except KeyError:
                print "Drop which item?"
        if pact[0] == 'go':
            if pact[1] == "north" or pact[1] == "n":
                player.go_n()
                player.turn(demon)
            if pact[1] == "east" or pact[1] == "e":
                player.go_e()
                player.turn(demon)
            if pact[1] == "south" or pact[1] == "s":
                player.go_s()
                player.turn(demon)
            if pact[1] == "west" or pact[1] == "w":
                player.go_w()
                player.turn(demon)
        if pact[0] == 'use':
            if pact[1] == "rope":
                if player.find_inv(item02):
                    player.use_rope()
                    player.turn(demon)
                else:
                    print "You don't have any rope."
            if pact[1] == "spoon":
                if player.find_inv(item01):
                    player.use_spoon()
                    player.turn(demon)
                else:
                    print "You don't have a spoon."
            if pact[1] == "cot":
                if player.find_rinv(item03):
                    player.use_cot()
                    player.turn(demon)
                else:
                    print "You do not see a cot here."
            if pact[1] == "key":
                if player.find_inv(item05):
                    player.use_key()
                    player.turn(demon)
                else:
                    print "You don't have a key."
        if pact[0] == 'look':
            look(player, pact[1])
        if pact[0] == 'throw':
            print "Try <throw> <object> <direction>"
        else:
            pass
        
    if len(pact) == 3:
        if pact[0] == 'use':
            print "Try just <use> <object>"
        if pact[0] == 'look':
            print "Try <look> <object>"
        if pact[0] == 'throw':
            pass

                # I'll have an if statement for the throw command here. #
    if player.pc == "stored":
        pass
    if player.pc == "pc":
        action(player, "")   

item01 = Item("a stainless steel spoon", "A dull metal spoon lies on the floor here.", True, 0)
item02 = Item("a long, frayed rope", "A long length of frayed rope lies on the floor here.", True, 0)
item03 = Item("a metal cot", "A metal framed cot with a stained mattress is here.", False, 0)
item04 = Item("a concrete door", "A windowless concrete door is locked and bars the way to the north.", False, 0)
item05 = Item("a worn metal key", "A worn metal key glimmers faintly on the floor.", True, 0)
item06 = Item("a concrete door", "A windowless concrete door opens to a hallway to the north.", False, 0)
item07 = Item("a crude metal shank", "A spoon that has been sharpened into a crude knife is here.", True, 0)
item08 = Item("a red plastic ball", "A red plastic ball is in the ballpit.", True, 0)
item09 = Item("a yellow plastic ball", "A yellow plastic ball is in the ballpit.", True, 0)
item10 = Item("a blue plastic ball", "A blue plastic ball is in the ballpit.", True, 0)
item11 = Item("a green plastic ball", "A green plastic ball is in the ballpit.", True, 0)
item12 = Item("a piece of pizza", "A piece of pizza has been abandoned in the ballpit.", True, 0)
item13 = Item("a smelly sock", "A smelly sock has been left in the ballpit.", True, 0) 
room01 = Room("A Prison Cell", "You are in a damp cell that is filled with the stench of unwashed human \nbodies. There are strange stains over the concrete floor. Your only light \nsource is a flickering incandescent bulb screwed within a grate covered \naluminum fixture.", [], [], "", "", "", "")
room02 = Room("A Hallway Lined with Cells", "You are in a long hallway lined with solid, windowless doors, each \napparently leading to a cell. The hallway stretches to the east and \nwest and the cell you emerged from is to the south.", [], [], "", "", "", "")
room03 = Room("East End of the Hallway", "You are at the eastern end of the cell lined hallway. The hallway leads \nto a dead end--however, it appears a large hole has been blasted in the \nmiddle of the floor here. The pit is shadowy and you cannot tell what \nlies beyond.", [], [], "", "", "", "")
room04 = Room("West End of the Hallway", "You are at the western end of the hallway. Besides the numerous cell doors \nto the north and south, there is a strange symbol on the western wall.", [], [], "", "", "", "")
room05 = Room("Northwestern corner of a Ballpit", "You are at the northwest corner of the ballpit.", [], [], "", "", "", "")              
room06 = Room("Northern side of a Ballpit", "You are at the northern side of the ballpit.", [], [], "", "", "", "")              
room07 = Room("Northeastern corner of a Ballpit", "You are at the northeast corner of the ballpit.", [], [], "", "", "", "")
room08 = Room("Western side of a Ballpit", "You are at the Western side of the ballpit.", [], [], "", "", "", "")
room09 = Room("Center of a Ballpit", "You are in the center of the Google HQ's ballpit.", [], [], "", "", "", "")
room10 = Room("Eastern side of a Ballpit", "You are at the Eastern side of the ballpit.", [], [], "", "", "", "")
room11 = Room("Southwestern corner of a Ballpit", "You are at the southwestern corner of the ballpit.", [], [], "", "", "", "")
room12 = Room("Southern side of a Ballpit", "You are at the southern side of the ballpit.", [], [], "", "", "", "")
room13 = Room("Southeastern corner of a Ballpit", "You are in the southeastern corner of a ballpit.", [], [], "", "", "", "") 
room02.add_exit_e(room03)
room03.add_exit_w(room02)
room02.add_exit_w(room04)
room04.add_exit_e(room02)
room09.add_exit_n(room06)
room06.add_exit_s(room09)
room09.add_exit_e(room10)
room10.add_exit_w(room09)
room09.add_exit_s(room12)
room12.add_exit_n(room09)
room09.add_exit_w(room08)
room08.add_exit_e(room09)
room05.add_exit_e(room06)
room06.add_exit_w(room05)
room06.add_exit_e(room07)
room07.add_exit_w(room06)
room05.add_exit_s(room08)
room08.add_exit_n(room05)
room07.add_exit_s(room10)
room10.add_exit_n(room07)
room11.add_exit_e(room12)
room12.add_exit_w(room11)
room12.add_exit_e(room13)
room13.add_exit_w(room12)
room11.add_exit_n(room08)
room08.add_exit_s(room11)
room13.add_exit_n(room10)
room10.add_exit_s(room13)
ballz = [item08, item09, item10, item11]
kwords = {"spoon": item01, "rope": item02, "cot": item03, "door": item04, "key": item05, "shank": item07, "red": item08, "yellow": item09, "blue": item10, "green": item11}
rooms = {'room01': room01, 'room02': room02, 'room03': room03, 'room04': room04, 'room05': room05, 'room06': room06, 'room07': room07, 'room08': room08, 'room09': room09, 'room10': room10, 'room11': room11, 'room12': room12, 'room13': room13}
ballpit = [room05, room06, room07, room08, room09, room10, room11, room12, room13]
items = {'item01': item01, 'item02': item02, 'item03': item03, 'item04': item04, 'item05': item05, 'item06': item06, 'item07': item07, 'item08': item08, 'item09': item09, 'item10': item10, 'item11': item11, 'item12': item12, 'item13': item13}
demon = NPC("Ballpit Demon", "A tiny demon bounces around the ballpit here.", room09, "npc", [], 10)
start()


