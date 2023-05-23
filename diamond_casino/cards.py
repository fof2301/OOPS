import random
class cards():
    def __init__(self):
        suites_list=("♠","♥","♣","♦")
        self.suite=(random.choice(suites_list))
        self.number=(random.randint(0,13))

def print_card(msg1,msg2,msg3, indent=1, width=None, title=None):
    lines = (msg1,"  "+str(msg2),"    "+msg3)
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)