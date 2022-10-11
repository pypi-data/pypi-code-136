import warnings
from copy import deepcopy


def build_symmetric_block_areas(geometry) -> list:
    symmetric_blocks = []
    n_blocks = geometry._calc_no_defined_blocks()
    for layer_def in geometry.layer_defs:
        layer_blocks = [next(filter(lambda x: x.block_def.no == block_index, geometry._blocks))
                        for block_index in layer_def.blocks[:n_blocks]]

        if layer_def.symm == 31:
            symmetric_blocks.extend(handle_symmetry_type_31(layer_blocks))
        elif layer_def.symm == 33:
            symmetric_blocks.extend(handle_symmetry_type_33(layer_blocks))
        elif layer_def.symm == 41:
            symmetric_blocks.extend(handle_symmetry_type_41(layer_blocks))
        elif layer_def.symm == 42:
            symmetric_blocks.extend(handle_symmetry_type_42(layer_blocks))
        elif layer_def.symm in {1, 3, 5, 7, 9, 11}:
            symmetric_blocks.extend(handle_symmetry_type_1_3_5_7_9_11(layer_blocks, layer_def.symm))
        elif layer_def.symm in {2, 4, 6, 8, 10, 12, 50, 52, 54, 56, 58, 60}:
            symmetric_blocks.extend(handle_symmetry_type_2_4_6_8_10_12_52_54_56_58_60(layer_blocks, layer_def.symm))
        elif layer_def.symm in {22, 24, 26, 28, 30, 32}:
            symmetric_blocks.extend(handle_symmetry_type_22_24_26_28_30_32(layer_blocks, layer_def.symm))
        else:
            warnings.warn(f"Symmetry type {layer_def.symm} not yet supported!")

    return symmetric_blocks


def handle_symmetry_type_31(layer_blocks) -> list:
    """
    The option 31 is intended for two-in-one window frame dipoles with the apertures atop each other.
    :param layer_blocks:
    :return:
    """
    rotated_blocks = [layer_block.rotate(180) for layer_block in layer_blocks]
    mirrored_blocks = [rotated_block.mirror_x() for rotated_block in layer_blocks + rotated_blocks]
    negated_mirrored_blocks = [mirrored_block.negate_current()
                               for mirrored_block in mirrored_blocks]
    return negated_mirrored_blocks + rotated_blocks


def handle_symmetry_type_33(layer_blocks) -> list:
    """
    The 33-option however, is designed for a single-aperture window frame quadrupole.
    :param layer_blocks:
    :return:
    """
    rotated_blocks = [layer_block.rotate(90).mirror_y() for layer_block in layer_blocks]
    mirrored_y_blocks = [rotated_block.mirror_y().negate_current() for rotated_block in layer_blocks + rotated_blocks]
    mirror_x_blocks = [mirrored_y_block.mirror_x().negate_current()
                       for mirrored_y_block in layer_blocks + rotated_blocks + mirrored_y_blocks]
    return mirror_x_blocks + mirrored_y_blocks + rotated_blocks


def handle_symmetry_type_41(layer_blocks) -> list:
    """
    The 33-option however, is designed for a single-aperture window frame quadrupole.
    :param layer_blocks:
    :return:
    """
    rotated_blocks = [layer_block.rotate(90).mirror_y() for layer_block in layer_blocks]
    mirrored_y_blocks = [rotated_block.mirror_y().negate_current() for rotated_block in layer_blocks + rotated_blocks]
    mirror_x_blocks = [mirrored_y_block.mirror_x().negate_current()
                       for mirrored_y_block in layer_blocks + rotated_blocks + mirrored_y_blocks]
    return mirror_x_blocks + mirrored_y_blocks + rotated_blocks


def handle_symmetry_type_42(layer_blocks) -> list:
    """
    The 33-option however, is designed for a single-aperture window frame quadrupole.
    :param layer_blocks:
    :return:
    """
    return [layer_block.mirror_x() for layer_block in layer_blocks]


def handle_symmetry_type_1_3_5_7_9_11(layer_blocks, symm):
    angle = 360 * (1 - 1/(symm + 1))
    rotated_blocks = [layer_block.rotate(angle) for layer_block in layer_blocks]
    mirrored_blocks = [rotated_block.mirror_x() for rotated_block in rotated_blocks]
    return [mirrored_block.negate_current() for mirrored_block in mirrored_blocks]


def handle_symmetry_type_2_4_6_8_10_12_52_54_56_58_60(layer_blocks, symm) -> list:
    """

    2 - Dipole
    4 - Quadrupole
    6 - Sextupole
    8 - Octupole
    10 - Decapole
    12 - Dodecapole

    52 - Dipole, Both Ends in 3D
    54 - Quadrupole, Both Ends in 3D
    56 - Sextupole, Both Ends in 3D
    58 - Octupole, Both Ends in 3D
    60 - Decapole, Both Ends in 3D


    :param layer_blocks:
    :param symm:
    :return:
    """
    rotated_blocks = rotate_blocks_and_change_current_sign(layer_blocks, symm)
    mirrored_blocks = [rotated_block.mirror_x() for rotated_block in layer_blocks + rotated_blocks]
    return mirrored_blocks + rotated_blocks


def handle_symmetry_type_22_24_26_28_30_32(layer_blocks, symm) -> list:
    """

    22 - dipole connection side
    24 - quadrupole connection side
    26 - sextupole connection side
    28 - octupole connection side
    30 - decapole connection side
    32 - dodecapole connection side

    :param layer_blocks:
    :param symm:
    :return:
    """
    SYMM_TYPE_BIAS = 20
    return rotate_blocks_and_change_current_sign(layer_blocks, symm - SYMM_TYPE_BIAS)


def rotate_blocks_and_change_current_sign(layer_blocks, symmetry_type) -> list:
    # According to ROXIE documentation, cases 2, 4, ..., 12 and 52, 54, ..., 60 in 2D are the same
    SYMM_TYPE_2D_3D_BIAS = 50
    prev_blocks = layer_blocks
    rotated_blocks = []
    symmetry_type = symmetry_type % SYMM_TYPE_2D_3D_BIAS
    for i in range(symmetry_type - 1):
        angle = 360 / symmetry_type
        temp_rotated_blocks = [prev_block.rotate(angle) for prev_block in prev_blocks]

        temp_rotated_blocks = [temp_rotated_block.negate_current()
                               for temp_rotated_block in temp_rotated_blocks]

        prev_blocks = deepcopy(temp_rotated_blocks)
        rotated_blocks.extend(temp_rotated_blocks)

    return rotated_blocks
