import csv
import os 

def format_step_name(step_name): 
    text = ""
    formatted = step_name.split("(")[0]
    return formatted

def format_transitions(transitions): 
    values = []
    for val in transitions: 
        if "(" in val:
            updated = val.split("(")[0]
            values.append(updated)

        else: 
            values.append(val)

    return values 

def get_corresponding_blue(name): 
    values = [x["step_name"].lower().rstrip() for x in blue_values]

    if name.lower().rstrip() in exceptions: 
        name = name.replace("&", "and")
        
    for val in blue_values:
        if val is not None: 
            if val["step_name"].lower().rstrip() == name.lower().rstrip(): 
                return val

def remove_dots(val): 
    new = []
    if "." in val[0]: 
        new.append(val[0].replace(".", ""))

    else: 
        new.append(val[0])

    if "." in val[1]: 
        new.append(val[1].replace(".", ""))

    else: 
        new.append(val[1])
        
    return tuple(new)

def get_corresponding_blue_value(red_val, blue_vals): 
    for ele in blue_vals: 
        if ele == red_val: 
            return ele

        else: 
            pass
    
    return None

def try_this_approach(red_val, blue_vals):  
        # A None value would signify that there is a discrepancy
        if get_corresponding_blue_value(red_val, blue_vals) is None: 
            print(red_val, "  ------> transition  not found in Blue Jira")
            
        else: 
            pass

def compare_values():
    for val in red_values:
        blue_step_name = get_corresponding_blue( val["step_name"])
        if blue_step_name is None: 
            print(val["step_name"], ">>>>>>>>>  step name not found in Blue Jira ")

        else: 
            r = val["transitions"]
            b = blue_step_name["transitions"]
            red_sorted = sorted(val["transitions"])
            blue_sorted = sorted(blue_step_name["transitions"]) 

            for val  in zip(red_sorted, blue_sorted):
                # updated_val = remove_dots(val)
                updated_val = val
                if updated_val[0] == updated_val[1]:
                    pass
                else: 
                    try_this_approach(updated_val[0], blue_sorted)

default_path = os.getcwd() + "/csv_files/"

red_values = []
blue_values = []
exceptions = ["testing qa & release"]
with open(default_path + "red.csv", "rt") as file: 
    data = csv.reader(file)

    for row in data:
        data_sets = {"step_name": "", "transitions": []}
        data_sets["step_name"] = format_step_name(row[0])
        data_sets["transitions"] = format_transitions(row[2].split("\n"))
        red_values.append(data_sets)

with open(default_path + "blue.csv", "rt") as file: 
    data = csv.reader(file)

    for row in data: 
        data_sets = {"step_name": "", "transitions": []}
        data_sets["step_name"] = format_step_name(row[0])
        data_sets["transitions"] = format_transitions(row[2].split("\n"))
        blue_values.append(data_sets)

compare_values()
