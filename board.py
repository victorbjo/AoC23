import os
import importlib.util

def import_day_module(day_path):
    spec = importlib.util.spec_from_file_location("module.name", os.path.join(day_path, "main.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_day(day_module):
    #print(f"Running {day_module.__name__}")
    print("Part 1:", day_module.part1())
    print("Part 2:", day_module.part2())

def main():
    base_dir = os.getcwd()
    for day in sorted(os.listdir(base_dir)):
        if not day.startswith("Day 15"):
            continue
        day_path = os.path.join(base_dir, day)
        if os.path.isdir(day_path):
            print("Day", day_path)
            day_module = import_day_module(day_path)
            run_day(day_module)

if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    main()
