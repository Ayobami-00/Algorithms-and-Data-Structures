#TWO SUM

#SolutionOne
"""
This is a brute-force solution but it is slow.
Time complexity: O(n^2)
"""
def brute_force_sol(nums,target):
    result_map  = set()
    for i,k in enumerate(nums):
        for j,l in enumerate(nums):
            if target - l == k:
                result_map.add(i)
                result_map.add(j)
                return(tuple(result_map))

                
            
#Solution Two
"""
This is a one-pass hash table solution for
faster lookup.
Time complexity: O(n)
""" 
def one_pass_hash_table_solution(nums,target):
    hash_map = {}
    for i,j in enumerate(nums):
        n = target - j
        if n not in hash_map:
            hash_map[j] = i
        else:
            return [hash_map[n],i]
            
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print('Solution One')
    print(brute_force_sol(nums,target))
    print('Solution Two')
    print(one_pass_hash_table_solution(nums,target))