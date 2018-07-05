"""
utility for project 9

:author: Seongsu Yoon <sople1@snooey.net>
:license: CC0
"""


def clear():
    import os
    import sys

    if sys.platform == 'win32':
        os.system('cls')  # on windows
    else:
        os.system('clear')  # on linux / os x


if __name__ == '__main__':
    raise Exception("please run main py")
