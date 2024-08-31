# Used to iterate over the sequence like list, string, dictionary, set or tuple

#Less like the for loop in other programming language

# Teams=['IND','PAK','AFG','SL','BAN','NEP','AUS','NZ','WI','ENG']
# for i in Teams:
#     print(i)
# Teams=[['IND','PAK'],['AFG','SL'],['BAN','NEP'],['AUS','NZ'],['WI','ENG']]
# for T1,T2 in Teams:
#     print(T1, 'Vs', T2)
#

Teams=[['IND','PAK'],['AFG','SL'],['BAN','NEP'],['AUS','NZ'],['WI','ENG']]
teams=dict(Teams)
print(teams)
for i,j in teams.items():
    print(i,'Vs',j)