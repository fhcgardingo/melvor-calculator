# importando tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tokenize import String
import pandas as pd
import datetime as date
from pyparsing import col
import math


root =Tk()
root.title("Tab Widget")
root.geometry('600x600')

tabControl = ttk.Notebook(root)
tabControl.place(x=0, y=0, width=600, height=600)

# cores
cor1 = '#3b3b3b'

#global functions

def total_xp(current, desired):
    current_xp = current
    desired_level_get = desired

    if current:
        desired_lvl_df = pd.read_excel('xp.xlsx')
        desired_lvl = int(desired_lvl_df.loc[desired_lvl_df['level'] == int(desired_level_get), 'exp'])
        total_xp = desired_lvl - int(current_xp)
        return total_xp
    else:
        return 0

# woodcutting
tab1 = Frame(tabControl)
tabControl.add(tab1, text='Woodcutting')

fr_wood_esq = Frame(tab1, borderwidth=1, relief='solid')
fr_wood_esq.place(x=0, y=0)
fr_wood_dir = Frame(tab1, borderwidth=1, relief='solid')
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
    return(skillcape_wood)

def master_wood():
    master_wood = var_master_wood.get()
    return(master_wood)

wood_list = ["Normal", "Oak", "Willow", "Teak",
             "Maple", "Mahogany", "Yew", "Magic", "Redwood", "None"]
var_wood_list1 = StringVar()
var_wood_list1.set(wood_list[0])
var_wood_list2 = StringVar()
var_wood_list2.set(wood_list[9])
tree1_wood_resp = OptionMenu(fr_wood_esq, var_wood_list1, *wood_list)
tree1_wood_resp.grid(column=1, row=0)
tree2_wood_resp = OptionMenu(fr_wood_esq, var_wood_list2, *wood_list)
tree2_wood_resp.grid(column=1, row=1)
var_skillcape_wood = IntVar()
skillcape_wood_resp = Checkbutton(fr_wood_esq,variable=var_skillcape_wood, onvalue=1, offvalue=0, command=skillcape_wood)
skillcape_wood_resp.pack()
skillcape_wood_resp.grid(column=1, row=2)
var_master_wood = IntVar()
master_wood_resp = Checkbutton(fr_wood_esq,variable=var_master_wood, onvalue=1, offvalue=0, command=master_wood)
master_wood_resp.pack()
master_wood_resp.grid(column=1, row=3)
axe_list = ["Base", "Iron", "Steel", "Black",
            "Mithril", "Adamant", "Rune", "Dragon"]
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
xp_hr_tree_text = Label(fr_wood_dir, text='Xp/Hr per Tree')
xp_hr_tree_text.grid(column=0, row=0)
logs_hour_text = Label(fr_wood_dir, text='Logs/Hour')
logs_hour_text.grid(column=1, row=0)
total_xp_hr_text = Label(fr_wood_dir, text='Total Xp/Hr')
total_xp_hr_text.grid(column=0, row=4)
current_xp_wood_text = Label(fr_wood_dir, text='Current Xp')
current_xp_wood_text.grid(column=0, row=5)
desired_lvl_wood_text = Label(fr_wood_dir, text='Desired Level')
desired_lvl_wood_text.grid(column=0, row=6)
hours_till_lvl_wood_text = Label(fr_wood_dir, text='Hours Till Lvl')
hours_till_lvl_wood_text.grid(column=0, row=7)
total_logs1_wood_text = Label(fr_wood_dir, text='Total Logs 1')
total_logs1_wood_text.grid(column=0, row=8)
total_logs2_wood_text =  Label(fr_wood_dir, text='Total Logs2')
total_logs2_wood_text.grid(column=0, row=9)


