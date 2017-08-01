import hashlib, binascii, struct, array, os, time, sys, optparse
import scrypt

from construct import *
bits = 0x1f00ffff
print (bits % 0x01000000) * 2 ** (8*(bits//0x01000000 - 3))
