import pygame 
from pygame.locals import *
from Dificuldade import continuar_dificuldade

class Player(pygame.sprite.Sprite):
    #construtor da classe
    def __init__(self, player_velocity, SCREEN_HEIGHT,SCREEN_WIDTH, plataforma_height, dificuldade):
        #iniciando o contrutor da classe sprite que está dentro do pygame
        pygame.sprite.Sprite.__init__(self)

        self.SCREEN_WIDTH = SCREEN_WIDTH

        self.player_position_x = 300 #começando no meio da tela
        self.player_position_y = SCREEN_HEIGHT - plataforma_height - 75 * 2
        #variavel que vai guardar a velocidade do player
        #é nada mais que a quantidade de px que ele vai andar por ação
        self.player_velocity = player_velocity
        #variavel que contém as sprites do player
        #(é um array pois quando tivermos animação será várias imagens)

        if dificuldade == "Easy":
            self.sprites = [
                pygame.image.load('assets/player/easy/cariani_easy.png'),
                pygame.image.load('assets/player/easy/cariani_easy1.png'),
                pygame.image.load('assets/player/easy/cariani_easy2.png'),
                pygame.image.load('assets/player/easy/cariani_easy1.png'),
            ]

        elif dificuldade == "Medium":
            self.sprites = [
                pygame.image.load('assets/player/medium/cariani_medium.png'),
                pygame.image.load('assets/player/medium/cariani_medium1.png'),
                pygame.image.load('assets/player/medium/cariani_medium2.png'),
                pygame.image.load('assets/player/medium/cariani_medium1.png'),
            ]

        elif dificuldade == "Hard":
            self.sprites = [pygame.image.load('assets/player/hard/cariani_hard.png'),
                            pygame.image.load('assets/player/hard/cariani_hard1.png')]

        #variavel que guarda a posição da imagem atual
        self.current_sprite = 0
        self.animation_velocity = 0.02
        #instanciando nosso player
        self.image = self.sprites[self.current_sprite]
        #mudando a escala dele para 1.5x
        self.player_width = 130
        self.player_height = 110
        # self.image = pygame.transform.scale(self.image, (self.player_width, self.player_height))
        self.turn_left = True
        #colocando nosso player como um objeto em cena e definindo sua posição
        self.rect = self.image.get_rect()
        self.rect.topleft = self.player_position_x, self.player_position_y

    #função que roda a cada frame
    def update(self):
        #atualizando a posição do player, aso tenha mudado
        self.rect.topleft = self.player_position_x, self.player_position_y

        if (pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]) and self.player_position_x > -20: 
            self.player_position_x -= self.player_velocity
            self.turn_left = True
        if (pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]) and self.player_position_x < self.SCREEN_WIDTH - self.player_width: 
            self.player_position_x += self.player_velocity 
            self.turn_left = False

        if int(self.current_sprite + self.animation_velocity) < len(self.sprites):
            self.current_sprite += self.animation_velocity
        else:
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

        if not self.turn_left:
            self.image = pygame.transform.flip(self.sprites[int(self.current_sprite)], True, False)

        #verificando se há colisão com a bolinha
    def get_rect(self):
        return self.rect