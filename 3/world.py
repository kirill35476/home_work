
_camera_x = 0
_camera_y = 0

SREEN_WIDTH = 800
SREEN_HEIGHT = 800

WIDTH = SREEN_WIDTH * 6
HEIGHT = SREEN_HEIGHT * 4

def set_camera_xy(x,y):
    global _camera_x, _camera_y
    if x <0:
        x = 0
    if y <0:
        y = 0

    if x > WIDTH -  SREEN_WIDTH:
        x = WIDTH -  SREEN_WIDTH
    if y > HEIGHT -  SREEN_HEIGHT:
        y = HEIGHT -  SREEN_HEIGHT

    _camera_x = x
    _camera_y = y

def move_camera(delta_x, delta_y):
    set_camera_xy(_camera_x + delta_x, _camera_y + delta_y)

def get_sreen_x(world_X):
    return world_X - _camera_x

def get_sreen_y(world_Y):
    return world_Y - _camera_y