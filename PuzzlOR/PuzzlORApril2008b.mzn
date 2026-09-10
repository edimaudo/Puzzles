% PuzzlOR April 2008 Restuarant scheduling
% minimize cost by finding the optimal number of workers
% Solution to seconf part of the problem
% working 5 days a week

% let xi represent when workers start based on day of the week i
% variables
var 0..5: x1;
var 0..5: x2;
var 0..5: x3;
var 0..5: x4;
var 0..5: x5;
var 0..5: x6;
var 0..5: x7;

% constraints
constraint x1+x4+x5+x6+x7>=4;
constraint x1+x2+x5+x6+x7>=5;
constraint x1+x2+x3+x6+x7>=5;
constraint x1+x2+x3+x4+x7>=10;
constraint x1+x2+x3+x4+x5>=12;
constraint x2+x3+x4+x5+x6>=12;
constraint x3+x4+x5+x6+x7>=2;

% minimize cost
solve minimize x1 + x2 + x3 + x4 + x5 + x6 + x7;

% output
output ["Working five days a week","\n",
"no. of monday workers = ", show(x1), "\n",
"no. of tuesday workers = ", show(x2), "\n",
"no. of wednesday workers = ", show(x3),"\n",
"no of thursday workers = ", show(x4),"\n",
"no of friday workers = ", show(x5), "\n",
"no of saturday workers = ", show(x6), "\n",
"no of sunday workers = ", show(x7), "\n",
"Savings = ",show(6000 - (400*x1 + 400*x2 + 400*x3 + 400*x4 + 400*x5 + 400*x6 + 400*x7))];
