import json

def get_total_words_from_synopsis() :
    with open ("web-scrapping/synoposis.json") as file:
        all_synopsis = json.load(file)
        all_total_words = []

        for synopsis in all_synopsis :
            all_total_words.append(get_total_words(synopsis))
        with open ("web-scrapping/total_words.json", "w") as file :
            json.dump(all_total_words,file)


def get_total_words (sentence) :

    sentence = sentence.split(" ")

    sentence = [word for word in sentence if word != '']

    sentence = [word.replace("\n","").replace("\r","") for word in sentence]


    return len(sentence)

if __name__ == "__main__" :
    get_total_words_from_synopsis()
