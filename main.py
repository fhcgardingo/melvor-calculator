# importando tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tokenize import String
from turtle import width
from xml.sax import parseString
import pandas as pd
import datetime as date
from pyparsing import col
import math
import tkmacosx
import items

root = tk.Tk()
root.title("Tab Widget")
root.geometry("1400x650")
root.resizable(0, 0)

style = ttk.Style()
style.theme_use("aqua")

tabControl = ttk.Notebook(root)
tabControl.place(x=0, y=0, width=1400, height=650)

# cores
cor1 = "#3b3b3b"

# global functions


def total_xp(current, desired):
    current_xp = current
    desired_level_get = desired

    if current:
        desired_lvl_df = pd.read_excel("xp.xlsx")
        desired_lvl = int(
            desired_lvl_df.loc[desired_lvl_df["level"] == int(desired_level_get), "exp"]
        )
        total_xp = desired_lvl - int(current_xp)
        return total_xp
    else:
        return 0


# woodcutting
tab1 = Frame(tabControl)
tabControl.add(tab1, text="Woodcutting")

fr_wood_esq = Frame(tab1, borderwidth=1, relief="solid")
fr_wood_esq.place(x=0, y=0)
fr_wood_dir = Frame(tab1, borderwidth=1, relief="solid")
fr_wood_dir.place(x=266, y=0)

# functions wood


# fr esquerdo woodcutting


tree1_wood_text = Label(fr_wood_esq, text="Tree 1")
tree1_wood_text.grid(column=0, row=0)
tree2_wood_text = Label(fr_wood_esq, text="Tree 2")
tree2_wood_text.grid(column=0, row=1)
skillcape_wood_text = Label(fr_wood_esq, text="Skill Cape")
skillcape_wood_text.grid(column=0, row=2)
master_wood_text = Label(fr_wood_esq, text="Master of Nature")
master_wood_text.grid(column=0, row=3)
current_wood_text = Label(fr_wood_esq, text="Current Axe")
current_wood_text.grid(column=0, row=4)
mastery_wood_text = Label(fr_wood_esq, text="Mastery")
mastery_wood_text.grid(column=0, row=5)


def skillcape_wood():
    skillcape_wood = var_skillcape_wood.get()
    return skillcape_wood


def master_wood():
    master_wood = var_master_wood.get()
    return master_wood


wood_list = [
    "Normal",
    "Oak",
    "Willow",
    "Teak",
    "Maple",
    "Mahogany",
    "Yew",
    "Magic",
    "Redwood",
    "None",
]
var_wood_list1 = StringVar()
var_wood_list1.set(wood_list[0])
var_wood_list2 = StringVar()
var_wood_list2.set(wood_list[9])
tree1_wood_resp = OptionMenu(fr_wood_esq, var_wood_list1, *wood_list)
tree1_wood_resp.grid(column=1, row=0)
tree2_wood_resp = OptionMenu(fr_wood_esq, var_wood_list2, *wood_list)
tree2_wood_resp.grid(column=1, row=1)
var_skillcape_wood = IntVar()
skillcape_wood_resp = Checkbutton(
    fr_wood_esq,
    variable=var_skillcape_wood,
    onvalue=1,
    offvalue=0,
    command=skillcape_wood,
)
skillcape_wood_resp.grid(column=1, row=2)
var_master_wood = IntVar()
master_wood_resp = Checkbutton(
    fr_wood_esq, variable=var_master_wood, onvalue=1, offvalue=0, command=master_wood
)
master_wood_resp.grid(column=1, row=3)
axe_list = ["Base", "Iron", "Steel", "Black", "Mithril", "Adamant", "Rune", "Dragon"]
var_material_axe_list = StringVar()
var_material_axe_list.set(axe_list[0])
current_wood_resp = OptionMenu(fr_wood_esq, var_material_axe_list, *axe_list)
current_wood_resp.grid(column=1, row=4)
lvl_list = list(range(1, 100))
var_mastery_wood = StringVar()
var_mastery_wood.set(lvl_list[0])
mastery_wood_resp = OptionMenu(fr_wood_esq, var_mastery_wood, *lvl_list)
mastery_wood_resp.grid(column=1, row=5)

# fr direito woodcutting
xp_skill_hr_tree_text = Label(fr_wood_dir, text="Xp/Hr per Tree")
xp_skill_hr_tree_text.grid(column=0, row=0)
logs_hour_text = Label(fr_wood_dir, text="Logs/Hour")
logs_hour_text.grid(column=1, row=0)
total_xp_skill_hr_text = Label(fr_wood_dir, text="Total Xp/Hr")
total_xp_skill_hr_text.grid(column=0, row=4)
current_xp_wood_text = Label(fr_wood_dir, text="Current Xp")
current_xp_wood_text.grid(column=0, row=5)
desired_lvl_wood_text = Label(fr_wood_dir, text="Desired Level")
desired_lvl_wood_text.grid(column=0, row=6)
hours_till_lvl_wood_text = Label(fr_wood_dir, text="Hours Till Lvl")
hours_till_lvl_wood_text.grid(column=0, row=7)
total_logs1_wood_text = Label(fr_wood_dir, text="Total Logs 1")
total_logs1_wood_text.grid(column=0, row=8)
total_logs2_wood_text = Label(fr_wood_dir, text="Total Logs2")
total_logs2_wood_text.grid(column=0, row=9)


xp_skill_hr_tree1_resp = Label(fr_wood_dir, text="0")
xp_skill_hr_tree1_resp.grid(column=0, row=2)
xp_skill_hr_tree2_resp = Label(fr_wood_dir, text="0")
xp_skill_hr_tree2_resp.grid(column=0, row=3)
logs_hour1_resp = Label(fr_wood_dir, text="0")
logs_hour1_resp.grid(column=1, row=2)
logs_hour2_resp = Label(fr_wood_dir, text="0")
logs_hour2_resp.grid(column=1, row=3)
total_xp_skill_hr_resp = Label(fr_wood_dir, text="0")
total_xp_skill_hr_resp.grid(column=1, row=4)
current_xp_wood_resp = Entry(fr_wood_dir, width=10)
current_xp_wood_resp.grid(column=1, row=5)
var_desired_wood = StringVar()
desired_lvl_wood_resp = OptionMenu(fr_wood_dir, var_desired_wood, *lvl_list)
desired_lvl_wood_resp.grid(column=1, row=6)
hours_till_lvl_wood_resp = Label(fr_wood_dir, text="00:00:00")
hours_till_lvl_wood_resp.grid(column=1, row=7)
total_logs1_wood_resp = Label(fr_wood_dir, text="0")
total_logs1_wood_resp.grid(column=1, row=8)
total_logs2_wood_resp = Label(fr_wood_dir, text="0")
total_logs2_wood_resp.grid(column=1, row=9)

# functions Woodcutting


def adj_cut_time(typetree, typeaxe):
    type_tree = typetree
    type_axe = typeaxe

    if type_axe == "Iron":
        percent_axe = 0.95
    elif type_axe == "Steel":
        percent_axe = 0.90
    elif type_axe == "Black":
        percent_axe = 0.80
    elif type_axe == "Mithril":
        percent_axe = 0.75
    elif type_axe == "Adamant":
        percent_axe = 0.65
    elif type_axe == "Rune":
        percent_axe = 0.60
    elif type_axe == "Dragon":
        percent_axe = 0.50
    else:
        percent_axe = 1

    master_of_nature = master_wood()
    if master_of_nature == 1:
        percent_master = 0.80
    else:
        percent_master = 1

    get_wood_df = pd.read_excel("Woodcutting.xlsx")
    cuttime = int(get_wood_df.loc[get_wood_df["Tree"] == type_tree, "Cut Time"])
    adjcuttime = cuttime * percent_axe * percent_master
    return adjcuttime


