import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from scripts.unofficial import import_agents, import_cosmetics, import_maps




def un_official():
    print("    Downloading un-official data...")
    print("        Downloading agents...")
    import_agents.main()
    print("        Downloading maps...")
    import_maps.main()
    print("        Downloading cosmetics...")
    import_cosmetics.main()
    print("    Done!")
    print()



def main():
    print("Starting downloading...")
    un_official()


if __name__ == "__main__":
    main()
