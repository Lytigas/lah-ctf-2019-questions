flag = "lah{b1n4ry_Is_Eve44w4343_G4L015_F1EEEELD}"

mask = "6kjads08xj.,308dasjl9d84298740k1j3hdasu04"

flag_bin = [ord(c) for c in flag]
mask_bin = [ord(c) for c in mask]
outp_bin = [a ^ b for a,b in zip(flag_bin, mask_bin)]

print(outp_bin)

def render_poly(l):
	r = reversed(l)
	out = []
	for byi in range(len(l)):
		byte = next(r)
		for bii in range(8):
			if byte & (1 << bii) > 0:
				out.append(byi*8 + bii)
	return out

def poly_str(l):
	return "x^" + " + x^".join(str(i) for i in l)

print("p = ", poly_str(render_poly(mask_bin)))
print("\n")
print("p = ", poly_str(render_poly(outp_bin)))

def solve(powers):
	out = [0] * 100
	for pow in powers:
		out[pow//8] += 1 << pow%8
	out.reverse()
	return out

print("".join(chr(a^b) for a,b in zip(solve(render_poly(mask_bin)), solve(render_poly(outp_bin)))))