def get_exp_tree(typep):
    type_tree = typep
    get_exp_tree_df = pd.read_excel("Woodcutting.xlsx")
    exp = int(get_exp_tree_df.loc[get_exp_tree_df["Tree"] == type_tree, "Exp"])
    return exp


# TODO tentar usar somente uma func xp_skill_hr_per_tree passando parametros
def xp_skill_hr_per_tree1():
    adjcuttime_tree1 = adj_cut_time(var_wood_list1.get(), var_material_axe_list.get())
    type_tree1 = var_wood_list1.get()
    exp_tree1 = get_exp_tree(type_tree1)

    if (exp_tree1 == 0) or (type_tree1 == "None"):
        xp_skill_hr_tree1_resp["text"] = 0
        xp_hour = 0
    else:
        xp_hour = exp_tree1 / (round(adjcuttime_tree1, 2)) * 3600
        xp_skill_hr_tree1_resp["text"] = round(xp_hour)
    return round(xp_hour)


def xp_skill_hr_per_tree2():
    adjcuttime_tree2 = adj_cut_time(var_wood_list2.get(), var_material_axe_list.get())
    type_tree2 = var_wood_list2.get()
    exp_tree2 = get_exp_tree(type_tree2)

    if (exp_tree2 == 0) or (type_tree2 == "None"):
        xp_skill_hr_tree2_resp["text"] = 0
        xp_hour = 0
    else:
        xp_hour = exp_tree2 / (round(adjcuttime_tree2, 2)) * 3600
        xp_skill_hr_tree2_resp["text"] = round(xp_hour)
    return round(xp_hour)


# TODO tentar usar somente uma func logs_hour passando parametros
def logs_hour1():
    adjcuttime_log1 = adj_cut_time(var_wood_list1.get(), var_material_axe_list.get())
    type_tree_log1 = var_wood_list1.get()
    level_log1 = var_mastery_wood.get()

    skill_cape = skillcape_wood()
    if skill_cape == 1:
        percent_skill = 2
    else:
        percent_skill = 1

    # logs/hour func
    if type_tree_log1 != "None":
        logs_hour_base = 3600 / (round(adjcuttime_log1, 2))
        woodcutting_df = pd.read_excel("Woodcutting.xlsx")
        mastery_multiplier = woodcutting_df.loc[
            woodcutting_df["Level"] == int(level_log1), "Multiplier"
        ]
        logs_hour = float(mastery_multiplier) * round(logs_hour_base) * percent_skill
        logs_hour1_resp["text"] = round(logs_hour)
    else:
        logs_hour1_resp["text"] = 0


def logs_hour2():
    adjcuttime_log2 = adj_cut_time(var_wood_list2.get(), var_material_axe_list.get())
    type_tree_log2 = var_wood_list2.get()
    level_log2 = var_mastery_wood.get()

    skill_cape = skillcape_wood()
    if skill_cape == 1:
        percent_skill = 2
    else:
        percent_skill = 1

    # logs/hour func
    if type_tree_log2 != "None":
        logs_hour_base = 3600 / (round(adjcuttime_log2, 2))
        woodcutting_df = pd.read_excel("Woodcutting.xlsx")
        mastery_multiplier = woodcutting_df.loc[
            woodcutting_df["Level"] == int(level_log2), "Multiplier"
        ]
        logs_hour = float(mastery_multiplier) * round(logs_hour_base) * percent_skill
        logs_hour2_resp["text"] = round(logs_hour)
    else:
        logs_hour2_resp["text"] = 0


def total_xp_skill_hr_wood():
    xp_tree1 = xp_skill_hr_per_tree1()
    xp_tree2 = xp_skill_hr_per_tree2()

    if (xp_tree1 != 0) and (xp_tree2 != 0):
        total_xp_skill_hr = xp_tree1 + xp_tree2
    elif (xp_tree1 != 0) and (xp_tree2 == 0):
        total_xp_skill_hr = xp_tree1
    elif (xp_tree1 == 0) and (xp_tree2 != 0):
        total_xp_skill_hr = xp_tree2
    else:
        total_xp_skill_hr = 0

    total_xp_skill_hr_resp["text"] = total_xp_skill_hr
    # print(total_xp_skill_hr)
    return total_xp_skill_hr


def hours_till_lvl_wood():
    xp_hour = total_xp(current_xp_wood_resp.get(), var_desired_wood.get())
    total_xp = total_xp_skill_hr_wood()

    if total_xp != 0:
        hours_till = xp_hour / total_xp
        hours_round = round(hours_till, 2)
        hora, minuto = str(hours_round).split(".")
        minuto2, segundo = str(round((int(minuto) * 0.6), 2)).split(
            "."
        )  # setar segundos para duas casa somente
        hours = "{}:{}:{}".format(hora, minuto2, segundo)
        hours_till_lvl_wood_resp["text"] = hours
    else:
        hours_till_lvl_wood_resp["text"] = 0


def total_logs1():
    total_xp_log1 = total_xp(current_xp_wood_resp.get(), var_desired_wood.get())
    total_xp = total_xp_skill_hr_wood()
    type_tree1 = var_wood_list1.get()

    if total_xp != 0:
        hours_till = total_xp_log1 / total_xp
        hours_round = round(hours_till, 2)

        logs_hour_df = pd.read_excel("Woodcutting.xlsx")
        logs_hour = int(
            logs_hour_df.loc[logs_hour_df["Tree"] == type_tree1, "Logs/Hour"]
        )
        total_logs1 = hours_round * logs_hour
        total_logs1_wood_resp["text"] = round(total_logs1)
    else:
        total_logs1_wood_resp["text"] = 0


def total_logs2():
    total_xp_log2 = total_xp(current_xp_wood_resp.get(), var_desired_wood.get())
    total_xp = total_xp_skill_hr_wood()
    type_tree2 = var_wood_list2.get()

    if total_xp != 0:
        hours_till = total_xp_log2 / total_xp
        hours_round = round(hours_till, 2)

        logs_hour_df = pd.read_excel("Woodcutting.xlsx")
        logs_hour = int(
            logs_hour_df.loc[logs_hour_df["Tree"] == type_tree2, "Logs/Hour"]
        )
        total_logs2 = hours_round * logs_hour
        total_logs2_wood_resp["text"] = round(total_logs2)
    else:
        total_logs2_wood_resp["text"] = 0


def button_calculate():
    xp_skill_hr_per_tree1()
    xp_skill_hr_per_tree2()
    logs_hour1()
    logs_hour2()
    total_xp_skill_hr_wood()
    hours_till_lvl_wood()
    total_logs1()
    total_logs2()


# buttons woodcutting
calculate_wood = Button(fr_wood_esq, text="Calcular", command=button_calculate)
calculate_wood.grid(column=0, row=7)


# Fishing
tab2 = Frame(tabControl)
tabControl.add(tab2, text="Fishing")

# frames
fr_fish_esq = Frame(tab2, borderwidth=1, relief="solid")
fr_fish_esq.place(x=0, y=0)
fr_fish_dir = Frame(tab2, borderwidth=1, relief="solid")
fr_fish_dir.place(x=266, y=0)

# frame 1
rod_text = Label(fr_fish_esq, text="Rod")
rod_text.grid(column=0, row=0)
fish_text = Label(fr_fish_esq, text="Fish")
fish_text.grid(column=0, row=1)
pet_text = Label(fr_fish_esq, text="Pet")
pet_text.grid(column=0, row=2)
skill_text = Label(fr_fish_esq, text="Skill Cape")
skill_text.grid(column=0, row=3)
mastery_text = Label(fr_fish_esq, text="Mastery Lvl")
mastery_text.grid(column=0, row=4)
potion_text = Label(fr_fish_esq, text="Fisherman's Potion")
potion_text.grid(column=0, row=5)
amulet_text = Label(fr_fish_esq, text="Amulet of Fishing")
amulet_text.grid(column=0, row=6)
pirates_text = Label(fr_fish_esq, text="Pirates Lost Ring")
pirates_text.grid(column=0, row=7)

