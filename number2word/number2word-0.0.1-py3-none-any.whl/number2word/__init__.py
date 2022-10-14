from typing import Union


class NumberToWords:
    def __init__(self):
        self.number_words = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven',
                             8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
                             14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
                             19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
                             70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred'}
        self.big_number_words = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion',
                                 'Sextillion', 'Septillion', 'Octillion', 'Nonillion', 'Decillion', 'Undecillion',
                                 'Duodecillion', 'Tredecillion', 'Quattuordecillion', 'Quindecillion', 'Sexdecillion',
                                 'Septendecillion', 'Octodecillion', 'Novemdecillion', 'Vigintillion', 'Unvigintillion',
                                 'Duovigintillion', 'Tresvigintillion', 'Quattuorvigintillion', 'Quinvigintillion',
                                 'Sesvigintillion', 'Septemvigintillion', 'Octovigintillion', 'Novemvigintillion',
                                 'Trigintillion', 'Untrigintillion', 'Duotrigintillion', 'Trestrigintillion',
                                 'Quattuortrigintillion', 'Quintrigintillion', 'Sestrigintillion',
                                 'Septentrigintillion', 'Octotrigintillion', 'Noventrigintillion', 'Quadragintillion']

    def number2word(self, number: str, use_and=False) -> str:
        # Split the number form its decimal point
        try:
            number, decimals = number.split('.')
        except ValueError:
            decimals = ''
        # Split numbers into groups of 3 in reverse order
        numbers = [number[-i - 1:-i - 4:-1][::-1] for i in range(0, len(number), 3)]
        words = []
        # If number too big end method
        if len(self.big_number_words) < len(numbers):
            print('number out of range')
            return ''
        # loop though all the groups of numbers and generate the corresponding words for that number
        for i, n in enumerate(numbers):
            nwords = self.small_number2word(n, use_and)
            if not nwords:
                continue
            # Add the corresponding suffix to the number
            words.append(f'{nwords} {self.big_number_words[i]}')
        # Reverse back the numbers and convert to string
        words.reverse()
        words = ' '.join(words)
        if not words:
            words = 'Zero'
        dwords = ''
        for i in decimals:
            dwords += ' '+self.number_words[int(i)]
        if dwords:
            dwords = ' point' + dwords
        return words + dwords

    def small_number2word(self, number: str, use_and=False) -> str:
        number = number.zfill(3)
        if number == '000':
            return ''
        dh = number[0]
        dt = number[1]
        do = number[2]
        words = ''

        if dh != '0':
            words += f'{self.number_words[int(number[0])]} {self.number_words[100]}'
            if dt + do == '00':
                return words
            else:
                words += ' and ' if use_and else ' '

        if dt != '1':
            words += self.number_words[int(dt) * 10] + '-' if dt != '0' else ''
            words += self.number_words[int(do)] if do != '0' else ''
            if words.endswith('-'):
                words = words[:-1]
            return words
        else:
            words += self.number_words[int('1' + do)]
            return words


def convert(number: Union[int, float, str], use_and=False):
    """
    Converts the given number to English words
    This Converter Supports up to 10^126-1

    Parameters
    ----------
    number : int, float, str
        The number to convert

    use_and : bool
        Rather to add 'and' between the hundreds and tens digit
    """
    return NumberToWords().number2word(str(number), use_and)


if __name__ == '__main__':
    print(convert(329509235923.1836290586320))
