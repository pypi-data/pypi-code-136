from __future__ import annotations
import math
import cyquant


def _name_symbol(name, symbol):
	return {
		"name": name,
		"symbol": symbol,
	}


def si_prefixes(scale: float, show_unit_symbol: bool) -> dict:
	"""Prefix units with symbol or name

	:param scale: 
	:type scale: float
	:param show_unit_symbol: Passed from `show_quantity`
	:type show_unit_symbol: bool
	:return: SI symbol and name
	:rtype: dict
	"""
	if scale == 1.0:
		return ""

	scale = float(f"{scale:.3e}")
	def ten_exp(exp): return 10 ** exp
	prefixes = {
		ten_exp(24): _name_symbol("yotta", "Y"),
		ten_exp(21): _name_symbol("zetta", "Z"),
		ten_exp(18): _name_symbol("exa", "E"),
		ten_exp(15): _name_symbol("peta", "P"),
		ten_exp(12): _name_symbol("tera", "T"),
		ten_exp(9): _name_symbol("giga", "G"),
		ten_exp(6): _name_symbol("mega", "M"),
		ten_exp(3): _name_symbol("kilo", "k"),
		ten_exp(2): _name_symbol("hecto", "h"),
		ten_exp(1): _name_symbol("deka", "da"),
		###### Beginning negatives #######
		ten_exp(-1): _name_symbol("deci", "d"),
		ten_exp(-2): _name_symbol("centi", "c"),
		ten_exp(-3): _name_symbol("milli", "m"),
		ten_exp(-6): _name_symbol("micro", "µ"),
		ten_exp(-9): _name_symbol("nano", "n"),
		ten_exp(-12): _name_symbol("pico", "p"),
		ten_exp(-15): _name_symbol("femto", "f"),
		ten_exp(-18): _name_symbol("atto", "a"),
		ten_exp(-21): _name_symbol("zepto", "z"),
		ten_exp(-24): _name_symbol("yocto", "y"),
	}
	prefix = prefixes.get(scale)
	if not prefix:
		raise ValueError("Unit prefix not found.")
	return prefix["symbol"] if show_unit_symbol else prefix["name"]


def si_unit_conversion(units: str) -> str:
	"""Converts SI base units string into a
		more readable unit of measurment.
		e.g. [kg*m]/[(s^2)] -> N (for Newtons)
			 [kg]/[m*(s^2)] -> Pa (for Pascals)

	:param units: SI base units string
	:type units: str
	:return: Concise unit of measurement found in dict
		returns keys: `name` and `symbol` else `None`
	:rtype: dict_or_None
	"""
	conversions = {
		"[kg*m]/[(s^2)]": _name_symbol("Newtons", "N"),
		"[kg]/[m*(s^2)]": _name_symbol("Pascals", "Pa"),
		"[kg*(m^2)]/[(s^2)]": _name_symbol("Joules", "J (N*m)"),
		"[kg*(m^2)]/[(s^3)]": _name_symbol("Watts", "W"),
		"[a*s]": _name_symbol("Coulombs", "C"),
		"[kg*(m^2)]/[a*(s^3)]": _name_symbol("Volts", "V"),
		"[(a^2)*(s^4)]/[kg*(m^2)]": _name_symbol("Farads", "F"),
		"[kg*(m^2)]/[(a^2)*(s^3)]": _name_symbol("Ohms", "Ω"),
		"[(a^2)*(s^3)]/[kg*(m^2)]": _name_symbol("Siemens", "S"),
		"[kg*(m^2)]/[a*(s^2)]": _name_symbol("Webers", "Wb"),
		"[kg]/[a*(s^2)]": _name_symbol("Teslas", "T"),
		"[kg*(m^2)]/[(a^2)*(s^2)]": _name_symbol("Henrys", "H"),
		"[(m^2)]/[(s^2)]": _name_symbol("Sieverts", "[J]/[kg]"),
	}
	return conversions.get(units, None)