# TODO terminar funções
def pet_fish():
    pass


def skill_fish():
    pass


def amulet_fish():
    pass


def pirate_fish():
    pass


material_list = [
    "Base",
    "Iron",
    "Steel",
    "Balck",
    "Mithril",
    "Adamant",
    "Rune",
    "Dragon",
]
var_rod_fish = StringVar()
var_rod_fish.set(material_list[0])
rod_fish_resp = OptionMenu(fr_fish_esq, var_rod_fish, *material_list)
rod_fish_resp.grid(column=1, row=0)
fish_list = [
    "Shrimp",
    "Sardine",
    "Blowfish",
    "Herring",
    "Seahorse",
    "Trout",
    "Leaping Trout",
    "Poison Fish",
    "Salmon",
    "Leaping Salmon",
    "Lobster",
    "Skeleton Fish",
    "Swordfish",
    "Anglerfish",
    "Fanfish",
    "Crab",
    "carp",
    "Shark",
    "Leaping Broad Fish",
    "Cave Fish",
    "Magic Fish",
    "Manta Fish",
    "Whale",
]
var_fish_list = StringVar()
var_fish_list.set(fish_list[0])
fish_resp = OptionMenu(fr_fish_esq, var_fish_list, *fish_list)
fish_resp.grid(column=1, row=1)
var_pet_fish = IntVar()
pet_fish_resp = Checkbutton(
    fr_fish_esq, variable=var_pet_fish, onvalue=1, offvalue=0, command=pet_fish
)
pet_fish_resp.grid(column=1, row=2)
var_skill_fish = IntVar()
skill_fish_resp = Checkbutton(
    fr_fish_esq, variable=var_skill_fish, onvalue=1, offvalue=0, command=skill_fish
)
skill_fish_resp.grid(column=1, row=3)
var_mastery_fish = IntVar()
mastery_fish_resp = OptionMenu(fr_fish_esq, var_mastery_fish, *lvl_list)
mastery_fish_resp.grid(column=1, row=4)
potion_list = ["No", "1", "2", "3", "4"]
var_potion_fish = StringVar()
var_potion_fish.set(potion_list[0])
potion_fish_resp = OptionMenu(fr_fish_esq, var_potion_fish, *potion_list)
potion_fish_resp.grid(column=1, row=5)
var_amulet_fish = IntVar()
amulet_fish_resp = Checkbutton(
    fr_fish_esq, variable=var_amulet_fish, onvalue=1, offvalue=0, command=amulet_fish
)
amulet_fish_resp.grid(column=1, row=6)
var_pirate_fish = IntVar()
pirate_fish_resp = Checkbutton(
    fr_fish_esq, variable=var_pirate_fish, onvalue=1, offvalue=0, command=pirate_fish
)
pirate_fish_resp.grid(column=1, row=7)

# frame 2
fish_hr_text = Label(fr_fish_dir, text="Fish/Hr")
fish_hr_text.grid(column=0, row=0)
xp_skill_hr_text = Label(fr_fish_dir, text="Xp/Hr")
xp_skill_hr_text.grid(column=0, row=1)
gp_hr_text = Label(fr_fish_dir, text="Gp/Hr")
gp_hr_text.grid(column=0, row=2)
current_text = Label(fr_fish_dir, text="Current Xp")
current_text.grid(column=0, row=3)
desired_text = Label(fr_fish_dir, text="Desired Level")
desired_text.grid(column=0, row=4)
hours_text = Label(fr_fish_dir, text="Hours Till Lvl")
hours_text.grid(column=0, row=5)

fish_hr_resp = Label(fr_fish_dir, text="função")
fish_hr_resp.grid(column=1, row=0)
xp_fish_resp = Label(fr_fish_dir, text="função")
xp_fish_resp.grid(column=1, row=1)
gp_fish_resp = Label(fr_fish_dir, text="função")
gp_fish_resp.grid(column=1, row=2)
current_fish_resp = Entry(fr_fish_dir, width=10)
current_fish_resp.grid(column=1, row=3)
var_desired_fish = StringVar()
var_desired_fish.set(lvl_list[0])
desired_fish_resp = OptionMenu(fr_fish_dir, var_desired_fish, *lvl_list)
desired_fish_resp.grid(column=1, row=4)
hour_fish_resp = Label(fr_fish_dir, text="função")
hour_fish_resp.grid(column=1, row=5)

# functions fish

# Firemaking
tab3 = Frame(tabControl)
tabControl.add(tab3, text="Firemaking")

# frames
fr_fire_esq = Frame(tab3, borderwidth=1, relief="solid")
fr_fire_esq.place(x=0, y=0)
fr_fire_dir = Frame(tab3, borderwidth=1, relief="solid")
fr_fire_dir.place(x=266, y=0)

# frame 1

logs_fire_text = Label(fr_fire_esq, text="Logs")
logs_fire_text.grid(column=0, row=0)
art_of_control_fire_text = Label(fr_fire_esq, text="Art of Control")
art_of_control_fire_text.grid(column=0, row=1)
lvl_fire_text = Label(fr_fire_esq, text="Lvl 99")
lvl_fire_text.grid(column=0, row=2)
bonfire_text = Label(fr_fire_esq, text="Bonfire")
bonfire_text.grid(column=0, row=3)
controlled_heat_text = Label(fr_fire_esq, text="Controlled Heat")
controlled_heat_text.grid(column=0, row=4)

# functions checkbuttons
# TODO terminar funções
def art_of_control():
    pass


def lvl_fire():
    pass


def bonfire():
    pass


def controlled_heat():
    pass


var_fire_logs = StringVar()
var_fire_logs.set(wood_list[0])
logs_fire_resp = OptionMenu(fr_fire_esq, var_fire_logs, *wood_list)
logs_fire_resp.grid(column=1, row=0)
var_art_of_control = IntVar()
art_of_control_fire_resp = Checkbutton(
    fr_fire_esq,
    variable=var_art_of_control,
    onvalue=1,
    offvalue=0,
    command=art_of_control,
)
art_of_control_fire_resp.grid(column=1, row=1)
var_lvl_fire = IntVar()
lvl_fire_resp = Checkbutton(
    fr_fire_esq, variable=var_lvl_fire, onvalue=1, offvalue=0, command=lvl_fire
)
lvl_fire_resp.grid(column=1, row=2)
var_bonfire = IntVar()
bonfire_resp = Checkbutton(
    fr_fire_esq, variable=var_bonfire, onvalue=1, offvalue=0, command=bonfire
)
bonfire_resp.grid(column=1, row=3)
var_controlled_heat = IntVar()
controlled_heat_resp = Checkbutton(
    fr_fire_esq,
    variable=var_controlled_heat,
    onvalue=1,
    offvalue=0,
    command=controlled_heat,
)
controlled_heat_resp.grid(column=1, row=4)

# frame 2

xp_log_fire_text = Label(fr_fire_dir, text="XP/Log")
xp_log_fire_text.grid(column=0, row=0)
xp_skill_hr_fire_text = Label(fr_fire_dir, text="XP/Hr")
xp_skill_hr_fire_text.grid(column=0, row=1)
coal_hr_fire_text = Label(fr_fire_dir, text="Caol/Hr")
coal_hr_fire_text.grid(column=0, row=2)
current_xp_fire_text = Label(fr_fire_dir, text="Current XP")
current_xp_fire_text.grid(column=0, row=3)
desired_lvl_fire_text = Label(fr_fire_dir, text="Desired Level")
desired_lvl_fire_text.grid(column=0, row=4)
logs_needed_fire_text = Label(fr_fire_dir, text="Logs Needed")
logs_needed_fire_text.grid(column=0, row=5)

