from sys import argv
from time import time
from kata_anagrams_weabreu import anagrams
from urllib import request

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

def run_streaming( url ):
    analyzer = anagrams.AnagramsAnalyzer()
    stream = request.urlopen( url )

    start_load_time = time()
    for line in stream:
        word = line.decode("latin-1").replace("\n", "")
        analyzer.load_word( word )

    start_time = time()
    anagrams_set = analyzer.get_anagrams()
    end_time = time()
    end_load_time = time()

    for anagram_set in anagrams_set:
        print( anagram_set )
    
    print("Set Count:", analyzer.get_set_count())
    print("Words Count:", analyzer.get_anagrams_words_count())
    print("Longest Word Set:", analyzer.get_longest_word_set())
    print("Most Words Set:", analyzer.get_most_words_set())
    print("Time:", end_time - start_time)
    print("Load Time:", end_load_time - start_load_time)

def main():
    
    words_list = ""
    url_path = argv[1]

    if not argv.__contains__("--full"):
        run_streaming( url_path )
        return

    start_load_time = time()
    with request.urlopen( url_path ) as resp:
        data: str = resp.read().decode("latin-1")
        words_list = data.splitlines()

    if argv.__contains__("--advanced"):
        run_advanced( words_list )
    else:
        run_normal( words_list )
    end_load_time = time()

    print("Load Time:", end_load_time - start_load_time)

if __name__ == "__main__":
    main()