def title():
    global kei
    music.jump_down.play()
    kei = sprites.create(img("""
            . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . . . . . . . b b b . . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . . . . b b c c c c c b b . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . . b b c c c c c c c c b b b . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . b c c c c c c f c c c c c c c b . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . b c c c c f c c f f c f c c c c c c c b b . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . e c c c c c f c c f f f f c f f f c c c c c c . . . . . . . . . . . . 
                    . . . . . . . . . . . . c c c c c c c c c f f f f f f f f f f f c f c c c c c . . . . . . . . . 
                    . . . . . . . . . . . c c b b b d b d b e e e e e e c f f c f f f f f c f c c c . . . . . . . . 
                    . . . . . . . . . . c e b d d d d d d b b e e e e e e f f c c f f f f f f f f c c . . . . . . . 
                    . . . . . . . . . c c b d d d d d d b b b e e e e e e e e e e f f f f f f f f f c c . . . . . . 
                    . . . . . . . . c c b b b b b b b b b b b e e e e e e e e e e e f f f f f f f f f c . . . . . . 
                    . . . . . . . . c c b b b b b b b b b b b e e e e e e e e e e e e c f f f f f f f c c . . . . . 
                    . . . . . . . . f c b b b b b b b b b b b e e e e e e e e e e e e e e f f f f f f f c . . . . . 
                    . . . . . . . . f c b b b b b b b b b b b e e e e e e e e e e e e e e f f f f f f f f . . . . . 
                    . . . . . . . . f c b b b b b b b b b b e e e e e e e e e e e e e e e c f f f f f f f . . . . . 
                    . . . . . . . f f e b b b b b b b b b e e e e e e e e e e e e e e e e e f f f f f f f . . . . . 
                    . . . . . . . f f e b b b e e e e e b e e e e e e e e e e e e e e e e c f f f f f f f . . . . . 
                    . . . . . . . f f b b b b b e e e e e e e e e e e e e e e e e e e e e f f f f f f f f . . . . . 
                    . . . . . . . f c b b b b e e e e e e e e e e e e e e e e e e e e e e f f f f f f f f . . . . . 
                    . . . . . . . f e b b e e e e e e b b e e e e e e e e e e e e e e e e f f f f f f f f . . . . . 
                    . . . . . . . f b b e c c f f e e b b b e e e e e c c e e e e e e e e e f f f f f f . . . . . . 
                    . . . . . . b e d d b b e e e e b d d b e e e e e f f f f e e e e e e e f f f f f f . . . . . . 
                    . . . . . . e e d d b b e e b b d d d b e e e e e e e e e e e e e e e e f f f f f f . . . . . . 
                    . . . . . . e b d d d d d d d d d d b b e e e e e e e e e e e e e e e e f f f f e e e . . . . . 
                    . . . . . . e b d d d d b b b d d b b e e e e e b e e e e e e e e e e e f f f f e e e . . . . . 
                    . . . . . . e b b b b b e e b b b e e e e e e e b b b b e e e e e e e e f f e e e e e e . . . . 
                    . . . . . . e b b b e e e e e e e e e e e e e e e b b e e e e e e e e e f f e e e e e e . . . . 
                    . . . . . . c b b e e e e e e e e e e e e e e e e e e e e e e e e e e e f e e e e e e . . . . . 
                    . . . . . . b b e e e e e e b b e e e e e e e e e e e e e e e e e e e e e e e e e e e . . . . . 
                    . . . . . . . b e e e e e b b b b e e e e e e e e e e e e e e e e e e e e e e e e e . . . . . . 
                    . . . . . . . b e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e . . . . . . . 
                    . . . . . . . c b e e e e f f e e e e e e e e e e e e e e e e e e e e e e e e b . . . . . . . . 
                    . . . . . . . c b e e e e e f f f f c f f f f f e e e e e e e e e e e b . . . . . . . . . . . . 
                    . . . . . . . . e e e e e e e f f f f f f f f f e e e e e e e e e e . . . . . . . . . . . . . . 
                    . . . . . . . . c e e e e e e e e e e e e e e e e e e e e e e e e e . . . . . . . . . . . . . . 
                    . . . . . . . . . e e e e e e e e e e e e e e e e e e e e e e e e . . . . . . . . . . . . . . . 
                    . . . . . . . . . . e e e b e e e e e e e e e e e e e e e e e b . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . b e e b e e e e e e e e e e e e e e e e e . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . b e b e e e e e e e e e e e e e e e b . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . c e e e e e e e e e e e e e e e e . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . e e e e e e e e e e e e e e b . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . c e e e e e e e e e e e e . . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . b b e e e e e e b . . . . . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
        """),
        SpriteKind.projectile)
    kei.set_position(80, 21)
    game.splash("けい の くるま")
    kei.destroy()
