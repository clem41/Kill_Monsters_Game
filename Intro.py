import sys
import os

from pip._vendor.distlib.compat import raw_input


def Intro():
    print("Welcome to Kill Monsters!\nYou'll have to exit each map\n"
          "while encountering monsters, merchants and objects\nTry to stay alive!"
          "\nTo START a new game : enter 1\nTo LOAD the previous game : enter 2"
          "\nTo EXIT : enter 3 (or close the tab)")
    choice = raw_input(">>>>>>>")