xp_log_fire_resp = Label(fr_fire_dir, text="0")
xp_log_fire_resp.grid(column=1, row=0)
xp_skill_hr_fire_resp = Label(fr_fire_dir, text="0")
xp_skill_hr_fire_resp.grid(column=1, row=1)
coal_hr_fire_resp = Label(fr_fire_dir, text="0")
coal_hr_fire_resp.grid(column=1, row=2)
current_xp_fire_resp = Entry(fr_fire_dir, width=10)
current_xp_fire_resp.grid(column=1, row=3)
var_desired_lvl_fire = IntVar()
var_desired_lvl_fire.set([0])
desired_lvl_fire_resp = OptionMenu(fr_fire_dir, var_desired_lvl_fire, *lvl_list)
desired_lvl_fire_resp.grid(column=1, row=4)
logs_needed_fire_resp = Label(fr_fire_dir, text="0")
logs_needed_fire_resp.grid(column=1, row=5)

# functions firemaking

# Cooking
tab4 = Frame(tabControl)
tabControl.add(tab4, text="Cooking")

# frames
fr_skill_boosts_cooking = Frame(tab4, borderwidth=1, relief="solid")
fr_skill_boosts_cooking.place(x=0, y=0)
fr_cooking_fire = Frame(tab4, borderwidth=1, relief="solid")
fr_cooking_fire.place(x=312, y=0)
fr_furnance = Frame(tab4, borderwidth=1, relief="solid")
fr_furnance.place(x=550, y=0)
fr_pot = Frame(tab4, borderwidth=1, relief="solid")
fr_pot.place(x=822, y=0)
fr_xp_calc_cooking = Frame(tab4, borderwidth=1, relief="solid")
fr_xp_calc_cooking.place(x=1078, y=0)

# lists cooking
log_list = [
    "Normal",
    "Oak",
    "Willow",
    "Teak",
    "Maple",
    "Mahogany",
    "Yew",
    "Magic",
    "Redwood",
]
recipe_cooking_fire_list = [
    "Shrimp",
    "Beef",
    "Sardine",
    "Herring",
    "Seahorse",
    "Trout",
    "Salmon",
    "Lobster",
    "Swordfish",
    "Anglerfish",
    "Fanfish",
    "Crab",
    "Carp",
    "Shark",
    "Cave Fish",
    "Manta Ray",
    "Whale",
]
recipe_cooking_furnance_list = [
    "Bread",
    "Chicken",
    "Plain Pizza Slice",
    "Beef Pie",
    "Meat Pizza Slice",
    "Strawberry Cupcake",
    "Cherry Cupcake",
    "Apple Pie",
    "Strawberry Cake",
    "Carrot Cake",
]
recipe_cooking_pot_list = [
    "Basic Soup",
    "Hearty Soup",
    "Cream Corn Soup",
    "Chicken Soup",
]
cape_skill_cook_list = [
    "Cape of Completion",
    "Cooking Skillcape",
    "Maximum Skillcape",
    "None",
]
recipe_cook_list = (
    recipe_cooking_fire_list + recipe_cooking_furnance_list + recipe_cooking_pot_list
)
summoning_boosts_list = ["Octopus + Devil", "Mole + Pig", "Pig + Salamander", "None"]
# classes


class items_cook:
    def __init__(self, ckint, xpm, xps):
        self.ckint = ckint
        self.xpm = xpm
        self.xps = xps

    def ckint_item(self):
        return self.ckint

    def xps_item(self):
        return self.xps

    def xpm_item(self):
        return self.xpm


# checkbutton functions
def cooking_gloves():
    cooking_gloves = var_cooking_gloves.get()
    if cooking_gloves != 0:
        return 10
    else:
        return 0


def art_of_control_cook():
    art_of_control_cook = var_art_of_control_cook.get()
    if art_of_control_cook == 1:
        return 0.85
    else:
        return 1


def chef_hat():
    chef_hat = var_chef_hat.get()
    if chef_hat != 0:
        item_chef_hat = items_cook(0.1, 1.01, 1.01)
        return item_chef_hat
    else:
        item_chef_hat = items_cook(0, 1, 1)
        return item_chef_hat


def cooking_apron():
    ancient_ring_of_skills = var_ancient_ring_of_skills.get()
    if ancient_ring_of_skills != 0:
        item_ancient_ring_of_skills = items_cook(0, 1.01, 1.01)
        return item_ancient_ring_of_skills
    else:
        item_ancient_ring_of_skills = items_cook(0, 1, 1)
        return item_ancient_ring_of_skills


def ancient_ring_of_skills():
    cooking_apron = var_cooking_apron.get()
    if cooking_apron != 0:
        item_cooking_apron = items_cook(0, 1, 1.01)
        return item_cooking_apron
    else:
        item_cooking_apron = items_cook(0, 1, 1)
        return item_cooking_apron


def chef_spoon():
    chef_spoon = var_chef_spoon.get()
    if chef_spoon != 0:
        item_chef_spoon = items_cook(0, 1.01, 1.01)
        return item_chef_spoon
    else:
        item_chef_spoon = items_cook(0, 1, 1)
        return item_chef_spoon


def burning_coals():
    burning_coals = var_burning_coals.get()
    if burning_coals != 0:
        item_burning_coals = items_cook(0, 1, 1.03)
        return item_burning_coals
    else:
        item_burning_coals = items_cook(0, 1, 1)
        return item_burning_coals


def sweltering_pools():
    sweltering_pools = var_sweltering_pools.get()
    if sweltering_pools != 0:
        item_sweltering_pools = items_cook(0.97, 1.03, 1)
        return item_sweltering_pools
    else:
        item_sweltering_pools = items_cook(1, 1, 1)
        return item_sweltering_pools


def summoning_boosts():
    select_summon = var_summoning_boosts_cook.get()

    if select_summon == "Octopus + Devil":
        item_octopus_devil = items_cook(0, 1, 0.85)
        return item_octopus_devil

    if select_summon == "Mole + Pig":
        item_mole_pig = items_cook(0, 1, 1)
        return item_mole_pig

    if select_summon == "Pig + Salamander":
        item_pig_salamander = items_cook(0.1, 1, 1)
        return item_pig_salamander

    if select_summon == "None":
        item_none = items_cook(0, 1, 1)
        return item_none


# TODO configurar o tamanho dos frames e o tamanho dos OptionMenu
# frame skill boots
skill_boosts_cook_text = Label(fr_skill_boosts_cooking, text="Skill Boosts")
skill_boosts_cook_text.grid(columnspan=2, row=0)

cape_skills_text = Label(fr_skill_boosts_cooking, text="Select Cape")
cape_skills_text.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
var_cape_skills = StringVar()
var_cape_skills.set(cape_skill_cook_list[3])
cape_skills_resp = OptionMenu(
    fr_skill_boosts_cooking, var_cape_skills, *cape_skill_cook_list
)
cape_skills_resp.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

chef_hat_text = Label(fr_skill_boosts_cooking, text="Chef's Hat")
chef_hat_text.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
var_chef_hat = IntVar()
chef_hat_resp = Checkbutton(
    fr_skill_boosts_cooking,
    variable=var_chef_hat,
    onvalue=1,
    offvalue=0,
    command=chef_hat,
)
chef_hat_resp.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

cooking_apron_text = Label(fr_skill_boosts_cooking, text="Cooking Apron")
cooking_apron_text.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
var_cooking_apron = IntVar()
cooking_apron_resp = Checkbutton(
    fr_skill_boosts_cooking,
    variable=var_cooking_apron,
    onvalue=1,
    offvalue=0,
    command=cooking_apron,
)
cooking_apron_resp.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

ancient_ring_of_skills_text = Label(
    fr_skill_boosts_cooking, text="Ancient Ring of Skills"
)
ancient_ring_of_skills_text.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
var_ancient_ring_of_skills = IntVar()
ancient_ring_of_skills_resp = Checkbutton(
    fr_skill_boosts_cooking,
    variable=var_ancient_ring_of_skills,
    onvalue=1,
    offvalue=0,
    command=ancient_ring_of_skills,
)
ancient_ring_of_skills_resp.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

