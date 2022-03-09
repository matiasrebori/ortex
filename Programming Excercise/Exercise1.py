import csv
from collections import Counter
import collections
import functools
import operator
import calendar

with open('2017.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    df = list(spamreader)
# extract exchange column
exchanges = [row[-1] for row in df]
# count exchanges
count_exchanges = Counter(exchanges)
# extract most common, means exchange with most transactions 
lista = list(count_exchanges.most_common(1))
print('What Exchange has had the most transactions in the file? ')
print(f'    The exchange with most transactions is: {lista[0][0]}\n')


# check if date is august 2017
def date_is_august_2017(date):
    if date[0:4] == '2017':
        if date[4:6] == '08':
            return True
    return False


# list with company and valueEUR
company_eur = [[row[2], row[27]] for row in df if date_is_august_2017(row[21])]
# sum valueEUR
combinedEUR = Counter()
for company, value in company_eur:
        combinedEUR[company] += float(value)

lista = list(combinedEUR.most_common(1))
print('In August 2017, which companyName had the highest combined valueEUR?')
print(f'    The company with highest combined valueEUR is: {lista[0][0]} with {lista[0][1]} valueEUR\n')


def date_is_2017(date):
    if date[0:4] == '2017':
        return True
    return False


print(f'For 2017, only considering transactions with tradeSignificance 3, what is the percentage of transactions per month?')
# get only months that passes condition
transactions = [row[21][4:6] for row in df if date_is_2017(row[21]) and row[-4] == '3']
# count 
transaction_per_month = Counter(transactions)
# get percentage
s = sum(transaction_per_month.values())
for k, v in transaction_per_month.items():
    pct = v * 100.0 / s
    print(calendar.month_name[int(k)], f'{round(pct)}%')