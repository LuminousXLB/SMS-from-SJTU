from grpc_tools import protoc
import subprocess
from glob import glob
from os.path import normpath
import sys

src_list = [normpath(p) for p in glob('*.proto')]


def main():
    # npm install -g grpc-tools
    # https://github.com/grpc/grpc/tree/v1.19.0/examples/node/static_codegen
    print(subprocess.run(
        [
            'grpc_tools_node_protoc',
            '-I.',
            '--js_out=import_style=commonjs,binary:build/js',
            '--grpc_out=build/js'
        ] + src_list,
        shell=True
    ))

    # pip install grpcio-tools
    # https://grpc.io/docs/tutorials/basic/python.html#generating-client-and-server-code
    sys.exit(protoc.main(
        [
            '-I.',
            '--python_out=build/py',
            '--grpc_python_out=build/py',
            '--js_out=import_style=commonjs,binary:build/js'
        ] + src_list
    ))


if __name__ == "__main__":
    main()
