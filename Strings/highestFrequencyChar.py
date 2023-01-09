#Python program to print the highest frequency character in a String.

str1 = input("Enter some text: ")

freq_dict={}

for ch in str1:
    if ch in freq_dict:
        freq_dict[ch] +=1
    else:
        freq_dict[ch] = 1

highest_freq = max(freq_dict, key=freq_dict.get)
print(f"The highest frequency character in the given string is '{highest_freq}'")