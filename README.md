# README
The sub folders contain tasks of different projects.
Each sub folder has a `README.md` file with additional information about the task

## Rock, Paper, Scissors
### ./game/rps.py + tests.py (1 day)

## Parse log, caculate some statistics of bit stream rate
### ./parser/get_stats.py (0.5 day)

## Steps to work on the the project
* Register your account on github.com if you don't have one
* Sign in your account on github.com
* Go to https://github.com/tonywgh/codingfun in the same browser
* Click "Fork" button at top-right corner on the page
* Then you can clone the project on you local computer
* Work on the project
* Push your work back to github
* Create a pull request by clicking "New pull request" on https://github.com/[your-github-username]/codingfun, comparing changes with
    
    base fork: tonywgh/codingfun|base: master <- head fork: [your-github-username]/codingfun|compare: master

## Steps to test the project
* Run pip install -r requirements.txt
* To test Rock Paper Scissors,

    python3 game/rpc.py

* To run the tests for the game,

    pytest game/tests.py

* Game - Assumptions made:
    1. We let the game run on a loop until user presses 'e'
    2. We are not raising an exception and killing the game if an invalid input is given(only logging it)

* To test the parser,

    python3 parser/get_stats.py

* Parser - Assumptions made:
    1. We calculate min, mid, max and average values for Old and New separately and display it