chef_spoon_text = Label(fr_skill_boosts_cooking, text="Chef's Spoon")
chef_spoon_text.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
var_chef_spoon = IntVar()
chef_spoon_resp = Checkbutton(
    fr_skill_boosts_cooking,
    variable=var_chef_spoon,
    onvalue=1,
    offvalue=0,
    command=chef_spoon,
)
chef_spoon_resp.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

burning_coals_text = Label(fr_skill_boosts_cooking, text="Burning Coals")
burning_coals_text.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
var_burning_coals = IntVar()
burning_coals_resp = Checkbutton(
    fr_skill_boosts_cooking,
    variable=var_burning_coals,
    onvalue=1,
    offvalue=0,
    command=burning_coals,
)
burning_coals_resp.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)

sweltering_pools_text = Label(fr_skill_boosts_cooking, text="Sweltering Pools")
sweltering_pools_text.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
var_sweltering_pools = IntVar()
sweltering_pools_resp = Checkbutton(
    fr_skill_boosts_cooking,
    variable=var_sweltering_pools,
    onvalue=1,
    offvalue=0,
    command=sweltering_pools,
)
sweltering_pools_resp.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)

art_of_control_cook_text = Label(fr_skill_boosts_cooking, text="Art of Control")
art_of_control_cook_text.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)
var_art_of_control_cook = IntVar()
art_of_control_cook_resp = Checkbutton(
    fr_skill_boosts_cooking,
    variable=var_art_of_control_cook,
    onvalue=1,
    offvalue=0,
    command=art_of_control_cook,
)
art_of_control_cook_resp.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)

cooking_gloves_text = Label(fr_skill_boosts_cooking, text="Cooking Gloves")
cooking_gloves_text.grid(column=0, row=9, sticky=tk.W, padx=5, pady=5)
var_cooking_gloves = IntVar()
cooking_gloves_resp = Checkbutton(
    fr_skill_boosts_cooking,
    variable=var_cooking_gloves,
    onvalue=1,
    offvalue=0,
    command=cooking_gloves,
)
cooking_gloves_resp.grid(column=1, row=9, sticky=tk.E, padx=5, pady=5)

summoning_boosts_title_text = Label(fr_skill_boosts_cooking, text="Summoning Boosts")
summoning_boosts_title_text.grid(columnspan=2, row=10)

summoning_boosts_cook_text = Label(fr_skill_boosts_cooking, text="Summonings")
summoning_boosts_cook_text.grid(column=0, row=11, sticky=tk.W, padx=5, pady=5)
var_summoning_boosts_cook = StringVar()
var_summoning_boosts_cook.set(summoning_boosts_list[3])
summoning_boosts_cook_resp = OptionMenu(
    fr_skill_boosts_cooking, var_summoning_boosts_cook, *summoning_boosts_list
)
summoning_boosts_cook_resp.grid(column=1, row=11, sticky=tk.E, padx=5, pady=5)

# frame cooking fire
cooking_fire_text = Label(fr_cooking_fire, text="Cooking Fire")
cooking_fire_text.grid(row=0, columnspan=2)

your_fire_cook_text = Label(fr_cooking_fire, text="Your Fire")
your_fire_cook_text.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
var_your_fire = StringVar()
var_your_fire.set(log_list[0])
your_fire_cook_resp = OptionMenu(fr_cooking_fire, var_your_fire, *log_list)
your_fire_cook_resp.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

recipe_cook_text = Label(fr_cooking_fire, text="Recipe")
recipe_cook_text.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
var_fish_cook = StringVar()
var_fish_cook.set(recipe_cooking_fire_list[0])
recipe_cook_resp = OptionMenu(fr_cooking_fire, var_fish_cook, *recipe_cooking_fire_list)
recipe_cook_resp.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

mastery_lvl_cook_text = Label(fr_cooking_fire, text="Mastery Level")
mastery_lvl_cook_text.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
var_mastery_lvl_cook = IntVar()
var_mastery_lvl_cook.set(lvl_list[0])
mastery_lvl_cook_resp = OptionMenu(fr_cooking_fire, var_mastery_lvl_cook, *lvl_list)
mastery_lvl_cook_resp.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

cook_rate_cook_text = Label(fr_cooking_fire, text="Cook Rate")
cook_rate_cook_text.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
cook_rate_cook_resp = Label(fr_cooking_fire, text="70")
cook_rate_cook_resp.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

# gloves_profit_cook_text = Label(fr_cooking_fire, text='Gloves Profit/Loss')
# gloves_profit_cook_text.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
# gloves_profit_cook_resp = Label(fr_cooking_fire, text='0')
# gloves_profit_cook_resp.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)


xp_skill_hr_cook_text = Label(fr_cooking_fire, text="Skill XP/Hr")
xp_skill_hr_cook_text.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
xp_skill_hr_cook_resp = Label(fr_cooking_fire, text="0")
xp_skill_hr_cook_resp.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)

# frame furnance

furnance_text = Label(fr_furnance, text="Furnance")
furnance_text.grid(row=0, columnspan=2)

your_fire_furnance_text = Label(fr_furnance, text="Your Fire")
your_fire_furnance_text.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
var_your_fire_furnance = StringVar()
var_your_fire_furnance.set(log_list[0])
your_fire_furnance_resp = OptionMenu(fr_furnance, var_your_fire_furnance, *log_list)
your_fire_furnance_resp.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

recipe_furnance_text = Label(fr_furnance, text="Recipe")
recipe_furnance_text.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
var_recipe_furnance = StringVar()
var_recipe_furnance.set(recipe_cooking_furnance_list[0])
recipe_furnance_resp = OptionMenu(
    fr_furnance, var_recipe_furnance, *recipe_cooking_furnance_list
)
recipe_furnance_resp.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

mastery_lvl_furnance_text = Label(fr_furnance, text="Mastery Level")
mastery_lvl_furnance_text.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
var_mastery_lvl_furnance = IntVar()
var_mastery_lvl_furnance.set(lvl_list[0])
mastery_lvl_furnance_resp = OptionMenu(fr_furnance, var_mastery_lvl_furnance, *lvl_list)
mastery_lvl_furnance_resp.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

cook_rate_furnance_text = Label(fr_furnance, text="Cook Rate")
cook_rate_furnance_text.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
cook_rate_furnance_resp = Label(fr_furnance, text="70")
cook_rate_furnance_resp.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

xp_skill_hr_furnance_text = Label(fr_furnance, text="Skill XP/Hr")
xp_skill_hr_furnance_text.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
xp_skill_hr_furnance_resp = Label(fr_furnance, text="0")
xp_skill_hr_furnance_resp.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)


# frame pot

pot_text = Label(fr_pot, text="Pot")
pot_text.grid(row=0, columnspan=2)

your_fire_pot_text = Label(fr_pot, text="Your Fire")
your_fire_pot_text.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
var_your_fire_pot = StringVar()
var_your_fire_pot.set(log_list[0])
your_fire_pot_resp = OptionMenu(fr_pot, var_your_fire_pot, *log_list)
your_fire_pot_resp.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

recipe_pot_text = Label(fr_pot, text="Recipe")
recipe_pot_text.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
var_recipe_pot = StringVar()
var_recipe_pot.set(recipe_cooking_pot_list[0])
recipe_pot_resp = OptionMenu(fr_pot, var_recipe_pot, *recipe_cooking_pot_list)
recipe_pot_resp.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

mastery_lvl_pot_text = Label(fr_pot, text="Mastery Level")
mastery_lvl_pot_text.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
var_mastery_lvl_pot = IntVar()
var_mastery_lvl_pot.set(lvl_list[0])
mastery_lvl_pot_resp = OptionMenu(fr_pot, var_mastery_lvl_pot, *lvl_list)
mastery_lvl_pot_resp.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

cook_rate_pot_text = Label(fr_pot, text="Cook Rate")
cook_rate_pot_text.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
cook_rate_pot_resp = Label(fr_pot, text="70")
cook_rate_pot_resp.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

