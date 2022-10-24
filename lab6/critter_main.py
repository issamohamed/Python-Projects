#!/usr/bin/env python3
# Critter World
# Adam Eck, 2018; Aaron Bauer, 2019-20

import argparse
import critter_model
import critter_gui
import inspect
import os
import threading
import sys
import json

def get_critters(critter_files):
    """
    Loads all the modules in the list critter_names
    """
    critters = {}
    for critter, filename in critter_files.items():
        if not filename.endswith(".py"):
            print("Expected filename for {} to end in '.py', instead found {}".format(critter, filename))
            continue
        try:
            exec("import {}".format(filename[:-3]))
        except ModuleNotFoundError as err:
            print("No {} file found for {}".format(filename, critter))
            continue
        except Exception as err:
            print("Encountered an error when importing {} for {}:".format(filename, critter))
            print(err)
            continue

        module = eval(filename[:-3])
        if not hasattr(module, critter):
            print("Expected to find class {} in {}, could not load {}".format(critter, filename, critter))
            continue
        critters[critter] = getattr(module, critter)
        for method in ["fight", "getColor", "getMove", "getChar", "fightOver"]:
            if not hasattr(critters[critter], method):
                print("{} is missing a {} method, not a valid critter".format(critter, method))
                critters.pop(critter)
                break
    return critters

def format_results(results):
    "Returns the results of a critter fight in a nice format."
    return '\n'.join(['%s:%20s kills %3s alive %3s total' % (critter.__name__, state.kills, 
                                                             state.alive, state.kills + state.alive)
                      for critter, state in results])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_file', nargs=1, required=False, default="critter_world_config.json")
    args = parser.parse_args()
    try:
        with open(args.config_file) as fp:
            config = json.load(fp)
    except Exception as err:
        print("There was an error loading {}:".format(args.config_file))
        print(err)
        print("Exiting...")
        sys.exit(1)

    for key in ["critter_files", "critter_pops", "width", "height"]:
        if key not in config:
            print("Configuration file {} must have a {} entry".format(args.config_file, key))
            print("Exiting...")
            sys.exit(1)

    critters = get_critters(config["critter_files"])
    if len(critters) < len(config["critter_files"]):
        print("Unable to load one or more of the critters specified in {}".format(args.config_file))
        print("Exiting...")
        sys.exit(1)

    if type(config["width"]) is not int or type(config["height"]) is not int:
        print("Width and height values in {} must be integers, instead found {} and {}".format(args.config_file, 
                                                                                               repr(config["width"]),
                                                                                               repr(config["height"])))
    model = critter_model.CritterModel(config["width"], config["height"], threading.Lock(), config)

    for critter in critters:
        if critter not in config["critter_pops"]:
            print("Could not find 'critter_pops' entry in {} for {}".format(args.config_file, critter))
            print("Exiting...")
            sys.exit(1)
        if type(config["critter_pops"][critter]) is not int:
            print("Critter population values in {} must be integers, instead found {} for {}".format(args.config_file,
                                                                                                     repr(config["critter_pops"][critter]),
                                                                                                     critter))
            print("Exiting..")
            sys.exit(1)
        model.add(critters[critter], config["critter_pops"][critter])

    if "quickfight" in config and config["quickfight"]:
        iterations = config["iterations"] if "iterations" in config else 1000
        for i in range(iterations):
            model.update()
        print(format_results(model.results()))
    else:
        c = critter_gui.CritterGUI(model)

if __name__ == '__main__':
    main()
