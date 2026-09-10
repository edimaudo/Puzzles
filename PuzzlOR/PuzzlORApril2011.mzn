% PuzzlOR April 2011 - Choose Your Crew
% http://www.puzzlor.com/2011-04_ChooseYourCrew.html
% Goal: Find the right amount of workers & used minizinc

%variables
%A	Skills for Amy
%B	Skills for Bill
%C	Skills for Carl
%D	Skills for Dan
%E	Skills for Eva
%F	Skills for Fred
%G	Skills for Greg
%H	Skills for Henry
%I	Skills for Ida
var 0..1: A;
var 0..1: B;
var 0..1: C;
var 0..1: D;
var 0..1: E;
var 0..1: F;
var 0..1: G;
var 0..1: H;
var 0..1: I;

% constraints
constraint 3*A + B + 3*C + 4*D + 4*E + F + 3*G + 5*H + 3*I >= 15;
constraint 5*A + 2*B + 4*C + 3*D + 2*E + 3*F + G + 4*H + 3*I >= 15;
constraint A + 5*B + 2*C + D + 2*E + 4*F + 5*G + 2*H + 3*I >= 15;

% Objective function - minimise cost of salary
solve minimize 46000*A + 43000*B + 47000*C + 36000*D + 43000*E + 55000*F + 68000*G + 64000*H + 60000*I;

% output
output ["Total Salary = ",show(46000*A + 43000*B + 47000*C + 36000*D + 43000*E + 55000*F + 68000*G + 64000*H + 60000*I), "\n"]

