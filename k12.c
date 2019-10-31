#include "k12.h"
#include "crypto/k12/KangarooTwelve.h"

void k12_hash(const char* input, char* output, uint32_t len) {
    KangarooTwelve((const unsigned char *)input, (size_t)len, (unsigned char *)output, 32, 0, 0);
}