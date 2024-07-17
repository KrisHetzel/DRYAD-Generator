# KTV 1400D DRYAD Cipher Sheet Generator

This Python script generates a KTV 1400D DRYAD Cipher Sheet, creating 25 rows of unique, randomly positioned letters (A-Y). Each row is prefixed with a header letter, consecutively from A-Z.

The generated Cipher Sheet is saved to a CSV file in the current working directory. The filename is randomly generated using an MD5 timestamp to avoid conflicts when generating multiple sheets simultaneously.

## Features

- Generates 25 rows of unique, randomly positioned A-Y letters.
- Includes headers for each row, consecutively from A-Y.
- Saves the Cipher Sheet to a CSV file with a unique, randomly generated name.

![Screenshot](https://github.com/user-attachments/assets/d34e3a5c-0b07-4e88-adda-a1600009092d)

## Using a DRYAD Cipher Sheet for Identity Auentication

DRYAD Cipher Sheets are utilized for two main purposes: authentication and rapid encryption. 
As such, they are essential for validating the identity of another individual, confirming the authenticity of a message, and quickly encoding text in situations such as unencrypted radio transmissions, or written messages suspetable to snooping.

Only individuals who share the same Cipher Sheet can authenticate their identities to eachother or encrypt/decrypt a message. 
This ensures that you are communicating with the authentic party as they have authenticated.
1. Generate a Cipher Sheet.
2. Share the Cipher Sheet with your party.
3. Choose a letter from the left-hand column of the Cipher Sheet.
4. Choose another letter from the same row as the selected letter in the left-hand column.
5. During authentication, state the two chosen letters (challenge letters).
6. The other individual will look at the Cipher Sheet, find the row of the first letter, and within that row, locate the second challenge letter.
7. The other individual will then recite the letter directly BENEATH the second challenge letter.
8. This response confirms the authenticity of the other individual.

## Using a DRYAD Cipher Sheet for Text Encryption

![cypher](https://github.com/user-attachments/assets/c4dd71f4-37c2-407e-a8c8-b07c817f2a5c)

Messages can be quickly encrypted, letter by letter, or number by number, using a DRYAD Cipher Sheet by refering to the Letters and Number Groups at the top of a DRYAD Cipher Sheet. This method ensures the concealment of sensitive messages, which can only be decrypted by other parties with the same cipher sheet.

1. Generate a Cipher Sheet.
2. Share the Cipher Sheet with your party.
3. Choose a letter from the left-hand column of the Cipher Sheet.
4. From the same row as the chosen letter, select another letter.
   - These two letters are your ID Letters.
5. Identify the letter directly to the RIGHT of your second ID Letter.
   - This is your SET Letter.
6. Locate the row corresponding to the SET Letter on the Cipher Sheet.
7. Encrypt your message by replacing each letter of the plaintext (Clear Text letters) with the corresponding letter from the SET Letter's Row.
8. Communicate the ID Letters and the resulting ciphertext to the other individual.
9. The other individual identifies the SET row using the ID Letters and decrypts the message accordingly.

As an example, if one wanted to encrypt and communicate the word "Hey":

They would state: "SET Alpha Papa.  Quebec X-Ray Hotel."

1. Go to the "Alpha" row.
2. Find the "Papa" letter within the "Alpha" row.
3. Choose the letter immediately to the RIGHT of "Papa," which is Bravo in this example.
4. Refer to the "Bravo" row in your Cipher sheet.
5. Decrypt "Quebec" as "Hotel," "X-Ray" as "Echo," and "Hotel" as "Yankee."
