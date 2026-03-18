import pygame
import sys

pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wall Collision")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 원의 초기 설정
circle_x = 400
circle_y = 300
circle_radius = 30
speed = 7

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -= speed
    if keys[pygame.K_RIGHT]:
        circle_x += speed
    if keys[pygame.K_UP]:
        circle_y -= speed
    if keys[pygame.K_DOWN]:
        circle_y += speed

    # 2. [추가] 화면 경계 제한 처리
    # X축 (가로) 제한: 원의 반지름(circle_radius)만큼 여유를 줍니다.
    if circle_x < circle_radius:
        circle_x = circle_radius
    if circle_x > screen_width - circle_radius:
        circle_x = screen_width - circle_radius

    # Y축 (세로) 제한
    if circle_y < circle_radius:
        circle_y = circle_radius
    if circle_y > screen_height - circle_radius:
        circle_y = screen_height - circle_radius

    # 3. 그리기
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (circle_x, circle_y), circle_radius)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()