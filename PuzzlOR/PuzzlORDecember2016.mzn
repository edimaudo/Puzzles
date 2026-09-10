% PuzzlOR December 2016 - Galaxy on fire

% variables

var 1..1: A;
var 1..1: B;
var 1..1: C;
var 1..1: D;
var 1..1: E;
var 1..1: F;
var 1..1: G;
var 1..1: H;
var 1..1: I;
var 1..1: J;

% constraints
constraint 25*A+350*B+38*C+28*D+45*E+80*F+60*G+50*H+65*I+30*J>=350;
constraint 2*A+0*B+4*C+2*D+2*E+2*F+4*G+3*H+2*I+2*J >= 4;
constraint 6*A+8*B+5*C+8*D+7*E+8*F+6*G+5*H+7*I+6*J >= 8;

%objective function
solve minimize 51975*A+168900*B+235600*C+171900*D+150000*E+250000*F+294900*G+100100*H+125400*I+72500*J;

%output
output [
"Cicero = ", show(25*A+2*A+6*A), "\n",
"Cormonant = ", show(350*B+0*B+8*B), "\n",
"Dace = ", show(38*C+4*C+5*C), "\n",
"Hatsuyuki = ", show(28*D+2*D+8*D), "\n",
"H'Soc = ", show(45*E+2*E+7*E), "\n",
"N'Tirrk = ", show(80*F+2*F+8*F), "\n",
"Razor6 = ", show(60*G+4*G+6*G), "\n",
"Taipan = ", show(50*H+3*H+5*H), "\n",
"Teneta = ", show(65*I+2*I+7*I), "\n",
"Type43 = ", show(30*J+2*J+6*J), "\n",
] 