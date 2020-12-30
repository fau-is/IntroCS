import csv
from routing_tree import BST as Tree

def read_csv(file, do_ips):
    f = open(file)
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    if "Domain" not in fields or "IP" not in fields:
        exit("File must have Domain and IP columns")
    for row in reader:
        do_ips.append((row['Domain'], row['IP']))
    f.close()

def main():
    do_ips = []
    read_csv('do_ip.csv', do_ips)
    for domain, ip in do_ips:
        Tree.add(domain, ip)

    print('DFS: ', Tree.preorder())
    print('BFS: ', Tree.bfs())
    print('Attempt to find facebook.com & google.com')
    to_find = ["facebook.com", "google.com"]
    for items in to_find:
        vertex = Tree.find(items)
        if vertex is not False:
            print(vertex.domain, "can be found at", vertex.IP)
        else:
            print(items, "does not exist")
    print("Attempt to delete 'quelle.de'")
    Tree.delete_method("quelle.de")
    vertex = Tree.find("quelle.de")
    if vertex is not False:
        print(vertex.domain, "can be found at", vertex.IP)
    else:
        print("quelle.de does not exist")

    print('DFS: ', Tree.preorder())

    print('BFS:', Tree.bfs())

if __name__ == '__main__':
    main()


