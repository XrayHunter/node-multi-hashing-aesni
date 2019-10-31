{
    "targets": [
        {
            "target_name": "multihashing",
            "sources": [
                "multihashing.cc",
                "cryptonight.c",
                "cryptonight_light.c",
                "sha3/sph_keccak.c",
                "crypto/oaes_lib.c",
                "crypto/c_keccak.c",
                "crypto/c_groestl.c",
                "crypto/c_blake256.c",
                "crypto/c_jh.c",
                "crypto/c_skein.c",
                "crypto/hash.c",
                "crypto/aesb.c",
                "k12.c",
                "crypto/k12/KangarooTwelve.c",
                "crypto/k12/KeccakP-1600-reference.c",
                "crypto/k12/KeccakSpongeWidth1600.c"
            ],
            "include_dirs": [
                "crypto",
                "<!(node -e \"require('nan')\")",
            ],
            "cflags_c": [
                "-std=gnu11 -march=native -fPIC -m64"
            ],
            "cflags_cc": [
                "-std=gnu++11 -fPIC -m64"
            ],
        }
    ]
}
