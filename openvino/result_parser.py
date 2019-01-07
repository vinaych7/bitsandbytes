from tabulate import tabulate
from collections import OrderedDict
from utils import ave


def main():
    experiments = {}
    net_names = set()
    experiments = load_result(
        'ncs1ov', 'results/ncs1_ovresult.txt', experiments)
    experiments = load_result(
        'ncs1ovusb2', 'usb2results/ncs1_ovresult.txt', experiments)
    experiments = load_result(
        'ncs1sdk', 'results/ncs1_sdkresult.txt', experiments)
    experiments = OrderedDict(sorted(experiments.items()))
    explist = ['ncs1sdk', 'ncs1ov']
    headers = ["Network", "NCS1 SDK", "NCS1 OV", 'speedup']
    explist = ['ncs1ovusb2', 'ncs1sdk', 'speedup']
    #headers = ["Network", "NCS1 OV"]

    table_results(experiments, explist, headers)


def table_results(experiments, explist, headers):
    results = []
    for key in experiments:
        result = []
        result.append(key)
        for exp in explist:
            if exp in experiments[key]:
                inftime = experiments[key][exp]
                fps = round(1000 / inftime, 2)
                result.append(fps)
            elif exp == 'speedup' and 'NA' not in result:
                result.append(round(result[-1]/result[-2], 2))
            else:
                result.append("NA")

        results.append(result)

    averages = robust_average(results)
    results.append(['average']+averages)
    # print(tabulate(results, headers=headers, tablefmt="latex"))
    print(tabulate(results, headers=headers))


def robust_average(results):
    cols = len(results[0]) - 1
    res_list = [[] for _ in range(cols)]
    for result in results:
        # cut out the network name
        for idx, elem in enumerate(result[1:]):
            if not elem == 'NA':
                res_list[idx].append(elem)

    averages = []
    for res in res_list:
        averages.append(round(ave(res), 2))

    return averages


def load_result(expname, filename, experiments):
    with open(filename, 'r') as resultsfile:
        for line in resultsfile:
            result = eval(line)
            network = result['network']
            inftime = result['inftime']
            if network in experiments:
                experiments[network][expname] = inftime
            else:
                experiments[network] = {expname: inftime}

    return experiments


if __name__ == '__main__':
    main()