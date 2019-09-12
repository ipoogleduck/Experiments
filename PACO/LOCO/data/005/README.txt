VERSION 0.1.3

If this experiment was fully and successfully completed by the participant, you only need you use the test data file, it contains all the data you need.
If something went wrong during the experiment, or it was aborted before it was finished, you can use the oldornew data file to recover the user's responses for each old or new trail.
The columns for the test data file are ordered by the order that they are presented at test (Only the old stimuli), and then are ordered by the order they were presented at Old Or New (Only new stimuli).

How to use data in the test file:
The stimuli name corresponds to each stimuli in the stimuli folder (located in the main LOCO folder).
Use the test order, oldorneworder, and study order to sort each data row. To do this, create an empty array and use a for loop to append the lowest to highest number of the order column, starting at 0.
User vs Correct is self explanatory, with old or new being added as N/A if it was skipped in the header file.
The X and Y are coordinates on the screen (0.5 is the highest y value, while 0.9? is the highest x value), color is out of 360, and rad# is out of 100 (most usefull because there are only 100 possible color options).
AproxColor is usefull for seeing if the participant was in the correct range, use it only for if one of the users color is in the correct colors, they are in range, and if not, they are out of range. Don't use this for any more accuracy than what was previously described. It is calculated by the maximum possible color that could possibly be in each category, and is subject to some human error.
Location distance is calculated using the pythagorean theorem, where a and b are the x and y coordinates.
radColorDist is calculated by the distance off they are from the correct color out of the 100 possible options (50 is the max number this can be).
OldOrNew rt and Test rt are reaction times of the user.
Start times are the start times of each trail, with hour, minute, second.
Onset time counts the amount of seconds when each stimuli was shown since the first reset (Fixation Cross) of that section (for example, the beginning of study) came on the screen
Date is the date and time that the experiment started, and is not updated every trail.
Psychopy running version should be at least 3.1.5.

Thanks for reading! Have any more questions? Contact me at ipoogleduck@gmail.com