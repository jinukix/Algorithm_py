def solution(skill, skill_trees):
    
    cnt = 0

    for skill_tree in skill_trees:

        for i in range(1, len(skill)):

            if skill_tree.index(skill[i]) > skill_tree.index(skill[i-1]):
                break
            cnt+=1

    return cnt  


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill,skill_trees))