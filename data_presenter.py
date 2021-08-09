open_file = open('CupcakeInvoices.csv')

for row in open_file:
    print(row)


# for line in open_file:
#     line = line.rstrip('\n').rstrip('\r').split(',')
#     print(line[2])

# total_invoice = 0
    
# for line in open_file:
#     line = line.rstrip('\n').rstrip('\r').split(',')

#     total_invoice += round(float(line[3]) * float(line[4]), 2)


# print(round(total_invoice, 2))