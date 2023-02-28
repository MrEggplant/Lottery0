from src.lottery.lottery import Lottery
from src.participants_list.prepare_participants_list import prepare_participants_list
from src.prizes.prepare_prizes_list import prepare_prizes_list
from src.utils.file_lists_preparation import file_list_preparation
import click


@click.option('--number_of_winners', required=True, type=int, nargs=1, help='Type how many winners do you need.')
@click.option('--participants_file', required=True, type=click.Choice(file_list_preparation('participants')), nargs=1,
              help='Type name of file with participants.')
@click.option('--lottery_template', required=False, nargs=1,
              type=click.Choice(file_list_preparation('lottery_templates')),
              help='Type name of file with lottery template.')
@click.option('--name_for_results_file', required=False, nargs=1, default=None, help='Type name for results file.')
@click.command()
def cli(number_of_winners, participants_file, lottery_template, name_for_results_file):
    if number_of_winners > 0:
        Lottery(prepare_participants_list(participants_file),
                prepare_prizes_list(lottery_template)).show_winners_and_prizes(
            number_of_winners, name_for_results_file)
    else:
        print('Number of winners cannot be 0 or less')


if __name__ == '__main__':
    cli()
