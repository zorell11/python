'''
Program create a new file based input file movies.csv. The new file contain a
new column - Year, which is the movie relase date. This date is parsed from the
Title column.

Input file:
Rank,Rating,Title,No. of Reviews
1,99%,The Wizard of Oz (1939),109
2,100%,The Third Man (1949),76
...

Output file:
Rank,Rating,Title,Year,No. of Reviews
1,99%,The Wizard of Oz ,1939,109
2,100%,The Third Man ,1949,76
...
'''

import os
import csv

file_path ="C:\\Users\\zveres\\Desktop\\docx\\learning\\python\\github\\Films list"
FILE_NAME = 'movies.csv'
FILE_NAME_2 = 'movies_2.csv'


def read_films(file):
    with open(file, 'r') as fp:
        reader = csv.reader(fp)
        table = []
        for row in reader:
            table.append(row)
        return table


def update_table(table):
    table[0].insert(3, 'Year')  #header
    for row in table[1:]:
        title = row[2][:-6]
        year = row[2][-5:-1]
        row[2] = title
        row.insert(3, year)
    return table



def write_table(update_table):
    destination = os.path.join(file_path, FILE_NAME_2)
    with open(destination, 'w', newline='') as fp:
        writer = csv.writer(fp)
        for row in update_table:
            writer.writerow(row)
    return True



def add_year(path):
    source = os.path.join(file_path, FILE_NAME)
    table = read_films(source)
    updated_table = update_table(table)
    write_to_file = write_table(updated_table)


add_year(file_path)
