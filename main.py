
"""
project 9
inspired by project 9, karlian(bidulgi)

:author: SnooeyNET <sople1@snooey.net>
:license: CCO
"""
from project_9 import util, view

if __name__ == '__main__':
    util.clear()
    view.intro()

    arg = ''
    while arg == '':
        arg = input()
    print(arg)
