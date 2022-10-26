
import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	input_dic = {}                 # input_dic will look like --> {0:'f y c l',...}
	for i in range(4):
		user_input = input(f'{i + 1} row of letters: ').lower()
		if not check(user_input):
			print('Illegal Format')
			break
		input_dic[i] = user_input
	start = time.time()
	x_y_dic = set_x_y(input_dic)
	neighbor_dic = find_neighbor()
	search(x_y_dic, neighbor_dic, read_dictionary())
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def check(string):
	"""
	:param string: user's input
	:return: whether the input is in legal format or not
	"""
	if len(string) != 7:
		return False
	else:
		for i in range(len(string)):
			if i % 2 == 0:
				if not string[i].isalpha():
					return False
			else:
				if string[i] is not ' ':
					return False
		return True


def set_x_y(input_dic):
	x_y_dic = {}
	for key, value in input_dic.items():
		new = ''

		for i in range(len(input_dic[key])):
			if i % 2 == 0:                  # remove blank space between each character
				new += input_dic[key][i]
		for j in range(len(new)):
			x_y_dic[(j, key)] = new[j]
	return x_y_dic                          # x_y_dic looks like --> {(x,y):'ch',...}


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dic = {}
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			ch = line[0]
			if ch not in dic:
				dic[ch] = [line]
			else:
				dic[ch].append(line)
	return dic


def search(x_y_dic, neighbor_dic, dic):
	"""
	:param x_y_dic: (x,y) for each character
	:param neighbor_dic:  neighbor for each character in (x,y) format (exclude itself)
	:param dic: words which were loaded from dictionary
	"""
	start_list = []  # contains characters that has become initial character
	word_result = []  # contains words that were found from boggle
	for i in range(4):
		for j in range(4):
			start_position = (i, j)
			start_list.append(start_position)
			search_helper(x_y_dic, neighbor_dic, start_position, start_list, [start_position], dic, word_result)
	print(f'There are {len(word_result)} words in total.')


def search_helper(x_y_dic, neighbor_dic, start_position, start_list, candidate_list, dic, word_result):
	"""
	:param x_y_dic: (x,y) for each character
	:param neighbor_dic: neighbor for each character in (x,y) format (exclude itself)
	:param start_position: initial character
	:param start_list: list contains each start position
	:param candidate_list: a combination of character, which could be a existing word
	:param dic: words which were loaded from dictionary
	:param word_result: words that were found from boggle
	"""
	for ele in neighbor_dic[start_position]:
		if len(candidate_list) >= 2:
			string = ''
			for ch in candidate_list:
				string += x_y_dic[ch]
			if not has_prefix(dic, string):
				break
			if len(candidate_list) >= 4:
				if string in dic[string[0]]:
					if string not in word_result:
						word_result.append(string)
						print(f'Found: {string}')
		if ele not in candidate_list:
			candidate_list.append(ele)
			search_helper(x_y_dic, neighbor_dic, ele, start_list, candidate_list, dic, word_result)
			candidate_list.pop()


def find_neighbor():
	neighbor_dic = {}
	for x in range(4):
		for y in range(4):
			search_lst = []
			for i in range(-1, 2):
				for j in range(-1, 2):
					if 0 <= x + i < 4:
						if 0 <= y + j < 4:
							search_lst.append((x + i, y + j))
			search_lst.remove((x, y))
			neighbor_dic[(x, y)] = search_lst        # neighbor_dic looks like --> {(x,y):[(x+1,y+1),...],...}
	return neighbor_dic


def has_prefix(dic, sub_s):
	"""
	:param dic: words which were loaded from dictionary
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
