controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    assets.animation`WalkDown`,
    100,
    false
    )
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    assets.animation`WalkLeft`,
    100,
    false
    )
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    assets.animation`WalkRight`,
    100,
    false
    )
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    assets.animation`WalkDown2`,
    100,
    false
    )
})
let mySprite: Sprite = null
scene.setBackgroundImage(assets.image`Background1`)
mySprite = sprites.create(assets.image`PlayerAsset1`, SpriteKind.Player)
controller.moveSprite(mySprite, 42, 50)
