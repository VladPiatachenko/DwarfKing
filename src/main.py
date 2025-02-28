import pygame
import random
import os

# Ініціалізація Pygame
pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 800, 600
TOKEN_RADIUS = 30
DICE_SIZE = 50
DICE_SPACING = 10
SEASONS = ["Spring", "Summer", "Autumn", "Winter"]
MONTHS_PER_SEASON = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dwarf Resource Gathering Game")

# Завантаження зображень
background = pygame.image.load("resources/background/back.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
button_background = pygame.image.load("resources/background/roll.jpg")
button_background = pygame.transform.scale(button_background, (150, 50))
dice_background = pygame.image.load("resources/background/dice.jpg")
dice_background = pygame.transform.scale(dice_background, (DICE_SIZE, DICE_SIZE))

# Завантаження токенів
token_images = [
    pygame.image.load("resources/token/1.png"),
    pygame.image.load("resources/token/2.png")
]

# Масштабуємо токени під потрібний розмір
token_images = [pygame.transform.scale(img, (TOKEN_RADIUS * 2, TOKEN_RADIUS * 2)) for img in token_images]

dice_results = []
resource_spots = [(300, 200), (400, 250), (500, 200), (450, 350), (350, 350), (550, 300), (250, 300)]
token_pool = [{'pos': (100 + i * 60, 550), 'image': random.choice(token_images)} for i in range(5)]
placed_tokens = []
season_index = 0
month_index = 1
rolling_phase = True
field_dice = []


def roll_dice():
    """Кидає 7 шестигранних кубиків і розподіляє їх по полях"""
    global dice_results, field_dice, rolling_phase
    dice_results = [random.randint(1, 6) for _ in range(7)]
    field_dice = [(pos, random.choice(dice_results)) for pos in resource_spots]
    rolling_phase = False  # Блокування кнопки кидка


def draw_interface():
    """Малює ігровий інтерфейс"""
    screen.blit(background, (0, 0))

    # Відображення сезону та місяця
    font = pygame.font.Font(None, 40)
    season_text = font.render(f"{SEASONS[season_index]}: {month_index}", True, (255, 255, 255))
    screen.blit(season_text, (50, 50))

    # Відображення кількості вільних гномів
    free_dwarfs_text = font.render(f"Free Dwarfs: {len(token_pool)}", True, (255, 255, 255))
    screen.blit(free_dwarfs_text, (50, 500))

    # Відображення результатів кубиків
    dice_x, dice_y = 680, 150
    positions = [
        (dice_x, dice_y), (dice_x + DICE_SIZE + DICE_SPACING, dice_y),
        (dice_x, dice_y + DICE_SIZE + DICE_SPACING),
        (dice_x + DICE_SIZE + DICE_SPACING, dice_y + DICE_SIZE + DICE_SPACING),
        (dice_x, dice_y + 2 * (DICE_SIZE + DICE_SPACING)),
        (dice_x + DICE_SIZE + DICE_SPACING, dice_y + 2 * (DICE_SIZE + DICE_SPACING)),
        (dice_x + DICE_SIZE // 2, dice_y + 3 * (DICE_SIZE + DICE_SPACING))
    ]

    for i, result in enumerate(dice_results):
        screen.blit(dice_background, positions[i])  # Використовуємо бекграунд для кубика
        text = font.render(str(result), True, (0, 0, 0))
        text_rect = text.get_rect(center=(positions[i][0] + DICE_SIZE // 2, positions[i][1] + DICE_SIZE // 2))
        screen.blit(text, text_rect)

    # Кнопка кидка кубиків (блокується після кидка)
    if rolling_phase:
        button_x, button_y = 650, 100
        screen.blit(button_background, (button_x, button_y))
        roll_text = font.render("Roll Dice", True, (0, 0, 0))
        screen.blit(roll_text, (button_x + 35, button_y + 10))

    # Відображення місць збору ресурсів та їхніх чисел
    for pos, dice_value in field_dice:
        pygame.draw.circle(screen, (0, 0, 255), pos, TOKEN_RADIUS)
        dice_text = font.render(str(dice_value), True, (255, 255, 255))
        screen.blit(dice_text, (pos[0] - 10, pos[1] - 10))

    # Відображення токенів у пулі
    for token in token_pool:
        screen.blit(token['image'], token['pos'])

    # Відображення токенів, розміщених на ресурсних полях
    for token in placed_tokens:
        screen.blit(token['image'], token['pos'])


# Основний цикл гри
running = True
selected_token = None
while running:
    screen.fill((0, 0, 0))
    draw_interface()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Кидок кубиків (дозволено тільки в фазі кидка)
            if rolling_phase and 600 <= x <= 750 and 100 <= y <= 150:
                roll_dice()
            # Вибір токена з пулу (тільки якщо не фаза кидка)
            if not rolling_phase:
                for token in token_pool[:]:
                    tx, ty = token['pos']
                    if tx <= x <= tx + TOKEN_RADIUS * 2 and ty <= y <= ty + TOKEN_RADIUS * 2:
                        selected_token = token
                        token_pool.remove(token)
                        break
                # Переміщення токенів на поле
                if selected_token:
                    for pos, dice_value in field_dice:
                        if (x - pos[0]) ** 2 + (y - pos[1]) ** 2 <= TOKEN_RADIUS ** 2:
                            placed_tokens.append({'pos': pos, 'image': selected_token['image']})
                            selected_token = None
                            break

    pygame.display.flip()

pygame.quit()