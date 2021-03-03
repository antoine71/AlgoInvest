"""
This modules defines the views to display the information to the user
"""


class ResultView:
    """
    This class displays the results obtained from the ShareManager
    algorithmic methods
    """

    def __init__(self, sample, wallet, algorithm, shares_manager):
        self.sample = sample
        self.wallet = wallet
        self.algorithm = algorithm
        self.shares_manager = shares_manager

    def display_result(self, results, execution_time):
        profit, shares, clean_sample_size = results
        wallet = 0
        print("###########################################################################")
        print("                                 AlgoInvest                                ")
        print("###########################################################################")
        print("")
        print(f"Echantillon évalué: {self.sample}")
        print(f"Taille de l'échantillon initial: {len(self.shares_manager)} actions")
        if self.algorithm == "optimized":
            print(f"Taille de l'échantillon après nettoyage: {clean_sample_size} actions")
        print(f"Somme disponible en portefeuille: {self.wallet} Euros")
        print(f"Algorithme utilisé: {self.algorithm}")
        print("")
        print("###########################################################################")
        print("")
        print("Résultats:")
        print("")
        print(f"Profit réalisé: {round(profit, 1)} Euros")
        print("")
        print("Actions achetées:")
        for name, quantity in shares.items():
            share = self.shares_manager.get_share_by_name(name)
            wallet += quantity * share.value
            print(f"\t{share.name}, valeur: {share.value} Euros, rendement: {share.yield_} %, quantité: {quantity}")
        print("")
        print(f"Somme dépensée: {round(wallet, 2)} Euros")
        print("")
        print("###########################################################################")
        print("")
        print(f"Temps d'exécution de l'algorithme: {round(execution_time, 3)} secondes")
        print("")
        print("###########################################################################")
