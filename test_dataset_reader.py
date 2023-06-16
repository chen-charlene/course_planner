
from dataset_reader import Reader

def test_example():
    assert 2 == 1+1

def test_find_code():
    test_reader = Reader()
    returned_word = test_reader.find_code("Chemistry")
    #assert len(returned_word) == 4

def test_populating_code_to_subject():
    test_reader = Reader()
    subject_list = {"Africana Studies","American Studies","Anthropology", "Applied Mathematics",
                                 "Applied Mathematics-Biology"}
    for subject in subject_list:
        test_reader.find_code(subject)

def test_constructore():
    test_reader = Reader()
    test_reader.__init__()

def test_outliers():
    test_reader = Reader()
    test_reader.find_code("Public Health")
    test_reader.find_code("Sociology")
    test_reader.find_code("Health and Human Biology")





