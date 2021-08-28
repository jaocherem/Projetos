from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fps_counter.enabled = False

# texturas
grassTex = load_texture('assets/grass_block.png')
stoneTex = load_texture('assets/stone_block.png')
brickTex = load_texture('assets/brick_block.png')
dirtTex = load_texture('assets/dirt_block.png')
skyTex = load_texture('assets/skybox.png')
armText = load_texture('assets/arm_texture.png')

block = 1

"""
Função que checa mudanças e teclas
"""
def update():
    global block

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['1']:
        block = 1
    if held_keys['2']:
        block = 2
    if held_keys['3']:
        block = 3
    if held_keys['4']:
        block = 4


"""
Características dos blocos, criação de novos blocos e destruição de blocos
"""
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grassTex):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.white,
            highlight_color = color.gray,
            scale = 0.5
        )

    def input(self, key):
        if self.hovered:
            # criação de novos blocos ao apertar o botão esquerdo do mouse
            if key == 'left mouse down':
                if block == 1: 
                    voxel = Voxel(position=self.position + mouse.normal, texture=grassTex)
                if block == 2: 
                    voxel = Voxel(position=self.position + mouse.normal, texture=stoneTex)
                if block == 3: 
                    voxel = Voxel(position=self.position + mouse.normal, texture=brickTex)
                if block == 4: 
                    voxel = Voxel(position=self.position + mouse.normal, texture=dirtTex)

            # destruição de blocos ao apertar o botão direito do mouse
            if key == 'right mouse down':
                destroy(self)

"""
Criação do céu
"""
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = skyTex,
            scale = 200,
            double_sided = True
        )

"""
Criação da mão
"""
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = armText,
            scale = 0.25,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.5, -0.6)
        )

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.5, -0.6)

"""
Criação do terreno
"""
for z in range(12):
    for x in range(12):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
sky = Sky()
hand = Hand()

app.run()