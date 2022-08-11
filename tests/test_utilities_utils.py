# flask_app/utilities/utils.py

from flask_app.constants import (
    LOCATION_WORDS,
)
from flask_app.utilities.utils import (
    extract_city_from_question,
    extract_question_from_text,
    extract_name_out_of_street,
    figure_out_city,
    remove_some_words_and_format_text,
    remove_accents,
    remove_punctuation,
)

def test_remove_accents():
    print("=> Remove all accents from question")
    text_to_format_is_int = 12345
    text_to_format_is_none = None
    text_to_format_is_dict = {"message": "Not string"}
    text_to_format_is_empty_str = ""
    text_to_format_has_accent = "éèàù-normal  çie ë"


    assert remove_accents(text_to_format_is_int) == ""
    assert remove_accents(text_to_format_is_none) == ""
    assert remove_accents(text_to_format_is_dict) == ""
    assert remove_accents(text_to_format_is_empty_str) == ""
    assert remove_accents(text_to_format_has_accent) == "eeau-normal  cie e"


def test_remove_punctuation():
    print("=> Remove punctuation from question")
    text_to_format_is_int = 12345
    text_to_format_is_none = None
    text_to_format_is_dict = {"message": "Not string"}
    text_to_format_is_empty_str = ""
    text_to_format_has_punctuation = "Salut, comment vas-tu ?...;!:"

    assert remove_punctuation(text_to_format_is_int) == ""
    assert remove_punctuation(text_to_format_is_none) == ""
    assert remove_punctuation(text_to_format_is_dict) == ""
    assert remove_punctuation(text_to_format_is_empty_str) == ""
    assert remove_punctuation(text_to_format_has_punctuation) == "Salut comment vastu "


def test_remove_some_words_and_format_text():
    print("=> Remove the provided words from the text and format the text")
    text_to_format_is_int = 12345
    text_to_format_is_none = None
    text_to_format_is_dict = {"message": "Not string"}
    text_to_format_is_empty_str = ""
    text_to_format_is_correct = (
        "Salût, comment vas-tu l'ami, "
        "à l'approche de la fin du monde? 5 espaces entre la>     <et là !")

    words_to_remove_is_int = 12345
    words_to_remove_is_None = None
    words_to_remove_is_str = "A simple string"
    words_to_remove_is_correct = ["de la fin", "du monde"]


    assert remove_some_words_and_format_text(
        text_to_format_is_int, words_to_remove_is_correct) == ""
    assert remove_some_words_and_format_text(
        text_to_format_is_none, words_to_remove_is_correct) == ""
    assert remove_some_words_and_format_text(
        text_to_format_is_dict, words_to_remove_is_correct) == ""
    assert remove_some_words_and_format_text(
        text_to_format_is_empty_str, words_to_remove_is_correct) == ""
    assert remove_some_words_and_format_text(
        text_to_format_is_correct, words_to_remove_is_int) == ""
    assert remove_some_words_and_format_text(
        text_to_format_is_correct, words_to_remove_is_None) == ""
    assert remove_some_words_and_format_text(
        text_to_format_is_correct, words_to_remove_is_str) == ""
    assert remove_some_words_and_format_text(
        text_to_format_is_correct, words_to_remove_is_correct) == (
        "salut comment vas tu l'ami à l'approche 5 espaces entre la et la")


