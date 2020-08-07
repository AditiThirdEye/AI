assignDur(ai, 1234, 1345).
assignDur(coa, 1345, 1456).
assignDur(os, 1245, 1375).
assignDur(pm, 1564, 1896).
assignDur(toc, 1654, 2100).

workQuestion(ai, 20).
workQuestion(coa, 23).
workQuestion(os, 50).
workQuestion(pm, 19).
workQuestion(toc, 37).

number(ai, 2).
number(coa, 3).
number(os, 4).
number(pm, 5).
number(toc, 6).


/*Greater than and Equal to operations!*/
task(X, Y) :- assignDur(X, A, B),
    Y>=A,
    Y=<B.
/*OUTPUT :
?- task(X, 1350).
X = coa ;
X = os ;
false.
*/


/*Using division and subtraction operator*/
workRate(X, Y):- assignDur(X, A, B), workQuestion(X, C),
    Y is C/(B-A).
/* OUTPUT :
?- workRate(ai, Y).
Y = 0.18018018018018017.
*/


/*Using multiplication operator*/
totalTime(X, Y):- assignDur(X, A, B), number(X, C),
    Y is C*(B-A).
/* OUTPUT :
?- totalTime(ai, Y).
Y = 222.
*/

/*Using multiplication operator*/
addWorkandNumber(X, Y):- workQuestion(X, C), number(X, D),
    Y is C+D.
/* OUTPUT :
?- addWorkandNumber(ai, Y).
Y = 22.
*/

/*Using loop*/
/* sum of integers from 1 to N inclusive */
sumto(1, 1).
sumto(N, M) :- N>1, N1 is N-1, sumto(N1, M1), M is M1+N.
/*
?- sumto(10,N).
N = 55 .
*/
