import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\a00559075\\Desktop\\나도코딩_오락실\\pygame_basic\\background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 파이게임 시작하려면 무조건 적어야함 / 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    # screen.fill((0, 0, 255)) # RGB
    screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update() # 게임 화면을 다시 그리기 / 반드시 계속해서 호출이 되어야함.

# pygame 종료
pygame.quit()