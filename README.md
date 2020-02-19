# 0011 - NTT Cha11enge 2020

### Huffman Code Compression Guide

1. In your program, read the text file that you get from the API as a string.
2. Compress the string with your own written Huffman code commpress program.
3. The result will be a string of binary.
4. Write a file of *RAW BYTES* from the string of binary.
5. When you get the compressed file. Hash it with SHA-256 Algorithm.
6. Submit your hash code via API.

### Prerequisite
* Git (ʘ‿ʘ)
* JSON Format
* JWT (JSON Web Token) (¬‿¬)
* RESTful API
* Huffman code algorithm
* SHA 256 hash algorithm


### Hint 0001
Please use [HuffmanGenerateTree.py](https://github.com/kaffir/chg2020_sample/blob/master/HuffmanGenerateTree.py) as guide or part of your code.

> ONLY REQUIRED A FINAL **SHA-256** HASH CODE FOR THE ANSWER.
>
> REMEMBER NOT TO WRITE THE BINARY STRING DIRECTLY!<br>
> OTHERWISE YOUR RESULT WOULD BE A FILE OF 0 and 1 ASCII WITH OVER 2MB LARGE..<br>
> AND THAT'S NOT COMPRESSION.. ;D

### Example
#### Source file - source.txt
`YDEHgBGxDQQQezsPkEOzoJDWUYAnDuwLCawpqsEESiHnalZsSbbHVMBQywllZKYxTldNJsBqMdpyueqJSaXrGxQsDsNyTkhYkgofl`

#### Output of the program
![alt text](https://github.com/kaffir/chg2020_sample/blob/master/sample/example.png "Sample result")

#### Checksum result (SHA256)
`5cec4b6500f02800c8b52b5ebe9dc24f9885acad803eea8123767ad6e252a756`
