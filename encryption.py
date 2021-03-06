key = [1, 7, 1, 4, 1, 3, 8, 2, 7, 1, 5, 4, 1, 5, 4, 6, 6, 6, 
10, 1, 9, 10, 8, 4, 1, 3, 4, 7, 2, 5, 5, 8, 4, 8, 1, 1, 6, 1,
3, 1, 8, 3, 2, 4, 9, 1, 1, 2, 1, 7, 3, 8, 5, 2, 9, 1, 7, 2, 3, 
1, 5, 3, 1, 4]

def encrypt(text):
	global key
	final_string = ''
	for index, value in enumerate(text):
		val = chr(ord(value) + key[index])
		final_string += val
	return final_string

def decrypt(text):
	global key
	final_string = ''
	for index, value in enumerate(text):
		val = chr(ord(value) - key[index])
		final_string += val
	return final_string

def user_input():
	choice = raw_input('Would you like to encrypt or decrypt?')
	if choice == 'd':
		word = raw_input('What would you like to decrypt?')
		return decrypt(word)
	elif choice == 'e':
		word = raw_input('What would you like to encrypt?')
		return encrypt(word)
	else:
		return "I didn't understand that... sorry."

if __name__ == ("__main__"):
	print user_input()