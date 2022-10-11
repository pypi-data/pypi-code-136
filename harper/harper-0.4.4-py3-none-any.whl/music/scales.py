"""Scales are container classes that have a predefined set of notes."""
# import abc
# from harper.music import notes


# class Scale(object):
#     """Create a scale."""

#     def __init__(self, tonic, flavor, number, duration=0.25):
#         self._tonic = tonic
#         self._flavor = flavor
#         self._number = number
#         self._note_duration = duration

#         self._idx = 0

#     @property
#     def tonic(self):
#         return getattr(notes, f"{self._tonic}{self._number}")

#     @property
#     def supertonic(self):
#         pass

#     @property
#     def mediant(self):
#         pass

#     @property
#     def subdominant(self):
#         pass

#     @property
#     def dominant(self):
#         pass

#     @property
#     def submediant(self):
#         pass

#     @property
#     def leading_note(self):
#         pass

#     @property
#     @abc.abstractmethod
#     # theres probalby a real word for this. i mean the sort of
#     # 'canonical' notes that make up the scale, as opposed to the
#     # _instance_ of notes (class vs. instance, eg)
#     def canon(self):
#         pass

#     @property
#     def notes(self):
#         return [n(self.note_duration) for n in self.canon]

#     def __iter__(self):
#         self._idx = 0
#         return self

#     def __next__(self):
#         if self._idx < len(self.notes):
#             now = self.notes[self._idx]
#             self._idx += 1
#             return now
#         else:
#             raise StopIteration
#
