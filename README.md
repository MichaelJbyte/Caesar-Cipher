# Caesar-Cipher
Python project to make a Caesar Cipher encoder/decoder. [10/22/25]

Today I will begin my very first python project, a Caesar Cipher encoder/decoder. I would like for this program to both encrypt and decrypt text using as Caesar cipher. This project will be based off my current knowledge and will not leverage any sort of tutorial. Help will be allowed from google for topics I may not currently know. Anything I may not understand will be properly learned and noted here, alongside the process of creating the cipher program. My aim for this project is to familarize myself with self learning and accomplish a, somewhat useful, beginner project.

## What is a Caesar Cipher?

Utilizing an [article](https://www.geeksforgeeks.org/ethical-hacking/caesar-cipher-in-cryptography/) from **_geeksforgeeks.org_**, I swiftly learned all about the caesar cipher. This article overviews its history, which I will not cover. However, I will note that a Caesar cipher is an encryption method which shifts plaintext over a specified amount alphabetically. The common shift is three letters, but it can range anywhere from zero to twenty-five.

For an example, you can use the cipher with a shift of three to change the name: **"JACOB"** to **"MDFRE."**

## Process

Below any noteworthy thoughts and processes will be listed when making the cipher program. Images of the code will be provided below as well:

1. I first began by laying down the skeleton of the program with the knowledge I already knew up until a point where I was unsure. This consisted of me implementing the below code:

![picture_one](https://github.com/MichaelJbyte/Caesar-Cipher/blob/950b501fc527e2b843406527b85d9379b73e5e55/C_cipher_01.png)

2. Before moving on and creating any more pivotal parts and beginning the decoder aspect, I 



## New Topics

Any syntax which I had not known of previously and was used to help me with this project will be below. I will attempt to learn these topics and not just copy or use them simply for this project:

### Unicode:

For this project I wanted to learn about unicode to understand what I would be dealing with when using certain functions. My understanding is that unicode is simply a standard which attaches a **_unique code_** to a variety of different letters, symbols, numbers and more for multiiple languages, including python.

---

### ord() and chr() Functions:

I needed to understand these two functions because the 'ord()' function would be used for my cipher encryption.   Code Used: [Functions]()

**ord():** This function can find the Unicode Code Point (UCP) of any character in a string.
  * You cannot use a string with 2 or more characters. UCP's are only attached to single characters.
  * To convert anything longer than one character, you must use list comprehension.
  * Symbols can also hold UCP's.
**chr():** This function can find the Unicode character attached to an integer value.
  * This function reverses the 'ord()' function.

