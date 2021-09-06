## QA/QC Bitpacking Explained

Integers are stored in computer memory in binary format. Binary is a string of values which are either 0 or 1, with each place referred to as a "bit". The more bits in a binary string, the more information can be stored. A binary string of two bits can have the following four integer values:

|Binary | Integer |
|-------|---------|
| 00    | 0       |
| 01    | 1       |
| 10    | 2       |
| 11    | 3       |

A binary string of three bits can have the following eight integer values:

| Binary | Integer |
|--------|---------|
| 000    | 0       |
| 001    | 1       |
| 010    | 2       |
| 011    | 3       |
| 100    | 4       |
| 101    | 5       |
| 110    | 6       |
| 111    | 7       |

Thus, the maximum integer value is a function of the number of bits used, which is `(2^n)-1`, where `n` is the number of bits. Note that bits are read from right to left, and the bit "location" starts at 0. So the right-most bit is bit 0, the bit immediately to the left of that is bit 1, etc. Most QA/QC data will be either 8 or 16 bits. The above does not account for negative numbers, which are generally not seen in QA/QC data so are not explained here.  

Each bit in a binary string can be thought of as a single flag which declares if a certain condition is present. For example the following describes the bit flags of the Landsat 4-7 Cloud Quality Assessment band.

| Bit | Flag Description            |
|-----|-----------------------------|
| 0   | Dark Dense Vegetation (DDV) |
| 1   | Cloud                       |
| 2   | Cloud Shadow                |
| 3   | Adjacent to cloud           |
| 4   | Snow                        |
| 5   | Water                       |
| 6-7 | Unused                      |

This band has 8 bits, so is read as an 8-bit integer and has a maximum value of `(2^8)-1 = 255`. The following table has several examples of possible QA integer values, their corresponding flags, and the binary value.

| Pixel Value | DDV | Cloud | Cloud Shadow | Adjacent to cloud | Snow | Water |                     Description                    |  Binary  |
|:-----------:|:---:|:-----:|:------------:|:-----------------:|:----:|:-----:|:--------------------------------------------------:|:--------:|
|      2      |  No |  Yes  |      No      |         No        |  No  |   No  |                  Pixel has a cloud                 | 00000010 |
|      24     |  No |   No  |      No      |        Yes        |  Yes |   No  |      Pixel has snow and is adjacent to a cloud     | 00011000 |
|      36     |  No |   No  |      Yes     |         No        |  No  |  Yes  |       Pixel includes water and a cloud shadow      | 00100100 |
|      5      | Yes |   No  |      Yes     |         No        |  No  |   No  | Pixel had dark dense vegetation and a cloud shadow | 00000101 |

Any pixel can have multiple flags set. Thus to extract a single mask representing the "Cloud Shadow" flag, for example, would require finding values of 5, 36, and all other integers where bit 2 is set. The unpackqa package simplifies this process and makes querying one, or multiple, flags straightforward. 
