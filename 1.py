from OCC.Display.SimpleGui import init_display
from OCC.gp import gp_Pnt
if __name__ == '__main__':
 display, start_display, add_menu, add_function_to_menu = init_display()
 P0=gp_Pnt(0,0,1)
 P1 =gp_Pnt(0, 30, 20)
 display.DisplayShape(P0)
 display.DisplayShape(P1)
 start_display()
