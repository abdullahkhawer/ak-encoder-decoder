# AK Encoder Decoder v1.0

-   Founder: Abdullah Khawer (LinkedIn: https://www.linkedin.com/in/abdullah-khawer/)

## Introduction

AK Encoder Decoder is a Python based executable is used for compression and decompression of texts and secrets.
It works both in Linux and Windows.
Kindly use it and give suggestions for improvements.

## Prerequisites

-   Python 2.7+ Installed
-   Pass code used by AK Encoder Decoder is stored in an environment variables. It should be a string. String can have alphabets numbers and special characters. Recommended length is 13 characters to avoid code cracking via brute force attack.
    To set pass code in Linux via Terminal:
    Syntax:
    ```console
    $ export AK_ENCODER_DECODER_PASS_KEY="<integer_string>"
    ```
    Example:
    ```console
    $ export AK_ENCODER_DECODER_PASS_KEY="ABC@123"
    ```
    To set pass code in Windows via CMD:
    Syntax:
    ```console
    > set AK_ENCODER_DECODER_PASS_KEY="<integer_string>"
    ```
    Example:
    ```console
    > set AK_ENCODER_DECODER_PASS_KEY=ABC@123
    ```

### Warning: Share the pass code with whom you want to decode it.

## Usage Notes

-   To encode a string in Linux via Terminal:
    Syntax:
    ```console
    $ ./akencoderdecoder 0 <string>
    ```
    Example:
    ```console
    $ ./akencoderdecoder 0 "Hello World!"
    ```
-   To encode a string in Windows via CMD:
    Syntax:
    ```console
    > akencoderdecoder.exe 0 <string>
    ```
    Example:
    ```console
    > akencoderdecoder.exe 0 "Hello World!"
    ```

-   To decode a string in Linux via Terminal:
    Syntax:
    ```console
    $ ./akencoderdecoder 1 <encoded-string>
    ```
    Example:
    ```console
    $ ./akencoderdecoder 1 "12O7O8O2"
    ```
-   To decode a string in Windows via CMD:
    Syntax:
    ```console
    > akencoderdecoder.exe 1 <encoded_string>
    ```
    Example:
    ```console
    > akencoderdecoder.exe "12O7O8O2"
    ```
