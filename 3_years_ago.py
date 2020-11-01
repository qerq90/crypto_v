def shifr(text,kluch,L):
	spisok_grup1 = list(text)
	kod_symbol = ''
	i = 0
	x = 0
	spisok_grup1 = [i + j for i,j in zip(spisok_grup1[::2], spisok_grup1[1::2])]
	for char in kluch:
		if char != '!':
			kod_symbol = kod_symbol + char
		else:	
			spisok_grup = spisok_grup1[i::L]
			for element in spisok_grup:
				c = i + (L * x)
				if i != 0 or i != 6 and i != 10 and i != 15 and i != 18 and i != 27:	
					spisok_grup1[c] = chr(int(str(element), 16) ^ int(str(kod_symbol)))
				x = x + 1
			x = 0
			kod_symbol = ''
			i = i + 1
	return spisok_grup1




def kluch(text,L):
	i = 0
	s = 0
	maximum_s = 0
	alfavit = 'ETAOINSHRDLCUMWFGYPBVKXJQZabcdefghijklmnopqrstuvwxyz '
	alf = ' etaoinshrdlcumwfgypbvkxjqz.'
	sum1 = 0
	max1 = 0
	kluch = ''
	kluch_symbol = '101'
	max_element = ''
	spisok_grup1 = list(text)
	spisok_grup1 = [i + j for i,j in zip(spisok_grup1[::2], spisok_grup1[1::2])]
	while i < L:
		spisok_grup = spisok_grup1[i::L]
		for element in spisok_grup:
			for char in spisok_grup:
				if element == char:
					sum1 = sum1 + 1
			if sum1 > max1:
				max1 = sum1
				max_element = element
		for symbol in alf:
			samii_chastii = ord(symbol)
			kluch_symbol_prov = samii_chastii ^ int(max_element, 16)
			for element in spisok_grup:
				rezult = int(element, 16) ^ kluch_symbol_prov
				if chr(rezult) in alfavit:
					s = s + 1
				else:
					s = -1
					break
			if(s > maximum_s):
				maximum_s = s
				kluch_symbol = kluch_symbol_prov
			s = 0
		i = i + 1
		maximum_s = 0
		kluch = kluch + str(kluch_symbol) + '!'
	return kluch

		



def index_razb(text,L):
	prov = []
	sum = 0
	index = 0
	k = 0
	i = 0
	spisok_grup = list(text)
	spisok_grup = [i + j for i,j in zip(spisok_grup[::2], spisok_grup[1::2])]
	spisok_grup = spisok_grup[::L]
	for symbol in spisok_grup:
		if symbol in prov:
			symbol = ''
		else:
			prov.append(symbol)
			for char in spisok_grup:
				if symbol == char:
					sum = sum + 1
		index_symbol = (sum *(sum - 1))/(len(spisok_grup)*(len(spisok_grup) - 1))
		index = index + index_symbol
		sum = 0
	return index

def main():
	shifr_text = "edd29e21b737ee4daf2769fd52f150a8c53bf3a4966b485ec07b664bd5d174e7c2ca688d37fb49bd667fe01ee011aec569e1a5d82a59438f7f785fc8c07bfbcf8f219d62fd53bd2864ae02f550b08072e1eac2655d0cdc6e6958dec07bf8cf8f6fde64e74ead2a74ae05fc11b3c57ee6eac2650d48c02b7e42d2c76ae6879e699779e401ac2e75f752ea59b1d577f6ead0654140c07c2a42d2d97be1c89e219179ea01bb2774eb06b958ad8079f7bec26f5f0cdb636b449bfd74e6878b729537e647f83278eb00fc11b7d33be1a5db6f0d41c6787e4bd0d17b"
	i = 5
	max_index = 0
	while i <= 15:
		a = index_razb(shifr_text,i)
		if a > max_index:
			max_index = a
			dlina_klucha = i
		i = i + 1
	index = kluch(shifr_text,31)
	print(index)
	rasshifr = shifr(shifr_text,index,31)
	rasshifr = ''.join(rasshifr)
	i = 0
	print(rasshifr)





if __name__ == '__main__':
		main()