from ungreat_matching import ungreat_match


test_data = [['python','Python'],
['python','python3.7'],
['PYTHON','python3.7'],
['PYTHON','python3.7.3']]
wrong_test_data = [['Css','Python'],['html','test'],['mess','test'],['have done','succesfully']]
for data in test_data:
    print(ungreat_match(data[0],data[1], mismatching_chars=5, mkdefault=0.7))
for data in wrong_test_data:
    print(ungreat_match(data[0],data[1], mismatching_chars=5, mkdefault=0.7))
