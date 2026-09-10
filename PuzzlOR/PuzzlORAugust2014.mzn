% PuzzlOR August 2014
% Goal maximize cost of burger

%variables
var 1..5: a; % Beef patty
var 1..5: b; % Bun
var 1..5: c; % Cheese
var 1..5: d; % Onions
var 1..5: e; % Pickles
var 1..5: f; % Lettuce
var 1..5: g; % Ketchup
var 1..5: h; % Tomato

% constraints
constraint 50*a + 330*b + 310*c + d + 260*e + 3*f + 160*g + 3*h <=3000; % sodium
constraint 17*a + 9*b + 6*c + 2*d <= 150; % fat
constraint 220*a + 260*b + 70*c + 10*d + 5*e + 4*f + 20*g + 9*h <=3000; % calories
constraint f = g;
constraint e = h;

% objective function
solve maximize 0.25*a + 0.15*b + 0.1*c + 0.09*d + 0.03*e + 0.04*f + 0.02*g + 0.04*h;

% output
output ["Beef = ", show(a), "\n",
        "Bun = ", show(b), "\n",
        "Cheese = ",show(c),"\n",
        "Onions = ",show(d),"\n",
        "Pickles = ",show(e),"\n",
        "Lettice = ",show(f),"\n",
        "Ketchup = ",show(g),"\n",
        "Tomato = ",show(h),"\n",
        "Burger Cost = ",show(0.25*a + 0.15*b + 0.1*c + 0.09*d + 0.03*e + 0.04*f + 0.02*g + 0.04*h),"\n"]
