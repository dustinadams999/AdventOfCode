"""
usage: $ python part2.py <input-file>
"""
from IPython import embed as shell
import sys

def main():
    f = open(sys.argv[1], 'r')

    lines = [a.replace('\n', '') for a in f.readlines()]

    all_bags = {}

    for line in lines:
        independent_bag = line.split()[0] + ' ' + line.split()[1]
        if line.split()[4] == 'no': # special case
            all_bags[independent_bag] = None

        else:
            dependencies = line[line.index(line.split()[4]):]
            if ',' not in dependencies: # only one dependency
                single_dependency = dependencies.split()[1] + ' ' + dependencies.split()[2]
                val = int(dependencies.split()[0])
                if independent_bag not in all_bags.keys(): # add the independent_bag to the dict
                    all_bags[independent_bag] = [{single_dependency: val}]
                else:
                    all_bags[independent_bag].append({single_dependency: val})
            else: # loop through all following dependencies
                for dependency in dependencies.split(','):
                    dependency = dependency.strip()
                    val = int(dependency.split()[0])
                    dep = dependency.split()[1] + ' ' + dependency.split()[2]
                    if independent_bag not in all_bags.keys():
                        all_bags[independent_bag] = [{dep: val}]
                    else:
                        all_bags[independent_bag].append({dep: val})

    print('total bags: {}'.format(find_all_bags('shiny gold', all_bags) - 1))

def find_all_bags(bag, all_bags):
    if all_bags[bag] == None:
        return 1
    else:
        result = 1
        for child in all_bags[bag]:
            val = list(child.values())[0]
            child = list(child.keys())[0]
            result = result + (val * find_all_bags(child, all_bags))
            
        return result

if __name__ == '__main__':
    main()
