"""This modules defines the controllers to that manage the application execution"""

from shares.shares import SharesManager
from views.result_view import ResultView
from utils.timer import timer


class ApplicationController:
    """This controller runs the algorithms and call the view to display the results"""

    def __init__(self, sample, wallet, algorithm):
        self.sample = sample
        self.wallet = wallet
        self.algorithm = algorithm
        self.shares = SharesManager()
        self.shares.import_csv(self.sample)
        self.view = ResultView(self.sample, self.wallet, self.algorithm, self.shares)

    def run(self):
        if self.algorithm == "optimized":
            result, execution_time = timer(self.shares.optimized)(self.wallet)
        elif self.algorithm == "brute_force":
            result, execution_time = timer(self.shares.brute_force)(self.wallet)
        self.view.display_result(result, execution_time)
