l = "hellooo"

frequency = {}
highest_frequency_chr = l[0]
frequency_count = 0
for i in l:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

highest_frequency = 0
highest_frequency_chr = ''
for chr, frequency_count in frequency.items():
    if frequency_count > highest_frequency:
        highest_frequency_chr = chr
        highest_frequency = frequency_count

print(f"highest_frequency_chr:{highest_frequency_chr},highest_frequency:{highest_frequency}")


