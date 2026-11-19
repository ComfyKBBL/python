
class Television:
    """
    A class to represent a television device
    Attributes:
        MIN_VOLUME: Minimum volume at 0
        MAX_VOLUME: Maximum volume at 2
        MIN_CHANNEL: Minimum channel at 0
        MAX_CHANNEL: Maximum channel at 3
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
        Initialize variables
        """

        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Turns the power on or off
        """

        self.__status = not self.__status

    def mute(self):
        """
        Checks the status, and mutes/unmutes
        """

        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Checks and turns the channel up
        """

        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        Checks and turns the channel down
        """

        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """
        Checks and turns the volume up
        """

        if self.__status:
            self.__muted = False

            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Checks and turns the volume down
        """

        if self.__status:
            self.__muted = False

            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Calls everything together
        :return: Status of Power, Channel and Volume
        """

        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"