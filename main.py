# [OBELIX]

from ClassLibrary.AsterixFile import AsterixFile

path = (
    'Ficheros_asterix/asterix_cat10', # Contains 12 blocks of Asterix category 10 data. Each block has one record. All records refer to a single moving target.
    'Ficheros_asterix/201002-lebl-080001_adsb.ast', #cat 21
    'Ficheros_asterix/201002-lebl-080001_mlat.ast', #cat 10
    'Ficheros_asterix/201002-lebl-080001_smr.ast', #cat 10
    'Ficheros_asterix/201002-lebl-080001_smr_mlat_adsb.ast') # mixed

def main():
    file = AsterixFile(path[0])
    file.read_file()
    file.divide_datablocks()
    file.divide_records()

    print("Data blocks: "+str(file.retrieve_num_datablocks()))
    m = 0
    while m<3:
        print(file.datablock_list[m].record)
        print(f'Fspec Length: {file.datablock_list[m].record.retrieve_fspec_length()}')
        print(f'Data Fields: {file.datablock_list[m].record.retrieve_num_datafields()}')
        
        m=m+1

if __name__ == '__main__':
    main()
