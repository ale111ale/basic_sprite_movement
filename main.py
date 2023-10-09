def on_up_pressed():
    animation.run_image_animation(mySprite, assets.animation("""
        WalkDown
    """), 100, False)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_left_pressed():
    animation.run_image_animation(mySprite, assets.animation("""
        WalkLeft
    """), 100, False)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        assets.animation("""
            WalkRight
        """),
        100,
        False)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    animation.run_image_animation(mySprite,
        assets.animation("""
            WalkDown2
        """),
        100,
        False)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

mySprite: Sprite = None
scene.set_background_image(assets.image("""
    Background1
"""))
mySprite = sprites.create(assets.image("""
    PlayerAsset1
"""), SpriteKind.player)
controller.move_sprite(mySprite, 42, 50)