def stretcher(source):
   """ stretch out the vowels in source by repeating them based on their position.
   a vowel in the first position will appear once... a vowel in the second
          position will be repeated twice... etc.
   """
   result = ""
   for i in range(len(source)):
        c = source[i]
        if 'aeiouAEIOU'.find(c) >= 0:
           result = result + c * (i + 1)
        else:
           result = result + c
   return result

def unittest_stretcher():
   if stretcher('whoa') != 'whoooaaaa':
       print("Unit test for stretcher failed for 'whoa' ", stretcher('whoa'))
   if stretcher('abraham!') != 'abraaaahaaaaaam!':
       print("unit test for stretcher failed for 'abraham!", stretcher('abraham!'))

unittest_stretcher()


'''


def stripset(source,strip):
   result = ""
   for i in source:
       iPos = strip.find(i)
       if iPos == -1:
           result = result + i
   return result

def unittest_stripset():
   if stripset('hello', 'l') != 'heo':
       print("stripset failed for string 'hello' stripping 'l' ")
   if stripset('hello', '') != 'hello':
       print("stripset failed for string 'hello' stripping '' ")
   if stripset('hello', 'lo') != 'he':
       print("stripset failed for string 'hello' stripping 'lo' ")
   if stripset('hello', 'helo') != '':
       print("stripset failed for string 'hello' stripping 'helo' ")

unittest_stripset()

def main():
   print(stripset('hello', 'l'))
   print(stripset('hello', ''))
   print(stripset('hello', 'lo'))
   print(stripset('hello', 'helo'))

main()


def stretcher(source):
   """ stretch out the vowels in source by repeating them based on their position.
   a vowel in the first position will appear once... a vowel in the second
          position will be repeated twice... etc.
   """
   result = ""
   for i in range(len(source)):
       c = source[i]
       if 'aeiouAEIOU'.find(c) != -1:
           result = result + (c * (i + 1))
       else:
           result = result + c
   return result


def unittest_stretcher():
   if stretcher('whoa') != 'whoooaaaa':
       print("Unit test for stretcher failed for 'whoa' ", stretcher('whoa'))
   if  stretcher('abrabam!') != 'abraaaabaaaaaam!':
       print("unit test for stretcher failed for 'abrabam!", stretcher('abraham!'))

unittest_stretcher()

'''