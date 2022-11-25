alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
s="""yhspqedirgvxwlukzofjambntc
rlhpndkqgjvszobmfiaeutcyxw
lizncrmbtouhdxsfapeqjvwkyg
kqlhazijdusvcrwnoxfpytebgm
gpfersjxwlokqacznutdhvbmyi
hjplgsdyxmoubnftqczawvkire
vmpeysukjtlwichdfobaqngzrx
yujmdqvtegrinhsolkwazfbpxc
mzgfoherplkuaxbicdjtnsvqwy
openjagrvqtxhdwzblcuiysfmk"""
codebooks=s.split('\n')

char_string = input()

def handle_input(char_string):
  # Check whether input is to be e or d
  if list(char_string)[0] == "e":
    # Handle encryption
    encrypted_str = ""
    for i in range(1, len(list(char_string))):
      if char_string[i] == " ":
        encrypted_str += " "
      elif char_string[i] == ",":
        encrypted_str += ","
      elif char_string[i] == ".":
        encrypted_str += "."
      elif char_string[i] == "-":
        encrypted_str += "-"
      elif char_string[i] == "@":
        encrypted_str += "@"
      else:
        row_index = (i % 10) - 1
        row = codebooks[row_index]
        char = (char_string[i]).lower()
        letter_index = alphabet.index(char)
        if char_string[i].isupper():
          encrypted_str += (row[letter_index]).upper()
        else:
          encrypted_str += (row[letter_index]).lower()
    print( encrypted_str, end="")
  else:
    # Handle decryption
    decrypted_str = ""
    for v in range(1, len(list(char_string))):
      if char_string[v] == " ":
        decrypted_str += " "
      elif char_string[v] == ",":
        decrypted_str += ","
      elif char_string[v] == ".":
        decrypted_str += "."
      elif char_string[v] == "-":
          decrypted_str += "-"
      elif char_string[v] == "@":
          decrypted_str += "@"
      else:
        row_index = (v % 10) - 1
        row = codebooks[row_index]
        char = (char_string[v]).lower()
        letter_index = row.index(char)
        letter = alphabet[letter_index]
        if char_string[v].isupper():
          decrypted_str += letter.upper()
        else:
          decrypted_str += letter.lower()
    print( decrypted_str, end="")
          
handle_input(char_string)
