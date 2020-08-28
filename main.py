def title():
    global kei
    music.jump_down.play()
    scene.set_background_color(6)
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
    scene.set_background_color(0)
    kei.destroy()
def scene2():
    tiles.set_tilemap(tiles.create_tilemap(hex("""
                200020000102020202020202020402020202020310161011111114151515151415141314050d090909090f090f090e040404040404041110101111151313151414141414050b040404040b040b040b040404040404040412121111151115131313161414050b04040d0908040b040a0e0404040404040404111211121112141514141414050b04040b0404040b04040a090909090909090e040411111212131514141313050b04040b0404040b040404040404040404040b040410111211161216151414050a09090c0909090c090909090f090e0404040b040404111112151213131414070612120606060606040404040b210a0909090c09090e041012121513151314141212121211111111040404040b201e1b1b1b1f1b1b0b041011101115121515141414151212101011121110100b1e20201e1e1f1c1b0b040411111212121214141514151111101010101011100b1b1f1b1e1d20201b0b040404041012161114151415141111101212111111040b2020201c20201f1b0b040404040411111114141514151111111111111111040b1e201b1b1d1e1b1f0b040404040404111011141514141511161212121611040a09090909090909090c0909090e041010101114131314141314111211121212111111040404040404040404040b040404041114151413131315151511121210121211111112111116110404040b040404141414141413131513151313151511121212101212101212111104040b040414141415151414141315141413131415151511161111111011160404040b04041416141514131314141514141413141410191a1a1a11111111110404040b04141414141414141414141415151414141411101111111011111104040d090804141514131416141416141414141415141416101010111010101004040b040404141514151415151414141404041414111111111110111010111010040b0404141414141413131414040404040404040404040404041111101011040d080414141413141413150d090e0404040404040404040404040404040404040b040414141314141413150b180b040404040404040404040d0909090909090908041414141314161414140a090c090909090909090909090804040404040404041414141313141414141404040404040404040404040404040404040404040414141413161414171714161404040404040404040404040404040404040404141415141414172222171414141414141416141414141414141614131515141414151513141722221717141414151515141414131414131415151315151514131314141422222217172214151414141413131313131315141414151414151514141414172217172117221414141414141414141414141414141414141314141414221717221717221722
            """),
            img("""
                . . . . . . . . . . . . . . . . . 2 . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . 2 . 2 . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . 2 . . . 2 . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . 2 . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 2 . . . . . 2 . . . . . . . 2 . 
                        . . . . . . . . . . . . . . 2 2 2 2 . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . 2 . . 2 . . . . . . . . 2 . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 . . . . 
                        . 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . 2 . . . . . . . 2 . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
            """),
            [myTiles.transparency16,
                sprites.castle.tile_path1,
                sprites.castle.tile_path2,
                sprites.castle.tile_path3,
                sprites.castle.tile_path5,
                sprites.castle.tile_path4,
                sprites.castle.tile_path8,
                sprites.castle.tile_path7,
                sprites.vehicle.road_turn4,
                sprites.vehicle.road_horizontal,
                sprites.vehicle.road_turn3,
                sprites.vehicle.road_vertical,
                sprites.vehicle.road_intersection1,
                sprites.vehicle.road_turn1,
                sprites.vehicle.road_turn2,
                sprites.vehicle.road_intersection3,
                sprites.castle.tile_grass2,
                sprites.castle.tile_grass1,
                sprites.castle.tile_grass3,
                sprites.castle.tile_dark_grass2,
                sprites.castle.tile_dark_grass3,
                sprites.castle.tile_dark_grass1,
                sprites.builtin.forest_tiles0,
                sprites.dungeon.hazard_lava0,
                sprites.dungeon.hazard_spike,
                sprites.builtin.forest_tiles1,
                sprites.builtin.forest_tiles2,
                sprites.dungeon.floor_dark0,
                sprites.dungeon.floor_dark3,
                sprites.dungeon.floor_dark4,
                sprites.dungeon.floor_dark_diamond,
                sprites.dungeon.floor_dark5,
                sprites.dungeon.floor_dark1,
                sprites.dungeon.chest_closed,
                sprites.dungeon.hazard_lava1],
            TileScale.SIXTEEN))
