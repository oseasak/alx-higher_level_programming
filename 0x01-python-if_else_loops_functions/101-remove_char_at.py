#!/usr/bin/python3
# Author - Asak Erhumuose
def remove_char_at(str, g):
    if g < 0:
        return (str)
    return (str[:g] + str[g+1:])
