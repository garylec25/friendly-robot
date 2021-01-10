input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Heart)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showIcon(IconNames.Sad)
})
basic.showString("A if even")
basic.showString("B ifodd")
basic.showNumber(randint(0, 100))