def createCar():
    global car, subCar
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
    controller.move_sprite(car, 100, 100)
    scene.camera_follow_sprite(car)
    subCar = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 6 6 6 6 6 6 6 6 . . 
                    . . . . . 6 c 6 6 6 6 6 6 9 6 . 
                    . . . . 6 c c 6 6 6 6 6 6 9 c 6 
                    . . d 6 9 c c 6 9 9 9 9 9 9 c c 
                    . d 6 6 9 c b 8 8 8 8 8 8 8 6 c 
                    . 6 6 6 9 b 8 8 b b b 8 b b 8 6 
                    . 6 6 6 6 6 8 b b b b 8 b b b 8 
                    . 6 6 6 6 8 6 6 6 6 6 8 6 6 6 8 
                    . 6 d d 6 8 f 8 8 8 f 8 8 8 8 8 
                    . d d 6 8 8 8 f 8 8 f 8 8 8 8 8 
                    . 8 8 8 8 8 8 8 f f f 8 8 8 8 8 
                    . 8 8 8 8 f f f 8 8 8 8 f f f f 
                    . . . 8 f f f f f 8 8 f f f f f 
                    . . . . f f f f . . . . f f f . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    subCar.set_position(160, 120)
    subCar.follow(car, 70)
def init():
    music.set_volume(255)

def on_overlap_tile(sprite, location):
    game.over(True, effects.hearts)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_spike,
    on_overlap_tile)

