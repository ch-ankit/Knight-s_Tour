import time
import matplotlib.pyplot as plt

from my_knight import knight_tour
def plot():
    chessboard=[i+1 for i in range(8)]
    time_difference=[]
    for i in range(8):
        initialization=knight_tour(N=i+1)
        start_time=time.time()
        initialization.start_tour()
        end_time=time.time()
        time_difference.append((end_time-start_time))
    plt.figure("Knight's Tour")
    plt.title("Time taken for solution of Knight's tour for differen sizes of chessboard")
    plt.xlabel("Chessboard Size")
    plt.ylabel("Time(in seconds)")
    plt.plot(chessboard, time_difference, '*', label="time")
    plt.legend()
    
if __name__=='__main__':
    plot()
    plt.show()