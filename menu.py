import pygame
import sys
import os

pygame.init()  #pygame initialization
DISPLAY = (1200, 800)  #display width and height
screen = pygame.display.set_mode(DISPLAY)  #setting display width and height
pygame.display.set_caption("MaDaM")  #display title

#colors used in menu
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (169, 169, 169)
BLUE = (0, 122, 204)
LIGHT_BLUE = (0, 162, 255)

# font used in menu
font_path = os.path.join('fonts', 'comicate.ttf')
font = pygame.font.Font(font_path, 74)

# background
background_path = os.path.join('images', 'menu-background.jpg')  # setting backgournd image path
background = pygame.image.load(background_path)  # load background image
background = pygame.transform.scale(background, DISPLAY)  # background image scaling


# definition button class
class Button:
    def __init__(self, text, pos, font, text_color=BLACK, hover_text_color=WHITE, bg_color=GRAY,
                 hover_bg_color=DARK_GRAY, border_color=BLACK):
        self.x, self.y = pos  # button position
        self.font = font  # button font
        self.text = text  # button text
        self.text_color = text_color  # button text color
        self.hover_text_color = hover_text_color  # button hover text color
        self.bg_color = bg_color  # button background color
        self.hover_bg_color = hover_bg_color  # button hover background color
        self.border_color = border_color  # button border color
        self.change_text()  # formatting the button

    def change_text(self):
        self.rendered_text = self.font.render(self.text, True,
                                              self.text_color)  #rendering text from defined text, font and text color
        self.rect = self.rendered_text.get_rect(center=(self.x, self.y))  #creating a rect surrounding the button text
        self.surface = pygame.Surface((self.rect.width + 20, self.rect.height + 20))  #rect padding 20px
        self.surface.fill(self.bg_color)  #filling the background with color
        self.rect_surface = self.surface.get_rect(center=(self.x, self.y))  #centering the rect

    def show(self):
        mouse_pos = pygame.mouse.get_pos()  #setting the mouse_pos value with current mouse position
        if self.rect_surface.collidepoint(mouse_pos):  #if mouse is inside of the rect
            text_surface = self.font.render(self.text, True, self.hover_text_color)  #hover text formatting
            bg_color = self.hover_bg_color  #hover background formatting
        else:
            text_surface = self.rendered_text  #no hover text formatting
            bg_color = self.bg_color  #no hover background formatting
        self.surface.fill(bg_color)  #fill the rect with background color
        pygame.draw.rect(self.surface, self.border_color, self.surface.get_rect(), 2)  #creating a button border
        self.surface.blit(text_surface, text_surface.get_rect(center=(
            self.surface.get_width() // 2, self.surface.get_height() // 2)))  #display rendered text and centering
        screen.blit(self.surface, self.rect_surface.topleft)  #display the rect surrounding the text

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect_surface.collidepoint(
                event.pos):  #checking whether the button was clicked with the mouse within it
            return True
        return False


def main_menu():
    buttons = [
        Button("Start", (DISPLAY[0] // 2, DISPLAY[1] - 650), font),  #defining start button
        Button("About", (DISPLAY[0] // 2, DISPLAY[1] - 550), font),  #defining about button
        Button("Instructions", (DISPLAY[0] // 2, DISPLAY[1] - 450), font),  #defining instructions button
        Button("Quit", (DISPLAY[0] // 2, DISPLAY[1] - 350), font)  #defining quit button
    ]

    while True:
        screen.blit(background, (0, 0))  #draw menu background
        for button in buttons:
            button.show()  #draw all of the buttons

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                if button.click(event):
                    if button.text == "Start":
                        import main  #start the game by import main module
                        main.main()
                    elif button.text == "About":
                        print("trzeba dodać info o nas")  #about us
                    elif button.text == "Instructions":
                        print("trzeba dodać instrukcję")  #instruction
                    elif button.text == "Quit":
                        pygame.quit()
                        sys.exit()  #pls dont click it

        pygame.display.update()


if __name__ == "__main__":
    main_menu()
