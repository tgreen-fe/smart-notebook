#include <stdio.h>
#include <stdlib.h>
#include <string.h>



// Function to decompress data compressed with Run-Length Encoding (RLE)
unsigned char* decompressRLE(const unsigned char* compressedData, size_t compressedSize, size_t* decompressedSize) {
    unsigned char* decompressedData = NULL;
    size_t decompressedIndex = 0;

    for (size_t i = 0; i < compressedSize; i += 2) {
        unsigned char currentByte = compressedData[i];
        size_t count = compressedData[i + 1];

        decompressedData = (unsigned char*)realloc(decompressedData, (decompressedIndex + count) * sizeof(unsigned char));
        if (decompressedData == NULL) {
            printf("Memory allocation error during decompression.\n");
            exit(1);
        }

        while (count > 0) {
            decompressedData[decompressedIndex++] = currentByte;
            count--;
        }
    }

    *decompressedSize = decompressedIndex;
    return decompressedData;
}

int main() {
    // Read compressed data from the file "compPic.cpp"
    FILE* compInFile = fopen("compPic.cpp", "r");
    if (compInFile == NULL) {
        printf("Error opening the file compPic.cpp for reading.\n");
        return 1;
    }

    // Allocate memory to read the compressed data
    size_t compressedSize = 0;
    unsigned char* compressedData = NULL;
    unsigned int tempByte;

    // Read compressed data from the file
    while (fscanf(compInFile, "%02X,", &tempByte) == 1) {
        compressedData = (unsigned char*)realloc(compressedData, (compressedSize + 1) * sizeof(unsigned char));
        if (compressedData == NULL) {
            printf("Memory allocation error during reading compressed data.\n");
            fclose(compInFile);
            return 1;
        }
        compressedData[compressedSize++] = (unsigned char)tempByte;
    }

    // Close the compressed data input file
    fclose(compInFile);

    // Decompress the data
    size_t decompressedSize;
    unsigned char* decompressedData = decompressRLE(compressedData, compressedSize, &decompressedSize);

    // Open the file for writing decompressed data
    FILE* outFile = fopen("pictureOut.cpp", "w");
    if (outFile == NULL) {
        printf("Error opening the file picture.cpp for writing.\n");
        return 1;
    }

    // Write decompressed data to the file in the desired format
    fprintf(outFile, "unsigned char data[] = {\n");
    for (size_t i = 0; i < decompressedSize; i++) {
        fprintf(outFile, "0x%02X", decompressedData[i]);
        if (i % 8 == 7 || i == decompressedSize - 1) {
            fprintf(outFile, ",\n");
        } else {
            fprintf(outFile, ", ");
        }
    }
    fprintf(outFile, "};\n");

    // Close the output file
    fclose(outFile);

    // Clean up memory
    free(decompressedData);

    return 0;
}