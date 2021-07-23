import random

def primary():
  # print("Keep it logically awesome.")

  #open the text file "quotes.txt" in read mode and reads each line from
  #the start and then closes it
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #find the last index in the quotes file
  last = len(quotes) - 1

  #creates a random number and stores it in the variable "rnd"
  rnd1 = random.randint(0,last)
  rnd2 = random.randint(0,last)

#prints the quote at the selected array index determined by the number in []
  print(quotes[rnd1], quotes[rnd2])

if __name__== "__main__":
  primary()
