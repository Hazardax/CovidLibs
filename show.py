import pygame
from Window import Window
from Surface import Surface
from Button import Button
from Text import Text


def main():
    # Теперь в окне не обязательно указывать его название
    window = Window(1280, 720)

    # Создаёт холст, позволяющий редактировать его и объекты на нём легче, чем в обычном холсте.
    surface = Surface(0, 0, 1280, 720)

    # Создание кнопки
    button = Button(200, 200, 200, 100)

    # Создаём и задаём цвет + прозрачность текста
    text = Text(200, 100, 20)
    text.set_color((255, 0, 0, 255))

    # Окно открыто, пока мы его не закроем по нажатию на крестик или кнопки Escape
    run = True
    while run:
        # Обработка действий пользователя
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Выход из цикла по нажатию крестика
                run = False
            elif event.type == pygame.KEYDOWN:  # Выход из цикла по нажатию Escape'а
                if event.key == pygame.K_ESCAPE:
                    run = False

        # Заполняем каждый кадр цветом, чтобы заливать предыдущий
        window.fill((0, 0, 0))

        # Говорим на чём рисовать холст
        surface.draw(window)

        # Вместо косвенной передачи поверхности через окно (button.draw(window))
        # можно передать саму поверхность, что оптимизирует код и делает его читаемым
        button.draw(surface)

        # Выводим текст на экран (по умолчанию выведится "text")
        text.print(window)

        # Обновляем окно через буффер и выводим на экран
        window.update()
    window.close()


if __name__ == '__main__':
    main()
