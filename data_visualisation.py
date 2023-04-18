import matplotlib.pyplot as plt
import numpy as np

def read_data_from_files():
    read_lists = []
    with open('patryk_logs/data.txt', 'r') as file:
        for i in range(5):
            line = file.readline()
            read_lists.append([float(x) for x in line.split(',')])

    arrivals_list = read_lists[0]
    capacity_list = read_lists[1]
    departures_list = read_lists[2]
    delays_list = read_lists[3]
    throughput_list = read_lists[4]

    cwnd_data = []
    server_time_elapsed = []
    with open('patryk_logs/cwnd_list.txt', 'r') as file:
       for line in file:
        cwnd, time_elapsed_microseconds = map(int, line.strip().split(","))
        time_elapsed_seconds = time_elapsed_microseconds / 1000000  # Convert microseconds to seconds
        cwnd_data.append(cwnd)
        server_time_elapsed.append(time_elapsed_seconds)

    thr_data = []
    client_time_elapsed = []

    with open('throughput.txt', 'r') as file:
        for line in file:
            raw_data = line.strip().split(",")
            thr, client_time_elapsed_microseconds = float(raw_data[0]), int(raw_data[1])
            client_time_elapsed_seconds = client_time_elapsed_microseconds / 1000000  # Convert microseconds to seconds
            thr_data.append(thr)
            client_time_elapsed.append(client_time_elapsed_seconds)

    with open('patryk_logs/rtt.txt', 'r') as file:
       rtt_content = file.readlines()
    rtt_list = [float(x.strip()) for x in rtt_content]


    return {
    # 'Arrivals' : read_lists[0],
    # 'Capacity' : read_lists[1], 
    # 'Departures' : read_lists[2],
    # 'Delays' : read_lists[3],
    
    # 'Throughput' : read_lists[4],
    # 'CWND' : read_lists[5]
    # 'Throughput' : content,
    'Throughput' : (thr_data, client_time_elapsed),
    'CWND' : (cwnd_data,server_time_elapsed),
    'RTT' : rtt_list
    }

def display_data_graph(ax, data, y_label="Data", x_label="Sample", samples=None, linewidth=1):
    if samples is None:
        samples = range(1, len(data) + 1)
    ax.plot(samples, data, linewidth=linewidth)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)


def main():

    results = read_data_from_files()

    # print("Arrivals: " + str(len(results['Arrivals'])))
    # print("Capacity: " + str(len(results['Capacity'])))
    # print("Departures: " + str(len(results['Departures'])))
    # print("Delays: " + str(len(results['Delays'])))
    print("Throughput: " + str(len(results['Throughput'])))
    print("CWND's: " + str(len(results['CWND'])))
    print("SRTT's: " + str(len(results['RTT'])))

    # arrivals_list = list(map(float, results['Arrivals']))
    # capacity_list = list(map(float, results['Capacity']))
    # departures_list = list(map(float, results['Departures']))
    # delays_list = list(map(float, results['Delays']))
    # throughput_list = list(map(float, results['Throughput']))
    # cwnd_list = list(map(float, results['CWND']))

    # samples = range(1, len(results['CWND']) + 1)

    # display_data_graph(results['CWND'], y_label='CWND (pkts)')
    # display_data_graph(results['Delays'], y_label='Delays')
    print(results['Throughput'][0][0:5])
    print(results['Throughput'][1][0:5])
    print("len cwnd: {}".format(len(results['CWND'])))
    print("CWND Avg (pkts): {}".format((sum(results['CWND'][0]))/len(results['CWND'][0])))
    print("Throughput Avg (Mbps): {}".format((sum(results['Throughput'][0]))/len(results['Throughput'][0])))
    print("SRTT Avg (ms): {}".format((sum(results['RTT']))/len(results['RTT'])))

    thr_samples = np.arange(0, (len(results['Throughput'])/50), 0.02)
    cwnd_samples = np.arange(0, (len(results['CWND'])/50), 0.02)

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15), sharex=True)
    fig.tight_layout(pad=4.0)

    display_data_graph(ax1, results['Throughput'][0], y_label='Throughput (Mbps)', x_label='Time (seconds)', samples=results['Throughput'][1], linewidth=0.5)
    display_data_graph(ax2, results['CWND'][0], y_label='CWND (pkt)', x_label='Time (seconds)', samples=results['CWND'][1], linewidth=0.5)
    display_data_graph(ax3, results['RTT'], y_label='SRTT (ms)', x_label='Time (seconds)', samples=results['CWND'][1], linewidth=0.5)

    plt.subplots_adjust(bottom=0.1)

    plt.show()
    # print(results['Throughput'])

    # fig, ax = plt.subplots()

    # ax.plot(arrivals_list, label='Arrivals')
    # ax.plot(capacity_list, label='Capacity')
    # ax.plot(departures_list, label='Departures')
    # ax.plot(delays_list, label='Delays')
    # ax.plot(throughput_list, label='Throughput')
    # plt.plot(samples, results['CWND'])

    # ax.set_xlabel('Time')

    # ax.set_ylabel('Data')

    # ax.set_title('My Data')

    # ax.legend()

    # plt.show()




 
if __name__ == "__main__":
    main()
