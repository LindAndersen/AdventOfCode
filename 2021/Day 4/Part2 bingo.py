import numpy as np

def get_inp():
    with open('input.txt', 'r') as inp:
        numbers = ''
        boards = ''
        count = 0
        for line in inp:
            if count == 0:
                numbers = np.fromstring(line, dtype=int, sep=',')
            else:
                boards += line
            count += 1
        boards = boards.replace('\n',' ')
        boards = np.fromstring(boards, dtype=int, sep=' ').reshape(500,5)

    return numbers, boards

def make_board(boards, board_no):
    board = boards[board_no*5:5+board_no*5]
    return board

def win_logic(board):
    for i in range(5):
        if np.sum(board[i,:]) == -5:
            return True
        elif np.sum(board[:,i]) == -5:
            return True
        
    return False

def calc_board(board, numbers):
    count = 0
    for n in numbers:
        count += 1
        board = np.where(board==int(n), -1, board)
        if win_logic(board) == True:
            break
        
    return count, board, n
    
def calc_score(board, n):
    pos = np.where(board == -1)
    result = np.sum(board) + len(pos[0])
    
    return result*n

def print_res(win_board, win_board_no, last_number, ite_pre, score):
    return print('Winning board:\n{}\n\nBoard_no: {}\nLast called no: {}\nIterations: {}\nScore: {}'.format(win_board, win_board_no, last_number, ite_pre, score))
    
def calc_a_board(board_no):
    numbers, boards = get_inp()
    board = make_board(boards, board_no)
    count, board, n = calc_board(board, numbers)
    score = calc_score(board, n)
    return print_res(board, board_no, n, count, score)

def main():
    board_no = 0
    ite_pre = 0
    win_board = ''
    win_board_no = 0
    last_number = -1
    numbers, boards = get_inp()
    for i in range(int(len(boards)/5)):
        board = make_board(boards, board_no)
        count, board, last_number_this = calc_board(board, numbers)
        if count > ite_pre:
            ite_pre = count
            win_board = board
            last_number = last_number_this
            win_board_no = board_no
        board_no += 1
            
    return print_res(win_board, win_board_no, last_number, ite_pre, calc_score(win_board, last_number))


if __name__ == '__main__': main()

