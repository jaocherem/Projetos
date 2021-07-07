import pygame
import sys
import time

import pedro

pygame.init()
size = width, height = 600, 400

# Cores
black = (0, 0, 0)
white = (220, 220, 220)
 
screen = pygame.display.set_mode(size)

# Fonte
mediumFont = pygame.font.Font("Jogo da Velha/OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("Jogo da Velha/OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("Jogo da Velha/OpenSans-Regular.ttf", 60)

user = None
board = pedro.initial_state()
ai_turn = False

"""
Loop principal para rodar o jogo
"""
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Escolher entre O e X
    if user is None:

        # Título
        title = largeFont.render("Jogo da Velha", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Botões
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playX = mediumFont.render("X", True, black)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, white, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playO = mediumFont.render("O", True, black)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playO, playORect)

        # Checando o clique do mouse
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = pedro.X
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = pedro.O

    else:

        # Desenho do tabuleiro
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != pedro.EMPTY:
                    move = moveFont.render(board[i][j], True, white)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)
                row.append(rect)
            tiles.append(row)

        game_over = pedro.terminal(board)
        player = pedro.player(board)

        # Título
        if game_over:
            winner = pedro.winner(board)
            if winner is None:
                title = f"Fim de Jogo: Velha."
            else:
                title = f"Fim de Jogo: {winner} Venceu."
        elif user == player:
            title = f"Jogue Como {user}"
        else:
            title = f"Pedro está pensando..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Checando o movimento do Pedro
        if user != player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = pedro.minimax(board)
                board = pedro.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Checando o movimento do humano
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == pedro.EMPTY and tiles[i][j].collidepoint(mouse)):
                        board = pedro.result(board, (i, j))

        # Final do jogo
        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Jogar de Novo", True, black)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    board = pedro.initial_state()
                    ai_turn = False

    pygame.display.flip()