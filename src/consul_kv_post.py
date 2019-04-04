import argparse, logging, json, yaml, sys, ssl
from logging.handlers import RotatingFileHandler
from operator import attrgetter
import consul
data_centre = dc1

consul_http = "consul.example.com"

if sys.version_info[0] < 3:
    from urlparse import urlparse
    from httplib import HTTPSConnection
else:
    from urllib.parse import urlparse
    from http.client import HTTPSConnection

LOG_FILE='/tmp/dsc.log'

def readjson (filename):
    return

def establish_consul_connection(https_url):
    consul_connection = consul.Consul(host=https_url, port=443, token=None, scheme='https', consistency='default', dc=data_centre, verify=False, cert=None)
    return (consul_connection)

def remove_from_consul():
    master = establish_consul_connection(data_centre)
    master.kv.delete('kv/', recurse=True)
    return

def push_to_consul(kv1, kv2, kv3, json_template):
    
    master = establish_consul_connection(data_centre)

    print("Pushing to consul")
    master.kv.put('kv/{}/{}/{}/{}/{}'.format(kv1, kv2, kv3), json_template)
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--kv1",required=True, help="KV1")
    parser.add_argument("--kv2",required=True, help="KV2")
    parser.add_argument("--kv3",required=True, help="KV3")
    parser.add_argument("--filename",required=True, help="Filename of JSON template")

    args = parser.parse_args()

    logLevel  = logging.INFO

    json_stanza = readjson(args.filename)

    #Clear KVs before run
    remove_from_consul()

    #Push KV to consul    
    push_to_consul(kv1=args.kv1, kv2=args.kv2, kv3=args.kv3, json_template=json_stanza)


if __name__ == '__main__':
    main()
