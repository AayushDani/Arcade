"""Flappy Bird, implemented using Pygame."""

import math
import os
from random import randint

import pygame
from pygame.locals import *


FPS = 60
EVENT_NEWPIPE = USEREVENT + 1  # custom event
PIPE_ADD_INTERVAL = 3000       # milliseconds
FRAME_ANIMATION_WIDTH = 3      # pixels per frame
FRAME_BIRD_DROP_HEIGHT = 3     # pixels per frame
FRAME_BIRD_JUMP_HEIGHT = 5     # pixels per frame
BIRD_JUMP_STEPS = 20           # see get_frame_jump_height docstring
WIN_WIDTH = 284 * 2            # BG image size: 284x512 px; tiled twice
WIN_HEIGHT = 512
PIPE_WIDTH = 80
PIPE_PIECE_HEIGHT = BIRD_WIDTH = BIRD_HEIGHT = 32


class PipePair:

    def __init__(self, surface, top_pieces, bottom_pieces):
        
        self.x = WIN_WIDTH
        self.surface = surface
        self.top_pieces = top_pieces
        self.bottom_pieces = bottom_pieces
        self.score_counted = False

    @property
    def top_height_px(self):
        """Get the top pipe's height, in pixels."""
        return self.top_pieces * PIPE_PIECE_HEIGHT

    @property
    def bottom_height_px(self):
        """Get the bottom pipe's height, in pixels."""
        return self.bottom_pieces * PIPE_PIECE_HEIGHT

    def is_bird_collision(self, bird_position):
        """Get whether the bird crashed into a pipe in this PipePair.

        Arguments:
        bird_position: The bird's position on screen, as a tuple in
            the form (X, Y).
        """
        bx, by = bird_position
        in_x_range = bx + BIRD_WIDTH > self.x and bx < self.x + PIPE_WIDTH
        in_y_range = (by < self.top_height_px or
                      by + BIRD_HEIGHT > WIN_HEIGHT - self.bottom_height_px)
        return in_x_range and in_y_range


def load_images():

    return {'background': pygame.image.load('Games\\sprites\\background.png'),
            'pipe-end': pygame.image.load('Games\\sprites\\pipe_end.png'),
            'pipe-body': pygame.image.load('Games\\sprites\\pipe_body.png'),            
            # images for animating the flapping bird -- animated GIFs are
            # not supported in pygame
            'bird-wingup': pygame.image.load('Games\\sprites\\bird_wing_up.png'),
            'bird-wingdown': pygame.image.load('Games\\sprites\\bird_wing_down.png')}


def get_frame_jump_height(jump_step):
    
    frac_jump_done = jump_step / float(BIRD_JUMP_STEPS)
    return (1 - math.cos(frac_jump_done * math.pi)) * FRAME_BIRD_JUMP_HEIGHT


def random_pipe_pair(pipe_end_img, pipe_body_img):
    
    surface = pygame.Surface((PIPE_WIDTH, WIN_HEIGHT), SRCALPHA)
    surface.convert()   # speeds up blitting
    surface.fill((0, 0, 0, 0))
    max_pipe_body_pieces = int(
        (WIN_HEIGHT -            # fill window from top to bottom
        3 * BIRD_HEIGHT -        # make room for bird to fit through
        3 * PIPE_PIECE_HEIGHT) / # 2 end pieces and 1 body piece for top pipe
        PIPE_PIECE_HEIGHT        # to get number of pipe pieces
    )
    bottom_pipe_pieces = randint(1, max_pipe_body_pieces)
    top_pipe_pieces = max_pipe_body_pieces - bottom_pipe_pieces
    # bottom pipe
    for i in range(1, bottom_pipe_pieces + 1):
        surface.blit(pipe_body_img, (0, WIN_HEIGHT - i*PIPE_PIECE_HEIGHT))
    bottom_pipe_end_y = WIN_HEIGHT - bottom_pipe_pieces*PIPE_PIECE_HEIGHT
    surface.blit(pipe_end_img, (0, bottom_pipe_end_y - PIPE_PIECE_HEIGHT))
    # top pipe
    for i in range(top_pipe_pieces):
        surface.blit(pipe_body_img, (0, i * PIPE_PIECE_HEIGHT))
    top_pipe_end_y = top_pipe_pieces * PIPE_PIECE_HEIGHT
    surface.blit(pipe_end_img, (0, top_pipe_end_y))
    # compensate for added end pieces
    top_pipe_pieces += 1
    bottom_pipe_pieces += 1
    return PipePair(surface, top_pipe_pieces, bottom_pipe_pieces)


