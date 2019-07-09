#!/usr/bin/python

from AKEncoderDecoder import AKEncoderDecoder
import os
import sys

pass_key = os.getenv("AK_ENCODER_DECODER_PASS_KEY", " ")
pass_key = '+'.join(str(ord(c)) for c in pass_key)
pass_key = eval(pass_key)/2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR: Invalid Number of Arguments Passed.")
        exit(1)

    code_mode = int(sys.argv[1])
    input_str = sys.argv[2]

    AKEncoderDecoder_OBJ = AKEncoderDecoder()

    print("Input String: " + input_str)

    if code_mode == 0:
        encoded_str = AKEncoderDecoder_OBJ.ak_encoder(input_str, int(pass_key))
        print("Encoded String: \"" + encoded_str + "\"")
        #decoded_str = AKEncoderDecoder_OBJ.ak_decoder(encoded_str, int(pass_key))
        #print("Decoded String: " + decoded_str)
    elif code_mode == 1:
        decoded_str = AKEncoderDecoder_OBJ.ak_decoder(input_str, int(pass_key))
        print("Decoded String: " + decoded_str)
    else:
        print("ERROR: Invalid Code Mode.")
