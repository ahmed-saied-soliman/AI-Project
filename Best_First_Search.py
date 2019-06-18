from State_Class import Mystate
from HeuristicFunctions import hn_outplaced
import util

def bestfs(initial_state,goal_state,fn):
    open=util.PriorityQueue()
    node = Mystate(initial_state)
    open.push(initial_state,fn(node))
    closed = []
    while not open.isEmpty():
        state= open.pop()
        if Mystate(state).is_goal(goal_state):
            print "Goal"
            return state
        else :
            node.append_Children()
            for i in range(len(state.childern.state)):
                child = state.children[i].state
                print(child)
                if not child in closed and not open.isIn(child):
                    open.push(child,fn(child))
                elif open.isIn(child):
                    cost, priority, path=open.getStateDetails(child)
                    newcost=fn(child)
                    if priority >newcost:
                        child.parent=path.parent
                        open.update(child, newcost)
                elif child in closed:
                    cost, priority, path = open.getStateDetails(child)
                    newcost=fn(child)
                    if priority> newcost:
                        closed.remove(child)
                        open.push(child,newcost)
            closed.append(state)
    return closed




