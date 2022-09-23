from sys import argv
from time import time
from kata_anagrams_weabreu import anagrams

def run_normal(words_list: list[str]) -> None:
    start_time = time()
    anagrams_set, words_count = anagrams.search_anagrams( words_list )
    end_time = time()

    for anagram_set in anagrams_set:
        print(anagram_set)
    
    print("Set Count:", len(anagrams_set))
    print("Words Count:", words_count)
    print("Time:", end_time - start_time)

def run_advanced(words_list: list[str]) -> None:
    start_time = time()
    anagrams_set, words_count, longest_word_set, most_words_set = anagrams.search_anagrams_advanced( words_list )
    end_time = time()

    for anagram_set in anagrams_set:
        print(anagram_set)
    
    print("Set Count:", len(anagrams_set))
    print("Words Count:", words_count)
    print("Longest Word Set:", longest_word_set)
    print("Most Words Set:", most_words_set)
    print("Time:", end_time - start_time)

def main():
    
    words_list = ""
    file_path = argv[1]

    with open(file_path, "r") as fp:
        words_list = fp.read().splitlines()

    if len(argv) == 3 and argv[2] == "--advanced":
        run_advanced( words_list )
    else:
        run_normal( words_list )

if __name__ == "__main__":
    main()