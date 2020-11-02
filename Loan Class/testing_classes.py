from loan_class_attributes import Loan
from loan_class_attributes import *


Lisa_Car = Loan(5000,.0859/12,"Lisa_Car")
print(Lisa_Car.interest_rate)
print(get_payments(Lisa_Car))
print('test')