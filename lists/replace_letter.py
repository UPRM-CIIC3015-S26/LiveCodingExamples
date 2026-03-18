def replace_letter(word, target_letter, replacement_letter):
    result = ''
    for c in word:
        if c == target_letter:
            result += replacement_letter
        else:
            result += c
    return result

print(replace_letter('Bienvenido', 'e', 'x'))  # 'Bixnvxnido'
print(replace_letter('Bienvenido', 'x', 'y'))  # 'Bienvenido'
print(replace_letter('', 'x', 'y'))  # ''
