**Tamil-Unicode-Reverser**

This Python script is designed to convert between Tamil Unicode and English transliteration using a provided mapping file. It supports two functionalities:

 1. Converting Tamil Unicode strings to their corresponding English
    transliteration.
 2. Reversing the operation by converting English transliteration back
    to Tamil Unicode.

The script reads a mapping file containing character mappings between Tamil and English characters, and the accuracy and quality of the conversion depend on the completeness and correctness of the character mappings provided in the mapping file.

**Usage**

 To use the script, follow these steps:
 - Prepare a mapping file with the Tamil to English character mappings
   in the following format:

       /sr/g, "ஸ்ரீ"
       /xau/g, "க்ஷௌ"

 - Replace 'mapping.txt' in the script with the correct path to your mapping file. 
 - Run the script, and enter the Tamil Unicode or English transliteration when prompted. The script will output the converted string based on the provided mapping.

Please note that the conversion quality from English transliteration back to Tamil Unicode might not be perfect, as some information might be lost during the initial conversion. The accuracy will depend on the quality and completeness of the provided mappings in the mapping file.
