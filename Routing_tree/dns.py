import dns
import routing_tree
import csv
from routing_tree import Node as Tree

def read_csv(file, do_ips):
    f = open(file)
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    print(fields)
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

    print(Tree.preorder())

    Tree.find_question("facebook.com")
    Tree.find_question("google.com")


    #Tree.bfs()
    #Tree.bfs_recursive()
    Tree.delete_method("quelle.de")
    Tree.find_question("quelle.de")
    print(Tree.preorder())
    #Tree.bfs()
if __name__ == '__main__':
    main()


