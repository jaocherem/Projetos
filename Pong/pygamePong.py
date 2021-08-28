import pygame

width = 600
height = 450

paddle1 = pygame.image.load('Pong/assets/1.png')
paddle2 = pygame.image.load('Pong/assets/2.png')
ball = pygame.image.load('Pong/assets/ball.png')
background = pygame.image.load('Pong/assets/universe.png')

white = (255, 255, 255)
black = (0, 0, 0)

delay = 30

pygame.init()

font = pygame.font.SysFont('Ubuntu', 40)

paddleSpeed = 20

paddleWidth = 46
paddleHeight = 104

paddle1X = 10
paddle1Y = height / 2 - paddleHeight / 2

paddle2X = width - paddleWidth - 10
paddle2Y = height / 2 - paddleHeight / 2

player1Score = 0
player2Score = 0

paddle1Up = False
paddle1Down = False
paddle2Up = False
paddle2Down = False

ballX = width / 2
ballY = height / 2

ballWidth = 42
ballXVel = -10
ballYVel = 0

screen = pygame.display.set_mode((width, height))

"""
Colocando os paddles, a bola e a pontuação na tela
"""
def draw():
    #screen.blit(background, (0, 0))

    screen.blit(paddle1, (paddle1X, paddle1Y))
    screen.blit(paddle2, (paddle2X, paddle2Y))

    screen.blit(ball, (ballX, ballY))

    score1 = font.render(f"{str(player1Score)}", False, black)
    score2 = font.render(f"{str(player2Score)}", False, black)

    #screen.blit(score1, (width / 4, 30))
    #screen.blit(score2, (width / 2 + width / 4, 30))

"""
Função que controla o movimento do jogador
"""
def playerMovement():
    global paddle1Y
    global paddle2Y
    global paddleSpeed

    if paddle1Up:
        paddle1Y -= paddleSpeed
        if paddle1Y < 0:
            paddle1Y = 0
    elif paddle1Down:
        paddle1Y += paddleSpeed
        if paddle1Y + paddleHeight > height:
            paddle1Y = height - paddleHeight

    if paddle2Up:
        paddle2Y -= paddleSpeed
        if paddle2Y < 0:
            paddle2Y = 0
    elif paddle2Down:
        paddle2Y += paddleSpeed
        if paddle2Y + paddleHeight > height:
            paddle2Y = height - paddleHeight

"""
Função que controla o movimento da bola
"""
def ballMovement():
    global ballX
    global ballY
    global ballXVel
    global ballYVel
    global player1Score
    global player2Score

    if (ballX < paddle1X + paddleWidth) and (paddle1Y < ballY + ballWidth < paddle1Y + paddleHeight):
        ballXVel = - ballXVel
        ballYVel = (paddle1Y + paddleHeight / 2 - ballY) / 15
        ballYVel = - ballYVel
    elif ballX + ballXVel < 0:
        player2Score += 1
        ballX = width / 2
        ballY = height / 2
        ballXVel = 10
        ballYVel = 0

    if (ballX > paddle2X - paddleWidth) and (paddle2Y < ballY + ballWidth < paddle2Y + paddleHeight):
        ballXVel = - ballXVel
        ballYVel = (paddle2Y + paddleHeight / 2 - ballY) / 15
        ballYVel = - ballYVel
    elif ballX + ballXVel > width:
        player1Score += 1
        ballX = width / 2
        ballY = height / 2
        ballXVel = -10
        ballYVel = 0

    if ballY + ballYVel < 0 or ballY + ballYVel > height:
        ballYVel = - ballYVel

    ballX += ballXVel
    ballY += ballYVel

pygame.display.set_caption("pong")
screen.fill(black)
pygame.display.flip()

playing = True
running = True

"""
Loop principal que faz o jogo rodar
"""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                paddle1Up = True
            if event.key == pygame.K_s:
                paddle1Down = True
            if event.key == pygame.K_UP:
                paddle2Up = True
            if event.key == pygame.K_DOWN:
                paddle2Down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                paddle1Up = False
            if event.key == pygame.K_s:
                paddle1Down = False
            if event.key == pygame.K_UP:
                paddle2Up = False
            if event.key == pygame.K_DOWN:
                paddle2Down = False

    if playing:
        screen.fill(white)

        playerMovement()
        ballMovement()
        draw()

        #if player1Score >= 1:
            #playing = False

    if playing == False:
        screen.fill(black)
        lost = font.render(f"VOCÊ PERDEU", False, white)
        screen.blit(lost, (width / 2 - 100, height / 2 - 5))

    pygame.display.flip()
    pygame.time.wait(delay)