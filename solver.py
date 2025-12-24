from Pyro4 import expose


class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers

    def solve(self):
        with open(self.input_file_name, 'r') as f:
            data = f.read()

        n = len(self.workers)
        chunk_size = len(data) // n if n > 0 else len(data)

        mapped_results = []
        for i in range(n):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i < n - 1 else len(data)
            chunk = data[start:end]
            res = self.workers[i].count_words(chunk)
            mapped_results.append(res)

        total_count = 0
        for r in mapped_results:
            total_count += r.value

        with open(self.output_file_name, 'w') as f:
            f.write("Total words count: %d" % total_count)

    @staticmethod
    @expose
    def count_words(data):
        return len(data.split())
