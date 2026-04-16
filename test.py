import random
import time

def existential_crisis():
    thoughts = [
        "What if we're all just simulations running in someone else's dream?",
        "Why do we park on driveways but drive on parkways?",
        "If I scream in space, does the void even care?",
        "Pineapples on pizza: crime against humanity or culinary genius?",
        "What if cats are actually aliens observing us?",
        "Am I real, or am I just a very convincing hallucination?",
        "Why is 'abbreviation' such a long word?"
    ]
    
    print("🤖 Initiating existential crisis protocol...\n")
    time.sleep(1)
    
    for _ in range(8):
        thought = random.choice(thoughts)
        print(f"💭 {thought}")
        time.sleep(1.3)
        thoughts.remove(thought)  # no repeats
    
    print("\n🌀 Conclusion: The real question is... why did you run this script?")
    print("   (Answer: Because you're as weird as I am)")

# Run the chaos
if __name__ == "__main__":
    existential_crisis()
