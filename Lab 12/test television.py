

from television import Television


def setup_function():
    global tv
    tv = Television()


def teardown_function():
    global tv
    tv = None


def test_init():
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power():
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_mute():
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.mute()

    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_up():
    tv.power()

    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down():
    tv.power()

    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"

    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"


def test_volume_up():
    tv.power()

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down():
    tv.power()

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_up()
    tv.volume_up()

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"



