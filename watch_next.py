import spacy
from rich import print
import csv

nlp = spacy.load("en_core_web_md")

# variables
movie_list = {}


# functions
def next_movie(desc):
    """
    Function uses spacy to find the best similar movie from the dictionary items of movie_list from the given
    movie_desc then returns the dict item of the best match from the movie_list dict
    """
    global movie_list
    # create a doc object from the given movie_desc
    doc = nlp(desc)
    score_dict = {}
    # iterate through the movie_list dict values
    for key, value in movie_list.items():
        # for each value create a space doc_temp object
        doc_temp = nlp(value)
        # calc similarity score between doc and doc_temp with spacy vector similarity
        score = doc.similarity(doc_temp)
        # append the key and its score as a value to score_dict
        score_dict[key] = score
    #print(score_dict)
    return max(score_dict, key=score_dict.get)


def load_movie_list():
    """
    load movie_list from movies.txt to dictionary movie A: description A
    """
    global movie_list
    with open("movies.txt", "r") as f:
        # csv.reader to load the file into a list delimited by colons
        reader = csv.reader(f, delimiter=":")
        # for each row in reader create a dictionary then append it to movie_list
        for row in reader:
            movie_list[row[0]] = row[1]


movie_desc = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,  \
             the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live  \
             in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a  \
             gladiator"""

load_movie_list()
print(f"Your next movie recommendation is: {next_movie(movie_desc)}")
