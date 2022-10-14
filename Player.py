import pygame 
from pygame.locals import *
from Halter import Halter


class Player(pygame.sprite.Sprite):
    #construtor da classe
    def __init__(self, SCREEN_HEIGHT, plataforma_height,  generate_random_position):
        #iniciando o contrutor da classe sprite que está dentro do pygame
        pygame.sprite.Sprite.__init__(self)

        self.player_position_x = 0
        self.player_position_y = SCREEN_HEIGHT - plataforma_height - 61 * 1.5
        #variavel que vai guardar a velocidade do player
        #é nada mais que a quantidade de px que ele vai andar por ação
        self.player_velocity = 2
        self.generate_random_position =  generate_random_position
        #variavel que contém as sprites do player
        #(é um array pois quando tivermos animação será várias imagens)
        self.sprites = [pygame.image.load('assets/player/cariani.png')]

        #variavel que guarda a posição da imagem atual
        self.current_sprite = 0

        #instanciando nosso player
        self.image = self.sprites[self.current_sprite]
        #mudando a escala dele para 1.5x
        self.image = pygame.transform.scale(self.image, (50*1.5, 61*1.5))

        #colocando nosso player como um objeto em cena e definindo sua posição
        self.rect = self.image.get_rect()
        self.rect.topleft = self.player_position_x, self.player_position_y

    #função que roda a cada frame
    def update(self):
        #atualizando a posição do player, aso tenha mudado
        self.rect.topleft = self.player_position_x, self.player_position_y

        if pygame.key.get_pressed()[K_a]: 
            self.player_position_x -= self.player_velocity
        if pygame.key.get_pressed()[K_d]: 
            self.player_position_x += self.player_velocity 

        #verificando se há colisão com a bolinha
    def get_rect(self):
        return self.rect