def show_quantity(quantity: cyquant.quantities.Quantity, show_unit_symbol=True):
	"""Formats cyquant Quantity as string showing dimension abbreviation

	:param quantity: cyquant quantity
	:type quantity: class:`cyquant.quantities.Quantity`
	:param show_unit_symbol: Shows unit symbol instead of name, defaults to False
	:param show_unit_symbol: bool, optional
	:return: Number as string (e.g. "23 m") or cyquant.quantities.Quantity
	:rtype: str_or_class:`cyquant.quantities.Quantity`
	"""
	if type(quantity) in {float, int, None}:
		return quantity
	try:
		# if `.units` attr cannot be extracted then
		# pass quantity through
		scale = quantity.units.scale
	except Exception as e:
		return quantity

	dims = ["kg", "m", "s", "k", "a", "mol", "cd"]
	units = {
		"[kg]": "kg",
		"[m]": "m" if show_unit_symbol else "meters",
		"[s]": "s" if show_unit_symbol else "second(s)",
		"[k]": "K" if show_unit_symbol else "Kelvin",
		"[a]": "A" if show_unit_symbol else "amperes",
		"[mol]": "mols",
		"[cd]": "cd",  # candelas
	}

	def _show_units(dim: str) -> str:
		"""Get dimension from units dict
		
		:return: Dimension Value from units dict
			else return input `dim`
		:rtype: str
		"""
		return units.get(dim, dim)

	def _count_dimensions(quantity) -> int:
		"""Checks how many dimensions are in the cyquant Quantity
			and stores dimensions in dictionary

		:return: Number of dimensions(units of measurement) in quantity
			and key/val pairs of dim. names and their values.
			keys: `count` & `dimensions`
		:rtype: dict
		"""
		# '0' in dimensions means that unit of measurement isn't being used
		# any dim. other than 0 represents the exponent of the unit
		# e.g. Dimensions(kg=1,m=-1,s=-2,k=0,a=0,mol=0,cd=0) -> kg/m(s**2) or Pascals
		#	   this would return 3 since there are three dimensions used
		bool_dims_list = [
			getattr(quantity.units.dimensions, dim) != 0 for dim in dims]
		dimensions_dict = {
			"count": sum(bool_dims_list),
			"dimensions": {}
		}

		for idx, dim in enumerate(dims):
			if bool_dims_list[idx]:
				dimensions_dict["dimensions"].update(
					{ dim: getattr(quantity.units.dimensions, dim) }
				)
		return dimensions_dict

	def _dim2str(dimensions) -> str:
		"""Converts `dimensions` from `_count_dimensions()`
			into formatted string
		"""
		items = sorted(list(dimensions.items()))
		positive_dims = []
		negative_dims = []
		for k, v in items:
			val = k if abs(v) == 1 else f'({k}^{abs(int(v))})'
			if v >= 0:
				positive_dims.append(val)
			else:
				negative_dims.append(val)

		def format_dims(dims): return f"[{'*'.join(dims)}]"
		if positive_dims and negative_dims:
			return format_dims(positive_dims) + "/" + format_dims(negative_dims)
		elif positive_dims and not negative_dims:
			return format_dims(positive_dims)
		elif negative_dims and not positive_dims:
			return f"[1]/{format_dims(negative_dims)}"
		else:  # No dimensions in dict
			return ""

	def _quantity2str(quantity, scale, dimensions, prefix="") -> str:
		"""Converts cyquant quantity to formatted string

		:param quantity: cyquant quantity
		:type quantity: class:`cyquant.quantities.Quantity`
		:param scale: Scale of SIUnit
		:type scale: float
		:param dimensions: `dimensions` from `_count_dimensions()`
		:type dimensions: dict
		:param prefix: SI Unit prefix, defaults to ""
		:type prefix: str, optional
		:return: Formatted quantity_or_`cyquant.quantities.Quantity`
		:rtype: str_or_class:`cyquant.quantities.Quantity`
		"""
		dims_len = len(dimensions.values())
		q = float(quantity)
		if dims_len == 1:
			# get the only dim in dimensions dict
			dim, exp = list(dimensions.items())[0]
			dim_str = _dim2str(dimensions)
			converted_dim = si_unit_conversion(dim_str)

			if converted_dim:  # if converted, reset `dim_str`
				dim_str = converted_dim["symbol"] if show_unit_symbol else converted_dim["name"]

			u = dim_str if exp <= 0 else f"{_show_units(dim_str)}"
			q_times_scale = q * scale

			if scale == 1.0:  # no prefix case
				return f"{q} {u}"
			else:  # scale not 1.0
				# If scale is not in kilograms -> use `grams`
				if dim == "kg":
					grams_scale = scale * 1000
					new_prefix = si_prefixes(grams_scale, show_unit_symbol)
					if show_unit_symbol:
						return f"{q} {new_prefix}g"
					else:
						return f"{q} {new_prefix}grams"
				elif dim in {"k", "mol", "cd"}:  # don't add prefix
					return f"{q_times_scale:.3e} {_show_units(dim_str)}"
				else:
					return f"{q} {prefix}{u}" if prefix else f"{q_times_scale:.3e} {u}"

		elif dims_len > 1:  # multiple dimensions in cyquant quantity
			q_times_scale = q * scale
			dim_str = _dim2str(dimensions)
			converted_dim = si_unit_conversion(dim_str)
			if converted_dim:
				_units = converted_dim["symbol"] if show_unit_symbol else converted_dim["name"]
				return f"{q_times_scale:.3e} {_units}"
			else:
				return f"{q_times_scale:.3e} {dim_str}"
		else:
			return quantity

	dimensions_dict = _count_dimensions(quantity)
	num_dims = dimensions_dict.get("count")
	dimensions = dimensions_dict.get("dimensions")

	if num_dims == 0:
		# si units for degrees and radians may be returned here
		if scale != 1.0:
			q_times_scale = float(quantity) * scale
			return f"{q_times_scale:.3e}"
		else:
			return f"{float(quantity)}"

	def _is_scale_decimal(scale):
		"""Checks if `scale` is a fraction
			e.g. 1.0000 -> returns False
			     0.0175 -> returns True

		:return: `True` if decimal, else `False`
		:rtype: bool
		"""
		return not scale - int(scale) == 0

	prefix = ""
	exp_greater_than_one = False
	dim_list = list(dimensions.items())
	for _, v in dim_list:
		if v > 1:
			exp_greater_than_one = True
	# only add prefix if not base si unit and
	# doesn't have exponent greater than 1
	# case: Liters has m^3 and should not have prefix
	if scale != 1.0 and not exp_greater_than_one:
		def _is_power_of_ten(num) -> bool:
			"""Is scale(`num`) base 10?"""
			if num < 0:
				return False
			else:
				# convert negative exponent scientific notation
				# numbers into natural numbered exponents so
				# the algorithm will work
				num_list = []
				sci_note_num = f"{num:.3e}"
				num_list[:0] = sci_note_num
				if "e" in num_list:
					num_split = sci_note_num.split('e')
					exp = abs(int(num_split[1]))
					num = float(f"{num_split[0]}e{exp}")
				power = int(math.log(num, 10) + 0.5)
				return 10 ** power == num

		if _is_power_of_ten(scale):
			prefix = si_prefixes(scale, show_unit_symbol)

	return _quantity2str(quantity, scale, dimensions, prefix)
