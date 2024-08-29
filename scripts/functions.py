import json
import numpy as np
from copy import deepcopy
import pickle

def unpack(data):
    '''chooses the last level of the tree'''
    do = True
    data_temp = data
    while do:
        try: 
            data_temp = data_temp['children']
        except:
            if type(data_temp) == list:
                data_temp = [unpack(branch) for branch in data_temp]
            do = False
    return data_temp

def extract(data):
    ''' make a list out of dictionary values 'name' '''
    vals = []
    for d in data:
        if type(d) == dict:
            vals.append(d['name'])
        if type(d) == list:
            vals.append([i for i in extract(d)])
    return vals

def flatten_list(lst):
    '''flattens nested list'''
    out = []
    for l in lst:
        if type(l) == list:
            temp = flatten_list(l)
            for t in temp:
                out.append(t)
        else:
            out.append(l)
    return out


def save_dict_as_json(d, filename, path):
    '''
    filename without json
    2-level dict, child can be converted to a list
    '''
    d_new = {}
    for key in d:
        if type(d[key]) != str: 
            d_new[key] = list(d[key])
        else:
            d_new[key] = d[key]
        
    with open(path+filename+'.json', 'w') as fp:
        json.dump(d_new, fp)
        
    return d_new

def produce_complementary_strain(strain):
    compl = {'A': 'T', 'T': 'A', 'C':'G', 'G':'C'}
    strain = [compl[base] for base in list(strain)]
    return ''.join(strain)

#convert roman to decimal
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
 
def romanToDecimal(str):
    res = 0
    i = 0
 
    while (i < len(str)):
 
        # Getting value of symbol s[i]
        s1 = value(str[i])
 
        if (i + 1 < len(str)):
 
            # Getting value of symbol s[i + 1]
            s2 = value(str[i + 1])
 
            # Comparing both values
            if (s1 >= s2):
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
 
    return res

def decimalToRoman(number):
    numerals={1:"I", 4:"IV", 5:"V", 9: "IX", 10:"X", 40:"XL", 50:"L",
              90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
    result=""
    for value, numeral in sorted(numerals.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
    return result

def df_argmax(df):
    '''returns the coordinates (index and column) of the maximum element in the dataframe'''
    idx = np.unravel_index(np.argmax(df), df.shape)
    if len(df.shape) == 2:
        return df.index[idx[0]], df.columns[idx[1]]
    if len(df.shape) == 1:
        return df.index[idx[0]]

def df_argmin(df):
    idx = np.unravel_index(np.argmin(df), df.shape)
    if len(df.shape) == 2:
        return df.index[idx[0]], df.columns[idx[1]]
    if len(df.shape) == 1:
        return df.index[idx[0]]