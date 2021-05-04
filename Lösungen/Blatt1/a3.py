initial_balance = input("Anfänglicher Kontostand: ")
savings_rate = input("Sparrate: ")

# cast strings to floats
initial_balance = float(initial_balance)
savings_rate = float(savings_rate)

# transform everything to integer cents instead of float euros
initial_balance = int(initial_balance * 100)
savings_rate = int(savings_rate * 100)

balance = initial_balance

# after 1st year
balance += savings_rate  # savings rate is added at start of year
interest = 0.03 * balance
balance += int(interest)
# Alternatively you can also compute the new balance by: balance = int(1.03 * balance)
# division by 100 gives results in eur
print(f"Der Kontostand nach einem Jahr beträgt: {balance/100}")

# after 2nd year
balance += savings_rate
balance *= 1.03
balance = int(balance)
print(f"Der Kontostand nach zwei Jahren beträgt: {balance/100}")

# after 3rd year
balance += savings_rate
balance *= 1.03
balance = int(balance)
print(f"Der Kontostand nach drei Jahren beträgt: {balance/100}")

# after 4th year
balance += savings_rate
balance *= 1.03
balance = int(balance)
print(f"Der Kontostand nach vier Jahren beträgt: {balance/100}")