## Description
This is a small script that is supposed to help you solve the Woordle game (https://www.nytimes.com/games/wordle/index.html) when you run out of ideas for words to try. 

<br>

## How to use
You need to first try out 1 or 2 words so that you get a list of letters to narrow down your search:
* Good, confirmed letters: letters that are shown by Woordle with yellow. These letters are contained in the solution-word, but are not in the position that you entered them
* Bad, confirmed letters: letters marked with gray in Woordle. These are letters that are not contained by the solution-word. 
* Good letters in known positions: letters marked with green in Woordle. These are letters that are conainted in the solution-word and are in the exact position that you have tried. 

NOTE: The script uses a file that contains around 12.500 5 letters words. You need to first try out few words in the game, then come and fill in the fields in order to narrow down your search. You would need to know at least one letter and its position in order for the results to be relevant. Otherwise, the script will take a long time to filter out the results (sometimes hanging) and it will also provide a long list of eligible words, not really helping you out that much. 

Here is an example: 

![Example](/Images/Example.png)
