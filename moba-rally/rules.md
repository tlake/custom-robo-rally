# MOBA RALLY
(...or **Defense of the Robots** or **League of Robots** or **Robots of the Storm** or **Robots of Newearth** or **Call of Robots**…)


## Summary
In this 4v4 team game, each team is trying to destroy the opposing team's base while defending their own. Defensive towers surround the bases, firing upon enemy robots within range.


##Winning and Scoring
A KDO (Kills/Deaths/Objectives) score is tracked for each robot. Every killing shot a robot makes on another robot increments the robot's Kills counter; every death increments its Deaths counter; every killing shot on an Objective increments the Objectives counter.

When one of the two bases is destroyed, the game ends. The winner is the robot with the highest KDO score on the team that still has its base. The KDO score is computed as follows:

`Kills - Deaths + (Objectives * 5)`

In the event of both bases being destroyed simultaneously, the winner is the robot with the highest KDO among all robots. In the event of a KDO tie, the winner is the robot with the highest Objectives score among tied robots; then, the robot with the highest Kills score among tied robots; then, the robot with the lowest Deaths score among tied robots.

Credit for kills and objectives is counted for all participants - if two robots fire a killing shot on the same robot or objective, both robots are awarded credit.


## Setup
The game board is composed of two identical boards ("Vault"), mirrored. Add a second copy of the _High-Power Laser_ and _Double-Barreled Laser_ option cards to the option card deck. Each team has a spawning zone behind their base, snugged up such that the spawn zones are only one square removed from the board. There are four towers, situated at the corners of the walls surrounding each base.


## Game Features

### Teamwork
A robot does not block weapons fire or line-of-sight for other allied robots. Robots do not deal damage to other allied robots (friendly fire is off).


### Spawning
A robot may only respawn in their team's spawning zone. Robots do not fire weapons while inside the spawn zone, and attacks from the board do not extend into spawn zones. The barrier is one-way; dying and respawning is the only way to re-enter the spawning zone.


### Objectives
"Objectives" is a term that means "towers and/or bases." Objectives cannot be damaged by a robot's regular laser fire; rather, the _Mini Howitzer_ option card is the only way to damage a tower or a base, and is a permanent global option. See the **Option Cards** section for rules.


### Towers
Towers have a range of 3 squares, calculated without diagonals (this creates a diamond-shaped threat zone - see diagram at end of section). When weapons are fired, a tower selects a target at random from enemy robots in range and deals 3 damage to that robot. Towers are tall, so walls and other robots don't block a tower's line of sight.

Towers have 10 hit points, and count as impassable terrain that blocks weapons fire and line of sight until destroyed.

When destroyed (check for destruction as the final step of the damage phase, after all other damages and deaths have been accounted for), a tower deals 5 damage to its friendly base, and each living enemy robot is awarded an option card.

```
tower threat pattern:

      x
    x x x
  x x x x x
x x x T x x x
  x x x x x
    x x x
      x
```


### Bases
Bases are represented by the four wrench squares clustered together in the center of the boards.

If a robot ends the round inside their own base, they heal 2 points of damage. They may also transfer an option card in their possession to the base, granting that option to the entire allied team. A base may only have one team option active at any point, and a robot may overwrite the existing team option. The replaced option card is sent to the graveyard.

Bases are equipped with a sophisticated ID system, so robots may only enter their own base, not the enemy's.

If an enemy robot is able to strike the base with its Mini Howitzer, it may instead elect to disrupt the base's option transmitter. Discard the base's team option card to the graveyard.

A base has 40 hit points, and the perimeter of the base counts as a wall for purposes of laser fire.


### Wrench Squares
The four wrenches in the center of each board represent the bases; see the **Bases** section for their rules.

The remaining wrenches (two in opposite corners of each board) grant a robot an option card when the robot ends its fifth phase upon the square - if and only if the robot is on the enemy board. A robot does not gain an option card from the wrenches on the board upon which the robot's base also resides.


### Option Cards
There are a few modifications to option cards, detailed here.

#### Mini Howitzer
Operates as normal, with the following modifications:
- Is a permanent global option
- Range of 3 squares
- Able to damage towers and bases
- No ammunition tracker
- With High-Power Laser: range of 4 squares
- With Double-Barreled Laser: deals 2 damage

#### High-Power Laser
Operates as normal, with the following modifications:
- Increases Mini Howitzer range by 1
- For the purposes of extending the laser through a wall or robot, towers count as walls

#### Double-Barreled Laser
Operates as normal, with the following modifications:
- Allows Mini Howitzer to deal 2 damage instead of 1

#### Ablative Coat
Operates as normal on an individual basis. When installed into a base as a team option, this card reads as follows:
- Give all living allied robots two green tokens.
- As long as this option is broadcast, an allied robot may discard a token instead of taking a point of damage.
- As long as this option is broadcast, an allied robot gains two green tokens upon respawning. The respawning robot still begins play with the normal two damage tokens.
- When this card is discarded from the base, remove all green tokens from allied robots.
- No robot may ever be in possession of more than two tokens (a robot cannot gain tokens, die by falling into a pit, and then gain two additional tokens upon respawning).


### Timings

#### Team Option Installation:
**End of Round**

After everything in Phase 5 has been resolved, conclude Phase 5 and begin the End of Round phase. At this point, a robot in a base may elect to install an option it's currently carrying into the base. This decision window closes with the termination of the End of Round phase (in other words, decide before the next round of program cards are dealt).

#### Team Option Destruction:
**Very End of Damage Resolution**

After all other damage has been resolved (robots shooting robots, board lasers shooting robots, towers shooting robots), if a robot has targeted a base's option transmitter, discard the base's option card to the graveyard. This allows robots to benefit from their team option during the damage phase when their option card would be lost.
