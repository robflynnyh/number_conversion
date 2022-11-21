from num2words import num2words
import re
from typing import List, Dict, Any


def contains_digits(text:str) -> bool:
    return bool(re.search(r'\d', text))

def isyear(text:str) -> bool:
    if not text.isdigit():
        return False
    numtext = int(text)
    if numtext > 1500 and numtext < 2100:
        return True
    return False


def convert_numeric(text:str) -> str:
    if isyear(text):
        return num2words(text, to='year')
    return num2words(text)

def convert_word(text:str) -> str:
    if text.isdigit() or text.replace('.', '', 1).isdigit():
        return convert_numeric(text)
    # split based on digits
    # then convert each part
    # then join back together
    split_text = re.split(r'(\d+)', text)    
    new_split_text = []
    for cur_el in split_text:
        if cur_el.isdigit():
            cur_el = convert_numeric(cur_el)
            new_split_text.extend([' ', cur_el, ' ']) # add spaces
        else:
            new_split_text.append(cur_el)
    new_text = ''.join(new_split_text)
    # replace " (punctuation) with "(punctuation)"
    new_text = re.sub(r' ([,.!?])', r'\1', new_text)
    # remove double spaces
    new_text = re.sub(' +', ' ', new_text)
    return new_text
    

def convert_doc(text:str) -> str:
    '''
    Converts numbers to words
    '''
    split_text = text.split(' ') # split based on spaces

    for i in range(len(split_text)):
        cur_word = split_text[i]
        if contains_digits(cur_word):
            cur_word = convert_word(cur_word)
        split_text[i] = cur_word

    return ' '.join(split_text)
