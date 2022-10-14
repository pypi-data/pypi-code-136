import regex as re

from kdmt.dateparser.utils.constants import DATE_REGEX, STRIP_CHARS, RANGE_SPLIT_REGEX, ALL_GROUPS


class DateFragment:
    def __init__(self):
        self.match_str = ''
        self.indices = (0, 0)
        self.captures = {}

    def __repr__(self):
        str_capt = ', '.join(['"{}": [{}]'.format(c, self.captures[c]) for c in self.captures])
        return '{} [{}, {}]\nCaptures: {}'.format(self.match_str, self.indices[0], self.indices[1], str_capt)

    def get_captures_count(self):
        return sum([len(self.captures[m]) for m in self.captures])


def split_date_range(text):
    st_matches = RANGE_SPLIT_REGEX.finditer(text)
    start = 0
    parts = []  # List[Tuple[str, Tuple[int, int]]]

    for match in st_matches:
        match_start = match.start()
        if match_start > start:
            parts.append((text[start:match_start], (start, match_start)))
        start = match.end()

    if start < len(text):
        parts.append((text[start:], (start, len(text))))

    return parts

def extract_date_strings_inner(text, text_start=0, strict=False):
    """
    Extends extract_date_strings by text_start parameter: used in recursive calls to
    store true text coordinates in output
    """

    # Try to find ranges first
    rng = split_date_range(text)
    if rng and len(rng) > 1:
        range_strings = []
        for range_str in rng:
            range_strings.extend(
                extract_date_strings_inner(
                    range_str[0], text_start=range_str[1][0], strict=strict
                )
            )
        for range_string in range_strings:
            yield range_string
        return

    tokens = tokenize_string(text)
    items = merge_tokens(tokens)
    for match in items:
        match_str = match.match_str
        indices = (match.indices[0] + text_start, match.indices[1] + text_start)

        ## Get individual group matches
        captures = match.captures
        # time = captures.get('time')
        digits = captures.get("digits")
        # digits_modifiers = captures.get('digits_modifiers')
        # days = captures.get('days')
        months = captures.get("months")
        years = captures.get("years")
        # timezones = captures.get('timezones')
        # delimiters = captures.get('delimiters')
        # time_periods = captures.get('time_periods')
        # extra_tokens = captures.get('extra_tokens')

        if strict:
            complete = False
            if len(digits) == 3:  # 12-05-2015
                complete = True
            elif (len(months) == 1) and (
                    len(digits) == 2
            ):  # 19 February 2013 year 09:10
                complete = True
            elif (len(years) == 1) and (len(digits) == 2):  # 09/06/2018
                complete = True

            elif (
                    (len(years) == 1) and (len(months) == 1) and (len(digits) == 1)
            ):  # '19th day of May, 2015'
                complete = True

            if not complete:
                continue

        ## sanitize date string
        ## replace unhelpful whitespace characters with single whitespace
        match_str = re.sub(r"[\n\t\s\xa0]+", " ", match_str)
        match_str = match_str.strip(STRIP_CHARS)

        ## Save sanitized source string
        yield match_str, indices, captures



def tokenize_string(text):
        """
        Get matches from source text. Method merge_tokens will later compose
        potential date strings out of these matches.
        :param text: source text like 'the big fight at 2p.m. mountain standard time on ufc.com'
        :return: [(match_text, match_group, {match.capturesdict()}), ...]
        """
        items = []

        last_index = 0

        for match in DATE_REGEX.finditer(text):
            match_str = match.group(0)
            indices = match.span(0)
            captures = match.capturesdict()
            group = get_token_group(captures)

            if indices[0] > last_index:
                items.append((text[last_index : indices[0]], "", {}))
            items.append((match_str, group, captures))
            last_index = indices[1]
        if last_index < len(text):
            items.append((text[last_index : len(text)], "", {}))
        return items

def get_token_group(captures):
        for gr in ALL_GROUPS:
            lst = captures.get(gr)
            if lst and len(lst) > 0:
                return gr
        return ""


def merge_tokens(tokens):
        """
        Makes potential date strings out of matches, got from tokenize_string method.
        :param tokens: [(match_text, match_group, {match.capturesdict()}), ...]
        :return: potential date strings
        """
        MIN_MATCHES = 5
        fragments = []
        frag = DateFragment()

        start_char, total_chars = 0, 0

        for token in tokens:
            total_chars += len(token[0])

            tok_text, group, tok_capts = token[0], token[1], token[2]
            if not group:
                if frag.indices[1] > 0:
                    if frag.get_captures_count() >= MIN_MATCHES:
                        fragments.append(frag)
                frag = DateFragment()
                start_char = total_chars
                continue

            if frag.indices[1] == 0:
                frag.indices = (start_char, total_chars)
            else:
                frag.indices = (frag.indices[0], total_chars)  # -1

            frag.match_str += tok_text

            for capt in tok_capts:
                if capt in frag.captures:
                    frag.captures[capt] += tok_capts[capt]
                else:
                    frag.captures[capt] = tok_capts[capt]

            start_char = total_chars

        if frag.get_captures_count() >= MIN_MATCHES:  # frag.matches
            fragments.append(frag)

        for frag in fragments:
            for gr in ALL_GROUPS:
                if gr not in frag.captures:
                    frag.captures[gr] = []

        return fragments