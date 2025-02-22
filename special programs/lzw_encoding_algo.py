def lzw_encode(text):
    # Initialize dictionary with single characters
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256  # Next available code in dictionary
    
    encoded_output = []
    current_string = ""

    for symbol in text:
        new_string = current_string + symbol  # Form a new sequence
        if new_string in dictionary:
            current_string = new_string
        else:
            encoded_output.append(dictionary[current_string])  # Output code for current string
            dictionary[new_string] = next_code  # Add new sequence to dictionary
            next_code += 1
            current_string = symbol  # Start new sequence

    # Output the last string
    if current_string:
        encoded_output.append(dictionary[current_string])

    return encoded_output

# Example usage
text = "ABRACADABRA"
encoded = lzw_encode(text)
print("Encoded Output:", encoded)
