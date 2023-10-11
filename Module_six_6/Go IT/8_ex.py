my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

values_string = ', '.join(my_dict.values())

print(values_string)

def save_applicant_data(source, output):
    values_strings = []
    with open(source, "r") as source_file:
        for line in source_file:
            values = line.strip().split(',')
            values_strings.append(', '.join(values))
        final_str = ', '.join(values_strings)
    with open(output, "w") as output_file:
        output_file.write(final_str)