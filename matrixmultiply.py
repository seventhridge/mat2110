

def mult(a,b):
    # first build empty result
    c = []
    for row in range(len(a)):
        rowlist = []
        for col in range(len(b[0])):
            rowlist.append(0)
        c.append(rowlist)
    # now multiply
    for crow in range(len(c)):
        for ccol in range(len(c[crow])):
            sum = 0 # accumulate sum
            for i in range(len(a[crow])):
                # add to sum the number we get by
                #   multiplying a at row crow, column i
                #   by b on row i and column ccol
                sum = sum + a[crow][i] * b[i][ccol]
            # now that we have the sum store it in c
            c[crow][ccol] = sum
    return c



def mult(a,b):
   # first build empty result
   c = []
   for row in range(len(a)):
       rowlist = []
       for col in range(len(b[0])):
           rowlist.append(0)
       c.append(rowlist)
   # now multiply
   for crow in range(len(c)):
       for ccol in range(len(c[crow])):
           sum = 0 # accumulate sum
           for i in range(len(a[crow])):
               # add to sum the number we get by
               #   multiplying a at row crow, column i
               #   by b on row i and column ccol
               sum = sum + a[crow][i] * b[i][ccol]
           # now that we have the sum store it in c
           c[crow][ccol] = sum
   return c

