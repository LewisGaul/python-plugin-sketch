import runpy

def test():
    runpy.run_module("mypkg", run_name="__main__")
