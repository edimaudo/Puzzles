% PuzzlOR Toy Builder February 2016

%variables
% let i represent color (1 - blue, 2, green, 3 - red)
% let j represent toy(1 - airplane, 2 helicopter, 3 - car)

var 0..3: x11;
var 0..2: x21;
var 0..1: x31;
var 0..2: x12;
var 0..4: x22;
var 0..1: x32;
var 0..1: x13;
var 0..2: x23;
var 0..4: x33;

% constraints
constraint x11 + x12 + x13 <= 25;
constraint x21 + x22 + x23 <= 29;
constraint x31 + x32 + x33 <= 30;
constraint x11 + x21 + x31 >= 1;
constraint x12 + x22 + x32 >= 1;
constraint x13 + x23 + x33 >=1;

% objective function
solve maximize (x11 + x21 + x31) + (x12 + x22 + x32) + (x13 + x23 + x33);

% output
output ["Surivial","\n",

"max. profit = ", show((x11 + x21 + x31) + (x12 + x22 + x32) + (x13 + x23 + x33)) ,"\n"]