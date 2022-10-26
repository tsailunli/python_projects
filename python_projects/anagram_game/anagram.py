"""
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
# searching = False


def main():
    searching = [False]
    print('Welcome to stanCode "Anagram Generator" (or ' + EXIT + ' to quit)')
    while True:
        s = (input('Find anagrams for: '))
        if s == EXIT:
            break
        start = time.time()
        dic = read_dictionary()
        find_anagrams(s, dic, searching)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    dic = {}
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            start_ch = line[0]
            if start_ch not in dic:
                dic[start_ch] = [line]
            else:
                dic[start_ch].append(line)
    return dic


def find_anagrams(s, dic, searching):
    s_lst = []
    index = []
    combination = []
    candidates = []
    print_out = []

    for i in range(len(s)):
        s_lst.append(s[i])
    candidates = find_anagrams_helper(s_lst, index, combination, candidates, dic, print_out)
    for candidate in candidates:
        if searching[0] is False:
            print('Searching...')
            searching[0] = True
        if has_prefix(candidate[0:1], dic):
            if candidate in dic[candidate[0]]:
                if candidate not in print_out:
                    print_out.append(candidate)
                    print(f'Found: {candidate}')
                    searching[0] = False
    print('Searching...')
    print(f'{len(print_out)} anagram(s): {print_out}')


def find_anagrams_helper(s_lst, index, combination, candidates, dic, print_out):
    for j in range(len(s_lst)):
        if j not in index:
            # choose
            combination.append(s_lst[j])
            index.append(j)
            # explore
            find_anagrams_helper(s_lst, index, combination, candidates, dic, print_out)
            # un-choose
            if len(combination) == len(s_lst):
                candidates.append(''.join(combination))
            combination.pop()
            index.pop()
    return candidates


def has_prefix(sub_s, dic):
    for word in dic[sub_s[0]]:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
