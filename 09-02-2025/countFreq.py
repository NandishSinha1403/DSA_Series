class Solution:
    def countFreq(self, arr, target):
        count = 0
        for i in arr:
            if i == target :
                count +=1 
        #count = arr.count(target)
        return count     
        