from sys import argv
import random
import re
import nltk
from nltk.corpus import cmudict
from nltk.probability import LidstoneProbDist

script, book = argv

e = cmudict.entries()
d = cmudict.dict()

banned_end_words = ['the', 'a', 'an', 'at', 'been', 'in', 'of', 'to', 'by', 'my',
					'too', 'not', 'and', 'but', 'or', 'than', 'then', 'no', 'o',
					'for', 'so', 'which', 'their', 'on', 'your', 'as', 'has',
					'what', 'is', 'nor']

print "importing source text..."
f = open(book)
print "reading source text..."
t = f.read()
print "tokenizing words..."
w = nltk.word_tokenize(t)


def make_word_list():
	print "making word list..."
	word_list = []
	for i in w:
		try:
			d[i.lower()]
		except KeyError:
			pass
		else:
			if i.lower() == "'s":
				pass
			elif i[-1] == ".":
				pass
			else:
				word_list.append((i.lower(), d[i.lower()][0]))
	return word_list
	
word_list = make_word_list()


def valid_words():
	print "extracting words from word list..."
	vw = []
	for (x, y) in word_list:
		vw.append(x)
	return vw
	
vw = valid_words()


def unique(s):
	print "making unique word list..."
	u = []
	for x in s:
		if x not in u:
			u.append(x)
		else:
			pass
	return u
    
word_list_u = unique(word_list)


def strip_numbers(x):
	xj = '.'.join(x)
	xl = re.split('0|1|2', xj)
	xjx = ''.join(xl)
	xlx = xjx.split('.')
	return xlx
	
	
def ends_in_vowel(pl):
	if 'A' in pl[-1:][0] or 'E' in pl[-1:][0] or \
	'I' in pl[-1:][0] or 'O' in pl[-1:][0] or \
	'U' in pl[-1:][0] or 'Y' in pl[-1:][0]:
		return True	
	else:
		return False


def contains_vowel(pl, n):
	if 'A' in pl[n][0] or 'E' in pl[n][0] or \
	'I' in pl[n][0] or 'O' in pl[n][0] or \
	'U' in pl[n][0] or 'Y' in pl[n][0]:
		return True	
	else:
		return False


def rhyme_finder(word):
	rhyming_words = []
	pron = strip_numbers(d[word][0])
	if len(pron) == 1:
		for (x, y) in word_list_u:
			ps = strip_numbers(y)
			if ps[-1] == pron[0]:
				rhyming_words.append(x)
			else:
				pass
	elif len(pron) == 2:
		if ends_in_vowel(pron):
			for (x, y) in word_list_u:
				ps = strip_numbers(y)
				if ps[-1] == pron[-1]:
					rhyming_words.append(x)
				else:
					pass
		else:
			for (x, y) in word_list_u:
				ps = strip_numbers(y)
				if ps[-2:] == pron:
					rhyming_words.append(x)
				else:
					pass
	elif len(pron) >= 3:
		if ends_in_vowel(pron):
			for (x, y) in word_list_u:
				ps = strip_numbers(y)
				if ps[-1] == pron[-1]:
					rhyming_words.append(x)
				else:
					pass
		else:
			if contains_vowel(pron, -2):
				for (x, y) in word_list_u:
					ps = strip_numbers(y)
					if ps[-2:] == pron[-2:]:
						rhyming_words.append(x)
					else:
						pass
			elif contains_vowel(pron, -3):
				for (x, y) in word_list_u:
					ps = strip_numbers(y)
					if ps[-3:] == pron[-3:]:
						rhyming_words.append(x)
					else:
						pass
			elif contains_vowel(pron, -4):
				for (x, y) in word_list_u:
					ps = strip_numbers(y)
					if ps[-4:] == pron[-4:]:
						rhyming_words.append(x)
					else:
						pass
			else:
				pass
	else:
		pass
	rw = [i for i in rhyming_words if not i == word]
	rw2 = [j for j in rw if not j in banned_end_words]
	return rw2
	

