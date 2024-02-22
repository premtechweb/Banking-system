import time

def loading_bar(total_steps):
    for i in range(1, total_steps + 1):
        percentage = (i / total_steps) * 100
        print(f"Loading: {percentage:.2f}% [{i}/{total_steps}]", end="\r")
        time.sleep(0.1)  # Simulate some work being done

    print("\nLoading complete!")

if __name__ == "__main__":
    total_steps = 20  # You can adjust this value based on the desired number of steps
    loading_bar(total_steps)
