from .autotaxo import *
from .autorels import *
from .autosyns import *

from .autotaxo.bp import AutoTaxoOrchestrator

autotaxo = AutoTaxoOrchestrator()


def keyterms(input_text: str,
             use_terms: bool = True,
             use_keyterms: bool = True,
             use_ngrams: bool = False,
             use_nounchunks: bool = False) -> list or None:
    """ Generate KeyTerms as a simple list

    Args:
        input_text (str): input text of any length or description
        use_terms (bool, optional). Use Simple Term extraction algorithms. Default is True.
        use_keyterms (bool, optional). Use KeyTerm extraction algorithms. Default is True.
        use_ngrams (bool, optional). Use n-Gram extraction algorithms. Default is False.
        use_nounchunks (bool, optional). Use Noun Chunk extraction algorithms. Default is False.

    Sample Input:
        A local area network (LAN) is a computer network that interconnects computers within a limited area such as a residence, school, laboratory, university campus or office building.
        By contrast, a wide area network (WAN) not only covers a larger geographic distance, but also generally involves leased telecommunication circuits.
        Ethernet and Wi-Fi are the two most common technologies in use for local area networks.
        Historical network technologies include ARCNET, Token Ring, and AppleTalk.

    Sample Output:
        [   'leased telecommunication circuit',
            'historical network technology',
            'large geographic distance',
            'interconnects computer',
            'local area network',
            'university campus',
            'common technology',
            'wide area network',
            'computer network',
            'office building',
            'include arcnet',
            'limited area',
            'token ring'
        ]

    Returns:
        list or None: list of keyterms
    """

    return autotaxo.keyterms(
        input_text=input_text,
        use_terms=use_terms,
        use_keyterms=use_keyterms,
        use_ngrams=use_ngrams,
        use_nounchunks=use_nounchunks)
