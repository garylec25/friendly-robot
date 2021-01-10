def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
    basic.show_icon(1100)
    basic.show_string("A if even")
    basic.show_string("B if odd")
    basic.show_number(randint(0,100))
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    basic.show_icon(IconNames.SAD)
    basic.show_icon(1100)
    basic.show_string("A if even")
    basic.show_string("B if odd")
    basic.show_number(randint(0,100))
input.on_button_pressed(Button.B, on_button_pressed_b)



basic.show_string("A if even")
basic.show_string("B if odd")
basic.show_number(randint(0,100))


