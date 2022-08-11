# flask_app/logic/papybot.py
# test the start method of the class PapyBot

import pytest

from flask_app.logic import papybot
from tests import params_test_logic_papybot_start

GeolocApi = papybot.GeolocApi
PapyBot = papybot.PapyBot
params = params_test_logic_papybot_start.params


@pytest.mark.parametrize(
    (
        "question, "
        "return_from_function_remove_some_words_and_format_text, "
        "return_from_function_extract_question_from_text, "
        "return_from_function_extract_city_from_question, "
        "return_from_function_figure_out_city, "
        "return_from_function_check_if_city_exists, "
        "return_from_function_get_geolocation, "
        "return_from_function_check_response_validity_of_geoloc, "
        "return_from_function_get_interesting_points_around, "
        "return_from_function_translate_points_categories, "
        "return_from_function_turn_interesting_points_into_html_version, "
        "return_from_function_get_info_from_wikipedia, "
        "expected_value"
    ),
    [*params]
    )
def test_start(
    monkeypatch,
    question,
    return_from_function_remove_some_words_and_format_text,
    return_from_function_extract_question_from_text,
    return_from_function_extract_city_from_question,
    return_from_function_figure_out_city,
    return_from_function_check_if_city_exists,
    return_from_function_get_geolocation,
    return_from_function_check_response_validity_of_geoloc,
    return_from_function_get_interesting_points_around,
    return_from_function_translate_points_categories,
    return_from_function_turn_interesting_points_into_html_version,
    return_from_function_get_info_from_wikipedia,
    expected_value
    ):
    
    Sut = PapyBot

    def mock_remove_some_words_and_format_text(text_to_format, WORDS_OF_COURTESY):
        return return_from_function_remove_some_words_and_format_text

    def mock_extract_question_from_text(formated_text, STOP_WORDS):
        return return_from_function_extract_question_from_text

    def mock_extract_city_from_question(question):
        return return_from_function_extract_city_from_question

    def mock_figure_out_city(question):
        if not (question and isinstance(question, str)):
            raise Exception(
                "Error in args of figure_out_city() "
                "Maybe question is missing. Question must be a non-empty string"
            )
        return return_from_function_figure_out_city

    def mock_check_if_city_exists(city):
        return return_from_function_check_if_city_exists

    def mock_get_geolocation(question, city, message_from_papy):
        return return_from_function_get_geolocation

    def mock_check_response_validity_of_geoloc(question, location_title, full_address, city):
        return return_from_function_check_response_validity_of_geoloc

    def mock_get_interesting_points_around(latitude, longitude):
        return return_from_function_get_interesting_points_around

    def mock_translate_points_categories(interesting_points_list, FRENCH):
        return return_from_function_translate_points_categories

    def mock_turn_interesting_points_into_html_version(interesting_points_list):
        return return_from_function_turn_interesting_points_into_html_version

    def mock_get_info_from_wikipedia(topic):
        if "theatre de beziers" in topic:
            return return_from_function_get_info_from_wikipedia[0]
        elif "Place Jean Jaurès" in topic:
            return return_from_function_get_info_from_wikipedia[1]
        elif "Jean Jaurès" in topic:
            return return_from_function_get_info_from_wikipedia[2]

    def mock_very_first_words_of_papy():
        return "Pour tout de dire...<br />"

    def mock_display_map(api_key, latitude, longitude):
        return (
            """<end_of_bubble />Pour finir, voici la carte ...<br />"""
            """<img src="https://image.maps.ls.hereapi.com/mia/1.6/mapview"""
            """?apiKey=xxx&z=17&w=1000&h=700&c=43.3418,3.21703" />""")

    monkeypatch.setattr(
        papybot,
        "remove_some_words_and_format_text",
        mock_remove_some_words_and_format_text
    )

    monkeypatch.setattr(
        papybot,
        "extract_question_from_text",
        mock_extract_question_from_text
    )

    monkeypatch.setattr(
        papybot,
        "extract_city_from_question",
        mock_extract_city_from_question
    )

    monkeypatch.setattr(
        papybot,
        "figure_out_city",
        mock_figure_out_city
    )

    monkeypatch.setattr(
        GeolocApi,
        "check_if_city_exists",
        mock_check_if_city_exists
    )

    monkeypatch.setattr(
        Sut,
        "get_geolocation",
        mock_get_geolocation
    )

    monkeypatch.setattr(
        Sut,
        "get_geolocation",
        mock_get_geolocation
    )

    monkeypatch.setattr(
        Sut,
        "check_response_validity_of_geoloc",
        mock_check_response_validity_of_geoloc
    )

    monkeypatch.setattr(
        GeolocApi,
        "get_interesting_points_around",
        mock_get_interesting_points_around
    )

    monkeypatch.setattr(
        Sut,
        "translate_points_categories",
        mock_translate_points_categories
    )

    monkeypatch.setattr(
        Sut,
        "turn_interesting_points_into_html_version",
        mock_turn_interesting_points_into_html_version
    )

    monkeypatch.setattr(
        Sut,
        "get_info_from_wikipedia",
        mock_get_info_from_wikipedia
    )

    monkeypatch.setattr(
        Sut,
        "very_first_words_of_papy",
        mock_very_first_words_of_papy
    )

    monkeypatch.setattr(
        Sut,
        "display_map",
        mock_display_map
    )
    
    assert Sut.start(question) == expected_value

             