xp_hr_tree1_resp = Label(fr_wood_dir, text='0')
xp_hr_tree1_resp.grid(column=0, row=2)
xp_hr_tree2_resp = Label(fr_wood_dir, text='0')
xp_hr_tree2_resp.grid(column=0, row=3)
logs_hour1_resp = Label(fr_wood_dir, text='0')
logs_hour1_resp.grid(column=1, row=2)
logs_hour2_resp = Label(fr_wood_dir, text='0')
logs_hour2_resp.grid(column=1, row=3)
total_xp_hr_resp = Label(fr_wood_dir, text='0')
total_xp_hr_resp.grid(column=1, row=4)
current_xp_wood_resp = Entry(fr_wood_dir, width=10)
current_xp_wood_resp.grid(column=1, row=5)
var_desired_wood = StringVar()
desired_lvl_wood_resp = OptionMenu(fr_wood_dir, var_desired_wood, *lvl_list)
desired_lvl_wood_resp.grid(column=1, row=6)
hours_till_lvl_wood_resp = Label(fr_wood_dir, text='00:00:00')
hours_till_lvl_wood_resp.grid(column=1, row=7)
total_logs1_wood_resp = Label(fr_wood_dir, text='0')
total_logs1_wood_resp.grid(column=1, row=8)
total_logs2_wood_resp = Label(fr_wood_dir, text='0')
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

    get_wood_df = pd.read_excel('Woodcutting.xlsx')
    cuttime = int(get_wood_df.loc[get_wood_df['Tree'] == type_tree, 'Cut Time'])
    adjcuttime = cuttime * percent_axe * percent_master
    return adjcuttime

def get_exp_tree(typep):
    type_tree = typep
    get_exp_tree_df = pd.read_excel('Woodcutting.xlsx')
    exp = int(get_exp_tree_df.loc[get_exp_tree_df['Tree'] == type_tree, 'Exp'])
    return exp

#TODO tentar usar somente uma func xp_hr_per_tree passando parametros
def xp_hr_per_tree1():
    adjcuttime_tree1 = adj_cut_time(var_wood_list1.get(), var_material_axe_list.get())
    type_tree1 = var_wood_list1.get()
    exp_tree1 = get_exp_tree(type_tree1)

    if (exp_tree1 == 0) or (type_tree1 == 'None'):
        xp_hr_tree1_resp['text'] = 0
        xp_hour = 0
    else:
        xp_hour = exp_tree1 / (round(adjcuttime_tree1, 2)) * 3600
        xp_hr_tree1_resp['text'] = (round(xp_hour))
    return (round(xp_hour))

def xp_hr_per_tree2():
    adjcuttime_tree2 = adj_cut_time(var_wood_list2.get(),var_material_axe_list.get())
    type_tree2 = var_wood_list2.get()
    exp_tree2 = get_exp_tree(type_tree2)

    if (exp_tree2 == 0) or (type_tree2 == 'None'):
        xp_hr_tree2_resp['text'] = 0
        xp_hour = 0
    else:
        xp_hour = exp_tree2 / (round(adjcuttime_tree2, 2)) * 3600
        xp_hr_tree2_resp['text'] = (round(xp_hour))
    return (round(xp_hour))

#TODO tentar usar somente uma func logs_hour passando parametros
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
    if type_tree_log1 != 'None':
        logs_hour_base = 3600 / (round(adjcuttime_log1, 2))
        woodcutting_df = pd.read_excel('Woodcutting.xlsx')
        mastery_multiplier = woodcutting_df.loc[woodcutting_df['Level'] == int(level_log1), 'Multiplier']
        logs_hour = float(mastery_multiplier) * round(logs_hour_base) * percent_skill
        logs_hour1_resp['text'] = (round(logs_hour))
    else:
        logs_hour1_resp['text'] = 0

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
    if type_tree_log2 != 'None':
        logs_hour_base = 3600 / (round(adjcuttime_log2, 2))
        woodcutting_df = pd.read_excel('Woodcutting.xlsx')
        mastery_multiplier = woodcutting_df.loc[woodcutting_df['Level'] == int(level_log2), 'Multiplier']
        logs_hour = float(mastery_multiplier) * round(logs_hour_base) * percent_skill
        logs_hour2_resp['text'] = (round(logs_hour))
    else:
        logs_hour2_resp['text'] = 0

