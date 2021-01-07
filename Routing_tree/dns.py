import csv
from routing_tree import BST


def read_csv(file, do_ips):
    with open(file) as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        if "Domain" not in fields or "IP" not in fields:
            exit("File must have Domain and IP columns")
        for row in reader:
            do_ips.append((row['Domain'], row['IP']))


def main():
    do_ips = []
    read_csv('do_ip.csv', do_ips)
    for domain, ip in do_ips:
        BST.add(domain, ip)

    print('DFS (preorder): ', BST.preorder())
    print('BFS: ', BST.bfs())
    print('Attempt to find facebook.com & google.com')
    requests = ["facebook.com", "google.com"]
    for domain in requests:
        vertex = BST.find(domain)
        if vertex is not False:
            print(f"For {vertex.domain} go to the address: {vertex.IP}")
        else:
            print(f"Is there a typo in {domain}\t DNS_PROBE_FINISHED_NXDOMAIN")
    print("Attempt to delete 'quelle.de' from DNS")
    BST.delete_method("quelle.de")
    vertex = BST.find("quelle.de")
    if vertex is not False:
        print("Unsuccessful deletion.")
    else:
        print("Deleted successfully!")


if __name__ == '__main__':
    main()


