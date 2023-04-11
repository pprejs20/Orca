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

    with open('patryk_logs/cwnd_list.txt', 'r') as file:
        # for i in range(2):
        line = file.readline()
        # print(line.split(','))
        read_lists.append([int(x) for x in line.split(',')[:-1]])

        line = file.readline()
        # print(line)
        read_lists.append([float(x) for x in line.split(',')[:-1]])
    with open('throughput.txt', 'r') as file:
        content = file.readlines() 
    content = [float(x.strip()) for x in content]
    content = [x for x in content if x != float('inf')]
    # print(read_lists[4])


    return {
    'Arrivals' : read_lists[0],
    'Capacity' : read_lists[1], 
    'Departures' : read_lists[2],
    'Delays' : read_lists[3],
    'Throughput' : content,
    # 'Throughput' : read_lists[4],
    'CWND' : read_lists[5]
    }

def display_data_graph(data, y_label = "Data", x_label="Sample", samples = None):
    if samples is None:
        samples = range(1, len(data) + 1)
    plt.plot(samples, data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def main():

    results = read_data_from_files()

    print("Arrivals: " + str(len(results['Arrivals'])))
    print("Capacity: " + str(len(results['Capacity'])))
    print("Departures: " + str(len(results['Departures'])))
    print("Delays: " + str(len(results['Delays'])))
    print("Throughput: " + str(len(results['Throughput'])))
    print("CWND's: " + str(len(results['CWND'])))

    # arrivals_list = list(map(float, results['Arrivals']))
    # capacity_list = list(map(float, results['Capacity']))
    # departures_list = list(map(float, results['Departures']))
    # delays_list = list(map(float, results['Delays']))
    # throughput_list = list(map(float, results['Throughput']))
    # cwnd_list = list(map(float, results['CWND']))

    # samples = range(1, len(results['CWND']) + 1)

    # display_data_graph(results['CWND'], y_label='CWND (pkts)')
    # display_data_graph(results['Delays'], y_label='Delays')

    samples =np.arange(0, (len(results['Throughput'])/2), 0.5)
    display_data_graph(results['Throughput'], y_label='Throughput (Mbps)', x_label='seconds', samples=samples)
    # print(results['Throughput'])
    print("SUM: {}".format(max(results['Throughput'])))
    print("LEN: {}".format(len(results['Throughput'])))
    print((sum(results['Throughput']))/len(results['Throughput']))

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
