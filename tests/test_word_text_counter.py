import json
import pytest, re

from word_text_counter import count_words, get_flatland_path, get_time_machine_path, get_lostworld_path

@pytest.fixture
def pyzen_counts() -> dict:
    return {
        'total': 143, 
        'details': {
            'the': 6, 'zen': 1, 'of': 3, 'python': 1, 'by': 1, 'tim': 1, 'peters': 1, 'beautiful': 1, 'is': 10, 'better': 8, 'than': 8, 'ugly': 1, 
            'explicit': 1, 'implicit': 1, 'simple': 1, 'complex': 2, 'complicated': 1, 'flat': 1, 'nested': 1, 'sparse': 1, 'dense': 1, 'readability': 1, 
            'counts': 1, 'special': 2, 'cases': 1, 'arent': 1, 'enough': 1, 'to': 5, 'break': 1, 'rules': 1, 'although': 3, 'practicality': 1, 'beats': 1, 
            'purity': 1, 'errors': 1, 'should': 2, 'never': 3, 'pass': 1, 'silently': 1, 'unless': 2, 'explicitly': 1, 'silenced': 1, 'in': 1, 'face': 1, 
            'ambiguity': 1, 'refuse': 1, 'temptation': 1, 'guess': 1, 'there': 1, 'be': 3, 'one': 3, 'and': 1, 'preferably': 1, 'only': 1, 'obvious': 2, 
            'way': 2, 'do': 2, 'it': 2, 'that': 1, 'may': 2, 'not': 1, 'at': 1, 'first': 1, 'youre': 1, 'dutch': 1, 'now': 2, 'often': 1, 'right': 1, 
            'if': 2, 'implementation': 2, 'hard': 1, 'explain': 2, 'its': 1, 'a': 2, 'bad': 1, 'idea': 3, 'easy': 1, 'good': 1, 'namespaces': 1, 'are': 1, 
            'honking': 1, 'great': 1, 'lets': 1, 'more': 1, 'those': 1
        }
    }

def flatland_counts() -> dict:
    with open("tests/flatland.json","r") as file:
        flatland = json.load(file)
    return flatland

def time_machine_counts() -> dict:
    with open("tests/time_machine.json","r") as file:
        time_machine = json.load(file)
    return time_machine

def lost_world_counts() -> dict:
    with open("tests/lost_world.json","r") as file:
        lost_world = json.load(file)
    return lost_world

@pytest.mark.parametrize(
    "filepath, counts",
    [
        (get_flatland_path(),flatland_counts()),
        (get_time_machine_path(),time_machine_counts()),
        (get_lostworld_path(),lost_world_counts())
    ]
)


def test_count_words(filepath, counts):
    expected = counts
    actual = count_words(filepath)
    assert actual == expected, f"{filepath.split('/')[-1].replace('.txt','')} quote counted incorrectly!"

def test_count_words_error(pyzen_counts):
    expected = pyzen_counts
    with pytest.raises(FileNotFoundError, match=re.escape("[Errno 2] No such file or directory: 'data/pyzen.txt'")):
        actual = count_words("data/pyzen.txt")
        assert actual == expected, "Pyzen quote counted incorrectly!"