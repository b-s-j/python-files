
import datetime 
import pytz
import parser
from decimal import Decimal
import delorean  

data = [
    (1000, 10),
    (2000, 17),
    (2500, 170),
    (2500, -170)
]
print('   REVENUE | PROFIT |    PERCENT')

TEMPLATE = '{revenue:>10,} | {profit:>+6} | {percent:>10.2%} '

for revenue, profit in data:
    row = TEMPLATE.format(revenue=revenue, profit=profit, percent=profit / revenue)
    print(row)
print('     ----- |  ----- |     -----\n')

value = 'VALUE'
print(f'This is the value, in curly brackets {{{value}}}')
print('\n')

INPUT_TEXT = '''    AFTER THE CLOSE OF THE SECOND QUARTER, OUR COMPANYM CASTAÑACORP HAS ACHIEVED A GROWTH IN THE REVENUE OF 7.47%. THIS IS IN LINE WITH THE OBJECTIVES FOR THE YER. THE MAIN DRIVER OF THE SALES HAS BEEN 
THE NEW PACKAGE DESIGNED UNDER THE SUPERVISION OF OUR MARKETING DEPARTMENT.
OUR EXPENSES HAS BEEN CONTAINED, INCREASING ONLY BY 0.7%, THOUGH THE BOARD
CONSIDERS IT NEEDS TO BE FURTHER REDUCED. THE EVALUATION IS SATISFACTORY.
AND THE FORECAST FOR THE NEXT QUARTER IS OPTIMISTIC. THE BOARD EXPECTS
AN INCREASE IN PROFIT OF AT LEAST 2 MILLION DOLLARS.
'''

words = INPUT_TEXT.split()
redacted = [''.join('X' if w.isdigit() else w for w in word) for word in words]