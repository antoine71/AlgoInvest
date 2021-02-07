class ResultView:

    def __init__(self, results, shares_manager):
        self.results = results
        self.shares_manager = shares_manager

    def display_result(self):
        profit, shares = self.results
        wallet = 0

        print(f"Profit réalisé: {profit}")
        print("Actions achetées:")
        for name, quantity in shares.items():
            share = self.shares_manager.get_share_by_name(name)
            wallet += quantity * share.value
            print(f"{share.name}, valeur:{share.value}, rendement:{share.yield_}, quantité:{quantity}")
        print(f"Somme dépensée: {wallet}")