xp_skill_hr_pot_text = Label(fr_pot, text="Skill XP/Hr")
xp_skill_hr_pot_text.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
xp_skill_hr_pot_resp = Label(fr_pot, text="0")
xp_skill_hr_pot_resp.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

# frame xp calculate

xp_calc_text = Label(fr_xp_calc_cooking, text="XP Calculate")
xp_calc_text.grid(row=0, columnspan=2)

current_xp_cook_text = Label(fr_xp_calc_cooking, text="Current XP")
current_xp_cook_text.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
current_xp_cook_resp = Entry(fr_xp_calc_cooking, width=10)
current_xp_cook_resp.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

desired_lvl_cook_text = Label(fr_xp_calc_cooking, text="Desired Level")
desired_lvl_cook_text.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
var_desired_lvl_cook = StringVar()
var_desired_lvl_cook.set(lvl_list[0])
desired_lvl_cook_resp = OptionMenu(fr_xp_calc_cooking, var_desired_lvl_cook, *lvl_list)
desired_lvl_cook_resp.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

your_fire_recipe_text = Label(fr_xp_calc_cooking, text="Your Fire")
your_fire_recipe_text.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
var_your_fire_recipe = StringVar()
var_your_fire_recipe.set(log_list[0])
your_fire_recipe_resp = OptionMenu(fr_xp_calc_cooking, var_your_fire_recipe, *log_list)
your_fire_recipe_resp.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

recipe_cook_text = Label(fr_xp_calc_cooking, text="Recipe")
recipe_cook_text.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
var_recipe_cook = StringVar()
var_recipe_cook.set(recipe_cook_list[0])
recipe_cook_resp = OptionMenu(fr_xp_calc_cooking, var_recipe_cook, *recipe_cook_list)
recipe_cook_resp.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

recipe_needed_cook_text = Label(fr_xp_calc_cooking, text="Recipe Needed")
recipe_needed_cook_text.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
recipe_needed_cook_resp = Label(fr_xp_calc_cooking, text="0")
recipe_needed_cook_resp.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

# functions cooking
def recipe_cook_xp(VarRecipe, fire):
    type_recipe = VarRecipe
    fire_cooking = fire.get()

    xp_df = pd.read_excel("cooking.xlsx")
    bonus_xp = int(xp_df.loc[xp_df["Logs"] == fire_cooking, "Bonus Xp"])
    xp_bonus = (int(xp_df.loc[xp_df["Recipe Cooking Fire"] == type_recipe, "Xp"])) * (
        1 + (bonus_xp * 0.01)
    )
    return xp_bonus


def cook_rate_cook(resp, VarLevel):
    cape_selected = var_cape_skills.get()
    summon_selected = var_summoning_boosts_cook.get()
    cooking_gloves_select = cooking_gloves()

    if summon_selected == "Mole + Pig":
        resp["text"] = 75
        return 75
    else:
        if cape_selected != "None":
            resp["text"] = 100
            return 100
        else:
            level = VarLevel.get()
            cook_rate = (int(level) * 0.6) + 70 + cooking_gloves_select
        if cook_rate > 100:
            resp["text"] = 100
            return 100
        else:
            resp["text"] = round(cook_rate)
            return cook_rate


def cook_time(VarRecipe):
    type_recipe = VarRecipe.get()
    cape_selected = var_cape_skills.get()

    cooking_df = pd.read_excel("cooking.xlsx")
    value = int(
        cooking_df.loc[cooking_df["Recipe Cooking Fire"] == type_recipe, "Cook Time"]
    )

    if cape_selected != "None":
        cook_time = (
            (value * 0.85 * art_of_control_cook() * sweltering_pools().ckint_item())
            - chef_hat().ckint_item()
            - summoning_boosts().ckint_item()
        )
        return cook_time
    else:
        cook_time = (
            (value * art_of_control_cook() * sweltering_pools().ckint_item())
            - chef_hat().ckint_item()
            - summoning_boosts().ckint_item()
        )
        return cook_time


# def gloves_profit_cook(rate, VarRecipe):
#     type_recipe = VarRecipe.get()
#     cook_rate = rate

#     cooking_df = pd.read_excel('cooking.xlsx')
#     value = int(cooking_df.loc[cooking_df['Recipe Cooking Fire'] == type_recipe, 'Value'])
#     gloves_profit = ((500*value)-((500*(1-(cook_rate*0.01)))*value))-50000
#     gloves_profit_cook_resp['text'] = round(gloves_profit)


def xp_skill_hr_cook(VarRecipe, fire, resp, VarLevel):
    xp_recipe_cook = recipe_cook_xp(VarRecipe.get(), fire)
    cook_rate_xp = cook_rate_cook(resp, VarLevel)
    cook_time_xp = cook_time(VarRecipe)

    xp_skill_hr = ((3600 / cook_time_xp) * (cook_rate_xp * 0.01)) * xp_recipe_cook
    xp_teste = (
        xp_skill_hr
        * chef_hat().xps_item()
        * cooking_apron().xps_item()
        * ancient_ring_of_skills().xps_item()
        * chef_spoon().xps_item()
        * burning_coals().xps_item()
        * summoning_boosts().xps_item()
    )
    print(xp_teste, cook_time_xp, cook_rate_xp, xp_recipe_cook)
    return round(xp_teste)


def recipe_needed_cook(CurrentXp, VarLevel, VarRecipe, fire):
    total_xp_recipe = total_xp(CurrentXp, VarLevel)
    xp_needed_cook = recipe_cook_xp(VarRecipe, fire)

    fish_needed = total_xp_recipe / xp_needed_cook
    return round(fish_needed)


# cooking buttons
def button_cooking_fire():
    # gloves_profit_cook(cook_rate_cook(cook_rate_cook_resp, var_mastery_lvl_cook), var_fish_cook)
    xp_skill_hr_cook_resp["text"] = xp_skill_hr_cook(
        var_fish_cook, var_your_fire, cook_rate_cook_resp, var_mastery_lvl_cook
    )


calculate_cooking = Button(
    fr_cooking_fire, text="Calcular", command=button_cooking_fire
)
calculate_cooking.grid(columnspan=2, row=7)


def button_furnance():
    xp_skill_hr_furnance_resp["text"] = xp_skill_hr_cook(
        var_recipe_furnance,
        var_your_fire_furnance,
        cook_rate_furnance_resp,
        var_mastery_lvl_furnance,
    )


calculate_cooking = Button(fr_furnance, text="Calcular", command=button_furnance)
calculate_cooking.grid(columnspan=2, row=6)


def button_pot():
    xp_skill_hr_pot_resp["text"] = xp_skill_hr_cook(
        var_recipe_pot, var_your_fire_pot, cook_rate_pot_resp, var_mastery_lvl_pot
    )


calculate_cooking = Button(fr_pot, text="Calcular", command=button_pot)
calculate_cooking.grid(columnspan=2, row=6)


def button_recipe():
    recipe_needed_cook_resp["text"] = recipe_needed_cook(
        current_xp_cook_resp.get(),
        var_desired_lvl_cook.get(),
        var_recipe_cook.get(),
        var_your_fire_recipe,
    )


calculate_cooking = Button(fr_xp_calc_cooking, text="Calcular", command=button_recipe)
calculate_cooking.grid(columnspan=2, row=6)

# Mining

tab5 = Frame(tabControl)
tabControl.add(tab5, text="Mining")

# frames
fr_skill_boosts_mining = tk.Frame(master=tab5, borderwidth=1, relief="solid")
fr_skill_boosts_mining.place(x=0, y=0)
fr_mining = tk.Frame(master=tab5, borderwidth=1, relief="solid")
fr_mining.place(x=326, y=0)

# lists mining

