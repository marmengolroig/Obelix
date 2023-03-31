# [OBELIX]

from ClassLibrary.AsterixFile import AsterixFile

path = (
    'Ficheros_asterix/asterix_cat10', # Contains 12 blocks of Asterix category 10 data. Each block has one record. All records refer to a single moving target.
    'Ficheros_asterix/201002-lebl-080001_adsb.ast', #cat 21
    'Ficheros_asterix/201002-lebl-080001_mlat.ast', #cat 10
    'Ficheros_asterix/201002-lebl-080001_smr.ast', #cat 10
    'Ficheros_asterix/201002-lebl-080001_smr_mlat_adsb.ast') # mixed

def main():
    file = AsterixFile(path[3])
    file.read_file()
    file.divide_datablocks()
    file.divide_records()
    file.decode_dataitems()
    

    print("Data blocks: "+str(file.retrieve_num_datablocks()))
    m = 0
    while m<1:
        print(file.datablock_list[m].record)
        print(f'Fspec Length: {file.datablock_list[m].record.retrieve_fspec_length()}')
        print(f'Number of "1" in FSPEC: {file.datablock_list[m].record.retrieve_num_ones_fspec()}')
        print(f'Data Fields: {file.datablock_list[m].record.retrieve_num_datafields()}')
        n = 0
        dataitems_list = file.datablock_list[m].record.decode_dataitems()
        while n<4:
            print(f'Dataitem {n+1}: {dataitems_list[n].dataitem.decode_data()}')
            n=n+1
        m=m+1

if __name__ == '__main__':
    main()
