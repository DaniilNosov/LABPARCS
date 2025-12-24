from Pyro4 import expose

class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.workers = workers
        print("INIT SUCCESS")

    def solve(self):
        print("SOLVE STARTED")
        print("Workers connected: %d" % len(self.workers))
        print("Hello from PARCS!")
        print("SOLVE FINISHED")
