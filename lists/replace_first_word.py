def replace_first_word(word_list, target_word, replacement_word):
    result = []
    replacements = 0
    for word in word_list:
        if replacements == 0 and word == target_word:
            result.append(replacement_word)
            replacements += 1
        else:
            result.append(word)
    return result

print(
    replace_first_word(['good', 'good', 'morning', 'everyone'], 'good',
                       'bad'))

print(
    replace_first_word([], 'morning',
                         'evening'))