def init():
    tiles.set_tilemap(tiles.create_tilemap(hex("""
                1000080001020202020202020203020202020203050f0b0b0b0b110b1006040404040406050d040404040d040d06040404040406050d04040f0b0a040d06040404040406050d04040d0404040d06040404040406050d04040d0404040d06040404040406050c0b0b0e0b0b0b0a0604040404040609070707070707070708070707070706
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            [myTiles.transparency16,
                sprites.castle.tile_path1,
                sprites.castle.tile_path2,
                sprites.castle.tile_path3,
                sprites.castle.tile_path5,
                sprites.castle.tile_path4,
                sprites.castle.tile_path6,
                sprites.castle.tile_path8,
                sprites.castle.tile_path9,
                sprites.castle.tile_path7,
                sprites.vehicle.road_turn4,
                sprites.vehicle.road_horizontal,
                sprites.vehicle.road_turn3,
                sprites.vehicle.road_vertical,
                sprites.vehicle.road_intersection1,
                sprites.vehicle.road_turn1,
                sprites.vehicle.road_turn2,
                sprites.vehicle.road_intersection3],
            TileScale.SIXTEEN))

def on_b_pressed():
    music.play_melody("C D E F G A B C5 ", 750)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    music.siren.play_until_done()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

kei: Sprite = None
music.set_volume(10)
title()
init()
car = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 2 2 2 2 2 2 2 2 . . 
            . . . . . 2 c 2 2 2 2 2 2 4 2 . 
            . . . . 2 c c 2 2 2 2 2 2 4 c 2 
            . . d 2 4 c c 2 4 4 4 4 4 4 c c 
            . d 2 2 4 c b e e e e e e e 2 c 
            . 2 2 2 4 b e e b b b e b b e 2 
            . 2 2 2 2 2 e b b b b e b b b e 
            . 2 2 2 2 e 2 2 2 2 2 e 2 2 2 e 
            . 2 d d 2 e f e e e f e e e e e 
            . d d 2 e e e f e e f e e e e e 
            . e e e e e e e f f f e e e e e 
            . e e e e f f f e e e e f f f f 
            . . . e f f f f f e e f f f f f 
            . . . . f f f f . . . . f f f . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
car.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
controller.move_sprite(car, 100, 100)

def on_on_update():
    if car.vx < 0:
        car.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . 2 2 2 2 2 2 2 2 . . 
                        . . . . . 2 c 2 2 2 2 2 2 4 2 . 
                        . . . . 2 c c 2 2 2 2 2 2 4 c 2 
                        . . d 2 4 c c 2 4 4 4 4 4 4 c c 
                        . d 2 2 4 c b e e e e e e e 2 c 
                        . 2 2 2 4 b e e b b b e b b e 2 
                        . 2 2 2 2 2 e b b b b e b b b e 
                        . 2 2 2 2 e 2 2 2 2 2 e 2 2 2 e 
                        . 2 d d 2 e f e e e f e e e e e 
                        . d d 2 e e e f e e f e e e e e 
                        . e e e e e e e f f f e e e e e 
                        . e e e e f f f e e e e f f f f 
                        . . . e f f f f f e e f f f f f 
                        . . . . f f f f . . . . f f f . 
                        . . . . . . . . . . . . . . . .
        """))
    elif car.vx > 0:
        car.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . 2 2 2 2 2 2 2 2 . . . . 
                        . . . 2 4 2 2 2 2 2 2 c 2 . . . 
                        . . 2 c 4 2 2 2 2 2 2 c c 2 . . 
                        . 2 c c 4 4 4 4 4 4 2 c c 4 2 d 
                        . 2 c 2 e e e e e e e b c 4 2 2 
                        . 2 2 e b b e b b b e e b 4 2 2 
                        . 2 e b b b e b b b b e 2 2 2 2 
                        . e e 2 2 2 e 2 2 2 2 2 e 2 2 2 
                        . e e e e e e f e e e f e 2 d d 
                        . e e e e e e f e e f e e e 2 d 
                        . e e e e e e f f f e e e e e e 
                        . e f f f f e e e e f f f e e e 
                        . . f f f f f e e f f f f f e . 
                        . . . f f f . . . . f f f f . . 
                        . . . . . . . . . . . . . . . .
        """))
    if car.vy < 0:
        car.set_image(img("""
            . . . . . . e e c c e e . . . . 
                        . . . . . e 2 2 2 2 2 2 e . . . 
                        . . . . 2 c 2 2 2 2 2 2 c 2 . . 
                        . . . e 2 c 4 2 2 2 2 2 c 2 e . 
                        . . . f 2 2 4 2 2 2 2 2 c 2 f . 
                        . . . f 2 2 4 2 2 2 2 2 2 2 f . 
                        . . . f 2 2 4 2 2 2 2 2 2 2 f . 
                        . . . f 2 c 2 4 4 2 2 2 c 2 f . 
                        . . . e 2 c e c c c c e c 2 e . 
                        . . . e 2 e c b b b b c e 2 e . 
                        . . . e 2 e b b b b b b e 2 e . 
                        . . . e e e e e e e e e e e e . 
                        . . . f e d e e e e e e d e f . 
                        . . . f e 2 d e e e e d 2 e f . 
                        . . . f f e e e e e e e e f f . 
                        . . . . f f . . . . . . f f . .
        """))
    elif car.vy > 0:
        car.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . 2 2 2 2 2 2 . . . . 
                        . . . . . 2 2 4 4 2 2 2 2 . . . 
                        . . . . . c 4 2 2 2 2 2 c . . . 
                        . . . . 2 c 4 2 2 2 2 2 c 2 . . 
                        . . . e 2 c 4 2 2 2 2 2 c 2 e . 
                        . . . f 2 c 4 2 2 2 2 2 c 2 f . 
                        . . . f e c 2 2 2 2 2 2 c e f . 
                        . . . f 2 c 2 b b b b 2 c 2 f . 
                        . . . e 2 2 b c c c c b 2 2 e . 
                        . . . e e b c c c c c c b e e . 
                        . . . f e 4 4 4 4 4 4 4 4 e f . 
                        . . . f e d 2 2 2 2 2 2 d e f . 
                        . . . . 2 d d 2 2 2 2 d d 2 f . 
                        . . . . f 2 d 2 2 2 2 d 2 f . . 
                        . . . . . e 2 2 2 2 2 2 e . . .
        """))
game.on_update(on_on_update)
