import pygame
import sys

class Pong:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pong Game")

        self.pong_icon = pygame.image.load("resources/images/icons/ping-pong.png")
        pygame.display.set_icon(self.pong_icon)

        self.screen = pygame.display.set_mode((800, 600))
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.clock = pygame.time.Clock()
        
        self.player_weidth = 20
        self.player_height = 120
        self.player_positions = [[30, (self.screen_height - self.player_height)/2], [self.screen_width - 50, (self.screen_height - self.player_height)/2]]
        self.player_movement = [[False, False], [False, False]]

        self.ball_weidth = 20
        self.ball_height = 20
        self.ball_position = [self.screen_width/2 - 10, self.screen_height/2 -10]
        self.ball_movement = []

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player_movement[0][0] = True
                    if event.key == pygame.K_s:
                        self.player_movement[0][1] = True
                    if event.key == pygame.K_UP:
                        self.player_movement[1][0] = True
                    if event.key == pygame.K_DOWN:
                        self.player_movement[1][1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.player_movement[0][0] = False
                    if event.key == pygame.K_s:
                        self.player_movement[0][1] = False
                    if event.key == pygame.K_UP:
                        self.player_movement[1][0] = False
                    if event.key == pygame.K_DOWN:
                        self.player_movement[1][1] = False

            self.screen.fill((0,0,0))

            left_player = pygame.Rect(*self.player_positions[0], self.player_weidth, self.player_height)
            right_player = pygame.Rect(*self.player_positions[1], self.player_weidth, self.player_height)
            game_ball = pygame.Rect(*self.ball_position, self.ball_weidth, self.ball_height)

            self.player_positions[0][1] +=  (self.player_movement[0][1] - self.player_movement[0][0])*8
            self.player_positions[1][1] +=  (self.player_movement[1][1] - self.player_movement[1][0])*8

            pygame.draw.rect(self.screen, (255, 255, 255), left_player)
            pygame.draw.rect(self.screen, (255, 255, 255), game_ball)
            pygame.draw.rect(self.screen, (255, 255, 255), right_player)

            pygame.display.update()
            self.clock.tick(60)

Pong().run()