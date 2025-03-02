import pygame.time

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
    for event in pygame.event.get(): #проходимся по событиям
        if event.type == pygame.QUIT: #если нажать на крестик
            pygame.QUIT() #выход из игры
    screen.fill((225, 225, 225)) #заливка фона
    r = pygame.Rect(150, 150, 100, 50) #создание прямоугольника
    pygame.draw.rect(screen, (0, 0, 0), r) #цвет прямоугольника
    rad = 10
    pygame.draw.circle(screen, (0, 225, 225), (50, 100), rad) #создание круга
    pygame.display.update()