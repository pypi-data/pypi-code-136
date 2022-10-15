# manuscriptify
# Compile google docs into a manuscript
# Copyright (c) 2022 Manuscriptify
# Open source, MIT license: http://www.opensource.org/licenses/mit-license.php
"""
file formatter

"""


class Formatter:

    @staticmethod
    def matter():
        """define the text style"""
        text_style = {
            'fontSize': {
                'magnitude': 12,
                'unit': 'PT'
            },
            'weightedFontFamily': {
                'fontFamily': 'Times New Roman'
            }
        }
        return text_style

    @staticmethod
    def paragraph():
        """define the paragraph style"""
        paragraph_style = {
            'indentFirstLine': {
                'magnitude': 36,
                'unit': 'PT'
            },
            'lineSpacing': 200
        }
        return paragraph_style

    @staticmethod
    def first_paragraph():
        """define the style of first para in seciotn"""
        return {
            'lineSpacing': 200
        }

    @staticmethod
    def heading():
        """define the chapter heading style"""
        heading_style = {
            'pageBreakBefore': True,
            'borderTop': {
                'width': {
                    'magnitude': 0,
                    'unit': 'PT'
                },
                'padding': {
                    'magnitude': 216,
                    'unit': 'PT'
                },
                'dashStyle': 'SOLID'
            },
            'alignment': 'center',
            'lineSpacing': 200
        }
        return heading_style

    @staticmethod
    def subheading():
        """define the chapter subheading style"""
        return {
            'alignment': 'center',
            'lineSpacing': 400
        }

    @staticmethod
    def address():
        """define the address style"""
        return {
            'lineSpacing': 115
        }

    @staticmethod
    def title():
        """title style for title page"""
        heading_style = {
            'borderTop': {
                'width': {
                    'magnitude': 0,
                    'unit': 'PT'
                },
                'padding': {
                    'magnitude': 180,
                    'unit': 'PT'
                },
                'dashStyle': 'SOLID'
            },
            'alignment': 'center',
            'lineSpacing': 400
        }
        return heading_style

    @staticmethod
    def subtitle():
        """subtitle style for title page"""
        return {
            'alignment': 'center',
            'lineSpacing': 2400
        }

    @staticmethod
    def prologue():
        """define the prologue/epilogue style"""
        prologue_style = {
            'pageBreakBefore': True,
            'borderTop': {
                'width': {
                    'magnitude': 0,
                    'unit': 'PT'
                },
                'padding': {
                    'magnitude': 216,
                    'unit': 'PT'
                },
                'dashStyle': 'SOLID'
            },
            'alignment': 'center',
            'lineSpacing': 400
        }
        return prologue_style

    @staticmethod
    def section():
        """define the section style"""
        return {
            'alignment': 'center',
            'lineSpacing': 200
        }

    @staticmethod
    def ending():
        """define the style for THE END"""
        ending_style = {
            'borderTop': {
                'width': {
                    'magnitude': 0,
                    'unit': 'PT'
                },
                'padding': {
                    'magnitude': 36,
                    'unit': 'PT'
                },
                'dashStyle': 'SOLID'
            },
            'alignment': 'center'
        }
        return ending_style

    @staticmethod
    def right():
        """define the right-aligned style"""
        return {
            'alignment': 'end' # seriously!
        }
