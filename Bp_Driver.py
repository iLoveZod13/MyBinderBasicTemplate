import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('max_colwidth',None)


class ItItem:
    wpbp_ind: 0
    wage_type: ''
    amount: 0.0
    num: 0.0
    rate: 0.0

    def __init__(self, wpbp_ind, wage_type,amount=0.0, num=0.0, rate=0.0):
        self.wpbp_ind = wpbp_ind
        self.wage_type = wage_type
        self.amount = amount
        self.num = num
        self.rate = rate



class Person:
    pernr = '00000000'
    it = []
    def __init__(self, pernr):
        self.pernr = pernr

    def __repr__(self):
        return self.pernr

    def __setattr__(self, name, value):
        if name == 'it':
            self.it.clear()
            for i in value:
                self.it.append(i.__dict__)



def get_companies(bpcw_path):
    companies = pd.read_excel(io=bpcw_path, sheet_name='Company Code')
    companies.drop([0,1,2], axis=0, inplace=True)
    companies = companies[['Co Code', 'Company Name', 'Company Name in ZH', 'Company Name in EN']]
    return companies.head(20)

def get_ent_struct(bpcw_path):
    ent_struct = pd.read_excel(io=bpcw_path, sheet_name='Enterprise Structure')
    ent_struct.drop([0], axis=0, inplace=True)
    ent_struct = ent_struct[['Company Code', 'P. Area', 'P. Area Text', 'Psub Area', 'Psub Area Text']]
    return ent_struct.head(69)

def get_emp_grp_struct(bpcw_path):
    emp_grp_struct = pd.read_excel(io=bpcw_path, sheet_name='Employee Group Structure')
    emp_grp_struct.drop([0,1],axis=0, inplace=True)
    emp_grp_struct = emp_grp_struct[['EE Group', 'EE Group Text', 'EE Sub Group', 'EE Subgroup Text', 'Country Assignment']]
    return emp_grp_struct.head(12)

def get_ratesOfPay_rule(bpcw_path):
    rates_of_pay = pd.read_excel(io=bpcw_path, sheet_name='Rates of Pay')
    return rates_of_pay[['Valuation Basis', 'Description', 'Composed by Wage Types', 'Divisor']].head(2)

def output():
    print('Bp_Driver.py has been run from backend to enable Python snippet samples in this document.')



