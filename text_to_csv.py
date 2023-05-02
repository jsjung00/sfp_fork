import os
import os.path as osp
import argparse 
import pandas as pd 


SAVE_DIR = osp.join(osp.abspath(osp.expanduser("~")), 'logs/saved_csv')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Take in log text file to convert to csv')
    parser.add_argument('filename', help='file name (including .txt) of log text file in default_s0 folder')

    args = parser.parse_args()
    fname, f_ext = os.path.splitext(args.filename)
    text_path = osp.join(osp.abspath(osp.expanduser("~")), 'logs', 'default_s0', args.filename)
    print("text path", text_path)
    read_file = pd.read_csv(text_path)
    os.makedirs(SAVE_DIR, exist_ok=True) 
    read_file.to_csv(osp.join(SAVE_DIR, fname + ".csv"), index=False)
 



