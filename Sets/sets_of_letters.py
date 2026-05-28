def distinct_letters(text):
    return set(text)

print(distinct_letters("Bienvenido"))

def has_all_chars(text, chars):
    return chars.issubset(set(text))

print(has_all_chars("Bienvenido", {"B", "o"}))
print(has_all_chars("Bienvenido", {"B", "o", "x"}))

def has_some_chars(text, chars):
    return len(set(text).intersection(chars)) > 1

print(has_some_chars("Bienvenido", {"B", "o", "x"}))
print(has_some_chars("Bienvenido", {"w", "y", "x"}))
