import random
import string
import csv
import hashlib
import time

def generate_string(start_letter):
    remaining_letters = list(string.ascii_uppercase)
    remaining_letters.remove(start_letter)

    # Exclude Z as it's not used in MILSTD for DRYAD    
    if 'Z' in remaining_letters:
        remaining_letters.remove('Z')
    
    random.shuffle(remaining_letters)
    #  A-Y only    
    random_letters = remaining_letters[:24]

    # Randomize Start Letter into Random_Letters  
    random_position = random.randint(0, 24)
    random_letters.insert(random_position, start_letter)

    # Row headers A-Y   
    return f"{start_letter},{','.join(random_letters)}"

# strings excluding 'Z' because of MILSTD requirement
strings = [generate_string(letter) for letter in string.ascii_uppercase if letter != 'Z']

# MD5 hash of current timestamp for unique filenames
md5_hash = hashlib.md5(str(time.time()).encode()).hexdigest()
csv_filename = f'{md5_hash}.csv'

# Write to a CSV file
with open(csv_filename, mode='w', newline='') as file:
    for s in strings:
        file.write(s + '\n')

print(f"Wrote '{csv_filename}'")

