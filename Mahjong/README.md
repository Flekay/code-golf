 Given a list of mahjong hands, print out all of the hands which are complete under the rules of Riichi Mahjong.

Mahjong tiles are divided into three suits of number tiles from 1 to 9, and seven honor tiles, which are not numbered. These are the Unicode characters representing the tiles in each suit, from 1 to 9:

    Characters 🀇🀈🀉🀊🀋🀌🀍🀎🀏
    Bamboo 🀐🀑🀒🀓🀔🀕🀖🀗🀘
    Circles 🀙🀚🀛🀜🀝🀞🀟🀠🀡

These are the Unicode characters representing honor tiles: 🀀🀁🀂🀃🀄🀅🀆

A triplet is a group of three identical tiles, e.g. 🀓🀓🀓 or 🀅🀅🀅. A sequence is a group of three number tiles of the same suit and with consecutive numbers, e.g. 🀇🀈🀉 or 🀜🀝🀞. A meld is either a triplet or a sequence. A pair is a group of two identical tiles.

A mahjong hand is complete if it consists of one of the following:

    Four melds and a pair.
    Seven distinct pairs. Four of the same tile do not count as two pairs.
    All seven honor tiles and the 1 and 9 of each suit, plus one duplicate tile that forms a pair.

The tiles in a mahjong hand are not ordered. For example, the hand 🀇🀈🀈🀈🀉🀓🀔🀕🀚🀛🀜🀀🀀🀀 is complete, as it can be split into the groups 🀇🀈🀉 🀓🀔🀕 🀚🀛🀜 🀀🀀🀀 🀈🀈. You may assume that no hand contains more than 4 of a single tile.

The input consists of a sequence of arguments, each containing a string of 14 Unicode characters which represent the tiles in the hand. Output the arguments that represent complete mahjong hands, in the same order as they appear in the argument list. 
