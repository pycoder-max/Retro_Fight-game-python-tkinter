import tkinter as tk

SCALE = 4
RESOURCE_FOLDER = "res"

MAX_HEALTH = 400

L_IDLE_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/idle{i}.png").zoom(SCALE)
                                   for i in ["", 2, 3]]

L_WALK_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/walk{i}.png").zoom(SCALE)
                                   for i in ["", 2, 3, 4]]

L_KICK_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/high kick{i}.png").zoom(SCALE)
                                   for i in range(1,6)]

L_PUNCH_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/punch{i}.png").zoom(SCALE)
                                   for i in range(1,4)]

L_AIRPUNCH_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/air punch{i}.png").zoom(SCALE)
                                   for i in range(1,5)]

L_AIRKICK_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/air kick{i}.png").zoom(SCALE)
                                   for i in range(1,4)]

L_LOWPUNCH_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/low punch{i}.png").zoom(SCALE)
                                   for i in range(1,4)]

L_LOWKICK_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/low kick{i}.png").zoom(SCALE)
                                   for i in range(1,7)]

L_HEADSHOTED_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/hurt head{i}.png").zoom(SCALE)
                                   for i in ["", 2]]

L_BODYSHOTED_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/hurt torso{i}.png").zoom(SCALE)
                                   for i in ["", 2]]

L_AIRHURT_IMAGES = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/hurt air.png").zoom(SCALE)
                   for _ in range(3)]

L_ONAIR_IMAGES = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/midair.png").zoom(SCALE)]

L_CROUCH_IMAGES = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/LeftPlayer/crouch.png").zoom(SCALE)]


R_IDLE_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/idle{i}.png").zoom(SCALE)
                                   for i in ["", 2, 3]]

R_WALK_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/walk{i}.png").zoom(SCALE)
                                   for i in ["", 2, 3, 4]]

R_KICK_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/high kick{i}.png").zoom(SCALE)
                                   for i in range(1,6)]

R_PUNCH_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/punch{i}.png").zoom(SCALE)
                                   for i in range(1,4)]

R_AIRPUNCH_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/air punch{i}.png").zoom(SCALE)
                                   for i in range(1,5)]

R_AIRKICK_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/air kick{i}.png").zoom(SCALE)
                                   for i in range(1,4)]

R_LOWPUNCH_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/low punch{i}.png").zoom(SCALE)
                                   for i in range(1,4)]

R_LOWKICK_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/low kick{i}.png").zoom(SCALE)
                                   for i in range(1,7)]

R_ONAIR_IMAGES = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/midair.png").zoom(SCALE)]

R_CROUCH_IMAGES = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/crouch.png").zoom(SCALE)]

R_HEADSHOTED_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/hurt head{i}.png").zoom(SCALE)
                                   for i in ["", 2]]

R_BODYSHOTED_IMAGES:list[tk.PhotoImage] = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/hurt torso{i}.png").zoom(SCALE)
                                   for i in ["", 2]]

R_AIRHURT_IMAGES = [tk.PhotoImage(file = f"{RESOURCE_FOLDER}/RightPlayer/hurt air.png").zoom(SCALE)
                   for _ in range(3)]