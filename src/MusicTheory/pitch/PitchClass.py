import collections
from Framework.ConstMeta import ConstMeta
"""
半音数からピッチクラスと相対オクターブを取得する。
"""
class PitchClass(metaclass=ConstMeta):
    __PitchClass = collections.namedtuple('PitchClass', ['PitchClass', 'RelativeOctave'])
    MaxPitchClass = 11
    MinPitchClass = 0

    @classmethod
    def Get(cls, halfToneNum:int):
        pitchClass = halfToneNum % (cls.MaxPitchClass+1)
        relativeOctave = halfToneNum // (cls.MaxPitchClass+1)
        if pitchClass < cls.MinPitchClass:
            pitchClass += (cls.MaxPitchClass+1)
        return cls.__PitchClass(pitchClass, relativeOctave)

