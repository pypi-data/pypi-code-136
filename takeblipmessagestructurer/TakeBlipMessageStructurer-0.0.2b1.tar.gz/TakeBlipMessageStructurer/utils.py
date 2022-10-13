from gensim.models import KeyedVectors
import typing as tp
import re

from TakeBlipMessageStructurer.regex_pattern import LINKING_VERB

Core_dict = tp.Dict[str, tp.Any]


def load_fasttext_embeddings(path, pad):
    fasttext = KeyedVectors.load(path, mmap=None)
    fasttext.add(pad, [0] * fasttext.vector_size, replace=True)
    return fasttext


def clean_tags(sentence: list,
               tags: list,
               ner: list,
               remove: list,
               remove_entities: bool = False) -> tp.Tuple[str, str, str]:
    """Remove words of the sentence based on a list of tags

        :param sentence: List of words in a sentence.
        :type sentence: list
        :param tags: List of POSTags of words in a sentence.
        :type tags: list
        :param ner: List of entities of words in a sentence.
        :type ner: list
        :param remove: List of tags to be remove. Can be POSTags or entities.
        :type remove: list
        :param remove_entities: True if the tags to be remove are entities.
        :type remove_entities: bool
        :return: A tuple with the processed sentence, POSTags and entities.
        :rtype: tp.Tuple[str, str, str]
        """
    split_msg = sentence.copy()
    split_tags = tags.copy()
    split_ner = ner.copy()
    if remove_entities:
        values_lst = reversed(list(enumerate(ner)))
    else:
        values_lst = reversed(list(enumerate(tags)))
    for ind, tag in values_lst:
        if tag in remove:
            split_msg.pop(ind)
            split_tags.pop(ind)
            split_ner.pop(ind)
    return ' '.join(split_msg), ' '.join(split_tags), ' '.join(split_ner)


def get_neighborhood(word_type: str, start: int, end: int,
                     message: list, postag: list) -> (str, str):
    """
    Get the verb and adjective on the neighborhood of an entity.

    :param word_type: Type of the entity.
    :type word_type: str
    :param start: index of the start position of the entity (number os previous words)
    :type start: int
    :param end: index of the end position of the entity
    :type end: int
    :param message: list with the words of the sentence
    :type message: list
    :param postag: list with the postags of the sentence
    :type postag: list
    :return: A tuple with a string with the entity and the neighborhood and a
    string with the postag of these words.
    :rtype: tuple(str, str)
    """
    found_word = message[start: end]
    postag_word = postag[start: end]
    tags_target = ['VERB', 'ADJ', 'PART']
    if start != 0 and postag[start - 1] in tags_target:
        found_word = [message[start - 1]] + found_word
        postag_word = [postag[start - 1]] + postag_word
    if end != len(message) and postag[end] in tags_target:
        found_word = found_word + [message[end]]
        postag_word = postag_word + [postag[end]]
    return ' '.join(found_word), ' '.join(postag_word)


def structure_output(message_tags: list,
                     sentence: str,
                     sentence_id: tp.Optional[int] = None) -> Core_dict:
    """Structure the core of the sentences.

        :param message_tags: A list with the dictionary with the tags of the words.
        :type message_tags: list
        :param sentence: String of the sentence.
        :type sentence: str
        :param sentence_id: The id of the message, used on batch prediction. Default is None.
        :type sentence_id: tp.Optional[int]
        :return: Dictionary with the core of the message.
        :rtype: Core_dict
        """
    sorted_content = sorted(message_tags,
                            key=lambda row: row['message_start'])
    sorted_content = [{key: value for (key, value) in item_dict.items() if
                       not key.startswith('message')} for item_dict in
                      sorted_content]
    output = {
        **({'id': sentence_id} if sentence_id is not None else {}),
        'filtered_message': sentence,
        'lowercase_filtered_message': sentence.lower(),
        'content': sorted_content
    }
    return output


def convert_class_verb(sentence: str, tags: str) -> str:
    """
    Convert the label of a linkage verb to be VERBL

    :param sentence: string of a sentence
    :type sentence: str
    :param tags: string with the postags of the sentence
    :param tags: str
    :return: Return the postags with the converted postags
    :rtype: str
    """
    list_sentence = sentence.split()
    list_tags = tags.split()

    for k in range(len(list_tags)):
        if list_sentence[k] in LINKING_VERB:
            list_tags[k] = 'VERBL'

    return ' '.join(list_tags)


def detect_linking_verb(input_sentence: str) -> bool:
    """
    Detect if the sentence has a linking verb

    :param input_sentence: string of a sentence to look for a linking verb
    :type input_sentence: str
    :return: True if the sentence has a linking verb
    :rtype: bool
    """
    link_verb_pattern = re.compile(r'(^|\s)'+'|'.join(LINKING_VERB)+r'(\s|$)')
    return bool(link_verb_pattern.search(input_sentence))
