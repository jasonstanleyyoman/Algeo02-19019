import json
def get_first_15_words_from_synopsis() :
    # Get first 15 word of all synopsis from web scrapping
    with open ("web-scrapping/synoposis.json") as file:
        all_synopsis = json.load(file)
        all_starting_word = []
        i = 0
        for synopsis in all_synopsis :
            all_starting_word.append(get_first_15_words(synopsis))
        with open ("web-scrapping/first_15_word.json", "w") as file :
            json.dump(all_starting_word,file)

def get_first_15_words (sentence) :
    # Get first 15 word of a sentence
    sentence    = sentence.split(" ")
    sentence    = [word for word in sentence if word != '']
    sentence    = [word.replace("\n","").replace("\r","") for word in sentence]
    sentence    = sentence[0:15]
    sentence    = " ".join(sentence) + "..."

    return sentence

if __name__ == "__main__" :
    get_first_15_words_from_synopsis()
