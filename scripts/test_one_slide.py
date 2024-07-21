import os
from LLBMA.front_end.api import heme_analyze

slide_path = "/media/hdd1/neo/BMA_AML_lite/H17-4780;S10;MSKK - 2023-09-06 21.22.16.ndpi"
dump_dir = "/media/hdd3/neo/LLBMA_dump_test"

if __name__ == "__main__":

    # if the dump directory does not exist, create it 
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)

    # Run the heme_analyze function 
    heme_analyze(
        slide_path=slide_path,
        dump_dir=dump_dir,
        hoarding=True,
        continue_on_error=False,
        do_extract_features=False,
    )
