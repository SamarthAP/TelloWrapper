import pygame
import Tello

def main():
    # initialize Tello 
    tello = Tello.Tello()
    speed = 60
    tello.connect_sdk()

    # initializes Pygame
    pygame.init()

    # sets the window title
    pygame.display.set_caption('Keyboard events')

    # sets the window size
    pygame.display.set_mode((400, 400))

    on = True

    while on:
        # gets a single event from the event queue
        for event in pygame.event.get():

            # if user closes pygame window 
            if event.type == pygame.QUIT:
                on = False
            
            # movement commands when key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    tello.send_rc_command(0, speed, 0, 0)
                elif event.key == pygame.K_s:
                    tello.send_rc_command(0, -speed, 0, 0)
                elif event.key == pygame.K_a:
                    tello.send_rc_command(-speed, 0, 0, 0)
                elif event.key == pygame.K_d:
                    tello.send_rc_command(speed, 0, 0, 0)
                elif event.key == pygame.K_t:
                    tello.takeoff()
                elif event.key == pygame.K_l:
                    tello.land()
                elif event.key == pygame.K_b:
                    on = False
            
            # when key is released stop moving tello
            if event.type == pygame.KEYUP:
                tello.send_rc_command(0, 0, 0, 0)
                    
    pygame.quit()


if __name__ == '__main__':
    main()