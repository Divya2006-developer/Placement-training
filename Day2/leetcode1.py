class Solution(object):
    def checkGoodInteger(self, n):
        dsumm=0
        sqsumm=0
        while n>0:
            k=n%10
            dsumm+=k
            sqsumm+=k**2
            n=n//10

        if sqsumm-dsumm >= 50:
            return True
        else:
            return False
        
