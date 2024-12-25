import pygame as pg

# Инициализация pg
pg.init()

# Размеры окна
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550
ICON_SIZE = 100
PENDING = 5

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60

font = pg.font.Font(None, 40)
mini_font = pg.font.Font(None, 15)

def load_image(image1, width, height):
    picture = pg.image.load(image1).convert_alpha()
    picture = pg.transform.scale(picture, (width, height))
    return picture

def text_render(text):
    return font.render(str(text), True, "black")

class Button:
    def __init__(self,text, x, y, width = BUTTON_WIDTH, height = BUTTON_HEIGHT, text_font = font):
        self.button = load_image("button.png", width, height)
        self.button_clicked =load_image("button_clicked.png", width, height)

        self.is_pressed = False

        self.knopka = self.button
        self.knopka_rect = self.knopka.get_rect()
        self.knopka_rect.topleft = (x, y)

        self.text_font = text_font
        self.text = text_font.render(str(text), True, "black")
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.knopka_rect.center



    def draw(self, screen):
        screen.blit(self.knopka, self.knopka_rect)
        screen.blit(self.text, self.text_rect)

    def update(self):
        mouse_pos = pg.mouse.get_pos()
        if self.knopka_rect.collidepoint(mouse_pos):
            if self.is_pressed:
                self.knopka = self.button_clicked
            else:
                self.knopka = self.button

    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.knopka_rect.collidepoint(event.pos):
                self.is_pressed = True
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.is_pressed = False

class Game:
    def __init__(self):

        # Создание окна
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")

        self.background = load_image("background.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        self.happiness = load_image("happiness.png", ICON_SIZE, ICON_SIZE)
        self.health = load_image("health.png", ICON_SIZE, ICON_SIZE)
        self.satiety = load_image("satiety.png", ICON_SIZE, ICON_SIZE)

        self.money = load_image("money.png", ICON_SIZE, ICON_SIZE)

        button_x = SCREEN_WIDTH - BUTTON_WIDTH - PENDING
        self.eat_button = Button("Еда", button_x, ICON_SIZE + PENDING)
        self.clothes_button = Button("Одежда", button_x, ICON_SIZE + 2*PENDING + BUTTON_HEIGHT)
        self.games_button = Button("Игра", button_x, ICON_SIZE + 3*PENDING + BUTTON_HEIGHT * 2)

        self.upgrade_button = Button("Улучшение", SCREEN_WIDTH - ICON_SIZE, 0,
                                     width=BUTTON_WIDTH // 3, height=BUTTON_HEIGHT // 3,
                                     text_font=mini_font)

        self.buttons = [self.eat_button, self.clothes_button, self.games_button, self.upgrade_button]


        self.dog = load_image("Dog.png", 310, 500)

        self.health_points = 100
        self.happiness_points = 100
        self.satiety_points = 100


        self.money_points = 10



        self.INCREASE_COINS = pg.USEREVENT + 1
        pg.time.set_timer(self.INCREASE_COINS, 1000)

        self.run()

    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type ==self.INCREASE_COINS:
                self.money_points += 2

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.money_points += 1

            for e in self.buttons:
                e.is_clicked(event)


    def update(self):
        for e in self.buttons:
            e.update()


    def draw(self):
        pg.display.flip()
        self.screen.blit(self.background, (0,0))

        self.screen.blit(self.happiness, (PENDING, PENDING))
        self.screen.blit(text_render(self.happiness_points),(PENDING + ICON_SIZE, PENDING * 8))
        self.screen.blit(self.health, (PENDING, PENDING + 200))
        self.screen.blit(text_render(self.health_points), (PENDING + ICON_SIZE, (PENDING * 8) * 6))
        self.screen.blit(self.satiety, (PENDING, PENDING + 100))
        self.screen.blit(text_render(self.satiety_points), (PENDING + ICON_SIZE, (PENDING * 8) * 3.5))

        self.screen.blit(self.money, (SCREEN_HEIGHT + 250, PENDING))
        self.screen.blit(text_render(self.money_points), (SCREEN_HEIGHT + 220, PENDING + 35))

        for e in self.buttons:
            e.draw(self.screen)

        self.screen.blit(self.dog, (300, 100))


if __name__ == "__main__":
    Game()
