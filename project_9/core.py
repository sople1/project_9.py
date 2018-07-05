"""
core for project 9

:author: Seongsu Yoon <sople1@snooey.net>
:license: CC0
"""
from . import util, view


class Project9:
    _size = {
        'x': 9,
        'y': 9
    }
    _pos = {
        'x': 0,
        'y': 0
    }
    _wall_touched = False

    def __init__(self, size_x=9, size_y=9):
        self.set_size(size_x, size_y)

    def start(self):
        """
        Start screen when after __init__

        :return: void
        """
        if self.run_intro():
            continue_game = True
            while continue_game:
                continue_game = self.run_board()

    def run_intro(self):
        """
        show intro and wait until user's response

        :return: bool for next step
        """
        util.clear()

        view.intro()

        arg = ''
        while arg == '':
            arg = input()

        return True

    def run_board(self):
        """
        show board and wait until user's response

        :return: bool for next step (exit)
        """
        util.clear()

        board = self.make_board()
        view.screen(board, self._wall_touched)
        self._wall_touched = False  # init

        arg = ''
        while arg == '':
            arg = input('')

        return self._parse_arg(arg[0])

    def make_board(self):
        """
        only make board with pre-defined variables

        :return: string : board string
        """
        rows = []

        for i in range(self._size['x']):
            row = []
            for j in range(self._size['y']):
                if i == self._pos['x'] and j == self._pos['y']:
                    row.append("9")
                else:
                    row.append("0")

            rows.append(" ".join(row))

        return "\n".join(rows)

    def set_size(self, size_x, size_y):
        """
        set playground for 9

        :param size_x: size for x
        :param size_y: size for y
        :return: self
        """
        import math

        self._size = {
            'x': size_x,
            'y': size_y,
        }
        self._pos = {
            'x': math.ceil((size_x-1)/2),
            'y': math.ceil((size_y-1)/2),
        }

        return self

    def _parse_arg(self, arg):
        """
        move 9 or close

        :param arg: only one letter
        :return: bool for go or stop
        """
        arg = arg.lower()

        if arg == 'n':  # End program
            return False

        if arg == 'w':  # move up
            self._pos['x'] -= 1
        if arg == 's':  # move down
            self._pos['x'] += 1
        if arg == 'a':  # move left
            self._pos['y'] -= 1
        if arg == 'd':  # move right
            self._pos['y'] += 1

        for k in ['x', 'y']:
            if self._pos[k] < 0:
                self._pos[k] = 0
                self._wall_touched = True
            elif self._pos[k] >= self._size[k]:
                self._pos[k] = self._size[k] - 1
                self._wall_touched = True

        return True


if __name__ == '__main__':
    raise Exception("please run main py")
