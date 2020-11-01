def get_normal_array(text):
    return [i + j for i,j in zip(text[::2], text[1::2])] 

def get_key_length(text):
    i = 5
    new_text = text[len(text) - i:] + text[:len(text) - i]
    needed_index = 0.05

    while i:
        counter = 0
        for j in range(len(text)):
            if text[j] == new_text[j]:
                counter += 1
        index = counter / len(text)
        if index >= needed_index:
            return i

        new_text = new_text[len(text) - 1:] + new_text[:len(text) - 1]
        i += 1 

def check_char(text, checking_key_char):
    alph = 'ETAOINSHRDLCUMWFGYPBVKXJQZabcdefghijklmnopqrstuvwxyz.(),- :'
    
    for char in text:
        decrypted_char = int(char, 16) ^ checking_key_char

        if not chr(decrypted_char) in alph:
            return False

    return True

def get_char(text, char):
    most_frequent_chars = ' etaoinshrdlcumwfgypbvkxjqz.,()-'

    for frequent_char in most_frequent_chars:
        checking_key_char = int(char, 16) ^ ord(frequent_char)
        
        if check_char(text, checking_key_char): return checking_key_char

    return int(char, 16) ^ ord('e') # в теории сюда никогда не зайдет, если мы найдем правильный ключ 

def get_key_char(text):
    dict_of_chars = {}

    for char in text:
        dict_of_chars[char] = dict_of_chars.get(char, 0) + 1

    max_v = 0
    max_char = ''
    for k, v in dict_of_chars.items():
        if v > max_v:
            max_v = v
            max_char = k

    return get_char(text, max_char)

def get_frag_array(text, num_of_frag, key_length):
    return text[num_of_frag::key_length]

def get_fragms(text, key_length):
    fragms = []

    for i in range(key_length):
        fragms.append(get_frag_array(text, i, key_length))

    return fragms

def get_key(text, key_length):
    arrays = get_fragms(text, key_length)
    key = []

    for i in range(key_length):
        key_char = get_key_char(arrays[i])
        key.append(key_char)

    return key

def get_decrypted_text(text, key):
    decrypted_text = ''

    for i in range(len(text)):
        key_char = key[i % len(key)]
        char = key_char ^ int(text[i], 16)
        decrypted_text += chr(char)
    
    return decrypted_text

def decrypt_v(text):
    text = get_normal_array(text)
    key_length = get_key_length(text)
    key = get_key(text, key_length)
    text = get_decrypted_text(text, key)
    
    return text

def main():
    text = "7aff6fd04bcc1bceca2a5952b865d858d01dca86654c1bbe2bd449d61ccec16f0a52ac2bd80cc706db86795e49b665de0cc10adfc3644e5eb17f9943cb4fdcc9674f1bac6eda5ec01b8fcd64454cb12bd642c9168fd2650a4fb76e995fcc08c1c378061bbe65dd0cca018fd2624f1bbc64d758c001db86654c1bab63dc0cc80adcd56b4d5eff69dc45cb088fd5634d55ba6f970cf606c8c86b5e4ead6eca0cc81adcd22a485eff7ddc5ecc0ecdca6f0a01ff6ad755ca01ca86694b55ff68d149c6048fd2624f1ba96ad545c106dbdf2a455dff7fd149851cc6c1644b4faa79dc02"
    decrypted_text = decrypt_v(text)
    print(decrypted_text)

    return 0

if __name__ == "__main__":
    main()