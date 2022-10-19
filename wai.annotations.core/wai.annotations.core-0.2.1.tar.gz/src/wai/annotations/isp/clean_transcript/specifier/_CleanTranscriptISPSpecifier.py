from typing import Type, Tuple

from ....core.component import ProcessorComponent
from ....core.domain import DomainSpecifier
from ....core.specifier import ProcessorStageSpecifier


class CleanTranscriptISPSpecifier(ProcessorStageSpecifier):
    """
    ISP that cleans speech transcripts.
    """
    @classmethod
    def description(cls) -> str:
        return "ISP that cleans speech transcripts."

    @classmethod
    def domain_transfer_function(
            cls,
            input_domain: Type[DomainSpecifier]
    ) -> Type[DomainSpecifier]:
        from ....domain.audio.speech import SpeechDomainSpecifier
        if input_domain is SpeechDomainSpecifier:
            return SpeechDomainSpecifier
        else:
            raise Exception(
                f"CleanTranscript only handles the "
                f"{SpeechDomainSpecifier.name()} domain"
            )

    @classmethod
    def components(cls) -> Tuple[Type[ProcessorComponent]]:
        from ...clean_transcript.component import CleanTranscript
        return CleanTranscript,
