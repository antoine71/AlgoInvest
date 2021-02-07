from shares.shares import SharesManager
from views.result_view import ResultView
from utils.timer import timer


class ApplicationController:

    def __init__(self, sample, wallet, algorithm):
        self.sample = sample
        self.wallet = wallet
        self.algorithm = algorithm
        self.shares = SharesManager()
        self.shares.import_csv(self.sample)
        self.view = ResultView(self.sample, self.wallet, self.algorithm, self.shares)

    def run(self):
        if self.algorithm == "knapsack":
            result, execution_time = timer(self.shares.knapsack)(self.wallet)
        elif self.algorithm == "brute_force":
            result, execution_time = timer(self.shares.brute_force)(self.wallet)
        self.view.display_result(result, execution_time)
