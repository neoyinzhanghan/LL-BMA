import os
from LLBMA.front_end.api import analyse_bma

slide_path = "/media/hdd1/neo/BMA_AML_lite/H21-2765;S10;MSK7 - 2024-01-02 14.55.59.ndpi"
dump_dir = "/media/hdd3/neo/LLBMA_dump_test"

if __name__ == "__main__":

    # if the dump directory does not exist, create it
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)
    else:
        # remove the dump directory if it already exists and recreate it
        os.system(f"rm -rf {dump_dir}")
        os.makedirs(dump_dir)

    # Run the heme_analyze function
    analyse_bma(
        slide_path=slide_path,
        dump_dir=dump_dir,
        hoarding=True,
        continue_on_error=False,
        do_extract_features=False,
    )