print "building content model..."
estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
content_model = nltk.NgramModel(5, vw, estimator=estimator)


def generate():
	sw1 = random.randint(0, len(vw) - 6)
	sw2 = sw1 + 6
	starting_words = vw[sw1:sw2]
	line_1 = content_model.generate(6, starting_words)
	line_1 = line_1[-6:]
	line_2 = content_model.generate(6, line_1)
	line_2 = line_2[-6:]
	line_3 = content_model.generate(5, line_2)
	line_3 = line_3[-5:]
	line_4 = content_model.generate(5, line_3)
	line_4 = line_4[-5:]
	line_5 = content_model.generate(6, line_4)
	line_5 = line_5[-6:]
	line_6 = content_model.generate(6, line_5)
	line_6 = line_6[-6:]
	line_7 = content_model.generate(5, line_6)
	line_7 = line_7[-5:]
	line_8 = content_model.generate(5, line_7)
	line_8 = line_8[-5:]
	line_9 = content_model.generate(6, line_8)
	line_9 = line_9[-6:]
	line_10 = content_model.generate(6, line_9)
	line_10 = line_10[-6:]
	line_11 = content_model.generate(5, line_10)
	line_11 = line_11[-5:]
	line_12 = content_model.generate(5, line_11)
	line_12 = line_12[-5:]
	line_13 = content_model.generate(6, line_12)
	line_13 = line_13[-6:]
	line_14 = content_model.generate(5, line_13)
	line_14 = line_14[-5:]
	lines = [line_1, line_2, line_3, line_4, line_5, line_6,
			 line_7, line_8, line_9, line_10, line_11, line_12,
			 line_13, line_14]
	return lines


def sylcount(s):
	try:
		sj = ''.join(d[s][0])
		sl = re.split('0|1|2', sj)
	except KeyError:
		return None
	else:
		return len(sl) - 1
		
		
def line_sylcount(line):
	count = 0
	for word in line:
		count += sylcount(word)
	return count


def couplet(x, y, lines):
	line_1 = lines[x]
	line_2 = lines[y]
	end_word_1 = line_1.pop()
	while end_word_1 in banned_end_words:
		end_word_1 = random.choice(vw)
	rhyming_words = rhyme_finder(end_word_1)
	while rhyming_words == []:
		end_word_1 = random.choice(vw)
		while end_word_1 in banned_end_words:
			end_word_1 = random.choice(vw)
		rhyming_words = rhyme_finder(end_word_1)
	end_word_2 = random.choice(rhyming_words)
	line_1.append(end_word_1)
	line_2.append(end_word_2)
	return [line_1, line_2]

	
def couplet_checker():
	lines = generate()
	c1 = couplet(0, 2, lines)
	c2 = couplet(1, 3, lines)
	c3 = couplet(4, 6, lines)
	c4 = couplet(5, 7, lines)
	c5 = couplet(8, 10, lines)
	c6 = couplet(9, 11, lines)
	c7 = couplet(12, 13, lines)
	return [c1[0], c2[0], c1[1], c2[1], c3[0], c4[0], c3[1], c4[1],
			c5[0], c6[0], c5[1], c6[1], c7[0], c7[1]]


def sonnetizer():
	s = couplet_checker()
	l1 = ' '.join(s[0])
	l2 = ' '.join(s[1])
	l3 = ' '.join(s[2])
	l4 = ' '.join(s[3])
	l5 = ' '.join(s[4])
	l6 = ' '.join(s[5])
	l7 = ' '.join(s[6])
	l8 = ' '.join(s[7])
	l9 = ' '.join(s[8])
	l10 = ' '.join(s[9])
	l11 = ' '.join(s[10])
	l12 = ' '.join(s[11])
	l13 = ' '.join(s[12])
	l14 = ' '.join(s[13])
	sonnet = [l1, l2, l3, l4, l5, l6, l7, l8, 
			  l9, l10, l11, l12, l13, l14]
	return '\n' + '\n'.join(sonnet) + '\n'


print "assembling poems..."		
for _ in range(100):
	print sonnetizer()
	
		