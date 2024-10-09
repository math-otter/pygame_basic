import pygame
import random

# 기본 초기화 과정: 반드시 필요
pygame.init()

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 폰트 설정
game_font = pygame.font.Font(None, 40) # 종류(기본값: None), 사이즈 

# 캐릭터 설정
character = pygame.image.load("character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height
character_speed = 1

# 적 설정
enemy = pygame.image.load("enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

# 시간 설정
total_time = 100
start_ticks = pygame.time.get_ticks()

# 배경 설정
background = pygame.image.load("background.png")

# FPS 설정
clock = pygame.time.Clock()

# 게임 루프
running = True
while running:
    dt = clock.tick(30)

    # 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        
        # 닫기를 누르면 게임을 종료
        if event.type == pygame.QUIT:
            running = False
        
        # 키보드를 누를 때 캐릭터 이동
        to_x = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        # 키보드를 뗄 때 캐릭터 멈춤
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    
    # 캐릭터의 좌표 조정
    character_x_pos += to_x * dt
    
    # 캐릭터의 좌표를 화면 내부로 제한
    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 적의 좌표 조정
    enemy_y_pos += enemy_speed
    
    # 적의 좌표가 맨 아래에 도달할 시 재조정
    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 충돌 이벤트를 위한 캐릭터, 적의 충돌 박스 정보 가져오기
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 이벤트 정의
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False

    # 타이머 설정
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False

    # 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(timer, (10, 10))
    pygame.display.update()

# 게임 종료 전 대기
pygame.time.delay(1000)

# 게임 종료
pygame.quit()