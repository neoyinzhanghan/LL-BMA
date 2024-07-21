import os
from LLBMA.front_end.api import analyse_bma

slide_path = "/media/hdd1/neo/BMA_AML_lite/H23-7023;S14;MSK5 - 2023-10-23 13.23.28.ndpi"
dump_dir = "/media/hdd3/neo/LLBMA_dump_test"

if __name__ == "__main__":

    # if the dump directory does not exist, create it 
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)

    # Run the heme_analyze function 
    analyse_bma(
        slide_path=slide_path,
        dump_dir=dump_dir,
        hoarding=True,
        continue_on_error=False,
        do_extract_features=False,
    )
