from japl.nlp import nlp
from pandas import DataFrame

my_example = DataFrame({"text": ["This is some random text to lemma.", "This is run running runner work workin.", "Hello World", "Builder the build work workshop working worker", "Have having had"]})

my_list = my_example["text"]

nlp(my_list)