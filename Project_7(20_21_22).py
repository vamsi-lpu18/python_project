# PYTHOM-PROJECT -{20_21_22}
# A code which generates random story 
import random
#importing random module
s=str(input('  Hello\nDear sir/madam \ntype your name : '))
situation=['A long ago','Once upon a time','Few years ago','That day','Yesterday','At the time of her birthday','Mean while',"Often"]
characters=['Shazam','Smith','Ceaser','Thor','Gwen ceazy','Bill','Doremaon','Nobita and Shezuka','Ben and Gwen','Shinchan','Power Rangers','Shradda kapoor']
places=['Grave yard','Death hell','Clock tower','Hongtong','Zerusalem','Zurassic world','Eighteenjan','In the dwelling heart']
role=['Comedian','Destroyer','Honourable','Leader','Heart stealer','side character','Trend setter','Made for each other','Long lasting forever','Torch bearers']
script=['is an intellectual','ready to do anything for her','has understand that she been suffering from that ','never gone wrong','cant live without ','cried over the graveyard','being an ',' got realization',' if the one which we like the most has gone does not mean that we should gone','There is life after evry like failure']
print( f'Dear {s} ur story : \n',random.choice(situation)+', '+random.choice(characters)+', '+random.choice(places)+' ,'+random.choice(role)+', '+random.choice(script)+', '+random.choice(characters)+', '+random.choice(places)+','+random.choice(role)+', '+random.choice(script)+',' +random.choice(script)+", "+random.choice(role)+", "+random.choice(script)+', '+random.choice(role)+', '+random.choice(script)+', '+random.choice(characters)+',  '+random.choice(script)+', '+random.choice(places)+', '+random.choice(situation)+'.')
# ''''Generates story randomly''''