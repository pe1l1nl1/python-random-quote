import random
def lychee():
  print("Keep it logically awesome.")
  python3 get-guote.py
  
  f = open("quotes.txt")
  quotes = f.readlines()
  
  f.close()
  last = 13. 
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  lychee()
