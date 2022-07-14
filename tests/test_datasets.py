import pytest

from word_text_counter import get_flatland_path, get_time_machine_path, get_lostworld_path

def test_get_flatland_path():
    expected_filename = "flatland.txt"
    actual = get_flatland_path().split('/')[-1]
    assert actual == expected_filename, "flatland filename incorrect!"

def test_get_flatland_path_error():
    expected_filename = "flatland.txt"
    actual = get_flatland_path()
    with pytest.raises(AssertionError, match="value must be flatland.txt!"):
        assert actual == expected_filename, "value must be flatland.txt!"

def test_get_time_machine_path():
    expected_filename = "time_machine.txt"
    actual = get_time_machine_path().split('/')[-1]
    assert actual == expected_filename, "time_machine filename incorrect!"

def test_get_time_machine_path_error():
    expected_filename = "time_machine.txt"
    actual = get_time_machine_path()
    with pytest.raises(AssertionError, match="value must be time_machine.txt!"):
        assert actual == expected_filename, "value must be time_machine.txt!"

def test_get_lostworld_path():
    expected_filename = "lostworld.txt"
    actual = get_lostworld_path().split('/')[-1]
    assert actual == expected_filename, "lostworld filename incorrect!"

def test_get_lostworld_path_error():
    expected_filename = "lostworld.txt"
    actual = get_lostworld_path()
    with pytest.raises(AssertionError, match="value must be lostworld.txt!"):
        assert actual == expected_filename, "value must be lostworld.txt!"