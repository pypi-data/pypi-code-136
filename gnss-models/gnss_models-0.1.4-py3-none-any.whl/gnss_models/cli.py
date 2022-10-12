import typer
from gnss_models import __app_name__, __version__
import argparse
import utils
import sys
import os
import model_generation as generate
import model_plotting as plot
import model_evaluation as evaluate
from save_pdf import save

app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


class CommandLineInterface:
    """
    CLI entry point
    """

    description = 'Tool to generate and evaluate mathematical models from GNSS satellites u-center csv files.'

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.description)

        self.parser.add_argument("--version", action="version", version=f"{__app_name__} v{__version__})")
        self.dir_or_file = self.parser.add_mutually_exclusive_group(required=False)
        self.dir_or_file.add_argument('-file', type=utils.file_path, help='CSV file to analyze')
        self.dir_or_file.add_argument('-dir', type=utils.dir_path,
                                 help='Directory which contains all CSV files to analyze (default is current directory)')

        self.parser.add_argument('-sat', type=int, help='Satellite number to analyze (default is all satellites)',
                            required=False)
        self.parser.add_argument('-save', type=utils.dir_path,
                            help='Directory where results will be saved (default is current directory', required=False)

    @classmethod
    def entrypoint(cls):
        """
        Main entrypoint
        """
        print('Processing . . .')
        cls().run(sys.argv[1:])

    def run(self, args):
        """
        Process Raw arguments and run the models
        """
        args = self.parser.parse_args(args)
        vargs = vars(args)

        if vargs['save'] is None:
            vargs['save'] = os.getcwd()

        if vargs['sat'] is not None:
            start = vargs['sat']
            end = vargs['sat'] + 1
        else:
            start = 1
            end = 33

        vargs['p_value'] = 0.997176
        vargs['eval_model'] = []
        vargs['eval_data'] = []

        for i in range(start, end):
            vargs['sat'] = str(i)

            if vargs['file'] is not None:
                x_df, y_df, period = utils.import_data(vargs['sat'], vargs['file'], vargs['p_value'])
                print(
                    'Generating Model for Satellite {} based on file {} . . .'.format(vargs['sat'], vargs['file']))
                analysis = self.run_analysis(vargs, x_df, y_df, period)
            else:
                if vargs['dir'] is None:
                    vargs['dir'] = os.getcwd()
                # Take the max size file for analysis
                list_of_files = [vargs['dir'] + file for file in os.listdir(vargs['dir'])]
                analysis_file = max(list_of_files, key=lambda x: os.stat(x).st_size)
                filepath = utils.file_path(analysis_file)
                vargs['file'] = filepath
                x_df, y_df, period = utils.import_data(vargs['sat'], vargs['file'], vargs['p_value'])
                print(
                    'Generating Model for Satellite {} based on file {} . . .'.format(vargs['sat'], vargs['file']))
                analysis = self.run_analysis(vargs, x_df, y_df, period)

                for file in os.listdir(vargs['dir']):
                    file = vargs['dir'] + file
                    if file != analysis_file:
                        utils.file_path(file)
                        vargs['file'] = os.path.join(vargs['dir'], file)
                        x_df, y_df, period = utils.import_data(vargs['sat'], vargs['file'], vargs['p_value'])
                        print('Applying Model for Satellite {} based on file {} . . .'.format(vargs['sat'],
                                                                                              vargs['file']))
                        analysis['file'] = vargs['file']
                        analysis = self.apply_analysis(analysis, x_df, y_df)
            print('Evaluating Model for Satellite {} . . .'.format(vargs['sat']))
            results = evaluate.evaluate(analysis, y_df)

            save(results)

    @staticmethod
    def run_analysis(vargs, x_df, y_df, period):
        data = vargs.copy()
        data['other_filenames'] = []
        data['analysis_filename'] = os.path.splitext(os.path.basename(data['file']))[0]

        x_period = period['time'].values
        y_period = period['elevation SV' + data['sat']].values
        str_model = generate.generate_piecewise_cubic_model(x_period, y_period)
        data['str_model'] = str_model
        analysis = CommandLineInterface.apply_analysis(data, x_df, y_df, analysis=True)

        return analysis

    @staticmethod
    def apply_analysis(data, x_df, y_df, analysis=False):
        data['filename'] = os.path.splitext(os.path.basename(data['file']))[0]
        if not analysis:
            data['other_filenames'].append(os.path.splitext(os.path.basename(data['file']))[0])

        np_model = generate.apply_model(data['p_value'], x_df, y_df, data['str_model'])
        data['np_model'] = np_model
        data = plot.plot_model(data, x_df, y_df, analysis)
        # Concat models and data for evaluation (may break if arrays len different)
        data['eval_model'] += list(np_model)
        data['eval_data'] += list(y_df)

        return data
