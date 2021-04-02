class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        map_hash = {1:'I', 5:'V', 10:'X',50:'L',
                    100     :   'C',
                    500     :   'D',
                    1000    :   'M',
                    4       :   'IV',
                    9       :   'IX',
                    40      :   'XL',
                    90      :   'XC',
                   400      :   'CD',
                   900      :   'CM'}
        
        result_string = "" 
        while num > 0 :
            for key in sorted(map_hash, reverse = True): 
                if key <= num:   
                    num -= key  
                    result_string += map_hash[key]
                    break
        return result_string 
        
