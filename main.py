import dearpygui.dearpygui as dpg
import random

# get teams
# -set rosters for both teams.
# -generate players/teams if necessary.

# get location
# -select location or generate a field/surface
# -set weather conditions and time of day

# play ball
# -simulate gameplay
# -output a play-by-play and stats for each player

STRIKE_ZONE_HEIGHT = 250
STRIKE_ZONE_WIDTH = 150

def throwPitch():
    #Choose pitch type
    #aim pitch
    #throw pitch

    pitchAccuracy = 1.0
    pitchSpeed = 1.0
    pitchTarget = (0,0)

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
    dpg.add_text(ballOrStrike,tag="lastPitchCall",parent="strike_zone")



dpg.create_context()
dpg.create_viewport(title='Play Ball', width=600, height=600)

with dpg.window(width=300,height=500,tag="strike_zone"):
    dpg.add_button(label="Throw Pitch",callback=throwPitch)
    dpg.draw_rectangle(pmin=(50, 100), pmax=(50+STRIKE_ZONE_WIDTH, 100+STRIKE_ZONE_HEIGHT))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()




