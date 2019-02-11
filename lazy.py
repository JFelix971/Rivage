import h5py
import numpy as np

#from lazy5.inspect import get_datasets
filename = 'CombinedOUTPUTS_ZONE_2_CAREME.h5'

fid = h5py.File(filename, 'r')

a_group_key = list(fid.keys())
#print( len( a_group_key ) )
#print(a_group_key[0])
#print(a_group_key[1])

dset = fid['DATA']
#print( dset.shape )
#print( dset.size )
#print( dset.dtype )
#print( type( dset[0] ) )
#print( dset.dtype )

dset2 = fid['_i_DATA/Scenario']
print( dset2.name )
print( type( dset2 ) )
gr_keys = list(dset2.keys())
print( len( gr_keys ) )

# print( gr_keys[0] )
# print( len(gr_keys[0]) )
#
# print( gr_keys[1] )
# print( len(gr_keys[1]) )
#
# print( gr_keys[2] )
# print( len(gr_keys[2]) )
#
# print( gr_keys[3] )
# print( len(gr_keys[3]) )
#
# print( gr_keys[4] )
# print( len(gr_keys[4]) )
#
# print( gr_keys[5] )
# print( len(gr_keys[5]) )
#
# print( gr_keys[6] )
# print( len(gr_keys[6]) )
#
# print( gr_keys[7] )
# print( len(gr_keys[7]) )
#
# print( gr_keys[8] )
# print( len(gr_keys[8]) )
#
# print( gr_keys[9] )
# print( len(gr_keys[9]) )

gr_val = list(dset2.values())
print( gr_val[0] )
print( type( gr_val[0] ) )

print(dset2.attrs.keys())
print(dset2.attrs['CLASS'])
print(dset2.attrs['DIRTY'])
print(dset2.attrs['FILTERS'])
print(dset2.attrs['TITLE'])
print(dset2.attrs['VERSION'])

print(dset2.attrs['blocksize'])
print(dset2.attrs['chunksize'])
print(dset2.attrs['optlevel'])
print(dset2.attrs['reduction'])
print(dset2.attrs['slicesize'])
print(dset2.attrs['superblocksize'])


print( '= Attributs du dataset DATA =' )
#for k in dset.attrs.keys():
#    print( str( k ) + ' -> ' + str( type( dset.attrs[k] ) ) )

#myds = subgrp[]
#print( dset2.shape )

fid.close()
