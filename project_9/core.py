"""
core for project 9

:author: Seongsu Yoon <sople1@snooey.net>
:license: CC0
"""
from . import util, view

# 각기맞는 방향의값을 딕셔너리를 정의합니다.
move = {
    'w': [-1, 0],
    's': [1, 0],
    'a': [0, -1],
    'd': [0, 1],
}

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

        rows = [['0'] * self._size['x'] for _ in range(self._size['y'])]
        rows[self._pos['x']][self._pos['y']] = "9"
        return "\n".join([" ".join(row) for row in rows])

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

        # 각 키에맞는 값을 가져옵니다. 저장된 값 w,a,s,d 가 아니라면 target_move는 값이 없어 if문을 통과하지 못합니다.
        target_move = move.get(arg)
        if target_move:  # move up
            dx = self._pos['x'] + target_move[0]
            dy = self._pos['y'] + target_move[1]

            # target_move에서 통과하지 못햇을경우 움직이지 못하므로 기존값과 동일하여 실행될 이유가 없다고 생각합니다.
            # 또한 해당값 움직여야할 값이 다음 비교식을 통과하지 못하면 다음 이동이 벽을 넘어가거나 혹은 현재 벽을 넘어가 있다는 가정이 있습니다.
            if 0 <= dx < self._size['x'] and 0 <= dy < self._size['y']:
                self._pos['x'] = dx
                self._pos['y'] = dy
            else:
                self._wall_touched = True

        return True


if __name__ == '__main__':
    raise Exception("please run main py")
