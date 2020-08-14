def main():
    loan, rate, years = read_inputs()
    r = rate / 100 /12 #interest rate
    number_of_months = years * 12 # number of months in which in the mortgage paid
    monthly_payment = mon_payment(loan, number_of_months, r)
    total_amount = total_mortgage(monthly_payment, number_of_months)
    total_interest = interest(total_amount, loan)
    table = count_individual_monthly_payments(total_amount, number_of_months, r, monthly_payment)
    header = create_header(loan, years, total_interest, monthly_payment)
    whole_table = create_table(table, header)
    print(whole_table)
    write_to_file(whole_table)

def mon_payment(loan, number_of_months, r):
    return round(loan*(r * (1 + r)**number_of_months) / ((1 + r)**number_of_months-1))

def interest(total_amount, loan):
    return total_amount - loan

def total_mortgage(monthly_payment, number_of_months):
    return monthly_payment * number_of_months


def read_inputs():
    borrow = int(input("How much do you want to borrow? "))
    rate = float(input("At what rate?: "))
    years = int(input("How many years?: "))
    return (borrow, rate, years)

def count_individual_monthly_payments(left_to_pay, number_of_months, r, monthly_payment):
    table = []
    for payment in range(1, number_of_months +1):
        monthly_interest = round(left_to_pay * r)
        principal = round(monthly_payment - monthly_interest)
        table.append((payment, monthly_interest, principal, left_to_pay))
        left_to_pay -= monthly_payment
    return table

def create_header(loan, years, total_interest, monthly_payment):
    header1 = ['Loan: %d' % loan, 'Years: %d' % years, 'Interest: %d' % total_interest,
     'Monthly Payment: %d' % monthly_payment]
    header2 = ['Payment', 'Interest', 'Principal', 'Left to Pay']
    return [header1, header2]

def columns(header):
    col = []
    for i in range(len(header[0])):
	       col.append(max(len(header[1][i]), len(header[0][i])) + 4)
    return col


def create_table(table, header):
    col = columns(header)
    formatted_table = []
    table = header + table
    for i in table:
        row = '|{:^' + str(col[0]) + '}|{:^' + str(col[1]) + '}|{:^' + str(col[2]) + '}|{:^' + str(col[3]) + '}|'
        row = row.format(*i)
        formatted_table.append(row)
    formatted_table = insert_lines(formatted_table, (0, 2, 4), col)
    return ('\n').join(formatted_table)

def insert_lines(table, rows, col, key = "="):
    width = len(max(table))
    for i in rows:
        table.insert(i, width * key)
    return table

def write_to_file(table):
    with open('mortage.txt', 'w') as file:
         file.write(table)

main()
