class ChangeLogException(Exception): pass
class UnsupportedTagException(ChangeLogException): pass
class UnCorrectTitleException(ChangeLogException): pass
class UnDetectLine(ChangeLogException): pass
class MissChangeBlock(ChangeLogException): pass
class UnKnownVersionAppendText(ChangeLogException): pass

class MissedVersionsSymbolException(ChangeLogException): pass
class NotDetectVersionException(ChangeLogException): pass
class VersionOverTextException(ChangeLogException): pass
class VersionDateConvertException(ChangeLogException): pass