potion_mining_list = [
    "None",
    "Perfect Swing Potion I",
    "Perfect Swing Potion II",
    "Perfect Swing Potion III",
    "Perfect Swing Potion IV",
]
summoning_boosts_mining_list = [
    "None",
    "Mone",
    "Mone + Crow",
    "Mone + Monkey",
    "Mone + Bear",
]
ore_list = [
    "Copper Ore",
    "Tin Ore",
    "Rune Essence",
    "Iron Ore",
    "Silver Ore",
    "Coal Ore",
    "Gold Ore",
    "Mithril Ore",
    "Adamantite Ore",
    "Runite Ore",
    "Dragonite Ore",
]
mastery_pool_mining_list = ["None", "25%", "50%", "95%"]
# classes
class pool_mining:
    def __init__(self, respawn, MiningInterval, RockHp):
        self.respawn = respawn
        self.MiningInterval = MiningInterval
        self.RockHp = RockHp

    def respawn_pool(self):
        return self.respawn

    def mining_pool(self):
        return self.MiningInterval

    def rock_pool(self):
        return self.RockHp


class summoning:
    def __init__(self, chance, double, maxhp):
        self.chance = chance
        self.double = double
        self.maxhp = maxhp

    def chance_summoning(self):
        return self.chance

    def double_summoning(self):
        return self.double

    def maxhp_summoning(self):
        return self.maxhp


# checkbutton function


def potion_mining():
    potion_select = var_potion_mining.get()
    if potion_select == "Perfect Swing Potion I":
        return 0.1
    if potion_select == "Perfect Swing Potion II":
        return 0.2
    if potion_select == "Perfect Swing Potion III":
        return 0.4
    if potion_select == "Perfect Swing Potion IV":
        return 0.8
    if potion_select == "None":
        return 0


def summoning_mining():
    summoning_select = var_summoning_boosts_mining.get()
    potion_select = var_potion_mining.get()
    ore_select = var_ore_mining.get()

    if summoning_select == "Mone":
        class_summoning = summoning(1.03, 1, 0)
        return class_summoning
    if summoning_select == "None":
        class_summoning = summoning(1, 1, 0)
        return class_summoning
    if summoning_select == "Mone + Monkey" and ore_select == (
        "Silver Ore" or "Gold Ore"
    ):
        class_summoning = summoning(1, 2, 0)
        return class_summoning
    elif summoning_select == "Mone + Bear" and potion_select != "None":
        class_summoning = summoning(1, 1, 20)
        return class_summoning
    elif summoning_select == "Mone + Crow" and ore_select == "Rune Essence":
        class_summoning = summoning(1, 2, 0)
        return class_summoning
    else:
        class_summoning = summoning(1, 1, 0)
        return class_summoning


def mastery_pool_mining():
    mastery_select = var_mastery_pool_mining.get()
    if mastery_select == "25%":
        class_mastery_25 = pool_mining(0.9, 0, 0)
        return class_mastery_25
    if mastery_select == "50%":
        class_mastery_50 = pool_mining(1, 0.2, 0)
        return class_mastery_50
    if mastery_select == "95%":
        class_mastery_95 = pool_mining(1, 0, 10)
        return class_mastery_95
    if mastery_select == "None":
        none_mastery = pool_mining(1, 0, 0)
        return none_mastery


def miner_helmet():
    miner_helmet = var_miner_helmet.get()
    if miner_helmet == 1:
        return 0.03
    else:
        return 0


def ancient_ring_mining():
    pass


def pipe_balance_mining():
    pipe_balance = var_pipe_balance_mining.get()

    if pipe_balance == 1:
        return 10
    else:
        return 0


def rock_climb_mining():
    rock_climb = var_rock_climb_mining.get()
    if rock_climb == 1:
        return 1.05
    else:
        return 1


def ice_jump_mining():
    ice_jump = var_ice_jump_mining.get()

    if ice_jump == 1:
        return 10
    else:
        return 0


def cool_rock_mining():
    cool_rock = var_cool_rock_mining.get()

    if cool_rock == 1:
        return 5
    else:
        return 0


def master_of_nature_mining():
    master_of_nature = var_master_of_nature_mining.get()
    if master_of_nature == 1:
        return 0.15
    else:
        return 0


def mining_gloves():
    mining_gloves = var_mining_gloves.get()
    if mining_gloves == 1:
        return 2
    else:
        return 1


# frame skill boots

skill_boosts_mining_text = Label(fr_skill_boosts_mining, text="Skill Boosts")
skill_boosts_mining_text.grid(columnspan=2, row=0)

potion_mining_text = Label(fr_skill_boosts_mining, text="Potions")
potion_mining_text.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
var_potion_mining = StringVar()
var_potion_mining.set(potion_mining_list[0])
potion_mining_resp = OptionMenu(
    fr_skill_boosts_mining, var_potion_mining, *potion_mining_list
)
potion_mining_resp.config(width=15)
potion_mining_resp.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

summoning_boosts_mining_text = Label(fr_skill_boosts_mining, text="Summonings")
summoning_boosts_mining_text.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
var_summoning_boosts_mining = StringVar()
var_summoning_boosts_mining.set(summoning_boosts_mining_list[0])
summoning_boosts_mining_resp = OptionMenu(
    fr_skill_boosts_mining, var_summoning_boosts_mining, *summoning_boosts_mining_list
)
summoning_boosts_mining_resp.config(width=15)
summoning_boosts_mining_resp.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

mastery_pool_mining_text = Label(fr_skill_boosts_mining, text="Mastery Pool")
mastery_pool_mining_text.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
var_mastery_pool_mining = StringVar()
var_mastery_pool_mining.set(mastery_pool_mining_list[0])
mastery_pool_mining_resp = OptionMenu(
    fr_skill_boosts_mining, var_mastery_pool_mining, *mastery_pool_mining_list
)
mastery_pool_mining_resp.config(width=15)
mastery_pool_mining_resp.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

miner_helmet_text = Label(fr_skill_boosts_mining, text="Miner's Helmet")
miner_helmet_text.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
var_miner_helmet = IntVar()
miner_helmet_resp = Checkbutton(
    fr_skill_boosts_mining,
    variable=var_miner_helmet,
    onvalue=1,
    offvalue=0,
    command=miner_helmet,
)
miner_helmet_resp.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

ancient_ring_mining_text = Label(fr_skill_boosts_mining, text="Ancient Ring of Skills")
ancient_ring_mining_text.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
var_ancient_ring_mining = IntVar()
ancient_ring_mining_resp = Checkbutton(
    fr_skill_boosts_mining,
    variable=var_ancient_ring_mining,
    onvalue=1,
    offvalue=0,
    command=ancient_ring_mining,
)
ancient_ring_mining_resp.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

pipe_balance_mining_text = Label(fr_skill_boosts_mining, text="Pipe Balance")
pipe_balance_mining_text.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
var_pipe_balance_mining = IntVar()
pipe_balance_mining_resp = Checkbutton(
    fr_skill_boosts_mining,
    variable=var_pipe_balance_mining,
    onvalue=1,
    offvalue=0,
    command=pipe_balance_mining,
)
pipe_balance_mining_resp.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)

rock_climb_mining_text = Label(fr_skill_boosts_mining, text="Rock Climb")
rock_climb_mining_text.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
var_rock_climb_mining = IntVar()
rock_climb_mining_resp = Checkbutton(
    fr_skill_boosts_mining,
    variable=var_rock_climb_mining,
    onvalue=1,
    offvalue=0,
    command=rock_climb_mining,
)
rock_climb_mining_resp.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)

ice_jump_mining_text = Label(fr_skill_boosts_mining, text="Ice Jump")
ice_jump_mining_text.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)
var_ice_jump_mining = IntVar()
ice_jump_mining_resp = Checkbutton(
    fr_skill_boosts_mining,
    variable=var_ice_jump_mining,
    onvalue=1,
    offvalue=0,
    command=ice_jump_mining,
)
ice_jump_mining_resp.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)

