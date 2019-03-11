import time
def getValidAnswer(question, answerText, answersList):
   print(question)
   validAnswerYet = False
   while not validAnswerYet:
       answer = input(answerText + " ")
       if answer in answersList:
           validAnswerYet = True
       else:
           print("That's not a valid answer!")
   return answer


lo = 1
hi = 100
print("Think of a number between ", lo, "to", hi)
time.sleep(10)

while (lo < hi):
   average = (lo + hi)//2
   answer = getValidAnswer("Is your number greater than "+ str(average) + "?", "yes (y) or no (n). Please select one.", ['y', 'n'])
   if answer == 'y':
       lo = average + 1
   else:
       hi = average
print("Your must be thinking of the number", lo)
