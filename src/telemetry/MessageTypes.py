from enum import Enum, auto

class MessageTypes(Enum):
    TURN_SW_ON      = auto()
    SW_ON           = auto()
    GPS_ON          = auto()
    STATUS          = auto()
    CAPTURING_READY = auto()
    START_CAPTURING = auto()
    CAPTURING_ON    = auto()
    STOP_CAPTURING  = auto()
    CAPTURING_OFF   = auto()
    TURN_SW_OFF     = auto()
    KILL_SW         = auto()
    SW_OFF          = auto()
    GPS_OFF         = auto()