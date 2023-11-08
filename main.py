import random

#global constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8,
}

symbol_values = {
  "A": 10,
  "B": 5,
  "C": 3,
  "D": 2,
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol_to_check != symbol:
        break
    else:
      winnings += values[symbol] * bet
      winning_lines.append(line + 1)

  return winnings, winning_lines    

#generate outcome of the slotmachine
def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count): # _ is an anonymous variable in python so we dont have unused variables when we dont care about the iteration value
      all_symbols.append(symbol)

  columns = [] #columns = [[], [], []]
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:] #copy a list so our og list doesn't change
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value) #when we choose a value we need to remove it from the list so we cant choose it again
      column.append(value)
    columns.append(column)

  return columns


def print_slot_machine(columns): #we have [[A, B, C], [A, B, C], [A, B, C]] and need to flip it vertically
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i!= len(columns) - 1:  #to not print the | after the last column
        print(column[row], end=" | ")
      else:
        print(column[row], end="")
    print()


#get input values: deposit and bet

def deposit():
  while True:
    amount = input("How much would you like to deposit? $")
    if amount.isdigit(): #check if its a valid number
      amount = int(amount) #convert to integer
      if amount > 0:
        break
      else:
        print("Amount must be greater than 0.")
    else:
      print("Please enter a valid number.")
  return amount

#get how much they want to bet and how man lines they want to bet on and then multiply amount by the number of lines
def get_number_of_lines():
  while True:
    lines = input("Enter the amount of lines to bet on (1-" + str(MAX_LINES) + "): ")
    if lines.isdigit(): #check if its a valid number
      lines = int(lines) #convert to integer
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Enter a valid numer of lines.")
    else:
      print("Please enter a valid number.")
  return lines

def get_bet():
  while True:
    bet = input("How much would you like to bet on each line? $")
    if bet.isdigit(): #check if its a valid number
      bet = int(bet) #convert to integer
      if MAX_BET >= bet >= MIN_BET:
        break
      else:
        print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
    else:
      print("Please enter a valid number.")
  return bet

def game(balance):
  lines = get_number_of_lines()
  while True:
    bet = get_bet()
    total_bet = bet * lines
    if total_bet > balance:
      print(f"You dont have enough to bet that amount, your current balance: ${balance}")
    else:
      break
  
  balance = balance - total_bet
  print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}.")

  columns = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(columns)

  winnings, winning_lines = check_winnings(columns, lines, bet, symbol_values)
  print(f"You won ${winnings}.")
  print(f"You won on lines:", *winning_lines)

  return winnings - total_bet


def main():
  balance = deposit()
  while True:
    print(f"Current balance is ${balance}")
    spin = print(input("Press enter to play (q to quit)."))
    if spin == "q":
      break
    balance += game(balance)
  print(f"You have ${balance} left")

main()


