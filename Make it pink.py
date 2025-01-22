# Function to print text in pink color
def print_pink(text):
    PINK = "\033[95m"  # ANSI escape code for pink/magenta
    RESET = "\033[0m"  # Reset color to default
    print(PINK + text + RESET)

# Example usage with arrival time
arrival_time = "12:30:45"  # Example arrival time
print_pink(f"Arrival Time: {arrival_time}")