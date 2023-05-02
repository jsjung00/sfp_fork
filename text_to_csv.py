import os
import os.path as osp
import argparse 
import pandas as pd 


SAVE_DIR = osp.join(osp.abspath(osp.expanduser("~")), 'logs/saved_csv')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Take in log text file to convert to csv')
    parser.add_argument('filename', help='file name (including .txt) of log text file', nargs='?', default="progress.txt")
    parser.add_argument('foldername', help='folder name (subfoler of logs) containing text file', nargs='?', default="default_s0")

    args = parser.parse_args()
    fname, f_ext = os.path.splitext(args.filename)
    text_path = osp.join(osp.abspath(osp.expanduser("~")), 'logs', args.foldername, args.filename)
    print("text path", text_path)
    read_file = pd.read_csv(text_path)
    os.makedirs(osp.join(SAVE_DIR, args.foldername), exist_ok=True) 
    try:
        read_file.to_csv(osp.join(SAVE_DIR, args.foldername, fname + ".csv"), index=False)
    except Error as e:
        print(e)
 



