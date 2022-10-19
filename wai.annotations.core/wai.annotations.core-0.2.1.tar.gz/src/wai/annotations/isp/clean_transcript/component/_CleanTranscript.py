from ....core.component import ProcessorComponent
from wai.annotations.domain.audio.speech import SpeechInstance, Transcription
from ....core.stream import ThenFunction, DoneFunction
from ....core.stream.util import RequiresNoFinalisation
from wai.common.cli.options import FlagOption, TypedOption

QUOTES = "'\"‘’“”‹›«»"

PUNCTUATION = ":;,.!?"

BRACKETS = "()[]{}〈〉"


class CleanTranscript(
    RequiresNoFinalisation,
    ProcessorComponent[SpeechInstance, SpeechInstance]
):
    """
    ISP that cleans up speech transcripts.
    """

    non_alpha_numeric: str = FlagOption(
        "-a", "--non-alpha-numeric",
        help="removes all characters that are not alpha-numeric"
    )

    non_letters: str = FlagOption(
        "-l", "--non-letters",
        help="removes all characters that are not letters"
    )

    numeric: str = FlagOption(
        "-n", "--numeric",
        help="removes all numeric characters"
    )

    quotes: str = FlagOption(
        "-q", "--quotes",
        help="removes quotes: %s" % QUOTES
    )

    punctuation: str = FlagOption(
        "-p", "--punctuation",
        help="removes punctuation characters: %s" % PUNCTUATION
    )

    brackets: str = FlagOption(
        "-b", "--brackets",
        help="removes brackets: %s" % BRACKETS
    )

    custom = TypedOption(
        "-c", "--custom",
        type=str,
        default="",
        required=False,
        help="the custom characters to remove"
    )

    verbose: bool = FlagOption(
        "--verbose",
        help="outputs information about processed transcripts"
    )

    def process_element(
            self,
            element: SpeechInstance,
            then: ThenFunction[SpeechInstance],
            done: DoneFunction
    ):
        # assemble characters to remove
        remove_chars = set()
        if self.quotes:
            remove_chars.update(QUOTES)
        if self.punctuation:
            remove_chars.update(PUNCTUATION)
        if self.brackets:
            remove_chars.update(BRACKETS)
        if len(self.custom) > 0:
            remove_chars.update(self.custom)

        # nothing to do?
        if (len(remove_chars) == 0) and not self.non_alpha_numeric and not self.non_letters and not self.numeric:
            then(element)
            return

        # clean transcript
        text = element.annotations.text
        if self.non_alpha_numeric:
            text = ''.join(c for c in text if c.isalnum())
        if self.non_letters:
            text = ''.join(c for c in text if c.isalpha())
        if self.numeric:
            text = ''.join(c for c in text if (not c.isnumeric()))
        if len(remove_chars) > 0:
            text = ''.join(c for c in text if (c not in remove_chars))

        modified = text != element.annotations.text

        if self.verbose:
            self.logger.info("%s -> %s (%s)" % (element.annotations.text, text, str(modified)))

        # any changes?
        if modified:
            new_transcript = Transcription(text)
            new_element = SpeechInstance(element.data, new_transcript)
            then(new_element)
        else:
            then(element)
