from collections import Counter


class CountVectorizer:
    def __init__(self):
        self.vocabulary = []
        self.vector = []

    def fit_transform(self, corpus):
        """
        Extracts all words from corpus,
        returns each sentence from corpus as list (vector) of numbers,
        where each number stands for a "frequency" if the word in the sentence
        :param corpus: list of strings (sentences)
        :return: list of lists of ints
        """
        temp = " ".join(corpus)
        vocabulary_template = dict.fromkeys(temp.lower().split(), 0)
        self.vocabulary = list(vocabulary_template)
        for sentence in corpus:
            copy = dict(vocabulary_template)
            vocabulary_sentence = dict(Counter(sentence.lower().split()))
            copy.update(vocabulary_sentence)
            self.vector.append(list(copy.values()))
        return self.vector

    def get_feature_names(self):
        """
        Returns list of all words from corpus
        :return: list of strings (words)
        """
        return self.vocabulary


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
