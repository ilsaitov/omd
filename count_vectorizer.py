#  flake8 tested

class CountVectorizer:
    def __init__(self):
        """
        Constructor, creates an example of a class
        """
        self.vocabulary = []

    def fit_transform(self, corpus):
        """
        Extracts all words from corpus,
        returns each sentence from corpus as list (vector) of numbers,
        where each number stands for a "frequency" if the word in the sentence
        :param corpus: list of strings (sentences)
        :return: list of lists of ints
        """
        sentence_words = [sentence.lower().split() for sentence in corpus]
        all_words = [word for word in sentence_words for word in word]
        self.vocabulary = list(dict.fromkeys(all_words))
        return [
               [word.count(word_from_vocabulary)
                for word_from_vocabulary in self.vocabulary]
                for word in sentence_words
               ]

    def get_feature_names(self):
        """
        Returns list of all words from corpus
        :return: list of strings (words)
        """
        return self.vocabulary


if __name__ == "__main__":
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
