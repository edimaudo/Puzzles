% PuzzlOR October 2015 Race car design

% let i represent race car part type { A - 1, B - 2, C - 3}
% let j represent part {engine - 1, tires - 2, trasmission - 3, brakes - 4}

% variables
var 1..20: x11;
var 1..20: x21;
var 1..20: x31;
var 1..20: x12;
var 1..20: x22;
var 1..20: x32;
var 1..20: x13;
var 1..20: x23;
var 1..20: x33;
var 1..20: x14;
var 1..20: x24;
var 1..20: x34;

% constraints
constraint x11 + x12 + x13 + x34 = 12;
constraint x31 + x22 + x13 + x34 = 17;
constraint x31 + x12 + x23 + x24 = 14;
constraint x21 + x22 + x13 + x34 = 13;
constraint x11 + x22 + x23 + x14 = 15;
constraint x11 + x32 + x23 + x34 = 11;
constraint x21 + x32 + x33 + x14 = 16;
constraint x21 + x22 + x13 + x24 = 19;
constraint x31 + x12 + x33 + x14 <= 18;
constraint x31 + x32 + x33 + x24 <= 20;


% objective function
solve minimize x11 + x12 + x13 + x14 + x21 + x22 + x23 + x24 + x31 + x32 + x33 + x34;

% output
output ["fastest speed ",show(x11 + x12 + x13 + x14 + x21 + x22 + x23 + x24 + x31 + x32 + x33 + x34),"\n",
"Awes engine ",show(x11),"\n",
"Baller engine ", show(x21),"\n",
"Charm engine ",show(x31),"\n",
"Aero tires ", show(x12),"\n",
"Boldo tires ",show(x22),"\n",
"Clingo tires ", show(x32),"\n",
"Accelo transmission ",show(x13),"\n",
"Beast transmission ", show(x23),"\n",
"Cert transmission ",show(x33),"\n",
"Aero brakes ", show(x14),"\n",
"Bolt brakes ",show(x24),"\n",
"Control brakes ", show(x34),"\n"
]
