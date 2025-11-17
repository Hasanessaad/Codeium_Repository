def print_multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i*j:3d}", end=" ")
        print()

def main():
    print_multiplication_table(10)

if __name__ == "__main__":
    main()
