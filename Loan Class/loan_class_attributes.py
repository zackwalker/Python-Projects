import math
import numpy as np
import numpy_financial as npf
from itertools import permutations

class Loan():
    def __init__(self, principal, interest_rate, min_payment, loan_name):
        self.principal      = round(principal,2)
        self.interest_rate  = round(interest_rate,8)
        self.min_payment    = round(min_payment,2)
        self.loan_name           = loan_name

    def __repr__(self):
        return self.loan_name

class UserFinances():
    def __init__(self, fname, lname, extra_money):
        self.fname       = fname
        self.lname       = lname
        self.extra_money = extra_money

    def get_payments(self,*args):
        
        sorted_args = sorted(args, key= lambda e:e.interest_rate)
        payoff_dict = {}
        payment_dict = {}
        # extra_money = 100
        perms = dict(enumerate(permutations(sorted_args)))
        
        for perm_item in range(len(perms)):
            payoff_list = []
                    #for each perm, this grabs the current NPER.
                    #It gives the first loan the extra amount and gets NPER based off min_payment for remaining loans
            
            for i in range(len(perms[perm_item])):
                #give extra money to first loan
                if i == 0: 
                    first_payment = round(perms[perm_item][i].min_payment + self.extra_money ,2)
                #otherwise its the normal amount
                else: first_payment = perms[perm_item][i].min_payment
                payoff_list.append(
                                    math.ceil(npf.nper(
                                                    perms[perm_item][i].interest_rate,
                                                    first_payment,
                                                    -perms[perm_item][i].principal)))
                payoff_dict[perm_item] = payoff_list
            
                if i == 0:
                    payment_dict[perm_item] = [first_payment] * payoff_list[i]
                else:
                    
                    payment_dict[perm_item].extend([perms[perm_item][i].min_payment] * payoff_list[i])
            temp_add_list = []
            for payment_list in payment_dict[perm_item]:
                try:
                    if len(payment_dict[perm_item][payment_list]) > len(payment_dict[perm_item][payment_list+1]):
                        length_longer = len(payment_dict[perm_item][payment_list])
                        length_shorter = len(payment_dict[perm_item][payment_list+1])
                        difference = length_longer - length_shorter
                        longer_payoff_amt = payment_dict[perm_item][payment_list][0]
                        shorter_payoff_amt = payment_dict[perm_item][payment_list+1][0]
                        temp_add_list.append(shorter_payoff_amt + longer_payoff_amt)
                        test_vector =  temp_add_list * difference
                        payment_dict[perm_item][payment_list][(length_shorter):] = test_vector
                except:
                    pass

        return payoff_dict,payment_dict

    def payoff_optimization(avalanche_order, df,base_case_flag):
        df.columns = ["Period", "Principal", "Payment"
                    ,"Interest","Amount_Towards_Principal","Ending Balance"
                    ,"Loan_Name", "Index","Inner_Loop_Iteration"]
        # df.to_csv("C:\\Users\\zwalk\\Documents\\Desktop\\sentdex\\Loan_Payments\\final1.csv")
        number_of_loans = len(avalanche_order)
        index_match = 0
        start=0
        end= number_of_loans
        #get index for dave ramsey
        dave_ramsey_index = df[(df['Period']==0)]
        loanname = list(dave_ramsey_index.Loan_Name.values)

Lisa_Car = Loan(5000,.0859/12,333,"Lisa_Car")
WF1_Loan = Loan(8250.25,.0774/12,84.62,"WF1")
WF2_Loan = Loan(20000.29,.0649/12,191.04,"WF2")
mortgage = Loan(180000,.04/12,1331.44,"mortgage")
fnc = UserFinances('Zack','Walker',300)
print(fnc.get_payments(WF1_Loan,Lisa_Car))
def main():
    np.warnings.filterwarnings('ignore')

if __name__ == '__main__':
    main()