import os
import argparse
import requests
import threading

ip_address_list = []

def main():
    parser = argparse.ArgumentParser(description="this script takes a list of \
    ip addresses and retrieve their domain names")
    parser.add_argument("-f", "--filename", help="specify a filename within the script directory", \
    required=True)
    parser.add_argument("-t", "--threads", help="number of threads u want to spawn[default is 10]")
    args = parser.parse_args()

    filename = args.filename
    thread_count = args.threads
    get_address_list(filename)
    if threads_count:
        create_threads(thread_count=thread_count)
    else:
        create_threads()
# create threads with the number parsed as argument
def create_threads(thread_count=10):
    thread_list = []
    for i in range(thread_count):
        new_thread = threading.Thread(target=get_domain_name, args=())
        thread_list.append(new_thread)

    for thread in thread_list:
        thread.start()
        sleep(0.5)

    for thread in thread_list:
        thread.join()


def get_domain_name():
    

# this function retrieves the addresses from the file and add them to the ip_address_list
def get_address_list(filename):
    with open(os.getcwd()+"/"+filename, "r") as f: # open the filename for reading
        lines = f.readlines()

    for line in lines:
        ip_address = line.strip("\n")
        ip_address_list.append(ip_address)
