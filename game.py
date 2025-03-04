import tkinter as tk
import time as t
import colorsys as colsys


WINSIZE = [1325,700]
BG = "orange"

SCALE = 4


RESOURCE_FOLDER = "res"

GROUND_HEIGHT = WINSIZE[1] - 165

class Player:
    def __init__(self, x = 0 , y = 0, dir = 1, control_keys = ["down", "up", "right", "left", "comma", "period"]):
        self.x = x
        self.y = y
        self.sx = 0
        self.sy = 0 
        self.failing = 9
        self.state = "idle"
        self.dir = dir
        self.health = MAX_HEALTH
        self.visible_health = self.health

        self.hitbox_body = []
        self.hitbox_head = []
        self.hitbox_legs = []
        
        self.punchbox = []
        
        self.control_keys = control_keys
        self.keys : list[str] = []

    def handle_event(self, event : tk.Event, etype : str):
        if etype == "P":
            if event.keysym.lower() not in self.keys:
                self.keys.append(event.keysym.lower())

        if etype == "R":
            if event.keysym.lower() in self.keys:
                self.keys.remove(event.keysym.lower())

    def tick(self, tick, start_time):
        x, y = self.x, self.y
        self.punchbox = []
        self.head = 0

        self.failing += 1

        self.visible_health += ( self.health - self.visible_health ) / 9

        if player.control_keys == self.control_keys:
            
            if x - player2.x > -80 and  x - player2.x < 0 and abs(y - player2.y) < 30:
                if self.sx > 0.5:
                    x = player2.x - 80

            if x - player2.x > 0 and  x - player2.x < 80 and abs(y - player2.y) < 30:
                if self.sx < -0.5:
                    x = player2.x + 80
                    
            try:
                if self.state != "headshot" and self.state != "bodyshot" and self.state != "airshot":
                    acentre = [max(player2.punchbox[0], player2.punchbox[2]) - 10,
                            max(player2.punchbox[1], player2.punchbox[3]) - 10]
                    hcentre = [max(self.hitbox_head[0], self.hitbox_head[2]) - 20,
                            max(self.hitbox_head[1], self.hitbox_head[3]) - 20]

                    brad = (max(self.hitbox_body[0], self.hitbox_body[2]) - \
                            min(self.hitbox_body[0], self.hitbox_body[2])) / 2, \
                            (max(self.hitbox_body[1], self.hitbox_body[3]) - \
                            min(self.hitbox_body[1], self.hitbox_body[3])) / 2
                    
                    bcentre = [max(self.hitbox_body[0], self.hitbox_body[2]) - brad[0],
                              max(self.hitbox_body[1], self.hitbox_body[3]) - brad[1]]
                    

                    lrad = (max(self.hitbox_legs[0], self.hitbox_legs[2]) - \
                            min(self.hitbox_legs[0], self.hitbox_legs[2])) / 2, \
                            (max(self.hitbox_legs[1], self.hitbox_legs[3]) - \
                            min(self.hitbox_legs[1], self.hitbox_legs[3])) / 2
                    
                    lcentre = [max(self.hitbox_legs[0], self.hitbox_legs[2]) - lrad[0],
                              max(self.hitbox_legs[1], self.hitbox_legs[3]) - lrad[1]]

                    
                    rad = 15
                    if abs(hcentre[0] - acentre[0]) < rad and abs(hcentre[1] - acentre[1]) < rad:
                        self.state = "headshot" if self.failing < 3 else "airshot"
                        self.health -= 20 + abs(player2.sx * 4)
                        self.dir = 0 - player2.dir
                        self.sx += player2.dir * (8 if self.failing < 3 else 14) + (player2.sx * 2)
                        self.sy = 0 if self.failing < 3 else -10

                    else:
                        if abs(bcentre[0] - acentre[0]) < brad[0] + rad and abs(bcentre[1] - acentre[1]) < brad[0] + rad:
                            self.state = "bodyshot" if self.failing < 3 else "airshot"
                            self.health -= 10 + abs(player2.sx * 4)
                            self.dir = 0 - player2.dir
                            self.sx += player2.dir * (8 if self.failing < 3 else 14) + (player2.sx * 2)
                            self.sy = 0 if self.failing < 3 else -10
                        elif abs(lcentre[0] - acentre[0]) < lrad[0] + rad and abs(lcentre[1] - acentre[1]) < lrad[0] + rad:
                            self.state = "airshot"
                            self.health -= 25
                            self.dir = 0 - player2.dir
                            self.sx += player2.dir * 14 + (player2.sx * 2)
                            self.sy = -10

            except:
                pass


        if player2.control_keys == self.control_keys:

            if x - player.x > -50 and  x - player.x < 0 and abs(y - player.y) < 30:
                if self.sx > 0.5:
                    x = player.x - 51

            if x - player.x > 0 and  x - player.x < 50 and abs(y - player.y) < 30:
                if self.sx < -0.5:
                    x = player.x + 51

            try:
                if self.state != "headshot" and self.state != "bodyshot" and self.state != "airshot":
                    acentre = [max(player.punchbox[0], player.punchbox[2]) - 10,
                            max(player.punchbox[1], player.punchbox[3]) - 10]
                    hcentre = [max(self.hitbox_head[0], self.hitbox_head[2]) - 20,
                            max(self.hitbox_head[1], self.hitbox_head[3]) - 20]

                    brad = (max(self.hitbox_body[0], self.hitbox_body[2]) - \
                            min(self.hitbox_body[0], self.hitbox_body[2])) / 2, \
                            (max(self.hitbox_body[1], self.hitbox_body[3]) - \
                            min(self.hitbox_body[1], self.hitbox_body[3])) / 2
                    
                    bcentre = [max(self.hitbox_body[0], self.hitbox_body[2]) - brad[0],
                              max(self.hitbox_body[1], self.hitbox_body[3]) - brad[1]]
                    
                    lrad = (max(self.hitbox_legs[0], self.hitbox_legs[2]) - \
                            min(self.hitbox_legs[0], self.hitbox_legs[2])) / 2, \
                            (max(self.hitbox_legs[1], self.hitbox_legs[3]) - \
                            min(self.hitbox_legs[1], self.hitbox_legs[3])) / 2
                    
                    lcentre = [max(self.hitbox_legs[0], self.hitbox_legs[2]) - lrad[0],
                              max(self.hitbox_legs[1], self.hitbox_legs[3]) - lrad[1]]

                    rad = 15
                    if abs(hcentre[0] - acentre[0]) < rad and abs(hcentre[1] - acentre[1]) < rad:
                        self.state = "headshot" if self.failing < 3 else "airshot"
                        self.health -= 20 + abs(player.sx * 4)
                        self.dir = 0 - player.dir
                        self.sx += player.dir * (8 if self.failing < 3 else 14) + (player.sx * 2)
                        self.sy = 0 if self.failing < 3 else -10

                    else:
                        if abs(bcentre[0] - acentre[0]) < brad[0] + rad and abs(bcentre[1] - acentre[1]) < brad[0] + rad:
                            self.state = "bodyshot" if self.failing < 3 else "airshot"
                            self.health -= 10 + abs(player.sx * 4)
                            self.dir = 0 - player.dir
                            self.sx += player.dir * (8 if self.failing < 3 else 14) + (player.sx * 2)
                            self.sy = 0 if self.failing < 3 else -10

                        elif abs(lcentre[0] - acentre[0]) < lrad[0] + rad and abs(lcentre[1] - acentre[1]) < lrad[0] + rad:
                            self.state = "airshot"
                            self.health -= 25
                            self.dir = 0 - player.dir
                            self.sx += player.dir * 14 + (player.sx * 2)
                            self.sy = -10

            except:
                pass

        if x < 0 - 30:
            x = WINSIZE[0] + 30
        if x > WINSIZE[0] + 30:
            x = 0 - 30

        x += self.sx
        y += self.sy
        
        px, py = 0, 0
        if (self.state != "punch" and self.state != "kick" \
            and self.state != "lowpunch" and self.state != "lowkick"\
            and self.state != "airpunch" and self.state != "airkick"\
            and self.state != "headshot" and self.state != "bodyshot"\
            and self.state != "airshot") or self.failing > 3:
            py = (self.control_keys[0] in self.keys) - (self.control_keys[1] in self.keys) #power on y axis
            px = (self.control_keys[2] in self.keys) - (self.control_keys[3] in self.keys) # power on x axis

        self.dir = px if px != 0 else self.dir

        px = px if py != 1 else 0

        self.sx += px / 3 if self.failing < 3 else px 
        self.sy -= 22 if py == -1 and self.failing < 2 else 0

        self.sy += 1.5
        self.sx *= 0.85

        if y > GROUND_HEIGHT:
            self.sy = 0
            self.failing = 0
            y = GROUND_HEIGHT

        if (self.state != "punch" and self.state != "kick" \
            and self.state != "lowpunch" and self.state != "lowkick"\
            and self.state != "airpunch" and self.state != "airkick"\
            and self.state != "headshot" and self.state != "bodyshot"\
            and self.state != "airshot" and t.time() - start_time > 0.25):
            
            if (self.control_keys[4] in self.keys):
                tick = 0
                if self.failing > 3:
                    self.state = "airpunch"
                elif py == 1:
                    self.state = "lowpunch"
                else:
                    self.state = "punch"

            if (self.control_keys[5] in self.keys):
                tick = 0
                if self.failing < 2:
                    self.state = "kick"
                    if py == 1:
                        self.state = "lowkick"
                else:
                    self.state = "airkick"


        if (self.state != "punch" and self.state != "kick" \
            and self.state != "lowpunch" and self.state != "lowkick"\
            and self.state != "airpunch" and self.state != "airkick"\
            and self.state != "headshot" and self.state != "bodyshot"\
            and self.state != "airshot"):

            if self.failing < 3:
                if px == 0:
                    self.state = "idle"
                else:
                    self.state = "walk"
                
                if py == 1:
                    self.state = "crouch"
            else:
                self.state = "air"

        tick += 0.25
        match self.state:
            case "idle":
                tick %= L_IDLE_IMAGES.__len__()
            case "air":
                tick %= 1
            case "walk":
                tick %= L_WALK_IMAGES.__len__()
            case "crouch":
                tick %= 1
            case "punch":
                tick %= L_PUNCH_IMAGES.__len__()
                self.punchbox = [x + 40, y - 15, x + 60, y-35] if self.dir == 1 \
                                else [x - 40, y - 15, x - 60, y-35]
                if tick == 0:
                    start_time = t.time()
                    self.state = "idle"
            case "kick":
                tick %= L_KICK_IMAGES.__len__()
                self.punchbox = [x + 60, y - 40, x + 80, y - 60] if self.dir == 1 \
                                 else [x - 60, y - 40, x - 80, y - 60]
                if tick == 0:
                    start_time = t.time()
                    self.state = "idle"
            case "lowkick":
                tick %= L_LOWKICK_IMAGES.__len__()
                self.punchbox = [x + 25, y + 45, x + 45, y + 25] if self.dir == 1 \
                                else [x - 25, y + 45, x - 45, y + 25]
                if tick == 0:
                    start_time = t.time()
                    self.state = "crouch"
            case "lowpunch":
                self.punchbox = [x + 25, y + 35, x + 45, y + 15] if self.dir == 1 \
                                else [x - 25, y + 35, x - 45, y + 15]
                tick %= L_LOWPUNCH_IMAGES.__len__()
                if tick == 0:
                    start_time = t.time()
                    self.state = "crouch"
            case "airkick":
                self.punchbox = [x + 35, y + 35, x + 55, y + 15] if self.dir == 1 \
                                else [x - 35, y + 35, x - 55, y + 15]
                tick %= L_AIRKICK_IMAGES.__len__()
                if tick == 0:
                    start_time = t.time()
                    self.state = "idle"
            case "airpunch":
                self.punchbox = [x + 20, y + 5, x + 40, y-15] if self.dir == 1 \
                                else [x - 20, y + 5, x - 40, y-15]
                tick %= L_AIRPUNCH_IMAGES.__len__()
                if tick == 0:
                    start_time = t.time()
                    self.state = "idle"
            case "headshot":
                tick %= L_HEADSHOTED_IMAGES.__len__()
                if tick == 0:
                    start_time = t.time()
                    self.state = "idle"
            case "bodyshot":
                tick %= L_BODYSHOTED_IMAGES.__len__()
                if tick == 0:
                    start_time = t.time()
                    self.state = "idle"
            case "airshot":
                tick %= L_AIRHURT_IMAGES.__len__()
                if tick == 0:
                    start_time = t.time()
                    self.state = "air"

        self.draw(tick)
        
        if py == 1:
            self.hitbox_body = [x - 20, y + 10, x + 15, y + 38]
        else:
            self.hitbox_body = [x - 20, y - 35, x + 15, y + 8]

        if py == 1:
            if self.dir == 1:
                self.hitbox_head = [x - 3, y + 10, x + 17, y - 10]
            else:
                self.hitbox_head = [x - 17, y + 10, x + 3, y - 10]
        else:
            self.hitbox_head = [x - 15, y - 40, x + 15, y - 60]

        
        self.hitbox_legs = [x - 25, y + 10, x + 25, y + 65]

        self.x, self.y = x, y


        return start_time, tick
    
    def draw(self, tick):
        x, y = self.x, self.y
        if self.dir == 1:
            match self.state:
                case "idle":
                    canvas.create_image(x, y, image = L_IDLE_IMAGES[int(tick)])
                case "air":
                    canvas.create_image(x, y, image = L_ONAIR_IMAGES[int(tick)])
                case "walk":
                    canvas.create_image(x, y, image = L_WALK_IMAGES[int(tick)])
                case "headshot":
                    canvas.create_image(x, y, image = L_HEADSHOTED_IMAGES[int(tick)])
                case "bodyshot":
                    canvas.create_image(x, y, image = L_BODYSHOTED_IMAGES[int(tick)])
                case "airshot":
                    canvas.create_image(x, y, image = L_AIRHURT_IMAGES[int(tick)])
                case "crouch":
                    y += 30
                    canvas.create_image(x, y, image = L_CROUCH_IMAGES[int(tick)])
                case "punch":
                    x += 15
                    canvas.create_image(x, y, image = L_PUNCH_IMAGES[int(tick)])
                case "kick":
                    x += 15
                    canvas.create_image(x, y, image = L_KICK_IMAGES[int(tick)])
                case "airkick":
                    canvas.create_image(x, y, image = L_AIRKICK_IMAGES[int(tick)])
                case "airpunch":
                    canvas.create_image(x, y, image = L_AIRPUNCH_IMAGES[int(tick)])
                case "lowkick":
                    y += 30
                    canvas.create_image(x, y, image = L_LOWKICK_IMAGES[int(tick)])
                case "lowpunch":
                    y += 30
                    canvas.create_image(x, y, image = L_LOWPUNCH_IMAGES[int(tick)])
        else:
            match self.state:
                case "idle":
                    canvas.create_image(x, y, image = R_IDLE_IMAGES[int(tick)])
                case "air":
                    canvas.create_image(x, y, image = R_ONAIR_IMAGES[int(tick)])
                case "walk":
                    canvas.create_image(x, y, image = R_WALK_IMAGES[int(tick)])
                case "headshot":
                    canvas.create_image(x, y, image = R_HEADSHOTED_IMAGES[int(tick)])
                case "bodyshot":
                    canvas.create_image(x, y, image = R_BODYSHOTED_IMAGES[int(tick)])
                case "airshot":
                    canvas.create_image(x, y, image = R_AIRHURT_IMAGES[int(tick)])
                case "crouch":
                    y += 30
                    canvas.create_image(x, y, image = R_CROUCH_IMAGES[int(tick)])
                case "punch":
                    x -= 15
                    canvas.create_image(x, y, image = R_PUNCH_IMAGES[int(tick)])
                case "kick":
                    x -= 15
                    canvas.create_image(x, y, image = R_KICK_IMAGES[int(tick)])
                case "airkick":
                    canvas.create_image(x, y, image = R_AIRKICK_IMAGES[int(tick)])
                case "airpunch":
                    canvas.create_image(x, y, image = R_AIRPUNCH_IMAGES[int(tick)])
                case "lowkick":
                    y += 30
                    canvas.create_image(x, y, image = R_LOWKICK_IMAGES[int(tick)])
                case "lowpunch":
                    y += 30
                    canvas.create_image(x, y, image = R_LOWPUNCH_IMAGES[int(tick)])
        
        y -= 80
        canvas.create_line( x - MAX_HEALTH / 8 - 2, y, x + MAX_HEALTH / 8 + 2, y, width = 14)
        canvas.create_line( x - MAX_HEALTH / 8 , y, x - MAX_HEALTH / 8 + self.visible_health / 4, y, width = 10, fill = "green") 
        

