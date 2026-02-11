 A deterministic finite automaton or DFA is a finite-state machine that moves between states as it reads characters from a string.

Each input consists of a table describing the DFA, and a quoted input string, like so:

    a b c d e f
> 0 0 0 0 1 0 0
  1 0 0 0 1 0 2
  2 3 0 0 1 0 0
 F3 3 3 3 3 3 3
"adbacadafad"

In this table, we can find the following information:

    There are four states, called 0, 1, 2, and 3.
        States are always digits 0-9. There may be up to 10 states.
    There are six characters in the input alphabet: a, b, c, d, e, and f.
        Input characters may be lowercase letters a-z or digits 0-9.
    The table entries describe the new state for each (current state, character) pair.
        For example, if the current state is 0, and a d is read, the next state is 1.
    The row describing state 0 is marked with > so it is the initial state. There is exactly one initial state.
    The row describing state 3 is marked with F so it is an accept state. There may be multiple accept states, or none at all.

Use the table to move the DFA between its states by feeding it characters from the input string.

In our example:

    The initial state is 0. The first character is a. Looking at the table, we see the new state is 0.
    The current state is 0. The next character is d. Looking at the table, we see the new state is 1.
    The current state is 1. The next character is b. Looking at the table, we see the new state is 0.
    …

Finally, print the name of the state, followed by a space, followed by either Accept (if it is an accept state) or Reject (otherwise). In this case, we end in state 1 so we print 1 Reject. 