def test_extract_question_from_text():
    print("=> Select from the question the location to find")
    text_to_format_is_int = 12345
    text_to_format_is_none = None
    text_to_format_is_dict = {"message": "Not string"}
    text_to_format_is_empty_str = ""
    text_to_format_is_a_word = "openclassrooms"
    text_to_format_is_correct = "quelle est l'adresse d'openclassrooms"
    STOP_WORDS_IS_INT = 12345
    STOP_WORDS_IS_NONE = None
    STOP_WORDS_IS_DICT = {"message": "Not list"}
    STOP_WORDS_IS_STRING = "string"
    STOP_WORDS_IS_CORRECT = ["l'adresse d'"]

    assert extract_question_from_text(text_to_format_is_int, STOP_WORDS_IS_CORRECT) == None
    assert extract_question_from_text(text_to_format_is_none, STOP_WORDS_IS_CORRECT) == None
    assert extract_question_from_text(text_to_format_is_dict, STOP_WORDS_IS_CORRECT) == None
    assert extract_question_from_text(text_to_format_is_empty_str, STOP_WORDS_IS_CORRECT) == None
    assert extract_question_from_text(text_to_format_is_a_word, STOP_WORDS_IS_CORRECT) == None
    assert extract_question_from_text(text_to_format_is_correct, STOP_WORDS_IS_INT) == None
    assert extract_question_from_text(text_to_format_is_correct, STOP_WORDS_IS_NONE) == None
    assert extract_question_from_text(text_to_format_is_correct, STOP_WORDS_IS_DICT) == None
    assert extract_question_from_text(text_to_format_is_correct, STOP_WORDS_IS_STRING) == None
    assert extract_question_from_text(text_to_format_is_correct, STOP_WORDS_IS_CORRECT) == "openclassrooms"


def test_extract_city_from_question():
    print("=> Select the city in the question thanks to specific words")
    question0 = 12345
    question1 = None
    question2 = {"message": "Not string"}
    question3 = ""
    question4 = "ou est le pont de la ville d'avignon"
    question5 = "ou est le pont d'avignon"
    assert extract_city_from_question(question0) == ("", None)
    assert extract_city_from_question(question1) == ("", None)
    assert extract_city_from_question(question2) == ("", None)
    assert extract_city_from_question(question3) == ("", None)
    assert extract_city_from_question(question4) == ("ou est le pont", "avignon")
    assert extract_city_from_question(question5) == ("ou est le pont d'avignon", None)


def test_figure_out_city():
    print('=> Try to determine the name of the city from the keyword "à", "a" and "de" ')
    question0 = 12345
    question1 = None
    question2 = {"message": "Not string"}
    question3 = ""
    question4 = "ou sont les ecluses a beziers"
    question5 = "ou est le musée de la peche de saint-pierre"
    question6 = "ou est le pont d'avignon"
    question7 = "ou se trouve le jardin des poetes"

    assert figure_out_city(question0) == (["", ""], ["", ""])
    assert figure_out_city(question1) == (["", ""], ["", ""])
    assert figure_out_city(question2) == (["", ""], ["", ""])
    assert figure_out_city(question3) == (["", ""], ["", ""])
    assert figure_out_city(question4) == (["ou sont les ecluses", ""], ["beziers", ""])
    assert figure_out_city(question5) == (["", "ou est le musée"], ["", "saint-pierre"])
    assert figure_out_city(question6) == (["", "ou est le pont"], ["", "avignon"])
    assert figure_out_city(question7) == (["", ""], ["", ""])


def test_extract_name_out_of_street():
    print("=> Get the number and the name of the street but not the type of street")
    street1 = None
    street2 = 12345
    street3 = ""
    street4 = {"message": "Not a string"}
    street5 = "10 Avenue Robespierre"
    street6 = "24Bis allée de la belle vue"
    assert extract_name_out_of_street(street1, LOCATION_WORDS) == ""
    assert extract_name_out_of_street(street2, LOCATION_WORDS) == ""
    assert extract_name_out_of_street(street3, LOCATION_WORDS) == ""
    assert extract_name_out_of_street(street4, LOCATION_WORDS) == ""
    assert extract_name_out_of_street(street5, "") == ""
    assert extract_name_out_of_street(street5, None) == ""
    assert extract_name_out_of_street(street5, {"message": "Not a string"}) == ""
    assert extract_name_out_of_street(street5, "uncorrect string") == ""
    assert extract_name_out_of_street(street5, LOCATION_WORDS) == "10 Robespierre"
    assert extract_name_out_of_street(street6, LOCATION_WORDS) == "2 belle vue"
