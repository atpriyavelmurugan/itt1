
color_map = {
    '0': 'red',
    '1': 'blue',
    '2': 'green'
}
sequence = input("Enter the sequence (e.g., 001): ")

result = []
for i in sequence:
    if i in color_map:
        result.append(color_map[i])
    else:
        result.append(f"[Invalid: {i}]")

print(" ".join(result))
