"# OSRS-API-CLI"

23/01/2026
I have used the OSRSBytes API to create a CLI application for Old School RuneScape
Within this application you will be able to search for a players name and have all relevant information
regarding this player show up.

-------------------------------search_function_branch-------------------------------
23/01/2026
You are also able to search up items to see their buying limits, buying and selling prices and if they are a members item or not

I have added the ability to search for a user and the skill that they would want to look up
I have also moveed Bosses and Clue Scrolls to their own module to seperate the information that is being searched
-------------------------------search_function_branch-------------------------------

----------------------------filter_selected_options_branch----------------------------
27/01/2026
Highscores, Items, Bosses and Cluescrolls have been added to their own classes and given the ability to search
All modules get passed to main which will be the main place to run the programme

I am moving all method searches for the user to the main.py programme
to allow the user to search for specific options within the CLI interface

cluescrolls.py has been changed to a dictionary lookup function to allow easy of
use and maintainability

Re-factor of highscores.py, cluescrolls.py and bosses.py to be able to search for a username
without asking which stat would like to be selected for lookup also

main.py has been refactored to act as a menu system to allow the user to choose what they would like to see
(Stats, Item, Clue Scrolls, Bosses)

Users can now search for a user and check thir skills and then return back to the menu to select another option

A dictionary has been added to highscores to allow for the American spelling of "defence" (defense), while
also adding in alterior methods of spelling out skills e.g. "str" as "strength"

items.py has now been added to the main.py menu to allow a real use of the API CLI applciation

Cluescrolls are now implemented into the manu to allow users to check how many of each cluescroll
they have completed (Beginner, Easy, Medium, Hard, Elite and Master)

Bosses is not implemented into the menu to allo users to check how many of eash boss they have defeated

----------------------------filter_selected_options_branch----------------------------

---------------------------------exit_condition_branch--------------------------------
03/02/2025
Exit conditions have been set to the all functions of the menu to allow the user to press ENTER to quit
the programme
---------------------------------exit_condition_branch--------------------------------
