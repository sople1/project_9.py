"""
core for project 9

:author: Seongsu Yoon <sople1@snooey.net>
:license: CC0
"""
from . import util, view


class Project9:
    def __init__(self, size_x=9, size_y=9):
        self.set_size(size_x, size_y)

    def start(self):
        """
        Start screen when after __init__

        :return: void
        """
        if self.run_intro():
            self.run_game()

    def set_size(self, size_x, size_y):
        """
        set playground for 9

        :param size_x: size for x
        :param size_y: size for y
        :return: self
        """
        return self

    def run_intro(self):
        """

        :return:
        """
        util.clear()
        view.intro()

        arg = ''
        while arg == '':
            arg = input()

        return True

    def run_game(self):
        pass


if __name__ == '__main__':
    raise Exception("please run main py")
