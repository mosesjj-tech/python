sales = 0
while sales <= 1000000:
commission = 0
for level in range(1, 4):
if level == 1:
if sales >= 5000:
commission = commission + 5000 * 0.06
else:
commission = commission + sales * 0.06

elif level == 2:
if sales > 5000
if sales >= 1000
commission = commission + 5000 * 0.08
else:
commission = commission + (sales - 5000) * 0.08
else:
if sales > 10000:
commission = commission + (sales - 10000) * 0.10
income = 5000 + commission
if income >= 30000:
break
sales = sales + 1
print("Minimum sales required: $", sales)


