P6 FIFA Rating Calculator

For the final project, I decided to work on a problem that I have personally faced while playing the popular soccer game EA Sports FIFA. In the game's Ultimate Team mode, you can create squads of 11 soccer players that each have their own overall stat. There are challenges where you have to create squads with certain qualifications, with one of the most important being the overall squad rating. The calculation of the overall squad rating is not as easy as adding the players' overall stats and dividing by 11. The actual calculation goes like this: 

1. Sum up ratings of 11 players

2. Divide by 11

3. Calcualte total excess(For every player above the average, calculate difference and sum them up

4. Add total excess to team sum

5. Round to nearest digit

6. Divide by 11

7. Round down for final squad rating

As you can see, this calculation is not super easy to do in the head, so there is a lot of trial and error while creating the squads. I wanted to create a program that would help me craft squads by quickly calculating the overal rating of the squad. Doing the actual calculation through code is pretty easy, so I wanted to also make it so that you can give it a list of players you aleady have, and then the program will tell you what players you need to meet the desired overall rating. I was going to also create a GUI for the program, but I do not have much experience coding so I was not able to implement it in time. I made the progam run on the Raspberry Pi 4.
