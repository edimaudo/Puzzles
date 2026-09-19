## Four couples attended a party. One couple was you and your spouse; another was Pat and Chris. Some people shook hands with one another, but nobody shook hands with oneself or with one's own spouse.

## After the party, you asked each person (except yourself) how many different people the person had shaken hands with. Each person replied with a different number--and each person's reply was truthful.

import itertools

def solve_handshake_puzzle():
    # Vertices: 0 = You, 1 = Your Spouse
    # Couples: (0,1), (2,3), (4,5), (6,7)
    couples = {i: i ^ 1 for i in range(8)}
    
    # 24 valid candidate edges (no self-loops, no handshakes between spouses)
    edges = [(u, v) for u in range(8) for v in range(u + 1, 8) if v != couples[u]]
    
    # Persons 1..7 MUST have unique handshake counts from 0 to 6
    degree_permutations = list(itertools.permutations(range(7)))
    
    for deg_1_to_7 in degree_permutations:
        for you_deg in range(7):
            target_degrees = [you_deg] + list(deg_1_to_7)
            
            adj = [[0] * 8 for _ in range(8)]
            curr_degrees = [0] * 8
            
            def backtrack(edge_idx):
                if edge_idx == len(edges):
                    return curr_degrees == target_degrees
                
                u, v = edges[edge_idx]
                
                # Try adding the handshake edge
                if curr_degrees[u] < target_degrees[u] and curr_degrees[v] < target_degrees[v]:
                    curr_degrees[u] += 1
                    curr_degrees[v] += 1
                    adj[u][v] = adj[v][u] = 1
                    
                    if backtrack(edge_idx + 1):
                        return True
                    
                    # Backtrack
                    curr_degrees[u] -= 1
                    curr_degrees[v] -= 1
                    adj[u][v] = adj[v][u] = 0
                
                # Try skipping the handshake edge
                return backtrack(edge_idx + 1)

            if backtrack(0):
                return target_degrees, adj, couples

target_degrees, adj, couples = solve_handshake_puzzle()

# Display Results
print("=== Handshake Counts ===")
print(f"You (Person 0): {target_degrees[0]} handshakes")
print(f"Your Spouse (Person 1): {target_degrees[1]} handshakes")
for i in range(2, 8):
    print(f"Person {i} (Spouse is Person {couples[i]}): {target_degrees[i]} handshakes")

print("\n=== Handshake Matrix (1 = Shook Hands) ===")
print("  " + " ".join(f"P{i}" for i in range(8)))
for i, row in enumerate(adj):
    print(f"P{i} " + " ".join(str(x) for x in row))