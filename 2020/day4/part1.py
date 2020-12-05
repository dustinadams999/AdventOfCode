"""
usage: $ python part1.py <input-file>
"""
import sys

f = open(sys.argv[1],'r')

reqd_flds = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

passports = f.read().split('\n\n') # separate the text file into a list of passports

valid_passports = 0
for p in passports:
    p = p.replace('\n', ' ') # don't need those new lines
    flds = [i.split(':')[0] for i in p.split()] # get which fields each passport has
    valid = True
    for f in reqd_flds:
        if f not in flds:
            valid = False

    if valid:
        valid_passports += 1

print(valid_passports)
