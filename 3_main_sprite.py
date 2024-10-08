import pygame

pygame.init() # 반드시 필요한 초기화 과정

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("pygame_basic") # 게임 이름

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

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
    
    screen.blit(background, (0, 0)) # 배경 그리기
    # screen.fill((0, 0, 255))도 가능
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 화면을 계속 그리기

# while루프를 탈출하고 pygame 종료
pygame.quit()