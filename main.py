# python3

def parallel_processing(n, m, data):
    output = []
    next_available=[0]*n
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(m):
        min_time=min(next_available)
        thread_id=next_available.index(min_time)
        output.append((thread_id,min_time))
        next_available[thread_id]+=data[i]

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m=map(int,input().split())
   

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data=list(map(int,input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for p in result:
        print(p[0],p[1])


if __name__ == "__main__":
    main()