def total_xp_hr_wood():
    xp_tree1 = xp_hr_per_tree1()
    xp_tree2 = xp_hr_per_tree2()

    if (xp_tree1 != 0) and (xp_tree2 != 0):
        total_xp_hr = xp_tree1 + xp_tree2
    elif (xp_tree1 != 0) and (xp_tree2 == 0):
        total_xp_hr = xp_tree1
    elif (xp_tree1 == 0) and (xp_tree2 != 0):
        total_xp_hr = xp_tree2
    else:
        total_xp_hr = 0

    total_xp_hr_resp['text'] = total_xp_hr
    # print(total_xp_hr)
    return total_xp_hr

def hours_till_lvl_wood():
    xp_hour = total_xp(current_xp_wood_resp.get(), var_desired_wood.get())
    total_xp = total_xp_hr_wood()

    if total_xp != 0:
        hours_till = xp_hour / total_xp
        hours_round = round(hours_till,2)
        hora, minuto = str(hours_round).split('.')
        minuto2, segundo = str(round((int(minuto)*0.6),2)).split('.')        # setar segundos para duas casa somente
        hours = '{}:{}:{}'.format(hora,minuto2,segundo)
        hours_till_lvl_wood_resp['text'] = (hours)
    else:
        hours_till_lvl_wood_resp['text'] = 0
    
def total_logs1():
    total_xp_log1 = total_xp(current_xp_wood_resp.get(), var_desired_wood.get())
    total_xp = total_xp_hr_wood()
    type_tree1 = var_wood_list1.get()

    if total_xp != 0:
        hours_till = total_xp_log1 / total_xp
        hours_round = round(hours_till,2)
        
        logs_hour_df = pd.read_excel('Woodcutting.xlsx')
        logs_hour = int(logs_hour_df.loc[logs_hour_df['Tree'] == type_tree1, 'Logs/Hour']) 
        total_logs1 = hours_round * logs_hour
        total_logs1_wood_resp['text'] = round(total_logs1)
    else:
        total_logs1_wood_resp['text'] = 0
    
def total_logs2():
    total_xp_log2 = total_xp(current_xp_wood_resp.get(), var_desired_wood.get())
    total_xp = total_xp_hr_wood()
    type_tree2 = var_wood_list2.get()

    if total_xp != 0:
        hours_till = total_xp_log2 / total_xp
        hours_round = round(hours_till,2)
        
        logs_hour_df = pd.read_excel('Woodcutting.xlsx')
        logs_hour = int(logs_hour_df.loc[logs_hour_df['Tree'] == type_tree2, 'Logs/Hour']) 
        total_logs2 = hours_round * logs_hour
        total_logs2_wood_resp['text'] = round(total_logs2)
    else:
        total_logs2_wood_resp['text'] = 0

def button_calculate():
    xp_hr_per_tree1()
    xp_hr_per_tree2()
    logs_hour1()
    logs_hour2()
    total_xp_hr_wood()
    hours_till_lvl_wood()
    total_logs1()
    total_logs2()

# buttons woodcutting
calculate_wood = Button(fr_wood_esq, text='Calcular',command=button_calculate)
calculate_wood.grid(column=0, row=7)


# Fishing
tab2 = Frame(tabControl)
tabControl.add(tab2, text='Fishing')

# frames
fr_fish_esq = Frame(tab2, borderwidth=1, relief="solid")
fr_fish_esq.place(x=0, y=0)
fr_fish_dir = Frame(tab2, borderwidth=1, relief='solid')
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

#TODO terminar funções
def pet_fish():
    pass

def skill_fish():
    pass

def amulet_fish():
    pass

def pirate_fish():
    pass   

