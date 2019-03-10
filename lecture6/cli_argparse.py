#!/usr/bin/python3

import argparse
#python3 cli_argparse.py -j 1 -n 2 -f yaml
#python3 cli_argparse.py -j 1 -n 2 -f 'yaml'
#python3 cli_argparse.py -j 1 -n 2 -f 'yaml' -t
#python3 cli_argparse.py -j 1 -n 2 -f 'yaml' -t -i -i



def main():
    parser = argparse.ArgumentParser(description='application functionality')
    parser.add_argument('-n', '--number', type=int, required=False, dest='opt_number', help='number of options')
    parser.add_argument('-j', '--jobs',   type=int, required=False, dest='job_number', help='number of jobs')
    parser.add_argument('-f', '--format', type=str, dest='data_format', default='json', help='format of data')
    parser.add_argument('-t', '--track', action="store_true", help='blabla')
    parser.add_argument('-i', '--index', action="count", help='blabla')
    subparsers = parser.add_subparsers(title='commands', help='list of commands', dest='command')

    args = parser.parse_args()
    
    numberOfOptions = -1
    numberOfJobs = -1
    formatOfData = 'xml'
    track = False
    index = 0
    if(args.opt_number):
        numberOfOptions = args.opt_number
    if(args.job_number):
        numberOfJobs = args.job_number
    if(args.data_format):
        formatOfData = args.data_format
    if(args.track):
        track = args.track
    if(args.index):
        index = args.index

    print("numberOfOptions={}; numberOfJobs={}; formatOfData={}; track={}; index={}.".format(numberOfOptions,numberOfJobs,formatOfData, track, index))

if __name__ == '__main__':
    main()