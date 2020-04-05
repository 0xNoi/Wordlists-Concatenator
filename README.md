# Wordlists-Concatenator

Basic Concatenating wordlists script-tool.

Combine words using from multiple wordlists

## Example:
There are 3 example wordlists as fruit.txt, color.txt, country.txt
![](https://raw.githubusercontent.com/ozancetin/Wordlists-Concatenator/master/screenshots/wordlists.png)


For example try to combine fruit.txt and color.txt:
```
AppleRed
AppleGreen
AppleBlue
ApricotRed
ApricotGren
.
... 
```
Same thing for 3 wordlists combining as fruit.txt, color.txt, country.txt
```
AppleRedTurkey
AppleRedTurkey
AppleRedTurkey
AppleRedUnitedStates
.
.
```
## Usage: 

```
python wordcon.py wordlist1.txt wordlist2.txt
python wordcon.py wordlist1.txt wordlist2.txt wordlist3.txt
```
![](https://raw.githubusercontent.com/ozancetin/Wordlists-Concatenator/master/screenshots/1.png)
![](https://raw.githubusercontent.com/ozancetin/Wordlists-Concatenator/master/screenshots/2.png)


```
python twoloopcon.py wordlist1.txt wordlist2.txt
```
## Requirements

```
pip install more-itertools 
```
## Installation

``` 
git clone https://github.com/ozancetin
```
## Differences Between wordcon.py and twoloopcon.py

wordcon.py is using itertools library which is good at combination algorithm stuff much more fast and efficient for it. Especially good at big wordlists.

twoloopcon.py is using nested 2 for loops which has more complexity than wordcon.py, purpose of itertools lib issue if that happen you can use it. its slow than wordcon.py for big wordlists.

## ATTENTION!

AVOID TO COMBINE MASSIVE WORDLISTS TOGETHER

for example do not use ``rockyou.txt + rockyou.txt`` it can be crash your computer.

If you still wanna use this concern about complexity and combination result, depends on your computer power and strorage.
