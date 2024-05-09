def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . # . # .
        # . . . #
        . # # # .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    music.play(music.string_playable("C5 B A G F E B C5 ", 240),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
