
from dataset_reader import Reader
from dataset_class_reader import ClassReader

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

def test_constructor():
    test_reader = Reader()
    test_reader.__init__()

def test_outliers():
    test_reader = Reader()
    test_reader.find_code("Public Health")
    test_reader.find_code("Sociology")
    test_reader.find_code("Health and Human Biology")


#test suite for the dataset class reader

def test_ClassReader_dict_populate():
    test_class_reader = ClassReader()
    test_class_reader.__init__()

def test_populate_class_list():
    test_class_reader = ClassReader()
    test_class_reader.populate_class_list()





