from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(direction,text,shift):
    cipher_text = ""
    cipher_text_index = 0
    if direction=="encode":
      for char in text:
        if char.isalpha():
          cipher_text_index = alphabet.index(char)+ shift
          if cipher_text_index > len(alphabet):
            shift_add = (shift%len(alphabet))-1
            cipher_text_index = shift_add
          cipher_text += alphabet[cipher_text_index]
        else:
          cipher_text += char
      print(f"The encoded text is {cipher_text}")
      restart = input("Do want to restart the cipher program ? yes or no: ").lower()
      if restart == "yes":
         direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
         text = input("Type your message:\n").lower()
         shift = int(input("Type the shift number:\n"))
         caesar(direction,text,shift)
      elif restart == "no":
        print("End Game")
    elif direction == "decode":
      for char in text:
        if char.isalpha():
          cipher_text_index = alphabet.index(char)- shift
          if cipher_text_index > len(alphabet):
            shift_add =  (alphabet.index(char) - shift)+len(alphabet)
            cipher_text_index = shift_add
          cipher_text += alphabet[cipher_text_index]
        else:
          cipher_text += char
      print(f"The encoded text is {cipher_text}") 
      restart = input("Do want to restart the cipher program ? yes or no:").lower()
      if restart == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction,text,shift)
      elif restart == "no":
        print("End Game")  
caesar(direction,text,shift)