rod_list = ["Base", "Iron", "Steel", "Balck", "Mithril", "Adamant", "Rune", "Dragon"]
var_rod_fish = StringVar()
var_rod_fish.set(rod_list[0])
rod_fish_resp = OptionMenu(fr_fish_esq, var_rod_fish, *rod_list)
rod_fish_resp.grid(column=1, row=0)
fish_list = ["Shrimp", "Sardine", "Blowfish", "Herring", "Seahorse", "Trout", "Leaping Trout", "Poison Fish", "Salmon", "Leaping Salmon","Lobster", "Skeleton Fish", "Swordfish", "Anglerfish", "Fanfish", "Crab", "carp", "Shark", "Leaping Broad Fish", "Cave Fish", "Magic Fish", "Manta Fish", "Whale"]
var_fish_list = StringVar()
var_fish_list.set(fish_list[0])
fish_resp = OptionMenu(fr_fish_esq, var_fish_list, *fish_list)
fish_resp.grid(column=1, row=1)
var_pet_fish = IntVar()
pet_fish_resp = Checkbutton(fr_fish_esq,variable=var_pet_fish, onvalue=1, offvalue=0, command=pet_fish)
pet_fish_resp.pack()
pet_fish_resp.grid(column=1, row=2)
var_skill_fish = IntVar()
skill_fish_resp = Checkbutton(fr_fish_esq,variable=var_skill_fish, onvalue=1, offvalue=0, command=skill_fish)
skill_fish_resp.pack()
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
amulet_fish_resp = Checkbutton(fr_fish_esq,variable=var_amulet_fish, onvalue=1, offvalue=0, command=amulet_fish)
amulet_fish_resp.pack()
amulet_fish_resp.grid(column=1, row=6)
var_pirate_fish = IntVar()
pirate_fish_resp = Checkbutton(fr_fish_esq,variable=var_pirate_fish, onvalue=1, offvalue=0, command=pirate_fish)
pirate_fish_resp.pack()
pirate_fish_resp.grid(column=1, row=7)

# frame 2
fish_hr_text = Label(fr_fish_dir, text="Fish/Hr")
fish_hr_text.grid(column=0, row=0)
xp_hr_text = Label(fr_fish_dir, text="Xp/Hr")
xp_hr_text.grid(column=0, row=1)
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
tabControl.add(tab3, text='Firemaking')

# frames
fr_fire_esq = Frame(tab3, borderwidth=1, relief="solid")
fr_fire_esq.place(x=0, y=0)
fr_fire_dir = Frame(tab3, borderwidth=1, relief='solid')
fr_fire_dir.place(x=266, y=0)

# frame 1

logs_fire_text = Label(fr_fire_esq, text="Logs")
logs_fire_text.grid(column=0, row=0)
art_of_control_fire_text = Label(fr_fire_esq, text="Art of Control")
art_of_control_fire_text.grid(column=0, row=1)
lvl_fire_text = Label(fr_fire_esq, text='Lvl 99')
lvl_fire_text.grid(column=0, row=2)
bonfire_text = Label(fr_fire_esq, text='Bonfire')
bonfire_text.grid(column=0, row=3)
controlled_heat_text = Label(fr_fire_esq, text='Controlled Heat')
controlled_heat_text.grid(column=0, row=4)

#functions checkbuttons
#TODO terminar funções
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
art_of_control_fire_resp = Checkbutton(fr_fire_esq,variable=var_art_of_control, onvalue=1, offvalue=0, command=art_of_control)
art_of_control_fire_resp.pack()
art_of_control_fire_resp.grid(column=1, row=1)
var_lvl_fire = IntVar()
lvl_fire_resp = Checkbutton(fr_fire_esq,variable=var_lvl_fire, onvalue=1, offvalue=0, command=lvl_fire)
lvl_fire_resp.pack()
lvl_fire_resp.grid(column=1, row=2)
var_bonfire = IntVar()
bonfire_resp = Checkbutton(fr_fire_esq,variable=var_bonfire, onvalue=1, offvalue=0, command=bonfire)
bonfire_resp.pack()
bonfire_resp.grid(column=1, row=3)
var_controlled_heat = IntVar()
controlled_heat_resp = Checkbutton(fr_fire_esq,variable=var_controlled_heat, onvalue=1, offvalue=0, command=controlled_heat)
controlled_heat_resp.pack()
controlled_heat_resp.grid(column=1, row=4)

# frame 2 

xp_log_fire_text = Label(fr_fire_dir, text='XP/Log')
xp_log_fire_text.grid(column=0, row=0)
xp_hr_fire_text = Label(fr_fire_dir, text='XP/Hr')
xp_hr_fire_text.grid(column=0, row=1)
coal_hr_fire_text = Label(fr_fire_dir, text='Caol/Hr')
coal_hr_fire_text.grid(column=0, row=2)
current_xp_fire_text = Label(fr_fire_dir, text='Current XP')
current_xp_fire_text.grid(column=0, row=3)
desired_lvl_fire_text = Label(fr_fire_dir, text='Desired Level')
desired_lvl_fire_text.grid(column=0, row=4)
logs_needed_fire_text = Label(fr_fire_dir, text='Logs Needed')
logs_needed_fire_text.grid(column=0, row=5)

