open_file = open(“CupcakeInvoices.csv")

# Number 3

for line in open_file:
  print(line)

# Number 4

for line in open_file:
  line = line.strip()
  values = line.split(',')
  print(values[2])

# Number 5

for line in open_file:
  line = line.strip()
  values = line.split(',')
  total = float(values[3]) * float(values[4])
  print(total)

# Number 6

for line in open_file:
  line = line.strip()
  values = line.split(',')
  total = int(values[3]) * float(values[4])
  total = total + (float(values[3]) * float(values[4]))
# Aditional
print(round(total, 2))

open_file.close()