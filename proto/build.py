from grpc_tools import protoc
import subprocess
from glob import glob
import os
import sys
import shutil

src_list = [os.path.normpath(p) for p in glob('*.proto')]


def copy_tree(source, target):
    [source, target] = map(os.path.normpath, [source, target])
    print(source, target)
    if os.path.exists(target):
        shutil.rmtree(target)

    shutil.copytree(source, target)


def build_for_js(build_dir):
    # npm install -g grpc-tools
    # https://github.com/grpc/grpc/tree/v1.19.0/examples/node/static_codegen
    if os.path.isdir(build_dir):
        shutil.rmtree(build_dir)

    os.mkdir(build_dir)

    r = subprocess.run(
        [
            'grpc_tools_node_protoc',
            '-I.',
            '--js_out=import_style=commonjs,binary:%s' % build_dir,
            '--grpc_out=%s' % build_dir
        ] + src_list,
        shell=True
    )

    if r.returncode:
        print(__func__, 'failed')
        sys.exit(r.returncode)
    # else:
        # copy_tree(build_dir, '../sms_from_sjtu/public/proto')


def build_for_python(build_dir):
    # pip install grpcio-tools
    # https://grpc.io/docs/tutorials/basic/python.html#generating-client-and-server-code
    if os.path.isdir(build_dir):
        shutil.rmtree(build_dir)

    os.mkdir(build_dir)

    r = protoc.main(
        [
            '-I.',
            '--python_out=%s' % build_dir,
            '--grpc_python_out=%s' % build_dir,
        ] + src_list
    )

    if r:
        print(__func__, 'failed')
        sys.exit(r)
    # else:
        # copy_tree(build_dir, '../rpc_server/proto')


def main():
    build_for_js('build/js')
    build_for_python('build/py')


if __name__ == "__main__":
    main()
