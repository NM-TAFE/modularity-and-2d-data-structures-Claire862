from player import Player

class BoardError(Exception):
    """Base class for all board errors
    """
    pass

class InvalidPositionError(BoardError):
    """Called when a position requested is out of bounds
    """
    pass

class PositionOccupiedError(BoardError):
    """Called when a position requested is already occupied
    """
    pass



class Board:
    def __init__(self, size = 3) -> None:
        self.size = size
        self.grid = self._create_2d_grid()

    def _create_2d_grid(self) -> []:
        grid_2d = []
        for row in range(self.size):
            grid_2d.append([])
            for col in range(self.size):
                grid_2d[row].append(None)

        return grid_2d

    def is_full(self) -> bool:
        for row, col in range(self.size, self.size):
            if self.grid[row][col] is None:
                return False
            else:
                return True



    def is_position_occupied(self, row, col) -> bool:
        return self.grid[row][col] is not None

    def make_move(self, row, col, player) -> None:
        if 0 > row or row > self.size-1 or 0 > col or col > self.size-1:
            raise InvalidPositionError("Invalid position")
        if self.is_position_occupied(row, col):
            raise PositionOccupiedError("Position already occupied")

        self.grid[row][col] = player

    def get_winner(self) -> None | Player:
        return self._has_horizontal_winner() or self._has_vertical_winner() or self._has_diagonal_winner()


    def _has_horizontal_winner(self) -> None | Player:
        for row in self.grid:
            check = all(player == row[0] for player in row)
            if check:
                return row[0]
        return None


    def _has_vertical_winner(self) -> None | Player:
        for column in range(self.size):
            #create a list with columns players
            column_list = []
            for row in self.grid:
                column_list.append(row[column])

            #check my list
            column_check = all(player == column_list[0] for player in column_list)
            if column_check:
                return column_list[0]

        return None

    def _has_diagonal_winner(self) -> None | Player:

        # create a list with 1st diagonal players
        diagonal1_list = []
        for i in range(self.size):
            diagonal1_list.append(self.grid[i][i])

        # check my list
        diagonal1_check = all(player == diagonal1_list[0] for player in diagonal1_list)
        if diagonal1_check:
            return diagonal1_list[0]

        # create a list with 2ndt diagonal players
        diagonal2_list = []
        for i in range(self.size):
            diagonal2_list.append(self.grid[i][self.size-1-i])

        # check my list
        diagonal2_check = all(player == diagonal2_list[0] for player in diagonal2_list)
        if diagonal2_check:
            return diagonal2_list[0]

        return None
    def __str__(self) -> str:
        return '\n'.join(["[" + ', '.join(map(str, self.grid[row])) + "]" for row in range(self.size)])