cool_rock_mining_text = Label(fr_skill_boosts_mining, text="Cool Rock")
cool_rock_mining_text.grid(column=0, row=9, sticky=tk.W, padx=5, pady=5)
var_cool_rock_mining = IntVar()
cool_rock_mining_resp = Checkbutton(
    fr_skill_boosts_mining,
    variable=var_cool_rock_mining,
    onvalue=1,
    offvalue=0,
    command=cool_rock_mining,
)
cool_rock_mining_resp.grid(column=1, row=9, sticky=tk.E, padx=5, pady=5)

master_of_nature_mining_text = Label(fr_skill_boosts_mining, text="Master of Nature")
master_of_nature_mining_text.grid(column=0, row=10, sticky=tk.W, padx=5, pady=5)
var_master_of_nature_mining = IntVar()
master_of_nature_mining_resp = Checkbutton(
    fr_skill_boosts_mining,
    variable=var_master_of_nature_mining,
    onvalue=1,
    offvalue=0,
    command=master_of_nature_mining,
)
master_of_nature_mining_resp.grid(column=1, row=10, sticky=tk.E, padx=5, pady=5)

mining_gloves_text = Label(fr_skill_boosts_mining, text="Mining Gloves")
mining_gloves_text.grid(column=0, row=11, sticky=tk.W, padx=5, pady=5)
var_mining_gloves = IntVar()
mining_gloves_resp = Checkbutton(
    fr_skill_boosts_mining,
    variable=var_mining_gloves,
    onvalue=1,
    offvalue=0,
    command=mining_gloves,
)
mining_gloves_resp.grid(column=1, row=11, sticky=tk.E, padx=5, pady=5)

# frame mining

mining_text = Label(fr_mining, text="Mining")
mining_text.grid(columnspan=2, row=0)

pickaxe_mining_text = Label(fr_mining, text="Pickace")
pickaxe_mining_text.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
var_pickaxe_mining = StringVar()
var_pickaxe_mining.set(material_list[0])
pickaxe_mining_resp = OptionMenu(fr_mining, var_pickaxe_mining, *material_list)
pickaxe_mining_resp.config(width=10)
pickaxe_mining_resp.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

ore_mining_text = Label(fr_mining, text="Ores")
ore_mining_text.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
var_ore_mining = StringVar()
var_ore_mining.set(ore_list[0])
ore_mining_resp = OptionMenu(fr_mining, var_ore_mining, *ore_list)
ore_mining_resp.config(width=10)
ore_mining_resp.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

mastery_lvl_mining_text = Label(fr_mining, text="Mastery Level")
mastery_lvl_mining_text.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
var_mastery_lvl_mining = IntVar()
var_mastery_lvl_mining.set(lvl_list[0])
mastery_lvl_mining_resp = OptionMenu(fr_mining, var_mastery_lvl_mining, *lvl_list)
mastery_lvl_mining_resp.config(width=10)
mastery_lvl_mining_resp.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

rock_hp_mining_text = Label(fr_mining, text="Rock HP")
rock_hp_mining_text.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
rock_hp_mining_resp = Label(fr_mining, text="6")
rock_hp_mining_resp.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

rock_max_hp_mining_text = Label(fr_mining, text="Rock Max HP")
rock_max_hp_mining_text.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
rock_max_hp_mining_resp = Label(fr_mining, text="0")
rock_max_hp_mining_resp.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

ores_hr_mining_text = Label(fr_mining, text="Ores/Hr")
ores_hr_mining_text.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
ores_hr_mining_resp = Label(fr_mining, text="0")
ores_hr_mining_resp.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)

xp_hr_mining_text = Label(fr_mining, text="XP/Hr")
xp_hr_mining_text.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
xp_hr_mining_resp = Label(fr_mining, text="0")
xp_hr_mining_resp.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)

gp_hr_mining_text = Label(fr_mining, text="GP/Hr")
gp_hr_mining_text.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)
gp_hr_mining_resp = Label(fr_mining, text="0")
gp_hr_mining_resp.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)

# functions mining
def rock_hp():
    rock_hp_mining = (
        5
        + var_mastery_lvl_mining.get()
        + summoning_mining().maxhp_summoning()
        + mastery_pool_mining().rock_pool()
        + pipe_balance_mining()
        + ice_jump_mining()
        + cool_rock_mining()
    )
    return rock_hp_mining


def rock_max_hp():
    rock_max_hp_mining = rock_hp() / (1 - (potion_mining() + miner_helmet()))
    return rock_max_hp_mining


def time_cicle():
    ore_select = var_ore_mining.get()
    pickaxe_select = var_pickaxe_mining.get()
    time_cicle = (
        rock_hp()
        * (3 * (items.pickaxe[pickaxe_select]["mine time"] - master_of_nature_mining()))
    ) + items.ores[ore_select]["respawn"]
    return time_cicle


def xp_hr_mining():
    ore_select = var_ore_mining.get()
    xp_hr = ((items.ores[ore_select]["xp"] * rock_hp()) / time_cicle()) * 3600
    return xp_hr


def ore_hr_mining():
    pickaxe_select = var_pickaxe_mining.get()
    ore_hr = (
        ((rock_hp() / time_cicle()) * 3600)
        * items.pickaxe[pickaxe_select]["chance"]
        * mining_gloves()
        * summoning_mining().chance_summoning()
        * rock_climb_mining()
    )
    return ore_hr


# mining buttons


def button_mining():
    rock_hp_mining_resp["text"] = rock_hp()
    rock_max_hp_mining_resp["text"] = round(rock_max_hp())
    xp_hr_mining_resp["text"] = round(xp_hr_mining())
    ores_hr_mining_resp["text"] = round(ore_hr_mining())


calculate_mining = Button(fr_mining, text="Calcular", command=button_mining)
calculate_mining.grid(columnspan=2, row=9)

# Xp Calculate
tab6 = Frame(tabControl)
tabControl.add(tab6, text="XP Calculate")

fr_xp_calculate_esq = Frame(tab6, borderwidth=1, relief="solid")
fr_xp_calculate_esq.place(x=0, y=0)

current_xp = Label(fr_xp_calculate_esq, text="Current Xp")
current_xp.grid(column=0, row=0)
desired_xp = Label(fr_xp_calculate_esq, text="Desired Level")
desired_xp.grid(column=0, row=1)
xptill_xp = Label(fr_xp_calculate_esq, text="XP Till level")
xptill_xp.grid(column=0, row=2)
xpaction_xp = Label(fr_xp_calculate_esq, text="XP/Action")
xpaction_xp.grid(column=0, row=3)
items_xp = Label(fr_xp_calculate_esq, text="Items Needed/Action")
items_xp.grid(column=0, row=4)
itemneeded_xp = Label(fr_xp_calculate_esq, text="Items Needed")
itemneeded_xp.grid(column=0, row=5)

current_xp_resp = Entry(fr_xp_calculate_esq, width=10)
current_xp_resp.grid(column=1, row=0)
var_lvl_list_xp = StringVar()
desired_xp_resp = OptionMenu(fr_xp_calculate_esq, var_lvl_list_xp, *lvl_list)
desired_xp_resp.grid(column=1, row=1)
xptill_xp_resp = Entry(fr_xp_calculate_esq, width=10)
xptill_xp_resp.grid(column=1, row=2)
xpaction_xp_resp = Label(fr_xp_calculate_esq, text="Resp")
xpaction_xp_resp.grid(column=1, row=3)
items_xp_resp = Entry(fr_xp_calculate_esq, width=10)
items_xp_resp.grid(column=1, row=4)
itemneeded_xp_resp = Label(fr_xp_calculate_esq, text="Resp")
itemneeded_xp_resp.grid(column=1, row=5)


def get_desired_level():
    des_lvl1 = var_lvl_list_xp.get()
    xp_df = pd.read_excel("xp.xlsx")
    print(xp_df.loc[int(des_lvl1), "exp"])


Button(fr_xp_calculate_esq, text="Calcular", command=get_desired_level).grid(
    column=0, row=6
)

root.mainloop()
