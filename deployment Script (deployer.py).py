import os
import shutil

def deploy():
    # Copy package to foundation directory
    src = 'pxl'
    dst = 'portalxox-foundation/pxl'
    if not os.path.exists(dst):
        shutil.copytree(src, dst)
    print("PXL Language System deployed successfully.")
