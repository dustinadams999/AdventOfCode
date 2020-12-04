from IPython import embed as shell
import re
import sys

f = open(sys.argv[1],'r')

reqd_flds = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
eye_colors = ['amb','blu','brn','gry','grn','hzl','oth']

passports = f.read().split('\n\n') # separate the text file into a list of passports

valid_passports = 0
for p in passports:
    p = p.replace('\n', ' ') # don't need those new lines
    keys = [i.split(':')[0] for i in p.split()] # get which fields each passport has
    vals = [i.split(':')[1] for i in p.split()] # get each field's value
    pass_dict = dict(zip(keys,vals))
    if ('byr' not in keys) or (not(1920 <= int(pass_dict['byr']) <= 2002)):
        continue

    if ('iyr' not in keys) or (not(2010 <= int(pass_dict['iyr']) <= 2020)):
        continue

    if ('eyr' not in keys) or (not(2020 <= int(pass_dict['eyr']) <= 2030)):
        continue

    if ('hgt' not in keys) or (('cm' not in pass_dict['hgt']) and ('in' not in pass_dict['hgt'])):
        continue
    else:
        num = int(pass_dict['hgt'][:-2])
        if pass_dict['hgt'][-2:] == 'cm':
            if not (150 <= num <= 193):
                continue
        else:
            if not (59 <= num <= 76):
                continue

    if ('hcl' not in keys) or (pass_dict['hcl'][0] != '#') or (not pass_dict['hcl'][1:].isalnum()):
        continue

    if ('ecl' not in keys) or (pass_dict['ecl'] not in eye_colors):
        continue

    if ('pid' not in keys) or (not(re.match('^[0-9]+$',pass_dict['pid']) and len(pass_dict['pid']) == 9)):
        continue

    valid_passports += 1

print(valid_passports)