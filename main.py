def on_button_pressed_a():
    global number1, operator, number2
    number1 = randint(1, 10)
    basic.show_number(number1)
    operator = randint(1, 2)
    if operator == 1:
        basic.show_string("+")
    else:
        basic.show_string("-")
    number2 = randint(1, 10)
    basic.show_number(number2)
    basic.show_string("=")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if operator == 1:
        basic.show_number(number1 + number2)
    else:
        basic.show_number(number1 - number2)
input.on_button_pressed(Button.B, on_button_pressed_b)

number2 = 0
operator = 0
number1 = 0
music.play(music.create_sound_expression(WaveShape.SINE,
        2803,
        0,
        255,
        0,
        500,
        SoundExpressionEffect.NONE,
        InterpolationCurve.LINEAR),
    music.PlaybackMode.UNTIL_DONE)