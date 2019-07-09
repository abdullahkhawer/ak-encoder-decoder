#!/usr/bin/python

import math

class AKEncoderDecoder:
  def __init__(self):
    pass

  def ak_encoder(self, raw_string, pass_key):
    encoded_str = ""

    for char in raw_string:
      converted_char = ord(char)

      if converted_char >= 65 and converted_char <= 122:
        converted_char -= 64
      else:
        converted_char += 58

      converted_char = (converted_char + pass_key) * int(math.sqrt(pass_key))

      encoded_str += str(converted_char)[::-1]

      encoded_str += 'O'

    return encoded_str

  def ak_decoder(self, encoded_str, pass_key):
    decoded_str = ""

    for number in encoded_str.split('O'):
      if number is not None and number != "":
        num = int(number[::-1])

        num = (num / int(math.sqrt(pass_key))) - pass_key

        if num >= 1 and num <= 58:
          num += 64
        else:
          num -= 58

        decoded_str += chr(num)

    return decoded_str
