class Solution:
    def intToRoman(self, num: int) -> str:
        ones={0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
        tens={0:'',1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
        hunds={0:'',1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}
        thous={0:'',1:'M',2:'MM',3:'MMM',4:'MMMM',5:'MMMMM',6:'MMMMMM',7:'MMMMMMM',8:'MMMMMMMM',9:'MMMMMMMMM'}
        rom={1:ones,2:tens,3:hunds,4:thous}
        digit=[int(x) for x in str(num)]
        level=len(digit)
        romans=""
        for i in range(level,0, -1):
            a=digit[level-i]
            romans=romans+rom[i][a]
        return romans

sol=Solution()
print(sol.intToRoman(3749))