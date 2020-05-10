MORSE_CODE_DICT = { 'A':'01', 'B':'1000',
                    'C':'1010', 'D':'100', 'E':'0',
                    'F':'0010', 'G':'110', 'H':'0000',
                    'I':'00', 'J':'0111', 'K':'101',
                    'L':'0100', 'M':'11', 'N':'10',
                    'O':'111', 'P':'0110', 'Q':'1101',
                    'R':'010', 'S':'000', 'T':'1',
                    'U':'001', 'V':'0001', 'W':'011',
                    'X':'1001', 'Y':'1011', 'Z':'1100',
                    '1':'01111', '2':'00111', '3':'00011',
                    '4':'00001', '5':'00000', '6':'10000',
                    '7':'11000', '8':'11100', '9':'11110',
                    '0':'11111', ', ':'110011', '0':'010101',
                    '?':'001100', '/':'10010', '1':'100001',
                    '(':'10110', ')':'101101'}

data = [1,0,1,0,3,1,1,1,3,1,0,1,0,3,1,1,1,3,1,1,1,3] 
result = ""
tmp = ""
addToResult = ""
for i in data:
        if i == 3:
            if tmp in MORSE_CODE_DICT.values():
                list = [k for (k, val) in MORSE_CODE_DICT.items() if val == tmp]
                for k in list:
                    addToResult = addToResult + str(k)
                result = result + addToResult
            addToResult = ""
            tmp = ""
        else:
             tmp += str(i)
print(result)
