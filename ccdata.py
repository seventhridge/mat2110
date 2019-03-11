import re

infile = "ccdata-raw.txt"
outfile= "ccdata.txt"


def formatDate(d):
    """
    calcuate date as Mmm dd, YYYY  from Month D, YYYY
    """
    try:
        parts = d.replace(',',' ').split()
        months = ["jan", "feb", 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct','nov', 'dec']
        month = months.index(parts[0][0:3].lower()) + 1
        day = int(parts[1])
        year = int(parts[2])
        return "{:04d}-{:02d}-{:02d}".format(year,month,day)
    except:
        print("Not a date but looking for one: ", d)
        return None


def getCategory(line):
    mappings = {
        'INGLES MARKET;PUBLIX':       'Grocery',
        "SAM'S":        'Grocery',
        'LTYGHOLISTI':  'Grocery',
        'HARRIS TEETER':   'Grocery',
        'I MARKET':   'Grocery',
        'EARTH FARE':   'Grocery',
        'HOPEY': 'Grocery',
        'TRADER JOE': 'Grocery',

        'REPUBLIC WIRELESS':    'Utility',
        'NETFLIX':              'Utility',

        'SIGMA TAU HEALTH;CLINIC;ALTERNATIVE CL': 'Medical',
        'B & B':            'Medical',
        'CVS':            'Medical',
        'THOMAS COWAN':     'Medical',
        'SIGMA TAU': 'Medical',
        'PEOPLES ACU': 'Medical',
        'CAROLINAMOUNTAIN': 'Medical', # Gastro
        'WALGREENS':    'Medical',

        'CITGO;Circle K;Pilot;Gas':    'Gas',
        'SHELL':    'Gas',
        'QT': 'Gas',
        'EXXON': 'Gas',  'SPEEDWAY': 'Gas', 'SUNOCO': 'Gas',

        'WWC DINING;WESTVILLE;DARK CITY':   'Dining',
        'MAMACITA;ASIAN EATERY;EL QUE PASA':     'Dining',
        '67 BILTMORE':  'Dining',
        'APOLLO FLAME': 'Dining',
        'CAFE':         'Dining',
        'NINE MILE':    'Dining',
        'PIZZA':        'Dining',
        'NO1 CHINA':    'Dining',
        'WALK - WEST ASHEVILLE':     'Dining',
        'ICHIBAN':      'Dining',
        'CANTINA':      'Dining',
        'TACO':         'Dining',
        'UNIVERSAL JOINT': 'Dining',
        'GRILL':        'Dining',
        'TRAILHEAD':    'Dining',
        'JACK OF THE WOOD': 'Dining',
        'DRAGON CHINA':  'Dining',
        'CREPERIE':      'Dining',
        'LONGHORN':          'Dining',
        'COCULA':        'Dining',
        'TODS': 'Dining',

        'MYDOMAIN':  'Misc',
        'PARKING':   'Misc',
        'RAVEN AND CRONE': 'Misc',
        'AMAZON': 'Misc',

        'AUDIBLE':  'Fun',




    }
    for keybatch in mappings:
        for key in keybatch.split(';'):
            if key in line:
                return mappings[keybatch]
    return ""


def formatTransactions(rawTs):
    """
    Data looks like this:
    November 18, 2016
    CITGO 32222235 EBLEN NC ASHEVILLE
    SOME OTHER DESCRIPTION LINE that may indicate type of purchase
    19.77

    November 18, 2016
    REPUBLIC WIRELESS 800-808-5150 NC
    31.86

    """
    newTs = []
    state = "date"
    lineNum = 0
    while lineNum < len(rawTs):
        print("line",lineNum, "state", state)
        line = rawTs[lineNum]

        #clean up the line, get rid of copy paste artifacts
        line = line.strip()

        if state == "date":
            lineNum += 1
            if "Left arrow" in line or "Down arrow" in line: line = ""

            if line: # skip blank lines and invalid dates to get to new date
                date = formatDate(line)
                if date is not None:
                    newT = date
                    state = 'payee'
        elif state == 'payee':
            lineNum += 1
            if "PAYMENT - THANK YOU" in line:
                state = "paymentAmount"
            else:
                category = getCategory(line)
                newT += "\t" + line
                state = "amountOrMorePayee"
        elif state == 'amountOrMorePayee':
            if re.match("\-*\d+\.\d\d", line) :
                state = "amount"  # do not consume line
            elif "UNLEAD" in line:
                lineNum += 1
                category = 'Gas'
            else: # extra payee details
                lineNum += 1
        elif state == "paymentAmount":
            # skip the payment amount and adding the line to the transactions
            lineNum += 1
            state = "date"
        else:  # amount
            lineNum += 1
            state = "date"
            newT += "\t" + line + "\t" + category + "\n"
            newTs.append(newT)
            print("New trans: " + newT)
    return newTs


def addNewIntoOld(newTs, oldTs):
    tDict = {}
    for oldT in oldTs:
        #thisT = '-'.join(oldT.split("\t")[0:3])  # Get rid of category
        thisTKey = '-'.join(oldT.split("\t")[0:3:2])  # Just look at date and price
        print(thisTKey)
        tDict[thisTKey] = True
    for newT in newTs:
        thisTKey = '-'.join(newT.split("\t")[0:3:2])  # get rid of category
        if thisTKey not in tDict:
            print("New: ", newT,thisTKey)
            oldTs.append(newT)
        # else:
        #     # whoa
        #     print("skip!")
        # # yeah
    oldTs.sort(reverse=True)
    return oldTs

#
# Read in old data
#
ifile = open(outfile, 'r')
transactons = ifile.readlines()
ifile.close()

#
# Read in raw data
#
ifile = open(infile, 'r')
newRawTransactions = ifile.readlines()
ifile.close()

newTransactions = formatTransactions(newRawTransactions)
transactions = addNewIntoOld(newTransactions, transactons)

#
# Write out new transaction data
# Note new transactions all have newline on end
#
ofile = open(outfile, 'w')
ofile.writelines(transactions)
ofile.close()

#ofile.writelines([ line.strip() for line in transactions])




