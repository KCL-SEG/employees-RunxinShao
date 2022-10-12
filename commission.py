


class Commission:
    def __init__(self,commissiontype):
        match commissiontype:
            case 'bonus':
            case 'contract':
            case _:
                raise 



class BonusCommission(Commission):




class ContractCommission(Commission):