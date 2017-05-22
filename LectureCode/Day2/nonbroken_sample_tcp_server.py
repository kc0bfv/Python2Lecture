#!/usr/bin/env python

from __future__ import print_function

import json
import socket

SERVER_PORT = 8080

def client_input(client, request):
    client[0].sendall(request)
    return client[0].recv(4096)

def client_print(client, data):
    client[0].sendall(data + "\n")

def input_branch(client, depth=0):
    possible_selections = ["B","L","N"]
    branch = list()
        
    keep_going = True
    while keep_going:
        selection = ""
        while selection not in possible_selections:
            selection = client_input(
                    client,
                    "Depth: {} - Add a (B)ranch, (L)eaf or "\
                            "(N)either? ".format(depth)
                    ).upper()[:1]
        if selection == "B":
            branch.append(input_branch(client, depth+1))
        elif selection == "L":
            branch.append(int(client_input(client, "Input leaf contents: ")))
        elif selection == "N":
            return branch
        else:
            client_print(
                    client, 
                    "I don't know how you did that man, but I'm done!"
                    )
            return branch
            
def print_branch(client, branch, indent=0):
    for item in branch:
        if type(item) is str or type(item) is unicode or type(item) is int:
            client_print(client, " "*indent + str(item))
        else:
            client_print(client, "-" * (indent+1))
            print_branch(client, item, indent+1)

def file_output(branch, filename="/tmp/outfile"):
    with open(filename, "w") as f:
        json.dump(branch, f)

def file_input(filename="/tmp/outfile"):
    with open(filename, "r") as f:
        return json.load(f)

def handle_client(client):
    client_filename = "/tmp/outfile_{}_{}.json".format(*client[1])

    root = input_branch(client)
    print_branch(client, root)

    file_output(root, filename=client_filename)

    read_new = file_input(filename=client_filename)

    print_branch(client, read_new)


if __name__ == "__main__":
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(("", SERVER_PORT))
    server_sock.listen(10)

    while True:
        client = server_sock.accept()
        handle_client(client)
        client[0].close()
