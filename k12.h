#ifndef K12_H
#define K12_H

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

void k12_hash(const char* input, char* output, uint32_t len);

#ifdef __cplusplus
}
#endif

#endif