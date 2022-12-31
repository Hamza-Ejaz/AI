'''Accept the electric units from user and calculate the bill according to the following rates.

Upto 100 Units     :  Rs 9.35 per unit.

Upto 200 Units      :  Rs 11.67 per unit.

Above 200 Units    :  Rs 13.99 per unit.

'''

ut = int(input("Enter number of unit(s): "))

if ut <=100:

     amt = ut* 9.35

elif ut >100 and ut <= 200:

     amt = (100*9.35) + (ut-100) *11.67

elif ut >200:

     amt = (200*11.67) + (ut - 200) *13.99

print("Total amount to pay is Rs{:.2f} ".format(amt))
