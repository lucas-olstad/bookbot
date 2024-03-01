def main():
    file_contents = ""
    
    cur_file = "books/frankenstein.txt"

    with open(cur_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        letter_count = count_letters(file_contents)
        
        print(f"--- Begin report of {cur_file} ---")
        print(f"{word_count} words found in the document\n")
        print_sorted_letters(letter_count)
        print("--- End report ---")



def count_words(string):
    words = string.split()
    return len(words)

def count_letters(string):
    letters = {}
    valid_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                   "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lowered_string = string.lower()
    for letter in lowered_string:
        if letter in valid_chars:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

    return letters

def print_sorted_letters(dict):
    list_of_dicts = []

    for k in dict:
        newdict = {}
        newdict["char"] = k
        newdict["num"] = dict[k]
        list_of_dicts.append(newdict)

    list_of_dicts.sort(reverse=True, key=sort_on)

    for d in list_of_dicts:
        curr_char = d["char"]
        curr_num = d["num"]

        print(f"The '{curr_char}' character was found '{curr_num}' times")

        
def sort_on(dict):
    return dict["num"]

if __name__ == "__main__":
    main()
