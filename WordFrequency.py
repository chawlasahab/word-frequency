import argparse
import requests
import re
import string


URL = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&pageids={}&explaintext&format=json'


def fetch(pageId, n):
    url = URL.format(pageId)
    try:
        response = requests.get(url).json()
    except requests.exceptions.HTTPError as e:
        print(e)
    content = response['query']['pages'][str(pageId)]
    processed_text = pre_process(content['extract'])
    word_count = count_words(processed_text)
    result = sort_words_by_count(word_count)
    generate_output(content['title'], result, n)


def pre_process(data):
    text = data.lower()
    for ch in string.punctuation:
        text = text.replace(ch, ' ')
    text = re.sub(r'\d+', ' ', text)
    text = re.sub('\s+', ' ', text)
    return text.strip()


def count_words(data):
    word_dictionary = dict()
    for word in data.split():
        if len(word) > 3:
            if word in word_dictionary.keys():
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1
        else:
            continue
    return word_dictionary


def sort_words_by_count(data):
    sorted_words = sorted(data.items(), key=lambda x: x[1], reverse=True)
    return sorted_words


def generate_output(title, sorted_word_count_list, n):
    count = 0
    previous_count = 0
    output = ""
    for data in sorted_word_count_list:
        if count == n and previous_count != data[1]:
            break
        elif previous_count == data[1]:
            output += ", " + str(data[0])
        else:
            output += "\n"
            output += str(data[1]) + " " + str(data[0])
            count += 1
        previous_count = data[1]
    print(f"Title: {title}", output)


if __name__ == '__main__':
    """
    usage:
        python3 WordFrequency.py --pageid 21721040 -n 5
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--pageid", "-id", type=int, default=21721040)
    parser.add_argument("--n", "-n", type=int, default=5)
    args = parser.parse_args()
    fetch(args.pageid, args.n)