xp_log_fire_resp = Label(fr_fire_dir, text='0')
xp_log_fire_resp.grid(column=1, row=0)
xp_hr_fire_resp = Label(fr_fire_dir, text='0')
xp_hr_fire_resp.grid(column=1, row=1)
coal_hr_fire_resp = Label(fr_fire_dir, text='0')
coal_hr_fire_resp.grid(column=1, row=2)
current_xp_fire_resp = Entry(fr_fire_dir, width=10)
current_xp_fire_resp.grid(column=1, row=3)
var_desired_lvl_fire = IntVar()
var_desired_lvl_fire.set([0]) 
desired_lvl_fire_resp = OptionMenu(fr_fire_dir, var_desired_lvl_fire, *lvl_list)
desired_lvl_fire_resp.grid(column=1, row=4)
logs_needed_fire_resp = Label(fr_fire_dir, text='0')
logs_needed_fire_resp.grid(column=1, row=5) 

#functions firemaking

# Cooking
tab4 = Frame(tabControl)
tabControl.add(tab4, text='Cooking')
tab4.columnconfigure(0, weight=1)
tab4.columnconfigure(1, weight=3)

# frames
fr_cook_esq = Frame(tab4, borderwidth=1, relief="solid")
fr_cook_esq.place(x=0, y=0)

fr_cook_dir = Frame(tab4, borderwidth=1, relief='solid')
fr_cook_dir.place(x=300, y=0)
fr_cook_dir2 = Frame(tab4, borderwidth=1, relief='solid')
fr_cook_dir2.place(x=300, y= 70)

# frame 1
cooking_fire_text = Label(fr_cook_esq, text='Cooking Fire')
cooking_fire_text.grid(row=0, columnspan=2 )
your_fire_cook_text = Label(fr_cook_esq, text='Your Fire')
your_fire_cook_text.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
skill_cape_text = Label(fr_cook_esq, text='Skill Cape/Cooking Gloves')
skill_cape_text.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
art_of_control_cook_text = Label(fr_cook_esq, text='Art of Control')
art_of_control_cook_text.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
recipe_cook_text = Label(fr_cook_esq, text='Recipe')
recipe_cook_text.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
mastery_lvl_cook_text = Label(fr_cook_esq, text='Mastery Level')
mastery_lvl_cook_text.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
burn_rate_cook_text = Label(fr_cook_esq, text='Burn Rate')
burn_rate_cook_text.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
gloves_profit_cook_text = Label(fr_cook_esq, text='Gloves Profit/Loss')
gloves_profit_cook_text.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
xp_hr_cook_text = Label(fr_cook_esq, text='XP/Hr')
xp_hr_cook_text.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)

def skill_cape_cook():
    skill_cape_cook = var_skill_cape_cook.get()
    return(skill_cape_cook)
    
def art_of_control_cook():
    art_of_control_cook = var_art_of_control_cook.get()
    if art_of_control_cook == 1:
        return 2.4
    else:
        return 3

log_list = ["Normal", "Oak", "Willow", "Teak","Maple", "Mahogany", "Yew", "Magic", "Redwood"]
recipe_cooking_fire_list = ["Shrimp","Beef", "Sardine", "Blowfish", "Herring", "Seahorse", "Trout", "Leaping Trout", "Poison Fish", "Salmon", "Leaping Salmon","Lobster", "Skeleton Fish", "Swordfish", "Anglerfish", "Fanfish", "Crab", "carp", "Shark", "Leaping Broad Fish", "Cave Fish", "Magic Fish", "Manta Fish", "Whale"]           

