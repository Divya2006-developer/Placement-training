class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letterlog=[]
        digitlog=[]
        for log in logs:
            k=log.split(" ",1)
            if k[1][0].isdigit():
                digitlog.append(log)
            else:
                letterlog.append(log)
    
        letterlog.sort(key=lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0]))
        return letterlog+digitlog
   
