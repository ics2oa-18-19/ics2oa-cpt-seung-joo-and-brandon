import arcade
import time
import random

high_score = 0
scramble = ['L', 'L2', 'L*', 'R', 'R2', 'R*',  'D', 'D2', 'D*', 'B', 'B*', 'B2', 'F', 'F2', 'F*', 'U', 'U2', 'U*']

# Global variables: variable that works with everything
WIDTH = 640
HEIGHT = 480

# This is when you want to move the character
def update(delta_time):
   global high_score
   while len(scramble) < 21:
       random.shuffle(scramble)

       print(scramble)

       start = input("Press enter to start the time")

       print("SOLVE")

       begin = time.time()

       endtimer = input("Press enter to stop the timer")

       end = time.time()

       elapsed = end - begin

       elapsed = float(elapsed)

       elapsed = round(elapsed, 2)


       if high_score == 0:
           high_score = elapsed
           print('The high score is', high_score, "Seconds")

       if elapsed < high_score:
           print("You beat your high score!")
           difference = (round, 2)

       print("The time you took is", elapsed, "Seconds")

       f = open("guru99.txt", "w+")
       f.write(str(elapsed))
       f.close()
       print(elapsed)


def on_draw():
   arcade.start_render()
   # Draw in here...
   arcade.draw_circle_filled(100, 100, 25, arcade.color.BLUE)


def on_key_press(key, modifiers):
   pass


def on_key_release(key, modifiers):
   pass


def on_mouse_press(x, y, button, modifiers):
   pass

def on_mouse_release(x, y, button, modifiers):
   pass


def setup():
   arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
   arcade.set_background_color(arcade.color.WHITE)
   arcade.schedule(update, 1/60)

   # Override arcade window methods
   window = arcade.get_window()
   window.on_draw = on_draw
   window.on_key_press = on_key_press
   window.on_key_release = on_key_release
   window.on_mouse_press = on_mouse_press

   arcade.run()


if __name__ == '__main__':
   setup()

    


