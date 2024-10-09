import pygame

pygame.init() # 반드시 필요한 초기화 과정

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("pygame_basic") # 게임 이름

# FPS(Frame Per Second)
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기
character_x_pos = screen_width / 2 - character_width / 2 # 캐릭터의 가로 위치
character_y_pos = screen_height - character_height # 캐릭터의 세로 위치
# 위치 시작 좌표는 좌상단 꼭지점

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(10) # 게임화면의 초당 프레임 수를 설정
    # print(str(clock.get_fps()))로 fps 확인
    # 캐릭터가 1초 동안 100만큼 이동해야할 때
    # 10 fps : 1초 동안 10번 동작 -> 1번에 10만큼 이동해야 10*10=100이 나온다.
    # 20 fps : 1초 동안 20번 동작 -> 1번에 5만큼 이동해야 5*20=100이 나온다.

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가? 지켜보고 있다.
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 왼쪽 이동
                to_x -= character_speed
            if event.key == pygame.K_RIGHT: # 오른쪽 이동
                to_x += character_speed
            if event.key == pygame.K_UP: # 위로 이동
                to_y -= character_speed
            if event.key == pygame.K_DOWN: # 아래로 이동
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # 방향키 떼면 멈춤(0을 더한다)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x * dt # fps에 속도가 영향을 받으면 안 됨
    character_y_pos += to_y * dt # dt를 곱함
    
    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    
    screen.blit(background, (0, 0)) # 배경 그리기
    # screen.fill((0, 0, 255))도 가능
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 화면을 계속 그리기

# while루프를 탈출하고 pygame 종료
pygame.quit()