import pygame
import random

_py_x = 1000
_py_y = 500
galaxy = [(250,250),(750,250)]

pygame.init()
bo = pygame.image.load("image\\bo.png")
jja = pygame.image.load("image\\jja.png")
gimchi = pygame.image.load("image\\gimchi.png")
pi = pygame.image.load("image\\pi.png")
chi = pygame.image.load("image\\chi.png")
ca = pygame.image.load("image\\ca.png")
udong = pygame.image.load("image\\udong.png")
pa = pygame.image.load("image\\pa.png")
la = pygame.image.load("image\\la.png")
deop = pygame.image.load("image\\deop.png")
sam = pygame.image.load("image\\sam.png")
cho = pygame.image.load("image\\cho.png")
nang = pygame.image.load("image\\nang.png")
ham = pygame.image.load("image\\ham.png")
don = pygame.image.load("image\\don.png")
gug = pygame.image.load("image\\gug.png")
sixteen = [bo,jja,gimchi,pi,chi,ca,udong,pa,la,deop,sam,cho,nang,ham,don,gug]
random.shuffle(sixteen)
eight = []
four = []
final = []
gamepad = pygame.display.set_mode((_py_x,_py_y)) # 창띄우는 코드
_state = 1 # 게임상태 분류
first_pic = []
second_pic = []

def startgame():
    while True:
        #events = pygame.event.get() # 발생하는 이벤트를 처리하는 코드
        while _state == 1:
            events = pygame.event.get()
            for event in events:

                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                #if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_UP:
                    #    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for _mouse_pos in galaxy:
                        if first_rect.collidepoint(event.pos):
                            exit()



            if len(first_pic) == 0 and len(second_pic) == 0:
                first_pic.append(sixteen.pop(0))
                first_rect = first_pic[0].get_rect(center=galaxy[0])
                second_pic.append(sixteen.pop(0))
                second_rect = second_pic[0].get_rect(center=galaxy[1])
            gamepad.blit(first_pic[0],first_rect) # 그릴 이미지 , 그릴 위치 [300,200]
            gamepad.blit(second_pic[0],second_rect)
            pygame.display.update()

        pygame.display.update()


startgame()