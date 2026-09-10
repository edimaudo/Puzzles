% PuzzlOR June 2010
% SurvivoR


% let j be a size (small, medium, large)
% let i be a condition (food, water, shelter, defense)

% variables
var 0..1: x11;
var 0..1: x12;
var 0..1: x13;
var 0..1: x21;
var 0..1: x22;
var 0..1: x23;
var 0..1: x31;
var 0..1: x32;
var 0..1: x33;
var 0..1: x41;
var 0..1: x42;
var 0..1: x43; 

% constraints
constraint x11 + x12 + x13 <= 1;
constraint x21 + x22 + x23 <= 1;
constraint x31 + x32 + x33 <= 1;
constraint x41 + x42 + x43 <= 1;
constraint 5*x11 + 8*x12 + 12*x13 + 3*x21 + 5*x22 + 8*x23 +
5*x31 + 8*x32 + 12*x33 + x41 + 2*x42 + 3*x43 <= 25;

% objective function
solve maximize 10*x11 + 20*x12 + 25*x13 + 10*x21 + 20*x22 + 25*x23 + 
5*x31 + 15*x32 + 20*x33 + 5*x41 + 15*x42 + 20*x43;


% output
output ["Surivial","\n",
"max surivial points = ", show(10*x11 + 20*x12 + 25*x13 + 10*x21 + 20*x22 + 25*x23 + 
5*x31 + 15*x32 + 20*x33 + 5*x41 + 15*x42 + 20*x43),"\n"]
