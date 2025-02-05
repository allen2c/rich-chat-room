from rich.console import Console

from rich_chat_room import render_chat_room

console = Console()


def test_render_rich_chat_room():
    messages = [
        {"role": "user", "content": "ggwp"},
        {
            "role": "assistant",
            "content": (
                "Good game! That was an amazing match with lots of action and intense moments.\n"
                "We should definitely play again sometime soon."
            ),
        },
        {
            "role": "user",
            "content": (
                "Let's play again! I'm up for another round whenever you are ready! I'm really excited "
                "to try out some new strategies and see how the game unfolds.\n"
                "What do you think?"
            ),
        },
        {
            "role": "assistant",
            "content": (
                "Absolutely, ready when you are.\n"
                "Let's plan a rematch and try some new tactics this time.\n"
                "What do you think?"
            ),
        },
        {
            "role": "user",
            "content": (
                "I've been thinking about some cool ideas that might just give us an edge next time.\n"
                "What do you say?"
            ),
        },
        {
            "role": "assistant",
            "content": (
                "I'm intrigued! Let's discuss those strategies over a quick break and then jump back in.\n"
                "What do you think?"
            ),
        },
        {
            "role": "assistant",
            "content": (
                "Let's keep this conversation dynamic! Imagine if, in the midst of our strategy talk, a mysterious challenger suddenly steps in with a twist—a clever riddle that could change the rules of our game."  # noqa: E501
            ),
        },
        {
            "role": "user",
            "content": (
                "A riddle from a mysterious challenger? That sounds exciting! \n"
                "I'm ready to unravel the puzzle. What kind of riddle are we talking about?"  # noqa: E501
            ),
        },
        {
            "role": "assistant",
            "content": (
                "Picture this: 'I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind.' \n"  # noqa: E501
                "Solving it might unlock a secret move or bonus for us!"
            ),
        },
        {
            "role": "user",
            "content": (
                "I love that idea—solving a riddle to unlock hidden potential adds a whole new layer of excitement. \n"  # noqa: E501
                "Bring on the challenge!"
            ),
        },
    ]

    layout = render_chat_room(messages)

    console.clear()
    console.print(layout)