var_your_fire = StringVar()
var_your_fire.set(wood_list[0])
wood_list_fire_cook =  wood_list.remove('None')
your_fire_cook_resp = OptionMenu(fr_cook_esq, var_your_fire, *log_list)
your_fire_cook_resp.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
var_skill_cape_cook = IntVar()
skill_cape_cook_resp = Checkbutton(fr_cook_esq,variable=var_skill_cape_cook, onvalue=1, offvalue=0, command=skill_cape_cook)
skill_cape_cook_resp.pack()
skill_cape_cook_resp.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
var_art_of_control_cook = IntVar()
art_of_control_cook_resp = Checkbutton(fr_cook_esq,variable=var_art_of_control_cook, onvalue=1, offvalue=0, command=art_of_control_cook)
art_of_control_cook_resp.pack()
art_of_control_cook_resp.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
var_fish_cook = StringVar()
var_fish_cook.set(recipe_cooking_fire_list[0]) 
recipe_cook_resp = OptionMenu(fr_cook_esq, var_fish_cook, *recipe_cooking_fire_list)
recipe_cook_resp.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
var_mastery_lvl_cook = IntVar()
var_mastery_lvl_cook.set(lvl_list[0]) 
mastery_lvl_cook_resp = OptionMenu(fr_cook_esq, var_mastery_lvl_cook, *lvl_list)
mastery_lvl_cook_resp.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
burn_rate_cook_resp = Label(fr_cook_esq, text='0')
burn_rate_cook_resp.grid(column=1, row=6, sticky=tk.E, padx=5, pady=5)
gloves_profit_cook_resp = Label(fr_cook_esq, text='0')
gloves_profit_cook_resp.grid(column=1, row=7, sticky=tk.E, padx=5, pady=5)
xp_hr_cook_resp = Label(fr_cook_esq, text='0')
xp_hr_cook_resp.grid(column=1, row=8, sticky=tk.E, padx=5, pady=5)

# frame 3

current_xp_cook_text = Label(fr_cook_dir2, text='Current XP')
current_xp_cook_text.grid(column=0, row=0)
desired_lvl_cook_text = Label(fr_cook_dir2, text='Desired Level')
desired_lvl_cook_text.grid(column=0, row=1)
recipe2_cook_text = Label(fr_cook_dir2, text='Recipe')
recipe2_cook_text.grid(column=0, row=2)
fish_needed_cook_text = Label(fr_cook_dir2, text='Fish Needed')
fish_needed_cook_text.grid(column=0, row=3)

current_xp_cook_resp = Entry(fr_cook_dir2, width=10)
current_xp_cook_resp.grid(column=1, row=0)
var_desired_lvl_cook = StringVar()
var_desired_lvl_cook.set(lvl_list[0]) 
desired_lvl_cook_resp = OptionMenu(fr_cook_dir2, var_desired_lvl_cook, *lvl_list)
desired_lvl_cook_resp.grid(column=1, row=1)
var_fish2_cook = StringVar()
var_fish2_cook.set(recipe_cooking_fire_list[0]) 
recipe2_cook_resp = OptionMenu(fr_cook_dir2, var_fish2_cook, *recipe_cooking_fire_list)
recipe2_cook_resp.grid(column=1, row=2)
recipe_needed_cook_resp = Label(fr_cook_dir2, text='Fish Needed')
recipe_needed_cook_resp.grid(column=1, row=3)

# functions cooking
def fish_cook_xp(typefish):
    type_recipe = typefish
    fire_cooking = var_your_fire.get()

    xp_df = pd.read_excel('cooking.xlsx')
    bonus_xp = int(xp_df.loc[xp_df['Logs'] == fire_cooking, 'Bonus Xp'])
    xp = (int(xp_df.loc[xp_df['Recipe Cooking Fire'] == type_recipe,'Xp']))*(1+(bonus_xp*0.01))
    return xp 

def burn_rate_cook():
    if skill_cape_cook() == 1:
        burn_rate_cook_resp['text'] = 0
        return 0
    else:
        level = var_mastery_lvl_cook.get()
        burn_rate = (30 - (int(level) * 0.6))+1
    if burn_rate < 0:
        burn_rate_cook_resp['text'] = 1
        return 1
    else:
        burn_rate_cook_resp['text'] = round(burn_rate)
        return burn_rate

