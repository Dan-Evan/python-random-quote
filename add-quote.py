import random

def primary():
  # print("Keep it logically awesome.")

  #Opens the text file in append mode or "edit at the mode" writes the new quote
  #and closes it at then end
  f = open("quotes.txt", 'a+')
  f.write("Be the change that you wish to see in the world.\n")
  f.close()

  print("Quote successfully added.")
if __name__== "__main__":
  primary()
