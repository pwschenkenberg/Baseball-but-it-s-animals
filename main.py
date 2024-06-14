import dearpygui.dearpygui as dpg
import random
from parameters import *

# get teams
# -set rosters for both teams.
# -generate players/teams if necessary.

# get location
# -select location or generate a field/surface
# -set weather conditions and time of day

# play ball
# -simulate gameplay
# -output a play-by-play and stats for each player

STRIKE_ZONE_HEIGHT = STRIKE_ZONE_HEIGHT_FT * FT_TO_PX_STRIKE_ZONE
STRIKE_ZONE_WIDTH = STRIKE_ZONE_WIDTH_FT * FT_TO_PX_STRIKE_ZONE
pitchx = 0
pitchy = 0

def throwPitch():
    pitchAccuracy = 1.0
    pitchSpeed = 1.0
    pitchTarget = (0,0)

    global pitchx
    global pitchy

    pitchx = random.randint(0,250)
    pitchy = random.randint(50,350)
    dpg.delete_item("lastPitch")
    dpg.draw_circle(center=(pitchx,pitchy),radius=15,parent="strike_zone",tag="lastPitch")

    ballOrStrike = "Ball"

    if pitchx > 45:
        if pitchx < 55 + STRIKE_ZONE_WIDTH:
            if pitchy > 95:
                if pitchy < 105 + STRIKE_ZONE_HEIGHT:
                    ballOrStrike = "Strike"

    dpg.delete_item("lastPitchCall")
    dpg.delete_item("lastSwing")
    dpg.add_text(ballOrStrike,tag="lastPitchCall",parent="strike_zone")

def swingAtPitch():
    bat_length = BAT_LENGTH
    bat_width = BAT_WIDTH

    batx = random.randint(pitchx-120,pitchx+20)
    baty = random.randint(pitchy-65,pitchy+35)

    dpg.delete_item("lastSwing")
    dpg.delete_item("lastHitPath")
    dpg.draw_rectangle(pmin=(batx,baty),pmax=(batx+bat_length,baty+bat_width),
                       tag="lastSwing",parent="strike_zone")

    if batHitsBall(pitchx,pitchy,batx,baty):
        hitx = random.randint(0,450)
        hity = random.randint(0,450)
        dpg.draw_line((50,50),(hitx,hity),tag="lastHitPath",parent="Baseball Field")
        dpg.draw_circle(center=(hitx,hity),radius=3,parent="ballLocation")

def batHitsBall(px,py,bx,by):
    if px > bx:
        if px < bx + BAT_LENGTH:
            if py > by:
                if py < by + BAT_WIDTH:
                    return True
    return False

def clearField():
    dpg.delete_item("ballLocation",children_only=True)
    dpg.delete_item("lastHitPath")



dpg.create_context()
dpg.create_viewport(title='Play Ball', width=VIEWPORT_1_WIDTH, height=VIEWPORT_1_HEIGHT)

with dpg.window(width=STRIKE_ZONE_WINDOW_WIDTH,height=STRIKE_ZONE_WINDOW_HEIGHT,tag="strike_zone",
                pos=(0,0),no_close=True,no_collapse=True,no_move=True):
    dpg.add_button(label="Throw Pitch",callback=throwPitch)
    dpg.add_button(label="Swing Bat",callback=swingAtPitch)
    dpg.add_button(label="Clear",callback=clearField)
    dpg.draw_rectangle(pmin=(50, 100), pmax=(50+STRIKE_ZONE_WIDTH, 100+STRIKE_ZONE_HEIGHT))

with dpg.window(width=FIELD_WINDOW_WIDTH,height=FIELD_WINDOW_HEIGHT,tag="Baseball Field",
                pos=(STRIKE_ZONE_WINDOW_WIDTH,0),no_close=True,no_collapse=True,no_move=True):

    dpg.draw_circle(center=(50,50),radius=330,fill=COLOR_FIELD_GRASS)
    dpg.draw_circle(center=(50, 50), radius=110,fill=COLOR_FIELD_DIRT)
    dpg.draw_rectangle(pmin=(50,50),pmax=(110,110),tag="diamond",fill=COLOR_FIELD_GRASS)

    dpg.draw_polygon(points=[[-50,-50],[600,-50],[600,50],[50,50],[50,600],[-50,600]],fill=COLOR_BACKGROUND)

    with dpg.draw_layer(tag="ballLocation"):
        pass


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()