#FIXME ao executar gloves_profit_cook a função burn_rate_cook tambem executa, corrigir.
def gloves_profit_cook():
    type_recipe = var_fish_cook.get()
    burn_rate = burn_rate_cook()

    cooking_df = pd.read_excel('cooking.xlsx')
    value = int(cooking_df.loc[cooking_df['Recipe Cooking Fire'] == type_recipe, 'Value'])
    gloves_profit = ((500*value)-((500*(1-(burn_rate*0.01)))*value))-50000
    gloves_profit_cook_resp['text'] = round(gloves_profit)

#FIXME ao executar xp_hr_cook a função burn_rate_cook tambem execura, corrigir.
def xp_hr_cook():
    xp_fish_cook = fish_cook_xp(var_fish_cook.get())
    cook_rate = 3600/art_of_control_cook() 
    burn_rate_xp = burn_rate_cook()
    
    xp_hr = (cook_rate*(burn_rate_xp*0.01))+((cook_rate*(1-(burn_rate_xp*0.01)))*xp_fish_cook)
    xp_hr_cook_resp['text'] = round(xp_hr)

def fish_needed_cook():
    total_xp_fish = total_xp(current_xp_cook_resp.get(), var_desired_lvl_cook.get())
    xp_needed_cook = fish_cook_xp(var_fish2_cook.get())
    burn_rate_needed = burn_rate_cook()

    fish_needed = total_xp_fish / (xp_needed_cook * (1-(burn_rate_needed*0.01)))
    recipe_needed_cook_resp['text'] = math.ceil(fish_needed)

def button_cooking():
    gloves_profit_cook()
    xp_hr_cook()
    fish_needed_cook()

# cooking button    

calculate_cooking = Button(fr_cook_esq, text='Calcular',command=button_cooking)
calculate_cooking.grid(columnspan=2, row=9)

# Xp Calculate
tab5 = Frame(tabControl)
tabControl.add(tab5, text='XP Calculate')

fr_xp_calculate_esq = Frame(tab5, borderwidth=1, relief='solid')
fr_xp_calculate_esq.place(x=0, y=0)

current_xp = Label(fr_xp_calculate_esq, text='Current Xp')
current_xp.grid(column=0, row=0)
desired_xp = Label(fr_xp_calculate_esq, text='Desired Level')
desired_xp.grid(column=0, row=1)
xptill_xp = Label(fr_xp_calculate_esq, text='XP Till level')
xptill_xp.grid(column=0, row=2)
xpaction_xp = Label(fr_xp_calculate_esq, text='XP/Action')
xpaction_xp.grid(column=0, row=3)
items_xp = Label(fr_xp_calculate_esq, text='Items Needed/Action')
items_xp.grid(column=0, row=4)
itemneeded_xp = Label(fr_xp_calculate_esq, text='Items Needed')
itemneeded_xp.grid(column=0, row=5)

current_xp_resp = Entry(fr_xp_calculate_esq, width=10)
current_xp_resp.grid(column=1, row=0)
var_lvl_list_xp = StringVar()
desired_xp_resp = OptionMenu(fr_xp_calculate_esq, var_lvl_list_xp, *lvl_list)
desired_xp_resp.grid(column=1, row=1)
xptill_xp_resp = Entry(fr_xp_calculate_esq, width=10)
xptill_xp_resp.grid(column=1, row=2)
xpaction_xp_resp = Label(fr_xp_calculate_esq, text='Resp')
xpaction_xp_resp.grid(column=1, row=3)
items_xp_resp = Entry(fr_xp_calculate_esq, width=10)
items_xp_resp.grid(column=1, row=4)
itemneeded_xp_resp = Label(fr_xp_calculate_esq, text='Resp')
itemneeded_xp_resp.grid(column=1, row=5)


def get_desired_level():
    des_lvl1 = var_lvl_list_xp.get()
    xp_df = pd.read_excel('xp.xlsx')
    print(xp_df.loc[int(des_lvl1), 'exp'])


Button(fr_xp_calculate_esq, text='Calcular',command=get_desired_level).grid(column=0, row=6)

root.mainloop()
