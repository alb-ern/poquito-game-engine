import sys
import os
base_path = os.path.dirname(__file__)
src_path = os.path.join(base_path, "..", "src")
sys.path.append(src_path)

import pygame

from core.game import Game
from core.scene import Scene
from core.UIText import UIText

from character import Character, CharacterCollider
from terrain import Terrain
from mainCamera import MainCamera

def main():

    cam = MainCamera(0, 0)

    scene = Scene("Scene1", cam)
    scene.addGameObject(cam)
    
    
    character = Character(0, -250, 32 * 2, 32 * 2, 0, [])
    scene.addGameObject(character)
    
    cam.referenceObject = character

    terrainSprite = pygame.image.load(os.path.join(base_path, "assets", "Terrain", "terrain.png"))

    for i in range(3):
        for j in range(3):
            scene.addGameObject(Terrain(500*i-160+(j%2)*250, 500*j-150, 160*2, 160*2, 0, terrainSprite))

    characterCollider = CharacterCollider(["Terrain"], character)
    scene.addGameObject(characterCollider)

    poquitoText1 = UIText("Poquito", 50, 50, 96, -10, (0,0,0))
    poquitoText2 = UIText("Poquito", 45, 45, 100, -12, (255,255,255))
    scene.addGameObject(poquitoText1)
    scene.addGameObject(poquitoText2)

    game = Game((1280, 720), "Scene1", 60, 100, pygame.NOFRAME , (216,189,155))
    game.run()

if __name__=="__main__":
    main()

