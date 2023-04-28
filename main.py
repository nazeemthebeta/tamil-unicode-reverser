import re
import csv

def read_mapping_file(file_path):
    mapping = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(',')
            tamil_char = re.sub('/(.+)/g', '\\1', parts[0]).strip('"')
            eng_char = parts[1].strip().strip('"')
            mapping[eng_char] = tamil_char
    return mapping

def english_to_tamil(english_string, mapping):
    tamil_string = ''
    i = 0
    while i < len(english_string):
        char = english_string[i]
        next_char = english_string[i+1] if i+1 < len(english_string) else ''
        combined_char = char + next_char
        if combined_char in mapping:
            tamil_string += mapping[combined_char]
            i += 2
        elif char in mapping:
            tamil_string += mapping[char]
            i += 1
        else:
            tamil_string += char
            i += 1
    return tamil_string

if __name__ == "__main__":
    mapping_file = 'mapping.txt'  # Replace this with the path to your mapping file
    mapping = read_mapping_file(mapping_file)

    input_file_path = input("Enter the path to the input CSV file: ")
    output_file_path = input("Enter the path to the output CSV file: ")

    with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            english_input = row[0]
            tamil_output = english_to_tamil(english_input, mapping)
            writer.writerow([tamil_output])
