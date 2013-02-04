# -*- coding: utf-8 -*-
# ^^^^^ The above is a magic comment to make unicode work.
COLORS = {
    'ENDC':0,  # RESET COLOR
    'DARK_RED':31,
    'RED':91,
    'RED_BG':41,
    'YELLOW':93,
    'YELLOW_BG':43,
    'BLUE':94,
    'BLUE_BG':44,
    'PURPLE':95,
    'MAGENTA_BG':45,
    'AUQA':96,
    'CYAN_BG':46,
    'GREEN':92,
    'GREEN_BG':42,
    'BLACK':30,
}

def termcode(num):
    return '\033[%sm'%num

def colorstr(astr, color):
    return termcode(COLORS[color])+astr+termcode(COLORS['ENDC'])
HEART = "♥"
DIAMOND = "♦"
SPADE = "♠"
CLUB = "♣"
print colorstr("A" + HEART, "RED")
