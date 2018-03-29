
filevar_exists = bool("__file__" in vars())
print("__file__ in vars(): %s" % filevar_exists)
if filevar_exists:
    print("__file__: %s" % __file__)


