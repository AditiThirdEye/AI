parentOf(ram,april).
parentOf(ram,rami).
parentOf(june, april).
parentOf(june, rami).
parentOf(april, august).
parentOf(sham, august).
parentOf(om,sham).
parentOf(may, sham).
parentOf(april, vijay).
parentOf(abc, vijay).
parentOf(rami, jay).
parentOf(sham, jay).

male(ram).
male(om).
male(abc).
male(sham).
male(vijay).
male(jay).
male(august)
female(june).
female(may).
female(april).
female(rami).


fatherOf(X,Y):- male(X),
    parentOf(X,Y).
/*
?- fatherOf(X,sham).
X = om ;
false.
*/

motherOf(X,Y):- female(X),
    parentOf(X,Y).
/*
?- motherOf(X, sham).
X = may ;
false.
*/

grandfatherOf(X,Y):- male(X),
    parentOf(X,Z),
    parentOf(Z,Y).
/*
?- grandfatherOf(X,august).
X = ram ;
X = om ;
false.
*/

grandmotherOf(X,Y):- female(X),
    parentOf(X,Z),
    parentOf(Z,Y).
/*
?- grandmotherOf(X,august).
X = june ;
X = may ;
false.
*/
