"""Fish Tank, by Sammy
A peaceful animation of a fish tank. Press Ctrl-C to stop.
Similar to ASCIIQuarium or @EmojiAquarium, but mine is based on an
older ASCII fish tank program for DOS.
https://robobunny.com/projects/asciiquarium/html/
https://twitter.com/EmojiAquarium
View this code at https://nostarch.com/big-book-small-python-projects
Tags: extra-large, artistic, bext"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

NUM_KELP = 2 # (!) Try changing this to 10.
NUM_FISH = 10 # (!) Try changing this to 2 or 100.
NUM_BUBBLERS = 1 # (!) Try changing this to 0 or 10.
FRAMES_PER_SECOND = 4 # (!) Try changing this number to 1 or 60.
# (!) Try changing the constants to create a fish tank with only kelp,
# or only bubblers.

FISH_TYPES = [
    {'right': ['><>'],   'left': ['<><']},
    {'right': ['>||>'],  'left': ['<||<']},
    {'right': ['>))>'],  'left': ['<[[<']},
    {'right': ['>||o', '>||.'],  'left': ['o||<', '.||<']},
    {'right': ['>))o', '>)).'],  'left': ['o[[<', '.[[<']},
    {'right': ['>-==>'],  'left': ['<==-<']},
    {'right': [r'>\\>'],  'left': ['<//<']},
    {'right': ['><)))*>'], 'left': ['<*(((><']},
    {'right': ['}-[[[*>'], 'left': ['<*]]]-{']},
    {'right': [']-<)))b>'], 'left': ['<d(((>-[']},
    {'right': ['><XXX*>'], 'left': ['<*XXX><']},
    {'right': ['_.-._.-^=>', '.-._.-.^=>',
    '-._.-._^=>', '._.-._.^=>'],'left': ['<=^-._.-._', '<=^.-._.-.',
    '<=^_.-._.-', '<=^._.-._.']},
    ] # (!) Try adding your own fish to FISH_TYPES.

LONGEST_FISH_LENGTH = 10 # Longest single string in FISH_TYPES.

# The x and y positions where a fish runs into the edge of the screen:
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2

def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP
    bext.bg('black')
    bext.clear()

    # Generate the global variables:
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    # NOTE: Bubbles are drawn, but not the bubblers themselves.
    BUBBLERS = []
    for i in range(NUM_BUBBLERS):
        # Each bubbler starts at a random position.
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))

    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelpx = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {'x': kelpx, 'segments': []}
        # Generate each segment of the kelp:
        for i in range(random.randint(6, HEIGHT - 1)):
            kelp['segments'].append(random.choice(['(',')']))
        KELPS.append(kelp)















