class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=digits[::-1] #reversing the array
        carry_1, i = 1 ,0   #i for position 
        
        
        while carry_1:
            if i < len(digits): #if i in bounds then we wil increment
                
                if digits[i]==9:
                    digits[i]=0
                    
                else:
                    digits[i] +=1
                    carry_1=0
                
            else:
                #out of bounds add aother element (appened)
                digits.append(1)
                carry_1=0
            
            i+=1 #increment our index
            
            
        return digits[::-1] # undo the reversing of the list 