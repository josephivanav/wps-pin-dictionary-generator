#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

def WPSchecksum(pin):
    '''
    Standard WPS checksum algorithm.
    @pin — A 7 digit pin to calculate the checksum for.
    Returns the checksum value.
    '''
    accum = 0
    while pin:
        accum += (3 * (pin % 10))
        pin = int(pin / 10)
        accum += (pin % 10)
        pin = int(pin / 10)
    return ((10 - accum % 10) % 10)


def genWPSPIN(n):
    return (str(n) + str(WPSchecksum(n))).zfill(8)


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        print('Usage: {} file.dic'.format(sys.argv[0]))
        exit(1)
    dictionary = open(filename, 'w', encoding='utf-8')

    for n in range(0, 10000000):
        pin = genWPSPIN(n)
        dictionary.write(pin + '\n')

    dictionary.close()
