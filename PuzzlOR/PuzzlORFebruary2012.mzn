% puzzlOR February 2012
% let xi represent the number of full time workers starting at day i
% let yi represent the number of part time workers starting at day i
% let i = {1,2,3,4,5,6,7}
% i represents the days of the week starting from Monday
% 100$ for full time
% 150$ for part time

% variables
var 0..10: x1;
var 0..10: x2;
var 0..10: x3;
var 0..10: x4;
var 0..10: x5;
var 0..10: x6;
var 0..10: x7;
var 0..10: y1;
var 0..10: y2;
var 0..10: y3;
var 0..10: y4;
var 0..10: y5;
var 0..10: y6;
var 0..10: y7;

% constraints
constraint x1+x4+x5+x6+x7+y1+y7>=5;
constraint x1+x2+x5+x6+x7+y1+y2>=7;
constraint x1+x2+x3+x6+x7+y2+y3>=7;
constraint x1+x2+x3+x4+x7+y3+y4>=10;
constraint x1+x2+x3+x4+x5+y4+y5>=16;
constraint x2+x3+x4+x5+x6+y5+y6>=18;
constraint x3+x4+x5+x6+x7+y6+y7>=12;

% minimize cost
solve minimize x1 + x2 + x3 + x4 + x5 + x6 + x7 + y1 + y2 + y3 + y4 + y5 + y6 + y7;

output ["Working five days a week","\n",
"no. of monday full time workers = ", show(x1), "\n",
"no. of tuesday full time workers = ", show(x2), "\n",
"no. of wednesday full time workers = ", show(x3),"\n",
"no of thursday full time workers = ", show(x4),"\n",
"no of friday full time workers = ", show(x5), "\n",
"no of saturday full time workers = ", show(x6), "\n",
"no of sunday full time workers = ", show(x7), "\n",
"no. of monday part time workers = ", show(y1), "\n",
"no. of tuesday part time workers = ", show(y2), "\n",
"no. of wednesday part time workers = ", show(y3),"\n",
"no of thursday part time workers = ", show(y4),"\n",
"no of friday part time workers = ", show(y5), "\n",
"no of saturday part time workers = ", show(y6), "\n",
"no of sunday part time workers = ", show(y7), "\n",
"Total cost per month = ", show(4*(100*(x1 + x2 + x3 + x4 + x5 + x6 + x7) + 150*(1 + y2 + y3 + y4 + y5 + y6 + y7))),"\n"]



