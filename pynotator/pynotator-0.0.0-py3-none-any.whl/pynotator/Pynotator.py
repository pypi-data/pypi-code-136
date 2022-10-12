def annotate(sentence,word):
    annotated_word=word
    sentence_with_annotated_word=sentence
    start_index=sentence_with_annotated_word.index(annotated_word)
    length_word=len(annotated_word)
    end_index=start_index+length_word
    
    if start_index and end_index: 
        return start_index,end_index
    else:
        None
