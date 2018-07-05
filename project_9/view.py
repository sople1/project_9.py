"""
view for project 9

:author: Seongsu Yoon <sople1@snooey.net>
:license: CC0
"""


def intro():
    """
    view for intro
    print only

    :return: void
    """
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n     - 9 move project -\n\n\n\n\n\n\n\n start!\n\n - plese Any key & Enter key -", end="")


def screen(board="", is_wall=False):
    print("\n\n\n\n\n\n\n\n\n\n")

    if is_wall:
        print("-it's wall, don't move\n")
    else:
        print("\n\n")

    print(board)

    print("------------------------------------------------------")
    print(" move up -  'w'")
    print(" move down -  's'")
    print(" move right -  'd'")
    print(" move left -  'a'")
    print("   AND Enter")
    print("  End program is 'n' key", end="")

if __name__ == '__main__':
    raise Exception("please run main py")
