# [OBELIX]

from ClassLibrary.AsterixFile import AsterixFile

path = (
    'Ficheros_asterix/asterix_cat10', # Contains 12 blocks of Asterix category 10 data. Each block has one record. All records refer to a single moving target.
    'Ficheros_asterix/201002-lebl-080001_adsb.ast', #cat 21
    'Ficheros_asterix/201002-lebl-080001_mlat.ast', #cat 10
    'Ficheros_asterix/201002-lebl-080001_smr.ast', #cat 10
    'Ficheros_asterix/201002-lebl-080001_smr_mlat_adsb.ast') # mixed

def main():
    file = AsterixFile(path[4])
    file.read_file()
    file.divide_datablocks()
    file.decode_dataitems()
    

    print("Data blocks: "+str(file.retrieve_num_datablocks()))
    m = 46
    while m<48:   # datablocks in a file
        print('-------------------------------')
        print(f'Datablock ID: {m+1}')
        print(file.datablock_list[m].record)
        print(f'Datablock category: {file.datablock_list[m].cat}')
        print(f'Datablock Lenght: {file.datablock_list[m].long}' )
        print(f'Fspec #FRNs: {file.datablock_list[m].record.retrieve_fspec_length()}')
        print(f'Record #DataItems: {file.datablock_list[m].record.retrieve_num_ones_fspec()}')
        print(f'Record #DataFields: {file.datablock_list[m].record.retrieve_num_datafields()}')
        n = 0
        dataitems_list = file.datablock_list[m].record.dataitems_list
        while n<len(dataitems_list): # dataitems in a datablock
            print('---')
            print(f'Dataitems list LENGTH: {len(dataitems_list)}')
            print(f'Dataitem FRN: {dataitems_list[n].FRN}')
            if dataitems_list[n].FRN==48 and dataitems_list[n].dataitem is not None:
                print(f'Dataitem Data: {dataitems_list[n].dataitem.get_data()}')
            elif dataitems_list[n].dataitem is not None:
                print(f'Dataitem Data: {dataitems_list[n].dataitem.data}')
                print(f'Dataitem Decoded: {dataitems_list[n].dataitem.decoded_data}')
            n=n+1
        m=m+1

if __name__ == '__main__':
    main()
