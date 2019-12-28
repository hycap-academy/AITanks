
import inspect
if "rungame" not in inspect.getmodule(inspect.stack()[0])._filesbymodname["__main__"]:
    import rungame