SUN_SIZE = 160

def loop(start_time1, start_time2, tick1 = 0, tick2 = 0, tick3 = 30):
    canvas.delete("all")

    canvas.create_oval(WINSIZE[0] / 2 - SUN_SIZE / 2, GROUND_HEIGHT - SUN_SIZE / 2 - 100,
                       WINSIZE[0] / 2 + SUN_SIZE / 2 , GROUND_HEIGHT + SUN_SIZE / 2 - 100,
                       fill = "yellow", outline = "")
    canvas.create_line(0, WINSIZE[1], WINSIZE[0], WINSIZE[1], width = 200)

    keys: list[str] = player.keys

    data2 = ["→" if k == "right" \
            else "←" if k == "left" \
            else "↑" if k == "up" \
            else "↓" if k == "down" \
            else "🤛" if k == "comma"\
            else "🦶" if k == "period"\
            else " " for k in keys]
    
    data1 = ["→" if k == "d" \
            else "←" if k == "a" \
            else "↑" if k == "w" \
            else "↓" if k == "s" \
            else "🤜" if k == "f"\
            else "🦶" if k == "g"\
            else " " for k in keys]

    canvas.create_text(100, 400, text= data1, font= ("Javanese Text", 20))
    canvas.create_text(WINSIZE[0] - 100, 400, text= data2, font=("Javanese Text", 20))
    
    tick3 += 2
    tick3 %= 100

    col = colsys.hsv_to_rgb(tick3 / 100 ,0.75,0.75)
    col = [format(int(p * 255), "x") for p in col]

    canvas.create_text(WINSIZE[0] // 2, 100, text= "Retro Fight is a PvP fighting game(🤼).\n \
    Player 1 can move using wasd keys and hit using Ⓖ and kick using Ⓗ \n \
    Player 2 can move using arrow keys and hit using [,] and kick using [.]\n \
    This game also supports arial atacks and low attacks + teleportation 🏃🏻🌌:¯_-¯-¯_¯:🌌🏃🏻 from sides",
    font= ("Segoe Script", 16, "bold"), fill= f"#{col[0] + col[1] + col[2]}")

    start_time1, tick1 = player.tick(tick1, start_time1)
    start_time2, tick2 = player2.tick(tick2, start_time2)


    if player.visible_health < 0:
        canvas.create_text(WINSIZE[0] // 2, WINSIZE[1] // 2, text = "Player 1 Won \n \
        Press Ⓡ to restart game", font = ("bold", 22))
    elif player2.visible_health < 0:
        canvas.create_text(WINSIZE[0] // 2, WINSIZE[1] // 2, text = "Player 2 Won \n \
        Press Ⓡ to restart game", font = ("bold", 22))
    else:
        root.after(30, loop, start_time1, start_time2, tick1, tick2, tick3)

def global_event_handler(event : tk.Event, etype):

    if etype == "P":
        if event.keysym.lower() == "r":
            if player2.visible_health < 0 or player.visible_health < 0:
                player.__init__(WINSIZE[0] - 100, 400, -1)
                player2.__init__(100, 400, 1, ["s", "w", "d", "a", "f", "g"])
                loop(t.time(), t.time())
            else:
                player.__init__(WINSIZE[0] - 100, 400, -1)
                player2.__init__(100, 400, 1, ["s", "w", "d", "a", "f", "g"])

    player.handle_event(event, etype)
    player2.handle_event(event, etype)


root = tk.Tk()
root.wm_title("Retro Fight!")
root.wm_geometry(f"{WINSIZE[0]}x{WINSIZE[1]}")

#some sort of linux versions doesn't allow this
try:
    root.wm_state("zoomed")
except:
    pass

root.wm_resizable(False, False)


#load images
from settings import *

canvas = tk.Canvas(root, width = WINSIZE[0], height = WINSIZE[1], bg = BG)
canvas.pack(padx = 20, pady = 20)

player = Player(WINSIZE[0] - 100, 400, -1)
player2 = Player(100, 400, 1, ["s", "w", "d", "a", "f", "g"])

loop(t.time(), t.time())


root.bind("<KeyPress>", lambda event: global_event_handler(event, "P"))
root.bind("<KeyRelease>", lambda event: global_event_handler(event, "R"))

root.mainloop()
