import serial
import time

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

# set up the serial line
ser = serial.Serial('COM4', 9600)
time.sleep(2)

# Read and record the data
data =[] # empty list to store the data
indice_matrice = 0

while (1):
    b = ser.readline()         # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip()  # remove \n and \r

    try:
        flt = float(string)
    except:
        flt = 0.0
   #print(flt)
    if flt == 1:
        timein = time.time()
        while flt == 1.0:
            b = ser.readline()
            string_n = b.decode()  # decode byte string into Unicode
            string = string_n.rstrip() # remove \n and \r
            try:
                flt = float(string)
            except:
                flt = 0.0
        timeout = time.time()
        dif = timeout - timein
        if dif < 0.2:
            data.append(0)
        if dif > 0.2:
            data.append(1)

    else:
        timein = time.time()
        while flt == 0.0:
            b = ser.readline()
            string_n = b.decode()  # decode byte string into Unicode
            string = string_n.rstrip() # remove \n and \r
            try:
                flt = float(string)
            except:
                flt = 0.0
        timeout = time.time()
        dif = timeout - timein
        if 2 < dif < 10:
            data.append(3)
            print(data)

        if dif > 10:
            result = ""
            tmp = ""
            for i in data:
                if i == 3:
                        #addToResult = list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(tmp)]
                    addToResult = addToResult+ MORSE_CODE_DICT.get(data)


                    result += addToResult
                    tmp = ""
                else:
                    tmp += str(i)
            print(result)



           # for i in data:
            #    ser.write([i])
             #   time.sleep(0.5)

ser.close()
