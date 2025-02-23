import pygame

pygame.init() #обязательная команда
window_size=(300, 300)
screen=pygame.display.set_mode(window_size) #создание окна размером 300 на 300
pygame.display.set_caption('Моя игра')
background_color = (0, 0, 225) #создаем цвет фона (синий)
screen.fill(background_color) #залить фон цвет
clock = pygame.time.Clock() #создание игрового таймера (фпс)
while True: #игровой цикл
    clock.tick(40) #частота обновления сцены (40 кдр/сек)
    pygame.display.update() #обновление содержимого экрана