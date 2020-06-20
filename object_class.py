import turtle

class Create_Object:
    def __init__(self, obj_name, obj_color, obj_shape='classic'):
        self.obj_name = obj_name
        self.obj_color = obj_color
        self.obj_shape = obj_shape

    def Create(self):
        self.obj_name = turtle.Turtle()
        self.obj_name.color(self.obj_color)
        self.obj_name.shape(self.obj_shape)
        self.obj_name.penup()
        return self.obj_name