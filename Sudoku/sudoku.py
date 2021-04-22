import copy

class Sudoku:
    def __init__(self, meno_suboru):
        self.tab = []
        with open(meno_suboru, 'r') as fp:
            for riadok in fp:
                r = []
                for j in riadok.strip():
                    if j != ' ':
                        try:
                            j = int(j)
                        except ValueError:
                            pass
                        r.append(j)
                self.tab.append(r)
        print("SUDOKU TASK:")
        print(self.__str__())

    def __str__(self):
        vysl = ''
        for r in self.tab:
            for j in r:
                vysl += str(j) + ' '
            vysl += '\n'
        return vysl

    def urob(self):
        item_len_0, item_len_1 = 0, 0
        tab1 = copy.deepcopy(self.tab)
        for row_number in range(0,9):
            row = self.get_row(row_number)
            for column_number in range(0,9):
                if self.tab[row_number][column_number] == '.':
                    column = self.get_column(column_number)
                    box = self.get_box(column_number, row_number)
                    possbilities = set(range(1, 10))    
                    poss = possbilities - row - column - box
                    if len(poss) == 1:
                        tab1[row_number][column_number] = poss
                    if len(poss) == 1:
                        item_len_1 += 1
                    elif len(poss) == 0:
                        item_len_0 += 1

        self.tab = tab1
        if item_len_0 > 0:
            return -1
        return item_len_1


    def get_column(self, column_number):
        return {i[column_number] for i in self.tab if i[column_number] != '.'}

    def get_row(self, row_number):
        return {i for i in self.tab[row_number] if i != '.'}

    def get_box(self, column_number, row_number):
        start_row = row_number//3 * 3
        start_column = column_number//3 * 3
        box = []
        for i in range(start_row, start_row+3):
            box.extend(self.tab[i][start_column:start_column+3])
        return set(box)

    def nahrad(self):
        for row in range(9):
            for column in range(9):
                if isinstance(self.tab[row][column], set) and len(self.tab[row][column]) == 1:
                    self.tab[row][column] = int(str(self.tab[row][column]).strip('{}'))
                elif isinstance(self.tab[row][column], set):
                    self.tab[row][column] = '.'                    


    def ries(self):
        condition = True
        while condition:
            sud = self.urob()
            self.nahrad()
            if self.pocet_nezaplnenych() == 0:
                print("SUDOKU solution:")
                print(self.__str__())
                condition = False
                #exit()
            
            if sud == -1 or sud == 0:
                print("SUDOKU doesn't have solution")
                print(self.__str__())
                condition = False
                #exit()
            
        

    def pocet_nezaplnenych(self):
        not_filled = 0
        for i in self.tab:
            not_filled += i.count('.')
        return not_filled

s1 = Sudoku('sudoku.txt')
s1.ries()

s2 = Sudoku('sudoku1.txt')
s2.ries()