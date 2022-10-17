from typing import Optional
import time
from .formatter import Formatter, space
from .game import Game


class Session:
    """API for a session of gameplay of IQ Tester"""

    def __init__(self) -> None:

        # Create a Formatter object to manage formats of statements to stdout
        self.f = Formatter(78)

        # Initialize session statistics
        self.played = 0
        self.total_score = 0
        self.board_size = 5

        # Initialize session settings
        self.keep_playing = True
        self.pause = 1.25
        self.msg_pause = 0.75

        # Initialize the attribute to store instances of Game
        self.game: Optional[Game] = None

    def get_average(self) -> float:
        """Return the average points per game for this session"""
        if self.played == 0:
            return round(0, 1)
        return round(self.total_score / self.played, 1)

    def start(self) -> None:
        """Initiate and manage a new session of games"""

        # Display package header and playing instructions
        self.print_new_session_header()
        self.print_instructions()

        # Keep playing until user elects to quit
        while self.keep_playing:

            # Display main menu and prompt user to make a selection
            self.main_menu()
            main_choice = self.menu_selection()

            # Handle selection to start new game
            if main_choice == "":

                # Instantiate a new Game instance
                self.game = Game(self.f, self.board_size, self.pause)

                # Launch game play and get back the number of points earned
                game_score = self.game.play()

                # Handle user selection to quit mid-game
                if game_score == -1:
                    continue

                # Update session statistics
                self.total_score += game_score
                self.played += 1

            # Handle selection to navigate to settings menu
            elif main_choice == "s":

                # Display settings menu and prompt user to make a selection
                self.settings_menu()
                setting_choice = self.menu_selection()

                # Handle selection to update board size
                if setting_choice == "s":
                    self.update_board_size()
                    time.sleep(self.msg_pause)

                # Handle selection to change pause time
                elif setting_choice == "p":
                    self.update_pause()
                    time.sleep(self.msg_pause)

                # Pause then return to main menu
                self.f.center("Returning to Main Menu...")
                time.sleep(self.msg_pause)

            # Handle any other selection, treating as a choice to quit
            else:
                self.quit()

    @space
    def main_menu(self) -> None:
        """Display the main menu including statistics and gameplay options"""

        # Set width of menu
        width = 40

        # Top of Menu box and header
        self.f.center("", [], '-', width - 2)
        self.f.center("", [], " ", width, '|')
        self.f.center("MAIN MENU", ['BOLD'], " ", width, '|')
        self.f.center("", [], " ", width, '|')

        # Game Statistics
        # Format total and average scores for display
        score_str = f"{self.total_score:,}"
        average = self.get_average()
        if average % 1 == 0:
            average = int(average)
        avg_str = f"{average:,}"

        # Assemble strings for each statistic, aligned left and right
        l, r = 18, max(6, len(score_str), len(avg_str)) + 1
        games_played = "GAMES PLAYED: ".ljust(l) + str(self.played).rjust(r)
        total_score = "YOUR TOTAL SCORE: ".ljust(l) + score_str.rjust(r)
        average_score = "AVERAGE SCORE: ".ljust(l) + avg_str.rjust(r)

        # Display each menu row with formatting
        formats = ['BOLD', 'GREEN']
        self.f.center(games_played, formats, " ", width, '|')
        self.f.center(total_score, formats, " ", width, '|')
        self.f.center(average_score, formats, " ", width, '|')
        self.f.center("", [], " ", width, '|')

        # Gameplay options
        formats = ['BOLD', 'RED']
        new_game_row = "New Game".ljust(l, '.') + "[ENTER]".rjust(r, '.')
        settings_row = "Settings".ljust(l, '.') + "[s]".rjust(r, '.')
        quit_row = "Quit".ljust(l, '.') + "[q]".rjust(r, '.')
        self.f.center(new_game_row, formats, " ", width, '|')
        self.f.center(settings_row, formats, " ", width, '|')
        self.f.center(quit_row, formats, " ", width, '|')

        # Bottom of Menu box
        self.f.center("", [], " ", width, '|')
        self.f.center("", [], '-', width - 2)

    @space
    def settings_menu(self) -> None:
        """Display settings menu and allow user to change settings"""

        # menu width
        width = 40
        l, r = 18, 4

        # Top of Menu box and header
        self.f.center("", [], '-', width - 2)
        self.f.center("", [], " ", width, '|')
        self.f.center("SETTINGS MENU", ['BOLD'], " ", width, '|')
        self.f.center("", [], " ", width, '|')

        # Menu options
        n = self.board_size
        size_row = f"Board Size ({n})".ljust(l, '.') + "[s]".rjust(r, '.')
        p = self.pause
        pause_row = f"Pause Time ({p})".ljust(l, '.') + "[p]".rjust(r, '.')
        return_row = "Return".ljust(l, '.') + "[r]".rjust(r, '.')
        self.f.center(size_row, [], " ", width, '|')
        self.f.center(pause_row, [], " ", width, '|')
        self.f.center(return_row, [], " ", width, '|')

        # Bottom of Menu box
        self.f.center("", [], " ", width, '|')
        self.f.center("", [], '-', width - 2)

    def update_board_size(self) -> None:
        """Prompt user to update the default number of rows for a new board"""

        low = 4  # minimum board size (3 or less doesn't work)
        high = 6  # maximum board size (7 or more uses > 26 pegs)

        # Infinite loop to re-prompt until input is valid
        while True:

            # Prompt user for desired board size
            prompt = f"Enter desired board size ({low} to {high}):"
            user_input = self.f.prompt(prompt)

            # Validate user input
            try:
                new_size = int(user_input)
                if low <= new_size <= high:
                    break

            # Handle nonnumeric user input
            except (TypeError, ValueError, NameError):
                self.f.center("Board size must be an integer. Try again.")

        # Update board size setting
        self.f.center(f"Updating board size to {new_size}...", end="\n\n")
        self.board_size = new_size

    def update_pause(self) -> None:
        """Prompt user to update the default pause time after game over"""

        # Set bounds
        low = 0
        high = 3

        # Infinite loop to re-prompt until input is valid
        while True:

            # Prompt user for desired pause time
            prompt = f"Enter the desired pause ({low} to {high} seconds):"
            user_input = self.f.prompt(prompt)

            # Validate user input
            try:
                new_pause = float(user_input)
                if low <= new_pause <= high:
                    break

            # Handle nonnumeric user input
            except (TypeError, ValueError, NameError):
                self.f.center("Pause must be a float or int. Try again.")

        # Update pause setting
        self.f.center(f"Updating pause to {new_pause:.2f}s...", end="\n\n")
        self.pause = new_pause

    @space
    def print_new_session_header(self) -> None:
        """Print header rows for a new session"""
        self.f.center('', ["BOLD", "BLUE"], '*')
        self.f.center(' WELCOME TO IQ TESTER ', ["BOLD"], '*')
        self.f.center('', ["BOLD", "BLUE"], '*')

    def print_instructions(self) -> None:
        """Print instructions for the game"""
        self.f.center("Start with any one hole empty.")
        self.f.center("As you jump the pegs remove them from the board.")
        self.f.center("Try to leave only one peg. See how you rate!")

    @space
    def footer(self) -> None:
        """Print footer rows for a session"""
        self.f.center("For even more fun compete with someone. Lots of luck!")
        self.f.center("Copyright (C) 1975 Venture MFG. Co., INC. U.S.A.")
        self.f.center("Python package `iqtester` by Andrew Tracey, 2022.")
        self.f.center("Follow me: https://www.github.com/andrewt110216")

    def menu_selection(self) -> str:
        """Prompt user to select menu option and return lowercased choice"""
        return self.f.prompt("Select a menu option").lower()

    def quit(self) -> None:
        """Handle user selection to quit playing"""
        self.f.center("Thanks for playing!", ['BOLD'])
        self.footer()
        self.keep_playing = False
