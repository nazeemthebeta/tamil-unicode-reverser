import csv
import re
import os
from io import StringIO
import streamlit as st

def read_mapping_file():
    mapping = {}
    with open('mapping.txt', 'r', encoding='utf-8') as f:
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

def read_input_csv(uploaded_file):
    csv_file = uploaded_file.getvalue().decode('utf-8')
    csv_reader = csv.reader(StringIO(csv_file))
    english_names = [row[0] for row in csv_reader]
    return english_names


def display_output_table(output_data):
    output_data_line = output_data.split("\n")
    st.write("Tamil Unicode string:")
    for tamil_str in output_data_line:
        st.write(tamil_str)
        
def main():
    st.title("English to Tamil Transliterator")

    # Read mapping file
    mapping = read_mapping_file()

    # Get input method from user
    input_method = st.radio("Select input method:", options=["CSV file", "Manual input"])

    if input_method == "CSV file":
        # Get CSV file from user
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

        if uploaded_file is not None:
            # Read input CSV file
            english_names = read_input_csv(uploaded_file)

            # Transliterate names to Tamil
            tamil_names = [english_to_tamil(name, mapping) for name in english_names]

            # Display output table
            st.write("Tamil transliterations:")
            st.write(tamil_names)

    else:
        # Get manual input from user
        english_input = st.text_area("Enter the English transliteration:")
        if st.button("Convert"):
            tamil_output = english_to_tamil(english_input, mapping)
            display_output_table(tamil_output)

if __name__ == "__main__":
    main()
