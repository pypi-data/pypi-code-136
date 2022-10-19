from thresult import auto_unwrap
import thcrypto


Bcrypt = auto_unwrap(thcrypto.Bcrypt)
Ed25519 = auto_unwrap(thcrypto.Ed25519)
Fernet = auto_unwrap(thcrypto.Fernet)
MultiFernet = auto_unwrap(thcrypto.MultiFernet)
SECP256K1 = auto_unwrap(thcrypto.SECP256K1)

gen_random_int = auto_unwrap(thcrypto.gen_random_int)
gen_random_int_hex = auto_unwrap(thcrypto.gen_random_int_hex)
gen_random_int_hex_bytes = auto_unwrap(thcrypto.gen_random_int_hex_bytes)
gen_random_int128 = auto_unwrap(thcrypto.gen_random_int128)
gen_random_int128_hex = auto_unwrap(thcrypto.gen_random_int128_hex)
gen_random_int128_hex_bytes = auto_unwrap(thcrypto.gen_random_int128_hex_bytes)
gen_random_int256 = auto_unwrap(thcrypto.gen_random_int256)
gen_random_int256_hex = auto_unwrap(thcrypto.gen_random_int256_hex)
gen_random_int256_hex_bytes = auto_unwrap(thcrypto.gen_random_int256_hex_bytes)
