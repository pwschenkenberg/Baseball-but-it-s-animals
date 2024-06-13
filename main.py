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
    bat_length = 100
    bat_width = 25

    #batx = random.randint(min(0,pitchx-100),max(pitchx+100,250-bat_length))
    #baty = random.randint(min(50,pitchy-50),max(pitchy+75,350-bat_width))

    batx = random.randint(pitchx-150,pitchx+50)
    baty = random.randint(pitchy-50,pitchy+75)

    dpg.delete_item("lastSwing")
    dpg.draw_rectangle(pmin=(batx,baty),pmax=(batx+bat_length,baty+bat_width),tag="lastSwing",parent="strike_zone")



dpg.create_context()
dpg.create_viewport(title='Play Ball', width=VIEWPORT_1_WIDTH, height=VIEWPORT_1_HEIGHT)

with dpg.window(width=STRIKE_ZONE_WINDOW_WIDTH,height=STRIKE_ZONE_HEIGHT,tag="strike_zone",pos=(0,0)):
    dpg.add_button(label="Throw Pitch",callback=throwPitch)
    dpg.add_button(label="Swing Bat",callback=swingAtPitch)
    dpg.draw_rectangle(pmin=(50, 100), pmax=(50+STRIKE_ZONE_WIDTH, 100+STRIKE_ZONE_HEIGHT))

with dpg.window(width=FIELD_WINDOW_WIDTH,height=FIELD_WINDOW_HEIGHT,tag="Baseball Field",pos=(STRIKE_ZONE_WINDOW_WIDTH,0)):
    dpg.draw_rectangle(pmin=(50,50),pmax=(110,110),tag="diamond")
    dpg.draw_line((50,50),(330,50))
    dpg.draw_line((50,50),(50,330))
    dpg.draw_polyline([(330,50),(330,100),(300,220),(220,300),(100,330),(50,330)])


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()




