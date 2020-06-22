 def containsDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        
        #loop through the array
        for n in nums:
            #check if the number is already been seen
            if n in numbers:
                return True #yes there's more than 1
            else:
                numbers.add(n)
        return False #no dupes found