class bcolors:
    HEADER = '\033[33m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.HEADER}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
dicts = {}
dicts.update({"fuck":22})
dicts.update({"fucks":24})
for key in dicts.keys():
    print(key)
dirs = [1,2,3,4,5,1,1]
dirs.remove(1)
print(dirs)
dicts = {(1,1,1,1):3,(1,1,1,2):4}
print((1,1,1,2) in dicts)