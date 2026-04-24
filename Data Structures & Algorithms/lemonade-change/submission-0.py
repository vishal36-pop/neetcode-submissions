class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_counter = {'5':0,'10':0,'20':0}

        for bill in bills:
            if bill == 5:
                bill_counter['5']+=1
            elif bill == 10:
                if bill_counter['5']>=1:
                    bill_counter['10']+=1
                    bill_counter['5']-=1
                else:
                    return False
            else:
                if bill_counter['5'] >=3:
                    bill_counter['5']-=3
                    bill_counter['20']+=1
                elif bill_counter['5']>=1 and bill_counter['10'] >=1:
                    bill_counter['20']+=1
                    bill_counter['5']-=1
                    bill_counter['10']-=1
                else:
                    return False
        return True
        
            


        