def on_b_pressed():
    subCar.say("まって～", 2000)
    music.play_melody("C D E F G A B C5 ", 750)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    controller.move_sprite(car, 200, 200)
    car.start_effect(effects.fire, 2000)
    music.siren.play_until_done()
    controller.move_sprite(car, 100, 100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

subCar: Sprite = None
car: Sprite = None
kei: Sprite = None
init()
title()
scene2()
createCar()

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
    if abs(subCar.vx) > abs(subCar.vy):
        if subCar.vx < 0:
            subCar.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . 6 6 6 6 6 6 6 6 . . 
                                . . . . . 6 c 6 6 6 6 6 6 9 6 . 
                                . . . . 6 c c 6 6 6 6 6 6 9 c 6 
                                . . d 6 9 c c 6 9 9 9 9 9 9 c c 
                                . d 6 6 9 c b 8 8 8 8 8 8 8 6 c 
                                . 6 6 6 9 b 8 8 b b b 8 b b 8 6 
                                . 6 6 6 6 6 8 b b b b 8 b b b 8 
                                . 6 6 6 6 8 6 6 6 6 6 8 6 6 6 8 
                                . 6 d d 6 8 f 8 8 8 f 8 8 8 8 8 
                                . d d 6 8 8 8 f 8 8 f 8 8 8 8 8 
                                . 8 8 8 8 8 8 8 f f f 8 8 8 8 8 
                                . 8 8 8 8 f f f 8 8 8 8 f f f f 
                                . . . 8 f f f f f 8 8 f f f f f 
                                . . . . f f f f . . . . f f f . 
                                . . . . . . . . . . . . . . . .
            """))
        elif subCar.vx > 0:
            subCar.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . 6 6 6 6 6 6 6 6 . . . . 
                                . . . 6 9 6 6 6 6 6 6 c 6 . . . 
                                . . 6 c 9 6 6 6 6 6 6 c c 6 . . 
                                . 6 c c 9 9 9 9 9 9 6 c c 9 6 d 
                                . 6 c 6 8 8 8 8 8 8 8 b c 9 6 6 
                                . 6 6 8 b b 8 b b b 8 8 b 9 6 6 
                                . 6 8 b b b 8 b b b b 8 6 6 6 6 
                                . 8 8 6 6 6 8 6 6 6 6 6 8 6 6 6 
                                . 8 8 8 8 8 8 f 8 8 8 f 8 6 d d 
                                . 8 8 8 8 8 8 f 8 8 f 8 8 8 6 d 
                                . 8 8 8 8 8 8 f f f 8 8 8 8 8 8 
                                . 8 f f f f 8 8 8 8 f f f 8 8 8 
                                . . f f f f f 8 8 f f f f f 8 . 
                                . . . f f f . . . . f f f f . . 
                                . . . . . . . . . . . . . . . .
            """))
    else:
        if subCar.vy < 0:
            subCar.set_image(img("""
                . . . . . . 8 8 c c 8 8 . . . . 
                                . . . . . 8 6 6 6 6 6 6 8 . . . 
                                . . . . 6 c 6 6 6 6 6 6 c 6 . . 
                                . . . 8 6 c 9 6 6 6 6 6 c 6 8 . 
                                . . . f 6 6 9 6 6 6 6 6 c 6 f . 
                                . . . f 6 6 9 6 6 6 6 6 6 6 f . 
                                . . . f 6 6 9 6 6 6 6 6 6 6 f . 
                                . . . f 6 c 6 9 9 6 6 6 c 6 f . 
                                . . . 8 6 c 8 c c c c 8 c 6 8 . 
                                . . . 8 6 8 c b b b b c 8 6 8 . 
                                . . . 8 6 8 b b b b b b 8 6 8 . 
                                . . . 8 8 8 8 8 8 8 8 8 8 8 8 . 
                                . . . f 8 d 8 8 8 8 8 8 d 8 f . 
                                . . . f 8 6 d 8 8 8 8 d 6 8 f . 
                                . . . f f 8 8 8 8 8 8 8 8 f f . 
                                . . . . f f . . . . . . f f . .
            """))
        elif subCar.vy > 0:
            subCar.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . 6 6 6 6 6 6 . . . . 
                                . . . . . 6 6 9 9 6 6 6 6 . . . 
                                . . . . . c 9 6 6 6 6 6 c . . . 
                                . . . . 6 c 9 6 6 6 6 6 c 6 . . 
                                . . . 8 6 c 9 6 6 6 6 6 c 6 8 . 
                                . . . f 6 c 9 6 6 6 6 6 c 6 f . 
                                . . . f 8 c 6 6 6 6 6 6 c 8 f . 
                                . . . f 6 c 6 b b b b 6 c 6 f . 
                                . . . 8 6 6 b c c c c b 6 6 8 . 
                                . . . 8 8 b c c c c c c b 8 8 . 
                                . . . f 8 9 9 9 9 9 9 9 9 8 f . 
                                . . . f 8 d 6 6 6 6 6 6 d 8 f . 
                                . . . . 6 d d 6 6 6 6 d d 6 f . 
                                . . . . f 6 d 6 6 6 6 d 6 f . . 
                                . . . . . 8 6 6 6 6 6 6 8 . . .
            """))
game.on_update(on_on_update)



def loopThree():
    for index in range(2):
        for index2 in range(2):
            music.play_tone(220, music.beat(BeatFraction.QUARTER))
        music.play_tone(440, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.QUARTER))
        for index3 in range(2):
            music.play_tone(196, music.beat(BeatFraction.QUARTER))
        music.play_tone(392, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.QUARTER))
        for index4 in range(2):
            music.play_tone(165, music.beat(BeatFraction.QUARTER))
        music.play_tone(330, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.QUARTER))
        for index5 in range(2):
            music.play_tone(247, music.beat(BeatFraction.QUARTER))
        music.play_tone(494, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.QUARTER))


def loopTwo():
    for index6 in range(2):
        music.play_tone(494, music.beat(BeatFraction.QUARTER))
        music.play_tone(440, music.beat(BeatFraction.QUARTER))
        music.play_tone(392, music.beat(BeatFraction.QUARTER))
        music.play_tone(440, music.beat(BeatFraction.QUARTER))
    for index7 in range(2):
        music.play_tone(247, music.beat(BeatFraction.QUARTER))
        music.play_tone(220, music.beat(BeatFraction.QUARTER))
        music.play_tone(196, music.beat(BeatFraction.QUARTER))
        music.play_tone(220, music.beat(BeatFraction.QUARTER))


def loopOne():
    for index8 in range(4):
        music.play_tone(165, music.beat(BeatFraction.QUARTER))
        music.play_tone(330, music.beat(BeatFraction.QUARTER))
    for index9 in range(4):
        music.play_tone(196, music.beat(BeatFraction.QUARTER))
        music.play_tone(392, music.beat(BeatFraction.QUARTER))
    for index10 in range(4):
        music.play_tone(165, music.beat(BeatFraction.QUARTER))
        music.play_tone(330, music.beat(BeatFraction.QUARTER))
    for index11 in range(4):
        music.play_tone(196, music.beat(BeatFraction.QUARTER))
        music.play_tone(392, music.beat(BeatFraction.QUARTER))