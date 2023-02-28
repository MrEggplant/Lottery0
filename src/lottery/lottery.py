from src.utils.save_results_to_file import save_and_show_lottery_results
import random


class Lottery:

    def __init__(self, participants_list, prizes_list):

        self.participants_list = participants_list
        self.prizes_list = prizes_list

    def run_lottery(self, number_of_winners):
        weights = []
        for instance in self.participants_list:
            weights.append(int(instance.weight))

        winners = random.choices(
            self.participants_list,
            weights,
            k=number_of_winners
        )
        return winners

    def show_winners_and_prizes(self, number_of_winners, name_for_results_file):
        winners = self.run_lottery(number_of_winners)
        winners_list_for_dump = []

        for index, value in enumerate(winners):
            value.prize = self.prizes_list[index].name

        if len(winners) <= len(self.prizes_list):
            for winner in winners:
                if name_for_results_file is None:
                    print("{} {} - {}".format(winner.name, winner.surname, winner.prize))

                else:
                    winners_list_for_dump.append({
                        'first_name': winner.name,
                        'last_name': winner.surname,
                        'prize': winner.prize
                    })
            save_and_show_lottery_results(winners_list_for_dump, name_for_results_file)
        else:
            print("We have not enough prizes.")
