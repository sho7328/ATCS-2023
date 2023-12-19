# 0% Chatgpt; I took this from the maze FSM lab that I coded.
# The big paragraph documentation is from the lab, written by Ms. Namasivayam, and the hashtag documentation is by me.

class FSM:
    def __init__(self, initial_state):
        # Dictionary (input_symbol, current_state) --> (action, next_state).
        self.state_transitions = {}
        self.current_state = initial_state

    # Add the transitions entered to the state transitions dictionary
    def add_transition(self, input_symbol, state, action=None, next_state=None):
        """
        Adds a transition to the instance variable state_transitions
        that associates:
            (input_symbol, current_state) --> (action, next_state)

        The action may be set to None in which case the process() method will
        ignore the action and only set the next_state.

        The next_state may be set to None in which case the current state will be unchanged.
        
        Args:
            input_symbol (anything): The input received
            state (anything): The current state
            action (function, optional): The action to take/function to run. Defaults to None.
            next_state (anything, optional): The next state to transition to. Defaults to None.
        """
        if next_state == None:
            next_state = state
        # Add to dictionary
        self.state_transitions[(input_symbol, state)] = (action, next_state)

    # Return the corresponding action and state to the input and state inputted
    def get_transition(self, input_symbol, state):
        """
        Returns tuple (action, next state) given an input_symbol and state.
        Normally you do not call this method directly. It is called by
        process().

        Args:
            input_symbol (anything): The given input symbol
            state (anything): The current state

        Returns:
            tuple: Returns the tuple (action, next_state)
        """
        # Return the corresponding action and state
        return self.state_transitions[(input_symbol, state)]

    # Runs the corresponding action method based on the input symbol and transition to the next state.
    def process(self, input_symbol):
        """
        The main method that you call to process input. This may
        cause the FSM to change state and call an action. This method calls
        get_transition() to find the action and next_state associated with the
        input_symbol and current_state. If the action is None then the action
        is not called and only the current state is changed. This method
        processes one complete input symbol.
        Args:
            input_symbol (anything): The input to process
        """
        # Next is the tuple for the next action and state
        next = self.get_transition(input_symbol, self.current_state)
        # If the action is not empty, run the action
        if next[0] != None:
            next[0]()
        # Set the state to the new state
        self.current_state = next[1]