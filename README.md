# Caesar-Cipher
Python project to make a Caesar Cipher encoder/decoder. [10/22/25 - 10/24/25] | **CODE USED: [CAESAR CIPHER](caesar_cipher_cracker.py)**

Today I will begin my very first python project, a Caesar Cipher encoder/decoder. I would like for this program to both encrypt and decrypt text using as Caesar cipher. This project will be based off my current knowledge and will not leverage any sort of tutorial. Help will be allowed from google for topics I may not currently know. Anything I may not understand will be properly learned and noted here, alongside the process of creating the cipher program. My aim for this project is to familarize myself with self learning and accomplish a, somewhat useful, beginner project.

## What is a Caesar Cipher?

Utilizing an **[article](https://www.geeksforgeeks.org/ethical-hacking/caesar-cipher-in-cryptography/)** from **_geeksforgeeks.org_**, I swiftly learned all about the caesar cipher. This article overviews its history, which I will not cover. However, I will note that a Caesar cipher is an encryption method which shifts plaintext over a specified amount alphabetically. The common shift is three letters, but it can range anywhere from zero to twenty-five.

For an example, you can use the cipher with a shift of three to change the name: **"JACOB"** to **"MDFRE."**

## Process

Below any noteworthy thoughts and processes will be listed when making the cipher program. Images of the code will be provided below as well:

1. I first began by laying down the skeleton of the program with the knowledge I already knew up until a point where I was unsure. This consisted of me implementing the below code:
   * The while loop ensures the program will end when I ask it too and will continue to prompt the user if any input is invalid.
   * Something to note was that I forgot the "__name__ == '__main__':" statement, a common practice and a mistake worth noting.

![picture_one](https://github.com/MichaelJbyte/Caesar-Cipher/blob/1cb6b03db605869c243ac71262f0e49b31b298e7/C_cipher_01.png)

2. Before moving on by creating any more pivotal parts and beginning the decoder aspect, I looked into how I would make the cipher method work. Using google I found a solution and studied on any ideas I did not recognize such as unicode and the 'ord()' function.

![picture_two](https://github.com/MichaelJbyte/Caesar-Cipher/blob/bfbd93daf4758cee9afdcda2d5e137a5291454c0/C_cipher_02.png)

3. After implementing this, I found the results were not shifting as they should.

   For instance, 'apple' with a shift of three would result as 'zookd,' moving each letter back by one.

   I first troubleshooted by laying out and printing the equation, realizing the potential issue may be because of the ordinal value of the 'shift' variable. For confirmation, I turned to ChatGPT and asked for a proper explanation as opposed to a fix, which confirmed my findings.

   ![picture_three](https://github.com/MichaelJbyte/Caesar-Cipher/blob/e2a1e82686edeed558f0de2f397eec30354b13dc/C_cipher_03.png)

   After fixing my code by converting the shift value to an integer and removing the improper 'ord()' function for the shift value in the equation, I was allowed to move on.

4. My next task was to develop input validation for both of my inputs, the shift and plain_text. My first attempts proved to be unsuccessful, so I once again turned to ChatGPT for explanation. Thanks to this, I learned two ways to implement input validation and used them both here for future reference.
   * I also learned two new functions/statements which would help me with the validation: _all()_ & _try/except_.
  
     ![picture_four](https://github.com/MichaelJbyte/Caesar-Cipher/blob/76ffe4b50708fc05c7503068cf5b3c2f1f647cda/C_cipher_04.png)

5.  



## New Topics

Any syntax which I had not known of previously and was used to help me with this project will be below. I will attempt to learn these topics and not just copy or use them simply for this project:

### Unicode:

For this project I wanted to learn about unicode to understand what I would be dealing with when using certain functions. My understanding is that unicode is simply a standard which attaches a **_unique code_** to a variety of different letters, symbols, numbers and more for multiiple languages, including python.

---

### ord() and chr() Functions:

I needed to understand these two functions because the 'ord()' function would be used for my cipher encryption.   Code Used: **[Functions](Unicode_func.py)**

**ord():** This function can find the Unicode Code Point (UCP) of any character in a string.
  * You cannot use a string with 2 or more characters. UCP's are only attached to single characters.
  * To convert anything longer than one character, you must use list comprehension.
  * Symbols can also hold UCP's.

**chr():** This function can find the Unicode character attached to an integer value.
  * This function reverses the 'ord()' function.
    
---

### all() Function:

...

---

### try/except Statment:

...

---
### Extra Notes:

* Thanks to some ChatGPT assitance, I learned about how my caesar_cipher() method works such as how the returned result is built incrementally, letter by letter. This helped me to understand later why an 'else' statement was necessary for a space to be kept included.

* I learned to be careful of indentations. This program requires many for and while loops and the indentations affected my code at one point. It is worth noting to go over them frequently and to let it be the first consideration when another issue arises.

* I want to clarify the equation used for the cipher for myself and any later use. I will do that here. The equation is:
  ###
      > ord("a") + (ord(char) - ord("a") + shift) % 26
  - **ord("a") =** This first part get the unicode of the first letter to set as a base. It will serve at the end to turn the alphabetical location back into an understandable unicode value.
  - **(ord(char) - ord("a")... =** This next part pretty much find the alphabetical location of each character iterated.
  - **...+ shift) % 26 =**  This last part adds/subtracts the shift for the cipher to move that alphabetical location found in the last part. the '% 26' allows the equation to wrap around the alphabet incase any unicode goes past 100.
 
* The 'strip()' function will remove any whitespace both before and after an input, killing any deadspace after clicking enter when prompted. This is an issue I learned about which affected my logic flow and would deliver incorrect results.
 
 * I learned a lot about logic flow which contributed to me learning about the 'strip()' function. With my last issue, I learned that an if-else statement will continue to go on after an else statement. This prevented my code from looping causing a small issue.

# Afterthoughts

Overall, this lab 
