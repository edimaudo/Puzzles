
% PuzzlOR August 2013 Urban Planning

include "globals.mzn"; 
int: n = 5;

int: residential = 1;
int: commercial = 2;

% scores
% 5 Residential lots = +5 points
% 4 Residential lots = +4 points
% 3 Residential lots = +3 points
% 5 Commercial lots = -5 points
% 4 Commercial lots = -4 points
% 3 Commercial lots = -3 points

% score table (for residental)
% Note: it's from 0..5.
array[0..5] of int: score_table =
   array1d(0..5, [
      -5, -4,-3, 3, 4, 5, % for residential
    ]);

% decision variables
array[1..n, 1..n] of var 1..2: x;

array[1..n] of var -5..5: row_scores;
array[1..n] of var -5..5: col_scores;

var 0..50: z = sum(row_scores) + sum(col_scores);


% scores for this row/column. Note we just count the
predicate scores(array[int] of var int: rc, var int: score) =
   let {
     var 0..n: cc
   } in 
   count(rc,1, cc)
   /\
   score = score_table[cc]
;

% solve maximize z;
solve :: int_search(
   [x[i,j] | i,j in 1..n] ++
   row_scores ++ col_scores, % ++ [x[i,j] | i,j in 1..n], 
   first_fail, 
   indomain_min, 
   complete) 
  % satisfy;
  maximize z;

constraint

   % z = 14 /\ % for solve satisfy

   forall(i in 1..n) (
      scores([x[i,j] | j in 1..n], row_scores[i]) /\
      scores([x[j,i] | j in 1..n], col_scores[i])
   )
   /\
   % 12 residential
   count([x[i,j] | i,j in 1..n], residential,12) 
;

output [
  "z: " ++ show(z) ++ "\n" ++
  "row_scores: " ++ show(row_scores) ++ "\n" ++
  "col_scores: " ++ show(col_scores) ++ "\n" ++ 
  "x:"
] ++
[
  if j = 1 then "\n" else " " endif ++
    show(x[i,j])
  | i,j in 1..n
] ++
["\n"]++
[
  if j = 1 then "\n" else " " endif ++
    if fix(x[i,j]) == residential then 
     "R"
    else 
     "C"
    endif
  | i,j in 1..n
]

;