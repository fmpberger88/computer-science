import streamlit as st

class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self, node):
        self.choices.append(node)

# Story structure

story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1) Roar back!
2) Run to the left...
""")

choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1) Shout 'Sorry bear!'
2) Yell 'Hooray!'
""")

choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1) Gasp 'A talking bear!'
2) Explain that the bear scared you.
""")

choice_a_1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.
YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a_2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.
YOU REMAIN LOST.
""")

choice_b_1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.
YOU REMAIN LOST.
""")

choice_b_2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.
YOU HAVE ESCAPED THE WILDERNESS.
""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)


def extract_choices(story_piece):
    """Extract the user choices from the story piece."""
    lines = story_piece.split("\n")
    choices = []
    for line in lines:
        if ")" in line:
            choice_text = line.split(")")[1].strip()
            choices.append(choice_text)
    return choices


def app():
    st.title("Interactive Story")

    story_node = story_root  # Start from the root
    session_state = st.session_state
    if 'story_position' not in session_state:
        session_state.story_position = story_node
    else:
        story_node = session_state.story_position

    # Print only the main story, not the choices
    main_story = "\n".join(story_node.story_piece.split("\n")[:-len(story_node.choices) - 1])
    st.write(main_story)

    if story_node.choices:
        options = extract_choices(story_node.story_piece)
        choice = st.selectbox("What will you do?", options)

        # Map the selected option to the corresponding child
        for idx, option in enumerate(options):
            if option == choice:
                session_state.story_position = story_node.choices[idx]

    if st.button("Continue"):
        app()


if __name__ == "__main__":
    app()