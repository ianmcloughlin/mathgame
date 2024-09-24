input.onButtonPressed(Button.A, function () {
    number1 = randint(1, 10)
    basic.showNumber(number1)
    operator = randint(1, 2)
    if (operator == 1) {
        basic.showString("+")
    } else {
        basic.showString("-")
    }
    number2 = randint(1, 10)
    basic.showNumber(number2)
    basic.showString("=")
})
input.onButtonPressed(Button.B, function () {
    if (operator == 1) {
        basic.showNumber(number1 + number2)
    } else if (false) {
        basic.showNumber(number1 - number2)
    }
})
let number2 = 0
let operator = 0
let number1 = 0
music.play(music.createSoundExpression(WaveShape.Sine, 2803, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