def main():

    pygame.init()

    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Pygame Flappy Bird')

    clock = pygame.time.Clock()

    score_font = pygame.font.SysFont(None, 32, bold=True)  # default font

    # the bird stays in the same x position, so BIRD_X is a constant
    BIRD_X = 50
    bird_y = int(WIN_HEIGHT/2 - BIRD_HEIGHT/2)  # center bird on screen

    images = load_images()

    # timer for adding new pipes
    pygame.time.set_timer(EVENT_NEWPIPE, PIPE_ADD_INTERVAL)
    pipes = []

    steps_to_jump = 2
    score = 0
    done = paused = False
    runs = 0
    while not done:
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE) or runs == 3:
                done = True
                break
            elif e.type == KEYUP and e.key in (K_PAUSE, K_p):
                paused = not paused
            elif e.type == MOUSEBUTTONUP or (e.type == KEYUP and
                    e.key in (K_UP, K_RETURN, K_SPACE)):
                steps_to_jump = BIRD_JUMP_STEPS
            elif e.type == EVENT_NEWPIPE:
                pp = random_pipe_pair(images['pipe-end'], images['pipe-body'])
                pipes.append(pp)

        clock.tick(FPS)
        if paused:
            continue  # don't draw anything

        for x in (0, WIN_WIDTH / 2):
            screen.blit(images['background'], (x, 0))

        for p in pipes:
            p.x -= FRAME_ANIMATION_WIDTH
            if p.x <= -PIPE_WIDTH:  # PipePair is off screen
                pipes.remove(p)
            else:
                screen.blit(p.surface, (p.x, 0))

        # calculate position of jumping bird
        if steps_to_jump > 0:
            bird_y -= get_frame_jump_height(BIRD_JUMP_STEPS - steps_to_jump)
            steps_to_jump -= 1
        else:
            bird_y += FRAME_BIRD_DROP_HEIGHT

        # because pygame doesn't support animated GIFs, we have to
        # animate the flapping bird ourselves
        if pygame.time.get_ticks() % 500 >= 250:
            screen.blit(images['bird-wingup'], (BIRD_X, bird_y))
        else:
            screen.blit(images['bird-wingdown'], (BIRD_X, bird_y))

        # update and display score
        for p in pipes:
            if p.x + PIPE_WIDTH < BIRD_X and not p.score_counted:
                score += 1
                p.score_counted = True

        score_surface = score_font.render(str(score), True, (255, 255, 255))
        score_x = WIN_WIDTH/2 - score_surface.get_width()/2
        screen.blit(score_surface, (score_x, PIPE_PIECE_HEIGHT))

        pygame.display.update()

        # check for collisions
        pipe_collisions = [p.is_bird_collision((BIRD_X, bird_y)) for p in pipes]
        if (0 >= bird_y or bird_y >= WIN_HEIGHT - BIRD_HEIGHT or
                True in pipe_collisions):
            print('You crashed! Score: %i' % score)
            break
    pygame.time.delay(3000)

for i in range(3):
    if __name__ == '__main__':
        # If this module had been imported, __name__ would be 'flappybird'.
        # It was executed (e.g. by double-clicking the file), so call main.
        main()
