from State_Class import Mystate
from Best_First_Search import bestfs
def A_Star(state,goalstate):

    def gn(node):
        return node.gn()

    def hn_outplaced(state, goal_state):
        outplaced_tiles_counter = 0
        for i in range(len(goal_state)):
            for j in range(len(goal_state)):
                num = goal_state[i][j]
                diff_of_i_k = 0
                diff_of_j_l = 0
                s=state
                print (type(s))
                for k in range(len(s)):
                    for l in range(len(s)):
                        if s[k][l] == num:
                            diff_of_i_k = abs(i - k)
                            diff_of_j_l = abs(j - l)
                #print (diff_of_i_k, diff_of_j_l, num)
                outplaced_tiles_counter += (diff_of_i_k + diff_of_j_l)
        return outplaced_tiles_counter

    def fn(state1):
        gn(Mystate(state1))+hn_outplaced(state1,goalstate)

    return bestfs(state,goalstate,fn)