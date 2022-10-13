import re

import typing as tp

from TakeBlipNer.nermodel import CRF
from TakeBlipMessageStructurer.tags_dict import ner_dict, postag_dict
from TakeBlipMessageStructurer.utils import clean_tags, structure_output, \
    get_neighborhood, convert_class_verb, detect_linking_verb
from TakeBlipMessageStructurer.regex_pattern import ENTITY_PATTERN, \
    POSTAGS_PATTERN, PLACEHOLDERS_LIST, ENTITIES_TO_NEIGHBORHOOD

Tags_dict = tp.Dict[str, str]
Core_dict = tp.Dict[str, tp.Any]


class MessageStructurer:
    def __init__(self, ner_model: CRF, use_neighborhood: bool = False):
        self.ner_model = ner_model
        self.ner_dict = ner_dict
        self.postagging_dict = postag_dict
        self.entity_pattern = re.compile(ENTITY_PATTERN)
        self.tag_pattern = re.compile(POSTAGS_PATTERN)
        self.use_neighborhood = use_neighborhood

    def __find_pattern(self,
                       ner_tags: str,
                       pos_tags: str,
                       message: str,
                       is_postag: bool) -> tp.List[Core_dict]:
        """Return a list with the dictionary of patterns founded.

        The patterns are entities or POSTags of the label ADJ, VERB, PART, ADV.

        Output example:
        For entity:

        {'value': 'Segunda via',
        'lowercase_value': 'segunda via',
        'postags': 'ADJ SUBS',
        'message_start': 0,
        'message_end': 1,
        'type' : 'financial'}

        For POSTags:
        {'value': 'Quero pagar',
        'lowercase_value': 'quero pagar',
        'postags': 'VERB',
        'message_start': 0,
        'message_end': 1,
        'type': 'postagging'}

        :param ner_tags: String with the label for the entities
        :type ner_tags: str
        :param pos_tags: String with the label for the postags
        :type pos_tags: str
        :param message: Message string.
        :type message: str
        :param is_postag: The pattern is a postag pattern.
        :type is_postag: bool
        :return: List with the dictionary of the patterns founded.
        :rtype: tp.List[Core_dict]
        """

        if is_postag:
            pattern = self.tag_pattern
            class_dict = self.postagging_dict
            tags = pos_tags
        else:
            pattern = self.entity_pattern
            class_dict = self.ner_dict
            tags = ner_tags

        splitted_message = message.split()
        splitted_postags = pos_tags.split()
        data_dicts_list = []
        for match in pattern.finditer(tags):
            found_dict = {}
            message_start = len(tags[:match.start()].split())
            message_end = len(tags[:match.end()].split())
            word_type = tags[match.start(): match.end()].split()[0]

            has_placeholder = [placeholders not in
                               splitted_message[message_start:message_end]
                               for placeholders in PLACEHOLDERS_LIST]

            if all(has_placeholder):
                if not is_postag and self.use_neighborhood and \
                        word_type in ENTITIES_TO_NEIGHBORHOOD:
                    found_word, postag_word = get_neighborhood(word_type,
                                                               message_start,
                                                               message_end,
                                                               splitted_message,
                                                               splitted_postags)
                else:
                    found_word = ' '.join(
                        splitted_message[message_start: message_end])
                    postag_word = ' '.join(
                        splitted_postags[message_start: message_end])

                found_dict['value'] = found_word
                found_dict['lowercase_value'] = found_word.lower()
                found_dict['postags'] = postag_word
                found_dict['message_start'] = message_start
                found_dict['message_end'] = message_end
                found_dict['type'] = class_dict[word_type]
                data_dicts_list.append(found_dict)
        return data_dicts_list

    @staticmethod
    def __process_sentence(sentence_lst: tp.List[str], tags_lst: tp.List[str],
                           ner_lst: tp.List[str], tags_to_remove: list,
                           ner_to_remove: tp.Optional[list]) -> tp.Tuple[
        str, str, str]:
        """Process sentences based on tags to be filtered

        :param sentence_lst: List with the words of the message.
        :type sentence_lst: tp.List[str]
        :param tags_lst: List with the postag of the words.
        :type tags_lst: tp.List[str]
        :param ner_lst: List with the entity labels of the words.
        :type ner_lst: tp.List[str]
        :param tags_to_remove: List of POSTags to be removed.
        :type tags_to_remove: list
        :param ner_to_remove: List with the entities to be removed.
        :type ner_to_remove: tp.Optional[list]
        :return: Sentence and tags processed
        :rtype: tp.Tuple[str, str, str]
        """
        sentence, tags, ner = clean_tags(sentence=sentence_lst,
                                         tags=tags_lst,
                                         ner=ner_lst,
                                         remove=tags_to_remove)
        if ner_to_remove:
            sentence, tags, ner = clean_tags(sentence=sentence_lst,
                                             tags=tags_lst,
                                             ner=ner_lst,
                                             remove=ner_to_remove,
                                             remove_entities=True)

        return sentence, tags, ner

    def __get_message_dicts(self,
                            input_sentence: str,
                            input_tags: str,
                            input_ner: str,
                            tags_to_remove: list,
                            filter_entity: tp.Optional[list] = None,
                            sentence_id: tp.Optional[int] = None) -> Core_dict:
        """Return the dictionary with the core of the message

        :param input_sentence: The message to be structured.
        :type input_sentence: str
        :param input_tags: The POSTags labels of the message.
        :type input_tags: str
        :param input_ner: The entities labels of the message.
        :type input_ner: str
        :param tags_to_remove: List of POSTags to be removed.
        :type tags_to_remove: list
        :param filter_entity: List with the entities to be removed. Default is None.
        :type filter_entity: tp.Optional[list]
        :param sentence_id: The id of the message, used on batch prediction. Default is None.
        :type sentence_id: tp.Optional[int]
        :return: Dictionary with the core information of the sentence.
        :rtype: Core_dict
        """
        sentence_lst = input_sentence.split()
        tags_lst = input_tags.split()
        ner_lst = input_ner.split()

        sentence, tags, ner = self.__process_sentence(sentence_lst,
                                                      tags_lst,
                                                      ner_lst,
                                                      tags_to_remove,
                                                      filter_entity)

        message_ner_list = self.__find_pattern(ner_tags=ner,
                                               pos_tags=tags,
                                               message=sentence,
                                               is_postag=False)

        message_tag_list = self.__find_pattern(ner_tags=ner,
                                               pos_tags=tags,
                                               message=sentence,
                                               is_postag=True)

        message_dict = message_ner_list + message_tag_list
        structured_output = structure_output(message_tags=message_dict,
                                             sentence=sentence,
                                             sentence_id=sentence_id)

        return structured_output

    def structure_message(self,
                          sentence: str,
                          tags_to_remove: list,
                          entities_to_remove: tp.Optional[list] = None,
                          use_pre_processing: bool = True) -> Core_dict:
        """Structures the message of a sentence

        :param sentence: The message to be structured.
        :type sentence: str
        :param tags_to_remove: List of POSTags to be removed.
        :type tags_to_remove: list
        :param entities_to_remove: List with the entities to be removed. Default is None.
        :type entities_to_remove: tp.Optional[list]
        :param use_pre_processing: Whether to pre process input data. Default True.
        :type use_pre_processing: bool
        :return: Dictionary with the core information of the sentence.
        :rtype: Core_dict
        """
        input_sentence, tags, ner = self.ner_model.predict_line(sentence,
                                                                use_pre_processing=use_pre_processing)
        if detect_linking_verb(input_sentence):
            tags = convert_class_verb(input_sentence, tags)

        return self.__get_message_dicts(input_sentence=input_sentence,
                                        input_tags=tags,
                                        input_ner=ner,
                                        tags_to_remove=tags_to_remove,
                                        filter_entity=entities_to_remove)

    def structure_message_batch(self,
                                sentences: list,
                                tags_to_remove: list,
                                entities_to_remove: tp.Optional[list] = None,
                                use_pre_processing: bool = True,
                                batch_size: int = 50,
                                shuffle: bool = True) -> tp.List[Core_dict]:
        """Structures the messages of a set of sentences

        :param sentences: List with the messages to be structured.
        :type sentences: list
        :param tags_to_remove: List of POSTags to be removed.
        :type  tags_to_remove: list
        :param entities_to_remove: List with the entities to be removed. Default is None.
        :type entities_to_remove: tp.Optional[list]
        :param use_pre_processing: Whether to pre process input data. Default True.
        :type use_pre_processing: bool
        :param batch_size: Batch size.
        :type batch_size: int
        :param shuffle: Whether to shuffle the dataset. Default True.
        :type shuffle: bool
        :return: List with the dictionary with the core information of the sentences.
        :rtype: tp.List[Core_dict]
        """
        structured_batches = []
        predictions_list = self.ner_model.predict_batch(
            filepath='',
            sentence_column='',
            batch_size=batch_size,
            shuffle=shuffle,
            use_pre_processing=use_pre_processing,
            output_lstm=False,
            sentences=sentences)

        for prediction in predictions_list:
            structured_batches.append(self.__get_message_dicts(
                input_sentence=prediction['processed_sentence'],
                input_tags=prediction['postaggings'],
                input_ner=prediction['entities'],
                sentence_id=prediction['id'],
                tags_to_remove=tags_to_remove,
                filter_entity=entities_to_remove))
        return structured_batches
